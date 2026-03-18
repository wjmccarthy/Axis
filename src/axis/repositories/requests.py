from __future__ import annotations

import sqlite3
from datetime import datetime
from pathlib import Path

from axis.domain.requests import Request


def _parse_timestamp(value: str | None) -> datetime | None:
    return datetime.fromisoformat(value) if value else None


class RequestRepository:
    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    def add_request(self, request: Request) -> None:
        self.connection.execute(
            """
            INSERT INTO requests (
              id, request_type, requester_agent_id, owner_agent_id, status, priority,
              request_text, response_text, response_path, metadata_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                request.id,
                request.request_type,
                request.requester_agent_id,
                request.owner_agent_id,
                request.status,
                request.priority,
                request.request_text,
                request.response_text,
                str(request.response_path) if request.response_path else None,
                request.metadata_json,
            ),
        )

    def open_requests_for_owner(self, owner_agent_id: str) -> list[Request]:
        rows = self.connection.execute(
            """
            SELECT id, request_type, requester_agent_id, owner_agent_id, status, priority,
                   requested_at, updated_at, fulfilled_at, request_text, response_text,
                   response_path, metadata_json
            FROM requests
            WHERE owner_agent_id = ? AND status = 'open'
            ORDER BY requested_at ASC
            """,
            (owner_agent_id,),
        ).fetchall()
        return [
            Request(
                id=row["id"],
                request_type=row["request_type"],
                requester_agent_id=row["requester_agent_id"],
                owner_agent_id=row["owner_agent_id"],
                status=row["status"],
                priority=row["priority"],
                requested_at=_parse_timestamp(row["requested_at"]),
                updated_at=_parse_timestamp(row["updated_at"]),
                fulfilled_at=_parse_timestamp(row["fulfilled_at"]),
                request_text=row["request_text"],
                response_text=row["response_text"],
                response_path=Path(row["response_path"]) if row["response_path"] else None,
                metadata_json=row["metadata_json"],
            )
            for row in rows
        ]

