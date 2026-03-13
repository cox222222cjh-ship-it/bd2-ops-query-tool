from __future__ import annotations

from pathlib import Path

import click

from common import OUTPUTS_DIR, read_json


@click.command()
@click.option("--indexes-dir", default="outputs/intermediate", show_default=True)
@click.option("--reports-dir", default="outputs/reports", show_default=True)
def main(indexes_dir: str, reports_dir: str) -> None:
    idx = Path(indexes_dir)
    rpt = Path(reports_dir)
    rpt.mkdir(parents=True, exist_ok=True)

    field_index = read_json(idx / "field_index.json", default=[])

    lines = ["# 字段字典", "", "| 表 | 字段 | 非空率 | 唯一值数量 | 示例值 |", "|---|---|---:|---:|---|"]
    for row in field_index:
        samples = ", ".join(row.get("sample_values", [])[:3])
        lines.append(
            f"| {row['table']} | {row['field']} | {row['non_null_rate']} | {row['unique_count']} | {samples} |"
        )

    (rpt / "field_dictionary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # 保持 outputs 与 docs 的兼容镜像说明
    mirror = Path("docs/item_query_minimum_path.md")
    if not mirror.exists():
        mirror.write_text(
            "# 物品查询最小链路\n\n"
            "1. scan_tables.py\n"
            "2. import_to_sqlite.py\n"
            "3. build_indexes.py\n"
            "4. detect_domains.py\n"
            "5. generate_reports.py\n"
            "6. query_item.py --keyword\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
