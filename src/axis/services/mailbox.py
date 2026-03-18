from __future__ import annotations

from axis.domain.messages import Message, MessageDelivery
from axis.repositories.messages import MessageRepository


class MailboxService:
    def __init__(self, message_repository: MessageRepository) -> None:
        self.message_repository = message_repository

    def send_message(self, message: Message, deliveries: list[MessageDelivery]) -> None:
        self.message_repository.add_message(message)
        for delivery in deliveries:
            self.message_repository.add_delivery(delivery)

    def mark_processed(
        self,
        message_id: str,
        recipient_agent_id: str,
        handling_note_text: str | None = None,
    ) -> None:
        self.message_repository.mark_delivery_processed(
            message_id=message_id,
            recipient_agent_id=recipient_agent_id,
            handling_note_text=handling_note_text,
        )

