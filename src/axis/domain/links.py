from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Link:
    id: str
    source_id: str
    source_type: str
    target_id: str
    target_type: str
    link_type: str
    created_at: datetime | None = None
    metadata_json: str | None = None

