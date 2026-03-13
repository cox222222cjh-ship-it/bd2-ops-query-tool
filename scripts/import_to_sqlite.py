from __future__ import annotations

import sqlite3
from pathlib import Path

import click
import pandas as pd

from common import PROJECT_ROOT, ensure_dirs, now_iso, read_json, setup_logging

logger = setup_logging("import_to_sqlite")


def normalize_table_name(name: str) -> str:
    safe = "".join(ch if ch.isalnum() or ch == "_" else "_" for ch in name)
    return safe.strip("_") or "table"


def load_table(file_path: Path, encoding: str, delimiter: str) -> pd.DataFrame:
    return pd.read_csv(
        file_path,
        sep=delimiter,
        encoding=encoding,
        dtype=str,
        keep_default_na=False,
        engine="python",
        on_bad_lines="skip",
    )


@click.command()
@click.option("--manifest", default="data/cache/tables_manifest.json", show_default=True)
@click.option("--db-path", default="outputs/sqlite/game_tables.db", show_default=True)
def main(manifest: str, db_path: str) -> None:
    ensure_dirs()
    manifest_payload = read_json(Path(manifest), default=[])
    db = Path(db_path)
    db.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS table_metadata (
            source_table_name TEXT,
            sqlite_table_name TEXT,
            source_file TEXT,
            row_count INTEGER,
            column_count INTEGER,
            import_status TEXT,
            imported_at TEXT
        )
        """
    )
    conn.execute("DELETE FROM table_metadata")

    table_name_seen: dict[str, int] = {}
    for item in manifest_payload:
        if item.get("status") != "scanned":
            continue
        source_name = item["table_name"]
        sqlite_name = normalize_table_name(source_name)
        table_name_seen[sqlite_name] = table_name_seen.get(sqlite_name, 0) + 1
        if table_name_seen[sqlite_name] > 1:
            sqlite_name = f"{sqlite_name}_{table_name_seen[sqlite_name]}"

        source_file = PROJECT_ROOT / item["relative_path"]
        status = "imported"
        row_count = 0
        column_count = 0
        try:
            df = load_table(source_file, item["encoding"], item["delimiter"])
            row_count = int(len(df))
            column_count = int(len(df.columns))
            df.to_sql(sqlite_name, conn, if_exists="replace", index=False)
            logger.info("imported %s => %s rows=%s", source_name, sqlite_name, row_count)
        except Exception as exc:
            status = f"failed: {exc}"
            logger.exception("import failed %s", source_file)

        conn.execute(
            "INSERT INTO table_metadata VALUES (?, ?, ?, ?, ?, ?, ?)",
            (source_name, sqlite_name, item["relative_path"], row_count, column_count, status, now_iso()),
        )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
