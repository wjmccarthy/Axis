from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(slots=True)
class Agent:
    id: str
    agent_type: str
    status: str = "active"
    definition_path: Path | None = None
    state_root: Path | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

