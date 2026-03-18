from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class Request:
    id: str
    request_type: str
    requester_agent_id: str
    request_text: str
    owner_agent_id: str | None = None
    status: str = "open"
    priority: str = "normal"
    requested_at: datetime | None = None
    updated_at: datetime | None = None
    fulfilled_at: datetime | None = None
    response_text: str | None = None
    response_path: Path | None = None
    metadata_json: str | None = None

