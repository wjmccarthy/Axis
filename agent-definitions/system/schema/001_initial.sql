BEGIN;

PRAGMA foreign_keys = ON;

-- Core agent registry. This is intentionally small and should not duplicate the
-- full agent prompt/config surface that lives in agent-definitions/agents/.
CREATE TABLE agents (
  id TEXT PRIMARY KEY,
  agent_type TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'active',
  definition_path TEXT,
  state_root TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_agents_type ON agents(agent_type);

-- Ingested documents entering watcher lanes.
CREATE TABLE documents (
  id TEXT PRIMARY KEY,
  source_family TEXT NOT NULL,
  publisher TEXT,
  source_type TEXT,
  title TEXT,
  author_text TEXT,
  observed_at TEXT,
  ingested_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  path TEXT NOT NULL,
  mime_type TEXT,
  checksum TEXT,
  language TEXT,
  queue_state TEXT NOT NULL DEFAULT 'new',
  quick_read_text TEXT,
  gate_decision TEXT,
  gate_reason_text TEXT,
  deep_read_artifact_path TEXT,
  metadata_json TEXT
);

CREATE INDEX idx_documents_source_family ON documents(source_family);
CREATE INDEX idx_documents_publisher ON documents(publisher);
CREATE INDEX idx_documents_queue_state ON documents(queue_state);
CREATE INDEX idx_documents_observed_at ON documents(observed_at);

-- Canonical normalized signals. The text fields are authoritative. Structured
-- helpers are intentionally optional.
CREATE TABLE signals (
  id TEXT PRIMARY KEY,
  source_document_id TEXT,
  signal_source TEXT NOT NULL,
  signal_type TEXT,
  origin TEXT NOT NULL,
  observed_at TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  normalized_statement TEXT NOT NULL,
  summary_text TEXT,
  rank_label TEXT,
  value_label TEXT,
  status TEXT NOT NULL DEFAULT 'active',
  payload_json TEXT,
  FOREIGN KEY (source_document_id) REFERENCES documents(id)
);

CREATE INDEX idx_signals_source_document_id ON signals(source_document_id);
CREATE INDEX idx_signals_signal_source ON signals(signal_source);
CREATE INDEX idx_signals_origin ON signals(origin);
CREATE INDEX idx_signals_observed_at ON signals(observed_at);
CREATE INDEX idx_signals_status ON signals(status);

-- Recipient-specific routing and handling state for signals.
CREATE TABLE signal_routes (
  id TEXT PRIMARY KEY,
  signal_id TEXT NOT NULL,
  recipient_agent_id TEXT NOT NULL,
  route_reason_text TEXT,
  route_basis_json TEXT,
  routed_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  inbox_status TEXT NOT NULL DEFAULT 'unread',
  first_seen_at TEXT,
  processed_at TEXT,
  handling_note_text TEXT,
  FOREIGN KEY (signal_id) REFERENCES signals(id),
  FOREIGN KEY (recipient_agent_id) REFERENCES agents(id)
);

CREATE UNIQUE INDEX idx_signal_routes_unique
  ON signal_routes(signal_id, recipient_agent_id);
CREATE INDEX idx_signal_routes_recipient_status
  ON signal_routes(recipient_agent_id, inbox_status);
CREATE INDEX idx_signal_routes_routed_at ON signal_routes(routed_at);

-- Direct inter-agent messages. Canonical meaning remains text-first.
CREATE TABLE messages (
  id TEXT PRIMARY KEY,
  message_type TEXT NOT NULL,
  sender_agent_id TEXT NOT NULL,
  thread_id TEXT,
  subject_text TEXT,
  body_text TEXT,
  content_path TEXT,
  priority TEXT NOT NULL DEFAULT 'normal',
  status TEXT NOT NULL DEFAULT 'open',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  payload_json TEXT,
  FOREIGN KEY (sender_agent_id) REFERENCES agents(id)
);

CREATE INDEX idx_messages_type ON messages(message_type);
CREATE INDEX idx_messages_sender ON messages(sender_agent_id);
CREATE INDEX idx_messages_thread ON messages(thread_id);
CREATE INDEX idx_messages_status ON messages(status);
CREATE INDEX idx_messages_created_at ON messages(created_at);

-- Recipient-specific delivery state for messages. This gives each recipient a
-- mailbox/inbox view without duplicating the message body.
CREATE TABLE message_deliveries (
  id TEXT PRIMARY KEY,
  message_id TEXT NOT NULL,
  recipient_agent_id TEXT NOT NULL,
  inbox_status TEXT NOT NULL DEFAULT 'unread',
  delivered_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  first_seen_at TEXT,
  processed_at TEXT,
  handling_note_text TEXT,
  FOREIGN KEY (message_id) REFERENCES messages(id),
  FOREIGN KEY (recipient_agent_id) REFERENCES agents(id)
);

CREATE UNIQUE INDEX idx_message_deliveries_unique
  ON message_deliveries(message_id, recipient_agent_id);
CREATE INDEX idx_message_deliveries_recipient_status
  ON message_deliveries(recipient_agent_id, inbox_status);
CREATE INDEX idx_message_deliveries_delivered_at
  ON message_deliveries(delivered_at);

-- Requests are workflow records. The request text is authoritative.
CREATE TABLE requests (
  id TEXT PRIMARY KEY,
  request_type TEXT NOT NULL,
  requester_agent_id TEXT NOT NULL,
  owner_agent_id TEXT,
  status TEXT NOT NULL DEFAULT 'open',
  priority TEXT NOT NULL DEFAULT 'normal',
  requested_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  fulfilled_at TEXT,
  request_text TEXT NOT NULL,
  response_text TEXT,
  response_path TEXT,
  metadata_json TEXT,
  FOREIGN KEY (requester_agent_id) REFERENCES agents(id),
  FOREIGN KEY (owner_agent_id) REFERENCES agents(id)
);

CREATE INDEX idx_requests_type ON requests(request_type);
CREATE INDEX idx_requests_requester ON requests(requester_agent_id);
CREATE INDEX idx_requests_owner_status ON requests(owner_agent_id, status);
CREATE INDEX idx_requests_requested_at ON requests(requested_at);

-- Published surfaces are metadata records pointing to the actual file-backed
-- surface content in agent-state/.
CREATE TABLE published_surfaces (
  id TEXT PRIMARY KEY,
  surface_type TEXT NOT NULL,
  owner_agent_id TEXT NOT NULL,
  content_path TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'current',
  published_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  supersedes_id TEXT,
  summary_text TEXT,
  metadata_json TEXT,
  FOREIGN KEY (owner_agent_id) REFERENCES agents(id),
  FOREIGN KEY (supersedes_id) REFERENCES published_surfaces(id)
);

CREATE INDEX idx_published_surfaces_owner_type
  ON published_surfaces(owner_agent_id, surface_type, status);
CREATE INDEX idx_published_surfaces_published_at
  ON published_surfaces(published_at);

-- Minimal structured linkage for provenance, attribution, workflow lineage, and
-- revision lineage.
CREATE TABLE links (
  id TEXT PRIMARY KEY,
  source_id TEXT NOT NULL,
  source_type TEXT NOT NULL,
  target_id TEXT NOT NULL,
  target_type TEXT NOT NULL,
  link_type TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  metadata_json TEXT
);

CREATE UNIQUE INDEX idx_links_unique
  ON links(source_id, source_type, target_id, target_type, link_type);
CREATE INDEX idx_links_source ON links(source_id, source_type, link_type);
CREATE INDEX idx_links_target ON links(target_id, target_type, link_type);

COMMIT;
