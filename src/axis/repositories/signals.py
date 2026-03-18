from __future__ import annotations

import sqlite3
from datetime import datetime

from axis.domain.signals import Signal, SignalRoute


def _parse_timestamp(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


class SignalRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def add_signal(self, signal: Signal) -> None:
        self.connection.execute(
            """
            INSERT INTO signals (
              id, source_document_id, signal_source, signal_type, origin, observed_at,
              normalized_statement, summary_text, rank_label, value_label, status, payload_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                signal.id,
                signal.source_document_id,
                signal.signal_source,
                signal.signal_type,
                signal.origin,
                signal.observed_at.isoformat() if signal.observed_at else None,
                signal.normalized_statement,
                signal.summary_text,
                signal.rank_label,
                signal.value_label,
                signal.status,
                signal.payload_json,
            ),
        )

    def add_route(self, route: SignalRoute) -> None:
        self.connection.execute(
            """
            INSERT INTO signal_routes (
              id, signal_id, recipient_agent_id, route_reason_text, route_basis_json,
              inbox_status, first_seen_at, processed_at, handling_note_text
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                route.id,
                route.signal_id,
                route.recipient_agent_id,
                route.route_reason_text,
                route.route_basis_json,
                route.inbox_status,
                route.first_seen_at.isoformat() if route.first_seen_at else None,
                route.processed_at.isoformat() if route.processed_at else None,
                route.handling_note_text,
            ),
        )

    def inbox_for_recipient(self, recipient_agent_id: str, inbox_status: str = "unread") -> list[SignalRoute]:
        rows = self.connection.execute(
            """
            SELECT id, signal_id, recipient_agent_id, route_reason_text, route_basis_json,
                   routed_at, inbox_status, first_seen_at, processed_at, handling_note_text
            FROM signal_routes
            WHERE recipient_agent_id = ? AND inbox_status = ?
            ORDER BY routed_at ASC
            """,
            (recipient_agent_id, inbox_status),
        ).fetchall()
        return [
            SignalRoute(
                id=row["id"],
                signal_id=row["signal_id"],
                recipient_agent_id=row["recipient_agent_id"],
                route_reason_text=row["route_reason_text"],
                route_basis_json=row["route_basis_json"],
                routed_at=_parse_timestamp(row["routed_at"]),
                inbox_status=row["inbox_status"],
                first_seen_at=_parse_timestamp(row["first_seen_at"]),
                processed_at=_parse_timestamp(row["processed_at"]),
                handling_note_text=row["handling_note_text"],
            )
            for row in rows
        ]

    def mark_route_processed(
        self,
        signal_id: str,
        recipient_agent_id: str,
        handling_note_text: str | None = None,
    ) -> None:
        self.connection.execute(
            """
            UPDATE signal_routes
            SET inbox_status = 'processed',
                processed_at = CURRENT_TIMESTAMP,
                handling_note_text = COALESCE(?, handling_note_text)
            WHERE signal_id = ? AND recipient_agent_id = ?
            """,
            (handling_note_text, signal_id, recipient_agent_id),
        )

