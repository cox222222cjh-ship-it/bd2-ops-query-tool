from __future__ import annotations

import click
from rich.console import Console

console = Console()


@click.command()
@click.argument("keyword")
@click.option("--db-path", default="data/db/config_tables.sqlite", show_default=True)
def main(keyword: str, db_path: str) -> None:
    """最小物品聚合查询入口骨架。"""
    console.print(f"[cyan]查询关键词[/cyan]：{keyword}")
    console.print(f"[cyan]数据库[/cyan]：{db_path}")
    console.print("[yellow]TODO[/yellow]：先查物品主表，再回溯任务、礼包、奖励、强化引用链。")


if __name__ == "__main__":
    main()
