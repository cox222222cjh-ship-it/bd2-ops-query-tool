from __future__ import annotations

import re
import sqlite3
from collections import defaultdict
from pathlib import Path
from typing import Any

import click

from common import OUTPUTS_DIR, ensure_dirs, setup_logging, write_json

logger = setup_logging("build_indexes")

STRONG_ITEM_RELATION_FIELD_WHITELIST = {
    "itemtid",
    "itemid",
    "completeitemtid",
    "useskilltid",
}
STRONG_ITEM_RELATION_PREFIX_IDLIKE_PATTERN = re.compile(r"^(dropitem|boxitem)(\d+|id|tid)$")


def normalize_name(value: str) -> str:
    return "".join(ch.lower() for ch in value if ch.isalnum())


def fetch_table_names(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name != 'table_metadata'"
    ).fetchall()
    return [row[0] for row in rows]


def is_id_like(field_name: str) -> bool:
    return field_name.lower().endswith(("id", "tid")) or "_id" in field_name.lower() or "_tid" in field_name.lower()


def is_strong_item_relation_field(field_name: str) -> bool:
    normalized = normalize_name(field_name)
    if normalized in STRONG_ITEM_RELATION_FIELD_WHITELIST:
        return True
    return bool(STRONG_ITEM_RELATION_PREFIX_IDLIKE_PATTERN.match(normalized))


@click.command()
@click.option("--db-path", default="outputs/sqlite/game_tables.db", show_default=True)
@click.option("--output-dir", default="outputs/intermediate", show_default=True)
def main(db_path: str, output_dir: str) -> None:
    ensure_dirs()
    conn = sqlite3.connect(db_path)
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    table_index: list[dict[str, Any]] = []
    field_index: list[dict[str, Any]] = []
    value_sample_index: list[dict[str, Any]] = []
    id_columns: list[dict[str, Any]] = []
    strong_relation_columns: list[dict[str, Any]] = []

    for table in fetch_table_names(conn):
        row_count = conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
        columns = conn.execute(f'PRAGMA table_info("{table}")').fetchall()
        table_index.append({"table": table, "row_count": row_count, "column_count": len(columns)})

        for col in columns:
            name = col[1]
            non_null = conn.execute(
                f'SELECT COUNT(*) FROM "{table}" WHERE "{name}" IS NOT NULL AND TRIM("{name}") != ""'
            ).fetchone()[0]
            unique_count = conn.execute(
                f'SELECT COUNT(DISTINCT "{name}") FROM "{table}" WHERE "{name}" IS NOT NULL AND TRIM("{name}") != ""'
            ).fetchone()[0]
            samples = [
                r[0]
                for r in conn.execute(
                    f'SELECT DISTINCT "{name}" FROM "{table}" WHERE "{name}" IS NOT NULL AND TRIM("{name}") != "" LIMIT 5'
                ).fetchall()
            ]
            field_row = {
                "table": table,
                "field": name,
                "non_null_rate": round(non_null / row_count, 4) if row_count else 0,
                "unique_count": unique_count,
                "sample_values": [str(v) for v in samples],
            }
            field_index.append(field_row)
            value_sample_index.append({"table": table, "field": name, "samples": [str(v) for v in samples]})
            if is_id_like(name) and unique_count > 0:
                id_columns.append({"table": table, "field": name, "values": set(str(v) for v in samples)})
            if is_strong_item_relation_field(name):
                strong_values = {
                    str(r[0])
                    for r in conn.execute(
                        f'SELECT DISTINCT "{name}" FROM "{table}" '
                        f'WHERE "{name}" IS NOT NULL AND TRIM(CAST("{name}" AS TEXT)) != ""'
                    ).fetchall()
                }
                if strong_values:
                    strong_relation_columns.append({"table": table, "field": name, "values": strong_values})

    candidates: list[dict[str, Any]] = []
    by_name: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for field in field_index:
        if is_id_like(field["field"]):
            by_name[normalize_name(field["field"])].append(field)

    for key, same_fields in by_name.items():
        if len(same_fields) < 2:
            continue
        for i in range(len(same_fields)):
            for j in range(i + 1, len(same_fields)):
                left = same_fields[i]
                right = same_fields[j]
                if left["table"] == right["table"]:
                    continue
                confidence = 0.65
                if left["unique_count"] and right["unique_count"]:
                    confidence += 0.1
                candidates.append(
                    {
                        "source_table": left["table"],
                        "source_field": left["field"],
                        "target_table": right["table"],
                        "target_field": right["field"],
                        "inference": "same_field_name",
                        "evidence_strength": "weak",
                        "confidence": round(min(confidence, 0.95), 2),
                        "status": "待确认",
                    }
                )

    # 简单交集匹配（基于样本值）
    for i in range(len(id_columns)):
        for j in range(i + 1, len(id_columns)):
            left = id_columns[i]
            right = id_columns[j]
            if left["table"] == right["table"]:
                continue
            inter = left["values"].intersection(right["values"])
            if inter:
                candidates.append(
                    {
                        "source_table": left["table"],
                        "source_field": left["field"],
                        "target_table": right["table"],
                        "target_field": right["field"],
                        "inference": "sample_value_intersection",
                        "evidence_strength": "weak",
                        "intersection_samples": sorted(inter)[:5],
                        "confidence": 0.55,
                        "status": "待确认",
                    }
                )

    # 强证据层（字段白名单 + 全量值精确匹配）
    for i in range(len(strong_relation_columns)):
        for j in range(i + 1, len(strong_relation_columns)):
            left = strong_relation_columns[i]
            right = strong_relation_columns[j]
            if left["table"] == right["table"]:
                continue
            inter = left["values"].intersection(right["values"])
            if inter:
                candidates.append(
                    {
                        "source_table": left["table"],
                        "source_field": left["field"],
                        "target_table": right["table"],
                        "target_field": right["field"],
                        "inference": "exact_value_match",
                        "evidence_strength": "strong",
                        "intersection_samples": sorted(inter)[:5],
                        "match_count": len(inter),
                        "confidence": 0.9,
                        "status": "待确认",
                    }
                )

    write_json(out_dir / "table_index.json", table_index)
    write_json(out_dir / "field_index.json", field_index)
    write_json(out_dir / "value_sample_index.json", value_sample_index)
    write_json(out_dir / "candidate_relationships.json", candidates)

    rel_md = OUTPUTS_DIR / "reports" / "candidate_relationships.md"
    lines = ["# 候选关系", "", "| 来源 | 目标 | 推断方式 | 证据层级 | 置信度 | 状态 |", "|---|---|---|---|---:|---|"]
    for rel in candidates[:500]:
        lines.append(
            f"| {rel['source_table']}.{rel['source_field']} | {rel['target_table']}.{rel['target_field']} | {rel['inference']} | {rel.get('evidence_strength', 'weak')} | {rel['confidence']} | {rel['status']} |"
        )
    rel_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    conn.close()
    logger.info("indexes built: tables=%s fields=%s rels=%s", len(table_index), len(field_index), len(candidates))


if __name__ == "__main__":
    main()
