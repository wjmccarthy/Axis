from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Signal:
    id: str
    signal_source: str
    origin: str
    normalized_statement: str
    source_document_id: str | None = None
    signal_type: str | None = None
    observed_at: datetime | None = None
    created_at: datetime | None = None
    summary_text: str | None = None
    rank_label: str | None = None
    value_label: str | None = None
    status: str = "active"
    payload_json: str | None = None


@dataclass(slots=True)
class SignalRoute:
    id: str
    signal_id: str
    recipient_agent_id: str
    route_reason_text: str | None = None
    route_basis_json: str | None = None
    routed_at: datetime | None = None
    inbox_status: str = "unread"
    first_seen_at: datetime | None = None
    processed_at: datetime | None = None
    handling_note_text: str | None = None

