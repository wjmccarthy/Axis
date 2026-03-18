from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ContentRef:
    body_text: str | None = None
    content_path: Path | None = None

    def has_content(self) -> bool:
        return self.body_text is not None or self.content_path is not None


Timestamp = datetime

