from __future__ import annotations

import hashlib
import re
import sqlite3
from pathlib import Path
from typing import Any

import click

from common import OUTPUTS_DIR, read_json


def sanitize_keyword_for_filename(keyword: str) -> str:
    digest = hashlib.sha1(keyword.encode("utf-8")).hexdigest()[:8]

    sanitized = keyword.strip().replace("..", "_")
    sanitized = re.sub(r"[\\/]+", "_", sanitized)
    sanitized = re.sub(r"[^0-9A-Za-z._-]", "_", sanitized)
    sanitized = sanitized.strip("._-")

    is_safe_ascii_unchanged = bool(re.fullmatch(r"[0-9A-Za-z._-]+", keyword)) and keyword == sanitized
    if is_safe_ascii_unchanged:
        return sanitized
    if not sanitized:
        return f"query_{digest}"
    return f"{sanitized}_{digest}"


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

    lines = [f"# 查询结果：{keyword}", "", "## 命中基础信息", ""]
    if matched_rows:
        for item in matched_rows[:20]:
            lines.append(f"- 表 `{item['table']}` 字段 `{item['field']}` 命中：`{item['record']}`")
    else:
        lines.append("- 未命中记录。")

    lines.extend(["", "## 候选关联（待确认）", ""])
    if related:
        for rel in related[:50]:
            lines.append(
                f"- `{rel['source_table']}.{rel['source_field']}` -> `{rel['target_table']}.{rel['target_field']}` "
                f"({rel['inference']}, confidence={rel['confidence']}, {rel['status']})"
            )
    else:
        lines.append("- 暂无候选关联。")

    report = Path(output) if output else build_default_report_path(keyword)
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines))
    print(f"\n报告输出: {report}")

    conn.close()


if __name__ == "__main__":
    main()
