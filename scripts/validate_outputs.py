from __future__ import annotations

from pathlib import Path

import click
from rich.console import Console

console = Console()

REQUIRED_OUTPUTS = [
    "data/cache/tables_manifest.json",
    "data/cache/raw_schema.json",
    "data/cache/parse_failures.json",
    "outputs/sqlite/game_tables.db",
    "outputs/intermediate/table_index.json",
    "outputs/intermediate/field_index.json",
    "outputs/intermediate/value_sample_index.json",
    "outputs/intermediate/candidate_relationships.json",
    "outputs/intermediate/domain_candidates.json",
    "outputs/reports/table_inventory.md",
    "outputs/reports/field_dictionary.md",
    "outputs/reports/candidate_relationships.md",
    "outputs/reports/domain_candidates_report.md",
    "outputs/reports/unknown_fields_report.md",
    "outputs/reports/scan_failures.md",
]


@click.command()
def main() -> None:
    missing = [path for path in REQUIRED_OUTPUTS if not Path(path).exists()]
    if missing:
        console.print("[red]缺失产物[/red]")
        for item in missing:
            console.print(f" - {item}")
        raise SystemExit(1)
    console.print("[green]第一阶段最小闭环产物已齐全[/green]")


if __name__ == "__main__":
    main()
