from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"
RULES_DIR = PROJECT_ROOT / "rules"
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
API_DIR = PROJECT_ROOT / "api"
TESTS_DIR = PROJECT_ROOT / "tests"
LOGS_DIR = PROJECT_ROOT / "logs"

REQUIRED_DIRS = [
    DATA_DIR / "current",
    DATA_DIR / "cache",
    DATA_DIR / "indexes",
    DATA_DIR / "db",
    DATA_DIR / "snapshots",
    DOCS_DIR,
    DOCS_DIR / "generated",
    RULES_DIR,
    SCRIPTS_DIR,
    API_DIR,
    TESTS_DIR,
    LOGS_DIR,
]


def ensure_dirs(paths: Iterable[Path] = REQUIRED_DIRS) -> list[Path]:
    created: list[Path] = []
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
        created.append(path)
    return created


def ensure_gitkeep(paths: Iterable[Path]) -> None:
    for path in paths:
        marker = path / ".gitkeep"
        if not marker.exists():
            marker.write_text("", encoding="utf-8")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
