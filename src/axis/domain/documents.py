from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class Document:
    id: str
    source_family: str
    path: Path
    source_type: str | None = None
    publisher: str | None = None
    title: str | None = None
    author_text: str | None = None
    observed_at: datetime | None = None
    ingested_at: datetime | None = None
    mime_type: str | None = None
    checksum: str | None = None
    language: str | None = None
    queue_state: str = "new"
    quick_read_text: str | None = None
    gate_decision: str | None = None
    gate_reason_text: str | None = None
    deep_read_artifact_path: Path | None = None
    metadata_json: str | None = None

