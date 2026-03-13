from __future__ import annotations

import click
from rich.console import Console

console = Console()


@click.command()
@click.option("--db-path", default="data/db/config_tables.sqlite", show_default=True)
@click.option("--output-dir", default="data/indexes", show_default=True)
def main(db_path: str, output_dir: str) -> None:
    """构建字段 / 枚举 / 关系索引骨架。"""
    console.print(f"[cyan]数据库[/cyan]：{db_path}")
    console.print(f"[cyan]输出目录[/cyan]：{output_dir}")
    console.print("[yellow]TODO[/yellow]：生成 table_registry / field_registry / enum_profiles / relation_candidates。")


if __name__ == "__main__":
    main()
