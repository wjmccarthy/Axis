# Axis Signal Ingestion

## Purpose

This document defines the Axis-specific ingestion model for incoming signals.

It governs:
- how raw source material relates to normalized `Signals`
- how ingestion-stage artifacts relate to retained source artifacts and normalized signals
- how signal-side outputs should remain legible to the rest of Axis

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
- an ingestion-stage artifact

A normalized `Signal` may reference one or more raw source artifacts and one or more derived ingestion-stage artifacts.

## Ingestion Layers

### 1. Raw Source Artifact

Examples:
- PDF report
- article HTML snapshot
- transcript payload
- video metadata payload
- company filing download
- market or economic release payload

Characteristics:
- closest retained representation of what was observed
- canonical evidence layer
- file-based or structured-payload-based depending on source type

### 2. Ingestion-Stage Artifact

Examples:
- screening output
- gate decision record
- extraction output
- normalization output
- transcript extraction output

Characteristics:
- derived from raw source artifacts
- durable and queryable
- not the same thing as the final normalized `Signal`

### 3. Normalized Signal

Characteristics:
- canonical Axis signal record
- structured enough for routing, ranking, deduplication, and linkage
- routable to experts
- may reference multiple raw artifacts and multiple ingestion-stage artifacts

## Signal Model

Implementation should treat a `Signal` as:
- a normalized record
- not a blob of raw source data
- not a one-to-one wrapper around a file

The minimal canonical signal envelope must stay stable enough to support:
- stable signal identity
- `signal_source`
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

For `Viewpoint Signals`:
- `signal_source` is `internal`
- `origin` is `viewpoint`
- the relevant strategist signal kind is distinguished in `signal_type`
- initial rank is treated as highest

## Downstream Consumption Clarification

After normalization:
- signals route to `Experts`
- experts update expert-local state
- experts surface desk-directed pressure through `Calls` and `Contributions`
- `Analytical Desks` synthesize through desk deliberation rather than receiving raw first-order routing as their main signal path

A normalized signal does not require:
- a desk note
- a desk-state mutation record
- a one-to-one downstream analytical artifact

## Ingestion Relationships

Implementation should support:

### Many raw artifacts -> one Signal

Examples:
- multiple articles or disclosures normalized into one development
- corroborating material supporting a single signal

### One raw artifact -> many Signals

Examples:
- one report yielding several distinct signal records
- one transcript containing multiple relevant developments

### One ingestion-stage artifact -> many Signals

Examples:
- one extraction pass supporting several normalized signals from one report

## Canonical Storage Posture

### Raw source artifacts

- files or structured payloads plus SQLite metadata

### Ingestion-stage artifacts

- file or structured payload plus SQLite metadata

### Normalized Signals

- SQLite record plus payload when needed

## Retrieval And Search

Most interactive retrieval should target:
- normalized `Signals`
- signal-side derived artifacts
- report parses
- transcripts
- rollups where present

Raw artifacts should remain preserved, but most signal-side recall should operate over normalized or extracted representations rather than only over original raw files.

## Compaction

Signal compaction should preserve raw truth and produce derived rollups without destroying canonical retained records.

Current policy:
- normalized `Signals` are retained canonically
- daily and weekly rollups may exist as derived artifacts
- signal-side compaction does not replace canonical retained signals
