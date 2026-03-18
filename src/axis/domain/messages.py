from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class Message:
    id: str
    message_type: str
    sender_agent_id: str
    thread_id: str | None = None
    subject_text: str | None = None
    body_text: str | None = None
    content_path: Path | None = None
    priority: str = "normal"
    status: str = "open"
    created_at: datetime | None = None
    updated_at: datetime | None = None
    payload_json: str | None = None


@dataclass(slots=True)
class MessageDelivery:
    id: str
    message_id: str
    recipient_agent_id: str
    inbox_status: str = "unread"
    delivered_at: datetime | None = None
    first_seen_at: datetime | None = None
    processed_at: datetime | None = None
    handling_note_text: str | None = None

