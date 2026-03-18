from __future__ import annotations

import sqlite3
from pathlib import Path


def schema_path(repo_root: Path) -> Path:
    return repo_root / "agent-definitions" / "system" / "schema" / "001_initial.sql"


def apply_schema(connection: sqlite3.Connection, sql_path: Path) -> None:
    connection.executescript(sql_path.read_text())

