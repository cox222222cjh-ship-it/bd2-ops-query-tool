from __future__ import annotations

from pathlib import Path

import click
from rich.console import Console

from common import PROJECT_ROOT, write_json

console = Console()


@click.command()
@click.option("--input-dir", default=str(PROJECT_ROOT / "data" / "current"), show_default=True, help="原始表目录")
@click.option("--output", default=str(PROJECT_ROOT / "data" / "cache" / "tables_manifest.json"), show_default=True, help="输出 manifest")
def main(input_dir: str, output: str) -> None:
    """扫描配置表目录，生成表清单。"""
    src = Path(input_dir)
    files = [p for p in src.rglob("*") if p.is_file()]
    records = [
        {
            "file_name": p.name,
            "relative_path": str(p.relative_to(PROJECT_ROOT)),
            "size_bytes": p.stat().st_size,
            "status": "pending_scan",
        }
        for p in sorted(files)
    ]
    write_json(Path(output), records)
    console.print(f"[green]已输出表清单[/green]：{len(records)} 个文件 -> {output}")
    console.print("[yellow]下一步[/yellow]：补编码识别、分隔符识别、行列统计。")


if __name__ == "__main__":
    main()
