from __future__ import annotations

from datetime import datetime, timezone

import click
from rich.console import Console

from common import DOCS_DIR, OUTPUTS_DIR, PROJECT_ROOT, REQUIRED_DIRS, ensure_dirs, ensure_gitkeep, write_json

console = Console()

PLACEHOLDER_FILES = {
    PROJECT_ROOT / "data" / "cache" / "tables_manifest.json": [],
    PROJECT_ROOT / "data" / "cache" / "raw_schema.json": {},
    PROJECT_ROOT / "data" / "cache" / "parse_failures.json": [],
    PROJECT_ROOT / "data" / "indexes" / "table_registry.json": [],
    PROJECT_ROOT / "data" / "indexes" / "field_registry.json": [],
    PROJECT_ROOT / "data" / "indexes" / "enum_profiles.json": {},
    PROJECT_ROOT / "data" / "indexes" / "relation_candidates.json": [],
    PROJECT_ROOT / "data" / "indexes" / "domain_candidates.json": [],
    OUTPUTS_DIR / "intermediate" / "table_index.json": [],
    OUTPUTS_DIR / "intermediate" / "field_index.json": [],
    OUTPUTS_DIR / "intermediate" / "value_sample_index.json": [],
    OUTPUTS_DIR / "intermediate" / "candidate_relationships.json": [],
}

DOC_STUBS = {
    DOCS_DIR / "scan_summary.md": "# 扫描总结\n\n待生成。\n",
    DOCS_DIR / "candidate_tables.md": "# 候选业务表\n\n待生成。\n",
    DOCS_DIR / "candidate_relations.md": "# 候选关系\n\n待生成。\n",
    DOCS_DIR / "field_dictionary_draft.md": "# 字段字典草案\n\n待生成。\n",
    DOCS_DIR / "unknown_fields_todo.md": "# 待确认字段\n\n待生成。\n",
    DOCS_DIR / "item_query_minimum_path.md": "# 物品查询最小链路\n\n待生成。\n",
    OUTPUTS_DIR / "reports" / "table_inventory.md": "# 表清单\n\n待生成。\n",
    OUTPUTS_DIR / "reports" / "field_dictionary.md": "# 字段字典\n\n待生成。\n",
    OUTPUTS_DIR / "reports" / "candidate_relationships.md": "# 候选关系\n\n待生成。\n",
    OUTPUTS_DIR / "reports" / "domain_candidates_report.md": "# 业务域候选归类\n\n待生成。\n",
    OUTPUTS_DIR / "reports" / "unknown_fields_report.md": "# 待确认字段\n\n待生成。\n",
    OUTPUTS_DIR / "reports" / "scan_failures.md": "# 扫描失败清单\n\n待生成。\n",
}


@click.command()
@click.option("--with-placeholders/--no-placeholders", default=True, show_default=True, help="是否初始化占位 JSON / Markdown 文件")
def main(with_placeholders: bool) -> None:
    ensure_dirs(REQUIRED_DIRS)
    ensure_gitkeep(
        [
            PROJECT_ROOT / "data" / "cache",
            PROJECT_ROOT / "data" / "db",
            PROJECT_ROOT / "data" / "indexes",
            PROJECT_ROOT / "data" / "snapshots",
            DOCS_DIR / "generated",
            PROJECT_ROOT / "tests",
            PROJECT_ROOT / "logs",
            OUTPUTS_DIR / "reports",
            OUTPUTS_DIR / "intermediate",
            OUTPUTS_DIR / "sqlite",
        ]
    )

    if with_placeholders:
        for path, payload in PLACEHOLDER_FILES.items():
            if not path.exists():
                write_json(path, payload)
        for path, content in DOC_STUBS.items():
            if not path.exists():
                path.write_text(content, encoding="utf-8")

    manifest = PROJECT_ROOT / "data" / "cache" / "project_bootstrap.json"
    write_json(
        manifest,
        {
            "project": "霸王大陆2 配置查询器",
            "bootstrapped_at": datetime.now(timezone.utc).isoformat(),
            "project_root": str(PROJECT_ROOT),
            "with_placeholders": with_placeholders,
        },
    )
    console.print(f"[cyan]初始化完成[/cyan]：{manifest}")


if __name__ == "__main__":
    main()
