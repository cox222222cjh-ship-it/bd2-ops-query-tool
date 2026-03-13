from __future__ import annotations

from datetime import datetime, UTC

import click
from rich.console import Console

from common import DOCS_DIR, PROJECT_ROOT, REQUIRED_DIRS, ensure_dirs, ensure_gitkeep, write_json

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
}

DOC_STUBS = {
    DOCS_DIR / "scan_summary.md": "# 扫描总结\n\n待生成。\n",
    DOCS_DIR / "candidate_tables.md": "# 候选业务表\n\n待生成。\n",
    DOCS_DIR / "candidate_relations.md": "# 候选关系\n\n待生成。\n",
    DOCS_DIR / "field_dictionary_draft.md": "# 字段字典草案\n\n待生成。\n",
    DOCS_DIR / "unknown_fields_todo.md": "# 待确认字段\n\n待生成。\n",
    DOCS_DIR / "item_query_minimum_path.md": "# 物品查询最小链路\n\n待生成。\n",
}


@click.command()
@click.option("--with-placeholders/--no-placeholders", default=True, show_default=True, help="是否初始化占位 JSON / Markdown 文件")
def main(with_placeholders: bool) -> None:
    created = ensure_dirs(REQUIRED_DIRS)
    ensure_gitkeep(
        [
            PROJECT_ROOT / "data" / "cache",
            PROJECT_ROOT / "data" / "db",
            PROJECT_ROOT / "data" / "indexes",
            PROJECT_ROOT / "data" / "snapshots",
            DOCS_DIR / "generated",
            PROJECT_ROOT / "tests",
            PROJECT_ROOT / "logs",
        ]
    )

    console.print(f"[green]目录已确认[/green]：{len(created)} 个")

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
            "bootstrapped_at": datetime.now(UTC).isoformat(),
            "project_root": str(PROJECT_ROOT),
            "with_placeholders": with_placeholders,
        },
    )
    console.print(f"[cyan]初始化完成[/cyan]：{manifest}")


if __name__ == "__main__":
    main()
