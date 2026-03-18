from __future__ import annotations

from axis.db.uow import transaction
from axis.domain.requests import Request
from axis.repositories.requests import RequestRepository
from axis.services.requests import RequestService


def test_open_requests_are_queryable_by_owner(connection) -> None:
    repo = RequestRepository(connection)
    service = RequestService(repo)

    with transaction(connection):
        service.open_request(
            Request(
                id="req-1",
                request_type="signal_request",
                requester_agent_id="macro-desk",
                owner_agent_id="markets-expert",
                request_text="Pull recent signals on oil and breakevens.",
            )
        )
        service.open_request(
            Request(
                id="req-2",
                request_type="research_request",
                requester_agent_id="macro-desk",
                owner_agent_id="macro-desk",
                request_text="Prepare a deeper note on stagflation transmission.",
            )
        )

    market_owned = repo.open_requests_for_owner("markets-expert")
    macro_owned = repo.open_requests_for_owner("macro-desk")

    assert [request.id for request in market_owned] == ["req-1"]
    assert [request.id for request in macro_owned] == ["req-2"]

