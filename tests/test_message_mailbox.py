from __future__ import annotations

from axis.db.uow import transaction
from axis.domain.messages import Message, MessageDelivery
from axis.repositories.messages import MessageRepository
from axis.services.mailbox import MailboxService


def test_message_delivery_creates_mailbox_entries(connection) -> None:
    repo = MessageRepository(connection)
    service = MailboxService(repo)

    with transaction(connection):
        service.send_message(
            Message(
                id="msg-1",
                message_type="expert_call",
                sender_agent_id="markets-expert",
                subject_text="Challenge macro desk",
                body_text="Oil shock repricing is underappreciated.",
            ),
            [
                MessageDelivery(
                    id="delivery-1",
                    message_id="msg-1",
                    recipient_agent_id="macro-desk",
                )
            ],
        )

    inbox = repo.inbox_for_recipient("macro-desk")
    assert len(inbox) == 1
    assert inbox[0].message_id == "msg-1"
    assert inbox[0].inbox_status == "unread"

    message = repo.get_message("msg-1")
    assert message is not None
    assert message.body_text == "Oil shock repricing is underappreciated."


def test_marking_message_processed_is_recipient_specific(connection) -> None:
    repo = MessageRepository(connection)
    service = MailboxService(repo)

    with transaction(connection):
        connection.execute(
            "INSERT INTO agents (id, agent_type, definition_path, state_root) VALUES (?, ?, ?, ?)",
            ("energy-desk", "desk", "agent-definitions/agents/energy-desk", "agent-state/agents/energy-desk"),
        )
        service.send_message(
            Message(
                id="msg-2",
                message_type="contribution",
                sender_agent_id="markets-expert",
                body_text="Energy equities are confirming the oil move.",
            ),
            [
                MessageDelivery(id="delivery-2", message_id="msg-2", recipient_agent_id="macro-desk"),
                MessageDelivery(id="delivery-3", message_id="msg-2", recipient_agent_id="energy-desk"),
            ],
        )

    with transaction(connection):
        service.mark_processed("msg-2", "macro-desk", "Read by macro.")

    macro_row = connection.execute(
        "SELECT inbox_status, handling_note_text FROM message_deliveries WHERE message_id = ? AND recipient_agent_id = ?",
        ("msg-2", "macro-desk"),
    ).fetchone()
    energy_row = connection.execute(
        "SELECT inbox_status FROM message_deliveries WHERE message_id = ? AND recipient_agent_id = ?",
        ("msg-2", "energy-desk"),
    ).fetchone()

    assert macro_row["inbox_status"] == "processed"
    assert macro_row["handling_note_text"] == "Read by macro."
    assert energy_row["inbox_status"] == "unread"

