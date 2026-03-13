from __future__ import annotations

import click
from rich.console import Console

console = Console()


@click.command()
@click.option("--indexes-dir", default="data/indexes", show_default=True)
@click.option("--rules-file", default="rules/domain_hints.yaml", show_default=True)
def main(indexes_dir: str, rules_file: str) -> None:
    """识别物品 / 任务 / 礼包 / 强化等候选业务域。"""
    console.print(f"[cyan]索引目录[/cyan]：{indexes_dir}")
    console.print(f"[cyan]规则文件[/cyan]：{rules_file}")
    console.print("[yellow]TODO[/yellow]：按字段名、表名、值分布输出 domain_candidates.json。")


if __name__ == "__main__":
    main()
