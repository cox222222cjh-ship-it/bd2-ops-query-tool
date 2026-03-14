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


def relation_categories(rel: dict[str, Any], table_domains: dict[str, set[str]]) -> list[str]:
    source_table = str(rel.get("source_table", "")).strip()
    target_table = str(rel.get("target_table", "")).strip()
    domains = set()
    domains.update(table_domains.get(source_table, set()))
    domains.update(table_domains.get(target_table, set()))

    inferred_text = " ".join(
        [
            str(rel.get("source_table", "")),
            str(rel.get("source_field", "")),
            str(rel.get("target_table", "")),
            str(rel.get("target_field", "")),
            str(rel.get("inference", "")),
        ]
    ).lower()

    # 并集策略：域线索 + 文本线索；按固定类别顺序稳定去重。
    merged_categories: list[str] = []
    for category, aliases in CATEGORY_DOMAIN_ALIASES.items():
        domain_hit = any(domain in aliases for domain in domains)
        text_hit = any(alias in inferred_text for alias in aliases)
        if domain_hit or text_hit:
            merged_categories.append(category)

    return merged_categories


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


def table_exists(conn: sqlite3.Connection, table: str) -> bool:
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name = ? LIMIT 1",
        (table,),
    ).fetchone()
    return row is not None


def table_columns(conn: sqlite3.Connection, table: str) -> list[str]:
    if not table_exists(conn, table):
        return []
    return [c[1] for c in conn.execute(f'PRAGMA table_info("{table}")').fetchall()]


def query_exact_rows(
    conn: sqlite3.Connection,
    table: str,
    column: str,
    value: str,
    limit: int = 3,
) -> list[dict[str, Any]]:
    columns = table_columns(conn, table)
    if not columns or column not in columns:
        return []
    rows = conn.execute(
        f'SELECT * FROM "{table}" WHERE CAST("{column}" AS TEXT) = ? LIMIT {limit}',
        (value,),
    ).fetchall()
    return [dict(zip(columns, row)) for row in rows]


def collect_key_business_paths(
    conn: sqlite3.Connection,
    matched_rows: list[dict[str, Any]],
    relationships: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    item_rows = [row for row in matched_rows if row.get("table") == "ItemTable"]
    item_tids: list[str] = []
    for row in item_rows:
        tid = str(row.get("record", {}).get("TID", "")).strip()
        if tid and tid not in item_tids:
            item_tids.append(tid)

    path_cards: list[dict[str, Any]] = []
    if not item_tids:
        return path_cards

    def add_direct_card(path_name: str, evidence_lines: list[str]) -> None:
        if not evidence_lines:
            return
        path_cards.append(
            {
                "path": path_name,
                "evidence_level": "直接证据",
                "status": "可复核",
                "lines": evidence_lines,
            }
        )

    shop_evidence: list[str] = []
    box_evidence: list[str] = []
    drop_evidence: list[str] = []
    production_evidence: list[str] = []
    skill_evidence: list[str] = []

    for tid in item_tids:
        sale_hits = query_exact_rows(conn, "SaleTable", "ItemTID", tid)
        if sale_hits:
            shop_evidence.append(f"ItemTable.TID={tid} -> SaleTable.ItemTID（命中 {len(sale_hits)} 条）")

        cash_hits = query_exact_rows(conn, "CashShopInfo", "ItemId", tid)
        if cash_hits:
            shop_evidence.append(f"ItemTable.TID={tid} -> CashShopInfo.ItemId（命中 {len(cash_hits)} 条）")

        box_fields = [c for c in table_columns(conn, "ItemBoxTable") if c.lower().startswith("boxitem")]
        for field in box_fields:
            hits = query_exact_rows(conn, "ItemBoxTable", field, tid)
            if hits:
                box_evidence.append(f"ItemTable.TID={tid} -> ItemBoxTable.{field}（命中 {len(hits)} 条）")

        drop_fields = [c for c in table_columns(conn, "ItemDropTable") if c.lower().startswith("dropitem")]
        for field in drop_fields:
            hits = query_exact_rows(conn, "ItemDropTable", field, tid)
            if hits:
                drop_evidence.append(f"ItemTable.TID={tid} -> ItemDropTable.{field}（命中 {len(hits)} 条）")

        product_hits = query_exact_rows(conn, "ProductItemTable", "CompleteItemTID", tid)
        if product_hits:
            production_evidence.append(
                f"ItemTable.TID={tid} <- ProductItemTable.CompleteItemTID（命中 {len(product_hits)} 条，疑似产出链路）"
            )

    seen_skill_pairs: set[tuple[str, str]] = set()
    for row in item_rows:
        tid = str(row.get("record", {}).get("TID", "")).strip()
        use_skill_tid = str(row.get("record", {}).get("UseSkillTID", "")).strip()
        if not tid or not use_skill_tid or use_skill_tid in {"0", "", "None", "null"}:
            continue
        pair = (tid, use_skill_tid)
        if pair in seen_skill_pairs:
            continue
        seen_skill_pairs.add(pair)
        skill_hits = query_exact_rows(conn, "SkillTable", "TID", use_skill_tid)
        if skill_hits:
            skill_evidence.append(
                f"ItemTable.TID={tid}.UseSkillTID={use_skill_tid} -> SkillTable.TID（命中 {len(skill_hits)} 条）"
            )
        else:
            skill_evidence.append(
                f"ItemTable.TID={tid}.UseSkillTID={use_skill_tid} -> SkillTable.TID（未命中，待确认数据一致性）"
            )

    add_direct_card("商店链路", shop_evidence)
    add_direct_card("箱子投放链路", box_evidence)
    add_direct_card("掉落链路", drop_evidence)
    add_direct_card("制作产出链路", production_evidence)
    add_direct_card("使用技能触发链路", skill_evidence)

    candidate_focus = [
        (("ItemTable", "TID"), ("SaleTable", "ItemTID"), "商店链路（SaleTable）"),
        (("ItemTable", "TID"), ("CashShopInfo", "ItemId"), "商店链路（CashShopInfo）"),
        (("ItemTable", "TID"), ("ItemBoxTable", "BoxItem"), "箱子投放链路"),
        (("ItemTable", "TID"), ("ItemDropTable", "DropItem"), "掉落链路"),
        (("ProductItemTable", "CompleteItemTID"), ("ItemTable", "TID"), "制作产出链路"),
        (("ItemTable", "UseSkillTID"), ("SkillTable", "TID"), "使用技能触发链路"),
    ]

    candidate_lines: list[str] = []
    for rel in relationships:
        source_table = str(rel.get("source_table", ""))
        target_table = str(rel.get("target_table", ""))
        source_field = str(rel.get("source_field", ""))
        target_field = str(rel.get("target_field", ""))
        for left, right, label in candidate_focus:
            forward = (
                source_table == left[0]
                and source_field.lower().startswith(left[1].lower())
                and target_table == right[0]
                and target_field.lower().startswith(right[1].lower())
            )
            backward = (
                source_table == right[0]
                and source_field.lower().startswith(right[1].lower())
                and target_table == left[0]
                and target_field.lower().startswith(left[1].lower())
            )
            if forward or backward:
                candidate_lines.append(
                    f"{label}：{source_table}.{source_field} -> {target_table}.{target_field} "
                    f"（{rel.get('inference', '候选推断')}，状态={rel.get('status', '待确认')}）"
                )
                break

    if candidate_lines:
        deduped = list(dict.fromkeys(candidate_lines))[:20]
        path_cards.append(
            {
                "path": "关键候选链路补充",
                "evidence_level": "候选推断",
                "status": "待确认",
                "lines": deduped,
            }
        )

    return path_cards


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
                rel_status = str(rel.get("status", "")).strip() or "待确认"
                lines.append(
                    f"- `{rel['source_table']}.{rel['source_field']}` -> `{rel['target_table']}.{rel['target_field']}` "
                    f"({rel['inference']}, confidence={rel['confidence']}, 状态={rel_status})"
                )
        else:
            lines.append("- 暂无候选（待确认）")
        lines.append("")

    lines.append(f"### {UNCATEGORIZED_LABEL}")
    uncategorized_bucket = category_items.get(UNCATEGORIZED_KEY, [])
    if uncategorized_bucket:
        for rel in uncategorized_bucket[:50]:
            rel_status = str(rel.get("status", "")).strip() or "待确认"
            lines.append(
                f"- `{rel['source_table']}.{rel['source_field']}` -> `{rel['target_table']}.{rel['target_field']}` "
                f"({rel['inference']}, confidence={rel['confidence']}, 状态={rel_status})"
            )
    else:
        lines.append("- 暂无候选（待确认）")
    lines.append("")

    key_cards = collect_key_business_paths(conn, matched_rows, relationships)
    lines.extend(["", "## 关键链路（高优先）", ""])
    if key_cards:
        for card in key_cards:
            lines.append(f"### {card['path']}")
            lines.append(f"- 证据层级：{card['evidence_level']}")
            lines.append(f"- 状态：{card['status']}")
            for detail in card["lines"]:
                lines.append(f"  - {detail}")
            lines.append("")
    else:
        lines.append("- 暂无可展开的关键链路。")
        lines.append("")

    report = Path(output) if output else build_default_report_path(keyword)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    print(f"\n报告输出: {report}")

    conn.close()


if __name__ == "__main__":
    main()
