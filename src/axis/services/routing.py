from __future__ import annotations

from axis.domain.signals import Signal, SignalRoute
from axis.repositories.signals import SignalRepository


class SignalRoutingService:
    def __init__(self, signal_repository: SignalRepository) -> None:
        self.signal_repository = signal_repository

    def create_signal(self, signal: Signal) -> None:
        self.signal_repository.add_signal(signal)

    def route_signal(self, route: SignalRoute) -> None:
        self.signal_repository.add_route(route)

    def mark_processed(
        self,
        signal_id: str,
        recipient_agent_id: str,
        handling_note_text: str | None = None,
    ) -> None:
        self.signal_repository.mark_route_processed(
            signal_id=signal_id,
            recipient_agent_id=recipient_agent_id,
            handling_note_text=handling_note_text,
        )

