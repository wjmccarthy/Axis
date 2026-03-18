from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

from axis.domain.messages import Message, MessageDelivery


def _parse_timestamp(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


class MessageRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def add_message(self, message: Message) -> None:
        self.connection.execute(
            """
            INSERT INTO messages (
              id, message_type, sender_agent_id, thread_id, subject_text, body_text,
              content_path, priority, status, payload_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                message.id,
                message.message_type,
                message.sender_agent_id,
                message.thread_id,
                message.subject_text,
                message.body_text,
                str(message.content_path) if message.content_path else None,
                message.priority,
                message.status,
                message.payload_json,
            ),
        )

    def add_delivery(self, delivery: MessageDelivery) -> None:
        self.connection.execute(
            """
            INSERT INTO message_deliveries (
              id, message_id, recipient_agent_id, inbox_status, first_seen_at, processed_at,
              handling_note_text
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                delivery.id,
                delivery.message_id,
                delivery.recipient_agent_id,
                delivery.inbox_status,
                delivery.first_seen_at.isoformat() if delivery.first_seen_at else None,
                delivery.processed_at.isoformat() if delivery.processed_at else None,
                delivery.handling_note_text,
            ),
        )

    def inbox_for_recipient(self, recipient_agent_id: str, inbox_status: str = "unread") -> list[MessageDelivery]:
        rows = self.connection.execute(
            """
            SELECT id, message_id, recipient_agent_id, inbox_status, delivered_at,
                   first_seen_at, processed_at, handling_note_text
            FROM message_deliveries
            WHERE recipient_agent_id = ? AND inbox_status = ?
            ORDER BY delivered_at ASC
            """,
            (recipient_agent_id, inbox_status),
        ).fetchall()
        return [
            MessageDelivery(
                id=row["id"],
                message_id=row["message_id"],
                recipient_agent_id=row["recipient_agent_id"],
                inbox_status=row["inbox_status"],
                delivered_at=_parse_timestamp(row["delivered_at"]),
                first_seen_at=_parse_timestamp(row["first_seen_at"]),
                processed_at=_parse_timestamp(row["processed_at"]),
                handling_note_text=row["handling_note_text"],
            )
            for row in rows
        ]

    def get_message(self, message_id: str) -> Message | None:
        row = self.connection.execute(
            """
            SELECT id, message_type, sender_agent_id, thread_id, subject_text, body_text,
                   content_path, priority, status, created_at, updated_at, payload_json
            FROM messages
            WHERE id = ?
            """,
            (message_id,),
        ).fetchone()
        if row is None:
            return None
        return Message(
            id=row["id"],
            message_type=row["message_type"],
            sender_agent_id=row["sender_agent_id"],
            thread_id=row["thread_id"],
            subject_text=row["subject_text"],
            body_text=row["body_text"],
            content_path=Path(row["content_path"]) if row["content_path"] else None,
            priority=row["priority"],
            status=row["status"],
            created_at=_parse_timestamp(row["created_at"]),
            updated_at=_parse_timestamp(row["updated_at"]),
            payload_json=row["payload_json"],
        )

    def mark_delivery_processed(
        self,
        message_id: str,
        recipient_agent_id: str,
        handling_note_text: str | None = None,
    ) -> None:
        self.connection.execute(
            """
            UPDATE message_deliveries
            SET inbox_status = 'processed',
                processed_at = CURRENT_TIMESTAMP,
                handling_note_text = COALESCE(?, handling_note_text)
            WHERE message_id = ? AND recipient_agent_id = ?
            """,
            (handling_note_text, message_id, recipient_agent_id),
        )

