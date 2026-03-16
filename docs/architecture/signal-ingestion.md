# Axis Signal Ingestion

## Purpose

This document defines the Axis-specific ingestion model for incoming signals.

It governs:
- how raw source material relates to normalized Signals
- how Report Watch staged processing should be represented
- how source artifacts, parses, and normalized signal records relate to each other

It does not govern:
- OpenClaw runtime behavior
- Gateway behavior
- plugin or hook lifecycle behavior

Those remain governed by official OpenClaw documentation.

## Core Principle

A `Signal` is a normalized Axis record.

It is not the same thing as:
- the raw source artifact
- a report file
- a transcript
- a parse output
- a watch-stage result

A normalized Signal may reference one or more raw source artifacts and one or more derived ingestion-stage artifacts.

## Ingestion Layers

### 1. Raw Source Artifact

Examples:
- PDF report
- article HTML snapshot
- transcript payload
- video metadata payload
- company filing download
- market/economic release payload

Characteristics:
- closest retained representation of what was observed
- canonical evidence layer
- may be file-based or structured payload-based depending on source type

### 2. Ingestion-Stage Artifact

Examples:
- Quick Read output
- Deep Read Gate decision record
- Deep Read extraction output
- normalization output
- transcript extraction output

Characteristics:
- derived from raw source artifacts
- durable and queryable
- not the same thing as the final normalized Signal

### 3. Normalized Signal

Characteristics:
- canonical Axis signal record
- structured enough for routing, ranking, deduplication, and linkage
- may reference multiple raw artifacts and multiple ingestion-stage artifacts

## Signal Model

Implementation should treat a Signal as:
- a normalized record
- not a blob of raw source data
- not a one-to-one wrapper around a file

Before multiple watcher types are implemented, Axis should define a minimal canonical Signal envelope that every watcher can emit consistently.

That envelope does not need to settle every watcher-specific field up front, but it must be stable enough to support:

- stable signal identity
- `signal_source`: `external` or `internal`
- `signal_type`
- `origin`
- routing
- ranking
- observed time
- a normalized one-line statement
- a bounded summary
- deduplication
- linkage to supporting artifacts

`signal_type` is watcher-scoped.

It exists so each watcher can distinguish the specific signal kinds it emits without forcing a premature global type taxonomy across all watchers.

For Viewpoint Signals:

- `signal_source` should be `internal`
- `signal_type` should distinguish the relevant Strategist signal kind
- `origin` should be `viewpoint`
- initial rank should be treated as highest

A single Signal may be supported by:
- one raw artifact
- multiple raw artifacts
- one staged parse
- multiple staged parses

This is important for:
- corroboration
- deduplication
- multi-source normalization
- later reinterpretation

## Desk Consumption Clarification

When a normalized Signal is routed to a Domain Desk:
- the desk should receive a persistent desk-local routed-signal record
- that record only needs a `reviewed` flag for destination-desk handling
- the desk may use reviewed signals to evolve internal theses or views without creating explicit per-signal mutation records
- a reviewed signal does not require a Desk Note unless the desk judges that outward expression is warranted

## Report Watch Stages

Report Watch should preserve stage outputs as their own stored records/artifacts.

### Quick Read

Purpose:
- low-cost early classification and extraction

Should produce:
- a stored Quick Read artifact/record
- preliminary metadata
- preliminary relevance and routing hints
- preliminary extracted signal material

### Deep Read Gate

Purpose:
- determine whether full processing is justified

Should produce:
- a stored gate-decision artifact/record
- reason for passing or stopping
- linkage to the triggering Quick Read artifact

### Deep Read

Purpose:
- full extraction and richer interpretive support for signal generation

Should produce:
- a stored Deep Read artifact/record
- extracted structures and richer text outputs
- linkage to the raw report and earlier stage artifacts

Important:
- these stage artifacts are all durable records
- they should not be collapsed away into only the final Signal

## Many-to-One and One-to-Many Relationships

Implementation should support:

### Many raw artifacts -> one Signal

Examples:
- multiple articles or disclosures normalized into one development
- corroborating source material supporting a single signal

### One raw artifact -> many Signals

Examples:
- one report yielding several distinct signal records
- one transcript containing multiple relevant developments

### One stage artifact -> many Signals

Examples:
- one Deep Read extraction supporting several normalized signals from one report

## Canonical Storage Posture

### Raw source artifacts

- canonical posture: files or structured payloads plus SQLite metadata

### Ingestion-stage artifacts

- canonical posture: file/JSON payload plus SQLite metadata

### Normalized Signals

- canonical posture: SQLite record plus payload when needed

## Retrieval and Search

### Default retrieval targets

- normalized Signals
- report parse outputs
- transcripts
- rollups

### Do not rely only on raw artifacts for retrieval

Raw artifacts should remain preserved, but most interactive retrieval should target:
- normalized signal records
- staged extraction outputs
- daily/weekly rollups

## Compaction

Signal compaction should preserve raw truth and produce derived rollups.

Current policy:
- raw Signals are retained canonically
- daily source/watch rollups are canonical derived artifacts
- weekly source/watch rollups are canonical derived artifacts
- desk/theme rollups may be derived later when useful

## Open Questions

These still need later implementation detail:

1. Exact normalized Signal schema
2. Exact required metadata fields for each watch type
3. Exact deduplication strategy
4. Exact corroboration model
5. Exact storage schema for stage artifacts
