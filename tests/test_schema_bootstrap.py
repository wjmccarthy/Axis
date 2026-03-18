from __future__ import annotations


def test_schema_bootstrap_creates_expected_tables(connection) -> None:
    rows = connection.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table'"
    ).fetchall()
    table_names = {row["name"] for row in rows}

    assert "agents" in table_names
    assert "documents" in table_names
    assert "signals" in table_names
    assert "signal_routes" in table_names
    assert "messages" in table_names
    assert "message_deliveries" in table_names
    assert "requests" in table_names
    assert "published_surfaces" in table_names
    assert "links" in table_names

