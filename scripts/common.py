from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
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
OUTPUTS_DIR = PROJECT_ROOT / "outputs"

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
    OUTPUTS_DIR / "reports",
    OUTPUTS_DIR / "intermediate",
    OUTPUTS_DIR / "sqlite",
]


def setup_logging(name: str) -> logging.Logger:
    ensure_dirs([LOGS_DIR])
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")

    file_handler = logging.FileHandler(LOGS_DIR / f"{name}.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


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


def read_json(path: Path, default: object | None = None) -> object:
    if not path.exists():
        if default is None:
            raise FileNotFoundError(path)
        return default
    return json.loads(path.read_text(encoding="utf-8"))
