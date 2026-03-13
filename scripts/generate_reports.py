from __future__ import annotations

import click
from rich.console import Console

console = Console()


@click.command()
@click.option("--indexes-dir", default="data/indexes", show_default=True)
@click.option("--docs-dir", default="docs", show_default=True)
def main(indexes_dir: str, docs_dir: str) -> None:
    """根据索引生成 Markdown 报告骨架。"""
    console.print(f"[cyan]读取索引[/cyan]：{indexes_dir}")
    console.print(f"[cyan]输出文档[/cyan]：{docs_dir}")
    console.print("[yellow]TODO[/yellow]：生成 scan_summary / candidate_tables / candidate_relations / field_dictionary_draft。")


if __name__ == "__main__":
    main()
