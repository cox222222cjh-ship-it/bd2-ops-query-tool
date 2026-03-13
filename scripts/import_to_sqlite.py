from __future__ import annotations

from pathlib import Path

import click
from rich.console import Console

console = Console()


@click.command()
@click.option("--manifest", default="data/cache/tables_manifest.json", show_default=True)
@click.option("--db-path", default="data/db/config_tables.sqlite", show_default=True)
def main(manifest: str, db_path: str) -> None:
    """导入 SQLite 的入口骨架。"""
    console.print(f"[cyan]待处理 manifest[/cyan]：{Path(manifest)}")
    console.print(f"[cyan]目标数据库[/cyan]：{Path(db_path)}")
    console.print("[yellow]TODO[/yellow]：读取 manifest、标准化表名、建表并导入数据。")


if __name__ == "__main__":
    main()
