from __future__ import annotations

from axis.db.uow import transaction
from axis.domain.signals import Signal, SignalRoute
from axis.repositories.signals import SignalRepository
from axis.services.routing import SignalRoutingService


def test_signal_routes_are_recipient_specific(connection) -> None:
    repo = SignalRepository(connection)
    service = SignalRoutingService(repo)

    with transaction(connection):
        service.create_signal(
            Signal(
                id="sig-1",
                signal_source="report_watch",
                origin="external",
                signal_type="commodity_price_move",
                normalized_statement="Brent crude moved above $100/bbl.",
                value_label="high",
            )
        )
        service.route_signal(
            SignalRoute(
                id="route-1",
                signal_id="sig-1",
                recipient_agent_id="markets-expert",
                route_reason_text="Market-state relevance",
            )
        )
        service.route_signal(
            SignalRoute(
                id="route-2",
                signal_id="sig-1",
                recipient_agent_id="macro-desk",
                route_reason_text="Macro inflation relevance",
            )
        )

    expert_inbox = repo.inbox_for_recipient("markets-expert")
    desk_inbox = repo.inbox_for_recipient("macro-desk")

    assert len(expert_inbox) == 1
    assert len(desk_inbox) == 1
    assert expert_inbox[0].signal_id == "sig-1"
    assert desk_inbox[0].signal_id == "sig-1"
    assert expert_inbox[0].inbox_status == "unread"
    assert desk_inbox[0].inbox_status == "unread"


def test_marking_one_route_processed_does_not_change_other_recipient(connection) -> None:
    repo = SignalRepository(connection)
    service = SignalRoutingService(repo)

    with transaction(connection):
        service.create_signal(
            Signal(
                id="sig-2",
                signal_source="report_watch",
                origin="external",
                normalized_statement="Euro inflation expectations repriced higher.",
            )
        )
        service.route_signal(
            SignalRoute(id="route-3", signal_id="sig-2", recipient_agent_id="markets-expert")
        )
        service.route_signal(
            SignalRoute(id="route-4", signal_id="sig-2", recipient_agent_id="macro-desk")
        )

    with transaction(connection):
        service.mark_processed("sig-2", "markets-expert", "Reviewed and incorporated.")

    expert_processed = connection.execute(
        "SELECT inbox_status, handling_note_text FROM signal_routes WHERE signal_id = ? AND recipient_agent_id = ?",
        ("sig-2", "markets-expert"),
    ).fetchone()
    desk_unread = connection.execute(
        "SELECT inbox_status FROM signal_routes WHERE signal_id = ? AND recipient_agent_id = ?",
        ("sig-2", "macro-desk"),
    ).fetchone()

    assert expert_processed["inbox_status"] == "processed"
    assert expert_processed["handling_note_text"] == "Reviewed and incorporated."
    assert desk_unread["inbox_status"] == "unread"

