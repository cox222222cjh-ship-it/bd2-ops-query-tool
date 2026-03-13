from __future__ import annotations

from pathlib import Path

import click
from rich.console import Console

console = Console()

REQUIRED_OUTPUTS = [
    "data/cache/tables_manifest.json",
    "data/cache/raw_schema.json",
    "data/cache/parse_failures.json",
    "data/db/config_tables.sqlite",
    "data/indexes/table_registry.json",
    "data/indexes/field_registry.json",
    "data/indexes/enum_profiles.json",
    "data/indexes/relation_candidates.json",
    "data/indexes/domain_candidates.json",
    "docs/scan_summary.md",
    "docs/candidate_tables.md",
    "docs/candidate_relations.md",
    "docs/field_dictionary_draft.md",
    "docs/unknown_fields_todo.md",
    "docs/item_query_minimum_path.md",
]


@click.command()
def main() -> None:
    missing = [path for path in REQUIRED_OUTPUTS if not Path(path).exists()]
    if missing:
        console.print("[red]缺失产物[/red]")
        for item in missing:
            console.print(f" - {item}")
        raise SystemExit(1)
    console.print("[green]主要产物已齐全[/green]")


if __name__ == "__main__":
    main()
