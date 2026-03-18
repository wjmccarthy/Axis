from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class PublishedSurface:
    id: str
    surface_type: str
    owner_agent_id: str
    content_path: Path
    status: str = "current"
    published_at: datetime | None = None
    supersedes_id: str | None = None
    summary_text: str | None = None
    metadata_json: str | None = None

