from __future__ import annotations

from pathlib import Path

import pytest

from axis.db.connection import connect
from axis.db.schema import apply_schema, schema_path
from axis.db.uow import transaction


@pytest.fixture()
def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


@pytest.fixture()
def connection(tmp_path: Path, repo_root: Path):
    db_path = tmp_path / "axis.db"
    conn = connect(db_path)
    apply_schema(conn, schema_path(repo_root))
    with transaction(conn):
        conn.execute(
            "INSERT INTO agents (id, agent_type, definition_path, state_root) VALUES (?, ?, ?, ?)",
            ("markets-expert", "expert", "agent-definitions/agents/markets-expert", "agent-state/agents/markets-expert"),
        )
        conn.execute(
            "INSERT INTO agents (id, agent_type, definition_path, state_root) VALUES (?, ?, ?, ?)",
            ("macro-desk", "desk", "agent-definitions/agents/macro-desk", "agent-state/agents/macro-desk"),
        )
    try:
        yield conn
    finally:
        conn.close()

