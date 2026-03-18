from __future__ import annotations

from axis.domain.requests import Request
from axis.repositories.requests import RequestRepository


class RequestService:
    def __init__(self, request_repository: RequestRepository) -> None:
        self.request_repository = request_repository

    def open_request(self, request: Request) -> None:
        self.request_repository.add_request(request)
