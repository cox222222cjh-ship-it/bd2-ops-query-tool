from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import click
import pandas as pd
from charset_normalizer import from_path

from common import OUTPUTS_DIR, PROJECT_ROOT, ensure_dirs, now_iso, setup_logging, write_json

SUPPORTED_SUFFIXES = {".csv", ".tsv", ".txt", ".ctrl"}
logger = setup_logging("scan_tables")


def detect_encoding(file_path: Path) -> str:
    result = from_path(file_path).best()
    return result.encoding if result and result.encoding else "utf-8"


def detect_delimiter(file_path: Path, encoding: str) -> str:
    sample = file_path.read_text(encoding=encoding, errors="replace")[:4096]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t|;")
        return dialect.delimiter
    except csv.Error:
        return ","


def parse_table(file_path: Path) -> tuple[pd.DataFrame, str, str]:
    encoding = detect_encoding(file_path)
    delimiter = detect_delimiter(file_path, encoding)
    try:
        dataframe = pd.read_csv(
            file_path,
            sep=delimiter,
            encoding=encoding,
            dtype=str,
            keep_default_na=False,
            engine="python",
        )
    except Exception:
        dataframe = pd.read_csv(
            file_path,
            sep=delimiter,
            encoding=encoding,
            dtype=str,
            keep_default_na=False,
            engine="python",
            on_bad_lines="skip",
        )
    return dataframe, encoding, delimiter


def field_profile(series: pd.Series) -> dict[str, Any]:
    normalized = series.astype(str).str.strip()
    non_empty = normalized[(normalized != "") & (~normalized.str.lower().isin(["nan", "none", "null"]))]
    row_count = len(series)
    non_null_count = len(non_empty)
    unique_count = int(non_empty.nunique(dropna=True))
    examples = non_empty.drop_duplicates().head(5).tolist()
    top_values = non_empty.value_counts().head(5)
    return {
        "name": series.name,
        "dtype": str(series.dtype),
        "non_null_rate": round((non_null_count / row_count), 4) if row_count else 0.0,
        "unique_count": unique_count,
        "unique_rate": round((unique_count / non_null_count), 4) if non_null_count else 0.0,
        "sample_values": examples,
        "top_values": [{"value": str(idx), "count": int(cnt)} for idx, cnt in top_values.items()],
    }


def find_pk_candidates(df: pd.DataFrame, profiles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    total_rows = len(df)
    candidates: list[dict[str, Any]] = []
    for profile in profiles:
        if total_rows == 0:
            continue
        name = profile["name"]
        unique_count = profile["unique_count"]
        non_null_rate = profile["non_null_rate"]
        is_full_unique = unique_count == total_rows and non_null_rate == 1.0
        looks_like_id = name.lower().endswith(("id", "tid"))
        high_unique = unique_count >= int(total_rows * 0.98)
        if is_full_unique or (looks_like_id and high_unique and non_null_rate > 0.95):
            candidates.append(
                {
                    "field": name,
                    "confidence": 0.95 if is_full_unique else 0.75,
                    "status": "待确认",
                    "reason": "full_unique" if is_full_unique else "id_like_high_uniqueness",
                }
            )
    return candidates


@click.command()
@click.option("--input-dir", default=str(PROJECT_ROOT / "data" / "current"), show_default=True)
@click.option("--manifest", default=str(PROJECT_ROOT / "data" / "cache" / "tables_manifest.json"), show_default=True)
@click.option("--schema", default=str(PROJECT_ROOT / "data" / "cache" / "raw_schema.json"), show_default=True)
@click.option("--failures", default=str(PROJECT_ROOT / "data" / "cache" / "parse_failures.json"), show_default=True)
def main(input_dir: str, manifest: str, schema: str, failures: str) -> None:
    ensure_dirs()
    src = Path(input_dir)
    manifest_records: list[dict[str, Any]] = []
    schema_payload: dict[str, Any] = {}
    failures_payload: list[dict[str, Any]] = []

    files = sorted([p for p in src.rglob("*") if p.is_file() and p.suffix.lower() in SUPPORTED_SUFFIXES])
    logger.info("scan start, files=%s", len(files))

    for file_path in files:
        rel_path = str(file_path.relative_to(PROJECT_ROOT))
        try:
            df, encoding, delimiter = parse_table(file_path)
            profiles = [field_profile(df[col]) for col in df.columns]
            pk_candidates = find_pk_candidates(df, profiles)
            record = {
                "table_name": file_path.stem,
                "file_name": file_path.name,
                "relative_path": rel_path,
                "encoding": encoding,
                "delimiter": delimiter,
                "row_count": int(len(df)),
                "column_count": int(len(df.columns)),
                "status": "scanned",
                "scanned_at": now_iso(),
            }
            manifest_records.append(record)
            schema_key = rel_path
            schema_payload[schema_key] = {
                "file": rel_path,
                "fields": profiles,
                "row_count": int(len(df)),
                "column_count": int(len(df.columns)),
                "pk_candidates": pk_candidates,
                "status": "scanned",
            }
        except Exception as exc:
            logger.exception("scan failed: %s", rel_path)
            failure = {"file": rel_path, "status": "failed", "error": str(exc), "scanned_at": now_iso()}
            failures_payload.append(failure)
            manifest_records.append(
                {
                    "table_name": file_path.stem,
                    "file_name": file_path.name,
                    "relative_path": rel_path,
                    "status": "failed",
                    "scanned_at": now_iso(),
                }
            )

    write_json(Path(manifest), manifest_records)
    write_json(Path(schema), schema_payload)
    write_json(Path(failures), failures_payload)

    scan_failures_md = OUTPUTS_DIR / "reports" / "scan_failures.md"
    lines = ["# 扫描失败清单\n"]
    if failures_payload:
        for item in failures_payload:
            lines.append(f"- `{item['file']}`: {item['error']}")
    else:
        lines.append("- 无失败记录。")
    scan_failures_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    inventory_md = OUTPUTS_DIR / "reports" / "table_inventory.md"
    rows = ["# 表清单", "", "| 表名 | 行数 | 列数 | 编码 | 分隔符 | 状态 |", "|---|---:|---:|---|---|---|"]
    for rec in manifest_records:
        rows.append(
            f"| {rec.get('table_name', '')} | {rec.get('row_count', 0)} | {rec.get('column_count', 0)} | {rec.get('encoding', '-') } | {rec.get('delimiter', '-') } | {rec.get('status')} |"
        )
    inventory_md.write_text("\n".join(rows) + "\n", encoding="utf-8")

    logger.info("scan completed: scanned=%s failed=%s", len(schema_payload), len(failures_payload))


if __name__ == "__main__":
    main()
