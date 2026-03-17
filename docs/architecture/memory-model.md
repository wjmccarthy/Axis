# Axis Memory Model

## Purpose

This document defines the implementation-facing memory model for Axis.

It exists to clarify:
- what Axis must remember
- which memory layers exist
- what the canonical source of truth is for each kind of state or artifact
- how retrieval should relate to canonical state
- how compaction and retention should work

This document should guide implementation choices without changing the behavioral contract in [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Design Goals

- keep the memory model low-risk, low-cost, and local-first
- keep mutable state separate from durable artifacts
- keep publication surfaces separate from underlying state memory
- keep retrieval/index layers separate from canonical storage
- preserve provenance and revision history where it materially matters

## Memory Layers

### 1. Runtime Memory

Purpose:
- agent/runtime continuity
- operator preferences
- setup and runbook knowledge
- lightweight working continuity across sessions

Expected posture:
- use native OpenClaw runtime memory conventions
- do not use this as the primary store for Axis analytical state or high-volume artifacts

### 2. Expert Memory

Purpose:
- signal-rooted specialist understanding

Includes current expert-local state:
- `Expert Feed`
- `Expert Watchlist`
- `Expert Ideas`
- `Expert Beliefs`
- `Expert Calls`

Publication surface:
- `Expert Surface`

Characteristics:
- mutable
- expert-local
- signal-rooted
- supports desk participation without itself being desk state

### 3. Analytical Desk Memory

Purpose:
- desk-level synthesis and deliberation

Includes current desk-local state:
- `Desk Feed`
- `Desk Ideas`
- `Desk Beliefs`
- `Desk Debates`

Publication surface:
- `Current State Surface`

Characteristics:
- mutable
- desk-local except for the published current-state surface
- current analytical synthesis layer

### 4. Producer Memory

Purpose:
- current working memory of `Editors Desk`

Includes:
- `Editorial Agenda`
- `Editors Feed`
- `Editors Scratchpad`

Characteristics:
- mutable
- producer-local
- distinct from workflow objects such as `Topic` and `Editorial Assignment`

### 5. Strategist Working Memory

Purpose:
- current working memory of Strategist for cross-desk synthesis, prioritization, and override decisions

Includes:
- `Strategist Feed History`
- `Strategist Scratchpad`

Characteristics:
- mutable
- strategist-local
- distinct from formal signals, approvals, and workflow objects

### 6. Artifact Memory

Purpose:
- durable records of what entered, what was produced, and what was published

Includes:
- source artifacts
- normalized signals
- ingestion-stage artifacts
- `Source Material`
- `Chart Follow-Up`
- `Research Request`
- `Signal Request`
- `Research Brief`
- `Desk Note`
- `Topic`
- `Editorial Assignment`
- drafts
- `Publication Item`

### 7. Retrieval Layer

Purpose:
- recall relevant state and artifacts
- support lexical and semantic discovery

Characteristics:
- derived
- never the source of truth
- rebuildable

### 8. Compaction And Archive Layer

Purpose:
- control cost and complexity over time
- reduce hot retrieval pressure
- preserve old information without keeping everything equally active

Characteristics:
- hot / warm / cold tiers
- derived rollups and summaries where useful
- no destructive replacement of canonical records by summaries

## Core Principle: Canonical Truth Vs Retrieval

Axis should distinguish clearly between:

- canonical truth
  - persisted state objects
  - publication objects
  - workflow records
  - durable artifacts

- retrieval support
  - search indexes
  - embeddings
  - rollups
  - summaries

The retrieval layer may help the system find relevant information, but it must not become the only copy of that information.

## Canonical Storage Principles

Default stack:
- flat Markdown for low-frequency, low-volume human-readable records
- structured payload files for machine-generated or higher-volume artifacts
- SQLite for metadata, workflow state, relationships, statuses, revision history, and structured queries
- SQLite FTS for lexical search
- a local vector index for selected semantic retrieval where useful

General rules:
- large artifacts should live as files rather than database blobs by default
- SQLite should hold structured metadata and relationship state
- vector indexes should be treated as rebuildable derived infrastructure

## Current Canonical Storage Posture

- `Expert Feed`, `Expert Watchlist`, `Expert Ideas`, `Expert Beliefs`, `Expert Calls`: expert-owned working state
- `Expert Surface`: persisted expert publication object
- `Desk Feed`, `Desk Ideas`, `Desk Beliefs`, `Desk Debates`: desk-owned working state
- `Current State Surface`: persisted analytical-desk publication object
- `Editorial Agenda`, `Editors Feed`, `Editors Scratchpad`: Editors-Desk working state
- `Strategist Feed History`, `Strategist Scratchpad`: strategist working state
- signals, requests, workflow records, and structured metadata: SQLite-centered records with file or structured payload where needed
- durable artifacts such as reports, transcripts, notes, briefs, drafts, and publication items: files plus SQLite metadata

## Mutable State Vs Publication Objects

### Mutable State

These represent current evolving internal state:
- expert-side state objects
- desk-side state objects
- producer working memory
- strategist working memory

### Persisted Publication Objects

These are outward-facing current or point-in-time publication surfaces:
- `Expert Surface`
- `Current State Surface`
- `Desk Note`

Important:
- publication objects are not the same as the underlying state they summarize or expose
- `Current State Surface` is not a synonym for `Desk Beliefs`
- `Expert Surface` is not a synonym for full expert memory

## Retrieval Consequences

Current-state lookup should prefer:
- `Current State Surface` when the consumer needs standing desk state
- `Expert Surface` when the consumer needs current expert-facing state
- underlying desk or expert state only when the task is internal and explicitly requires it
- producer and strategist working-memory documents only when those current internal working states are the real target

Historical lookup should prefer:
- archived state snapshots where they exist
- durable artifacts and notes
- retained signals and supporting artifacts

## Stable Identity Rule

Every important Axis state or artifact record should have a stable ID.

This applies to:
- `Expert`
- `Expert Feed`
- `Expert Watchlist`
- `Expert Ideas`
- `Expert Beliefs`
- `Expert Calls`
- `Expert Surface`
- `Analytical Desk`
- `Desk Feed`
- `Desk Ideas`
- `Desk Beliefs`
- `Desk Debates`
- `Current State Surface`
- `Editorial Agenda`
- `Editors Feed`
- `Editors Scratchpad`
- `Strategist Feed History`
- `Strategist Scratchpad`
- `Research Request`
- `Signal Request`
- `Signal`
- `Source Material`
- ingestion-stage artifacts
- `Chart Follow-Up`
- `Research Brief`
- `Desk Note`
- `Topic`
- `Editorial Assignment`
- `Draft`
- `Publication Item`

## Open Implementation Choices

These remain implementation choices rather than architectural contradictions:
- exact file and table schemas
- exact retention thresholds
- exact hot/warm/cold boundaries
- exact vector index choice
- exact archival cadence for working-memory history
