from __future__ import annotations

import hashlib
import re
import sqlite3
from pathlib import Path
from typing import Any

import click

from common import OUTPUTS_DIR, read_json


CATEGORY_DOMAIN_ALIASES: dict[str, set[str]] = {
    "rewards": {"reward", "award", "item"},
    "quests": {"task", "quest", "mission"},
    "gift packs": {"gift", "package", "bundle", "mall"},
    "shops": {"shop", "store", "mall"},
    "drops": {"drop", "loot"},
    "activities": {"activity", "event"},
}
UNCATEGORIZED_KEY = "uncategorized"
UNCATEGORIZED_LABEL = "未分类候选（待确认）"


def normalize_domain(value: str) -> str:
    return value.strip().lower().replace("_", " ")


def build_table_domain_map(domain_candidates: list[dict[str, Any]]) -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = {}
    for row in domain_candidates:
        table = str(row.get("table", "")).strip()
        domain = normalize_domain(str(row.get("domain", "")))
        if not table or not domain:
            continue
        mapping.setdefault(table, set()).add(domain)
    return mapping


def relation_categories(rel: dict[str, Any], table_domains: dict[str, set[str]]) -> set[str]:
    source_table = str(rel.get("source_table", "")).strip()
    target_table = str(rel.get("target_table", "")).strip()
    domains = set()
    domains.update(table_domains.get(source_table, set()))
    domains.update(table_domains.get(target_table, set()))

    categories: set[str] = set()
    for category, aliases in CATEGORY_DOMAIN_ALIASES.items():
        if any(domain in aliases for domain in domains):
            categories.add(category)

    if not categories:
        inferred_text = " ".join(
            [
                str(rel.get("source_table", "")),
                str(rel.get("source_field", "")),
                str(rel.get("target_table", "")),
                str(rel.get("target_field", "")),
                str(rel.get("inference", "")),
            ]
        ).lower()
        for category, aliases in CATEGORY_DOMAIN_ALIASES.items():
            if any(alias in inferred_text for alias in aliases):
                categories.add(category)
    return categories


def sanitize_keyword_for_filename(keyword: str) -> str:
    digest = hashlib.sha1(keyword.encode("utf-8")).hexdigest()

    sanitized = keyword.strip().replace("..", "_")
    sanitized = re.sub(r"[\\/]+", "_", sanitized)
    sanitized = re.sub(r"[^0-9A-Za-z._-]", "_", sanitized)
    sanitized = sanitized.strip("._-")

    is_safe_ascii_unchanged = bool(re.fullmatch(r"[0-9A-Za-z._-]+", keyword)) and keyword == sanitized
    if is_safe_ascii_unchanged:
        return sanitized
    if not sanitized:
        return f"~query_{digest}"
    return f"~{sanitized}_{digest}"


def build_default_report_path(keyword: str) -> Path:
    safe_keyword = sanitize_keyword_for_filename(keyword)
    filename = Path(f"query_item_{safe_keyword}.md").name
    return OUTPUTS_DIR / "reports" / filename


@click.command()
@click.argument("keyword")
@click.option("--db-path", default="outputs/sqlite/game_tables.db", show_default=True)
@click.option("--output", default="", show_default=False, help="输出 markdown 路径")
def main(keyword: str, db_path: str, output: str) -> None:
    conn = sqlite3.connect(db_path)
    field_index = read_json(OUTPUTS_DIR / "intermediate" / "field_index.json", default=[])
    relationships = read_json(OUTPUTS_DIR / "intermediate" / "candidate_relationships.json", default=[])
    domain_candidates = read_json(OUTPUTS_DIR / "intermediate" / "domain_candidates.json", default=[])
    table_domains = build_table_domain_map(domain_candidates)

    key_lower = keyword.lower()
    matched_rows: list[dict[str, Any]] = []
    matched_tables: set[str] = set()

    for field in field_index:
        table = field["table"]
        column = field["field"]
        low_col = column.lower()
        if not any(token in low_col for token in ["item", "name", "tid", "id"]):
            continue

        rows = conn.execute(
            f'SELECT * FROM "{table}" WHERE CAST("{column}" AS TEXT) = ? OR LOWER(CAST("{column}" AS TEXT)) LIKE ? LIMIT 10',
            (keyword, f"%{key_lower}%"),
        ).fetchall()
        if rows:
            headers = [c[1] for c in conn.execute(f'PRAGMA table_info("{table}")').fetchall()]
            for row in rows[:3]:
                matched_rows.append({"table": table, "field": column, "record": dict(zip(headers, row))})
            matched_tables.add(table)

    related = [
        rel
        for rel in relationships
        if rel["source_table"] in matched_tables or rel["target_table"] in matched_tables
    ]

    category_items: dict[str, list[dict[str, Any]]] = {k: [] for k in CATEGORY_DOMAIN_ALIASES}
    category_items[UNCATEGORIZED_KEY] = []
    for rel in related:
        categories = relation_categories(rel, table_domains)
        if categories:
            for category in categories:
                category_items[category].append(rel)
        else:
            category_items[UNCATEGORIZED_KEY].append(rel)

    lines = [f"# 查询结果：{keyword}", "", "## 直接引用（已命中）", ""]
    if matched_rows:
        for item in matched_rows[:20]:
            lines.append(f"- 表 `{item['table']}` 字段 `{item['field']}` 命中：`{item['record']}`")
    else:
        lines.append("- 未命中记录。")

    lines.extend(["", "## 候选推断（待确认）", ""])
    for category in CATEGORY_DOMAIN_ALIASES:
        lines.append(f"### {category}")
        bucket = category_items.get(category, [])
        if bucket:
            for rel in bucket[:50]:
                lines.append(
                    f"- `{rel['source_table']}.{rel['source_field']}` -> `{rel['target_table']}.{rel['target_field']}` "
                    f"({rel['inference']}, confidence={rel['confidence']}, 状态=待确认)"
                )
        else:
            lines.append("- 暂无候选（待确认）")
        lines.append("")

    lines.append(f"### {UNCATEGORIZED_LABEL}")
    uncategorized_bucket = category_items.get(UNCATEGORIZED_KEY, [])
    if uncategorized_bucket:
        for rel in uncategorized_bucket[:50]:
            lines.append(
                f"- `{rel['source_table']}.{rel['source_field']}` -> `{rel['target_table']}.{rel['target_field']}` "
                f"({rel['inference']}, confidence={rel['confidence']}, 状态=待确认)"
            )
    else:
        lines.append("- 暂无候选（待确认）")
    lines.append("")

    report = Path(output) if output else build_default_report_path(keyword)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    print(f"\n报告输出: {report}")

    conn.close()


if __name__ == "__main__":
    main()
