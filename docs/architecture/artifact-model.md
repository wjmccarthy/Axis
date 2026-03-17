# Axis Artifact Model

## Purpose

This document defines the major Axis-owned state and artifact classes that implementation must support.

It governs:
- what the major Axis records are
- what category each record belongs to
- which records are mutable state versus persisted publication versus durable artifact
- what the canonical storage posture is for each class

It does not govern:
- OpenClaw runtime memory behavior
- Gateway behavior
- plugin lifecycle behavior

Those remain governed by official OpenClaw documentation.

## Categories

Axis records fall into four main categories.

### 1. Mutable State

These represent current evolving internal state.

- `Expert Feed`
- `Expert Watchlist`
- `Expert Ideas`
- `Expert Beliefs`
- `Expert Calls`
- `Desk Feed`
- `Desk Ideas`
- `Desk Beliefs`
- `Desk Debates`
- `Editorial Agenda`
- `Editors Feed`
- `Editors Scratchpad`
- `Strategist Feed History`
- `Strategist Scratchpad`

### 2. Persisted Publication Objects

These are outward-facing current or point-in-time publication surfaces.

- `Expert Surface`
- `Current State Surface`
- `Desk Note`

### 3. Durable Artifacts

These represent observed inputs, supporting material, analytical outputs, editorial outputs, and published outputs.

- `Signal`
- `Source Material`
- report artifact
- report parse
- ingestion-stage artifact
- `Chart Follow-Up`
- transcript
- `Research Brief`
- draft
- `Publication Item`

### 4. Workflow Records

These represent workflow state and lineage.

- `Research Request`
- `Signal Request`
- `Topic`
- `Editorial Assignment`

## Canonical Storage Posture

### Expert State

- category: mutable state
- canonical posture: expert-owned working state plus metadata
- includes: feed, watchlist, ideas, beliefs, calls

### Expert Surface

- category: persisted publication object
- canonical posture: persisted publication record plus metadata
- update behavior: current exposed expert state built from selected expert memory

### Desk State

- category: mutable state
- canonical posture: desk-owned working state plus metadata
- includes: feed, ideas, beliefs, debates

### Current State Surface

- category: persisted publication object
- canonical posture: persisted publication record plus metadata
- update behavior: current exposed desk state built from desk beliefs and selected desk ideas

### Editorial Working State

- category: mutable state
- canonical posture: Editors-Desk working documents plus metadata
- includes: `Editorial Agenda`, `Editors Feed`, `Editors Scratchpad`

### Strategist Working State

- category: mutable state
- canonical posture: strategist working documents plus metadata
- includes: `Strategist Feed History`, `Strategist Scratchpad`

### Signal

- category: durable artifact
- canonical posture: SQLite metadata with file or payload when needed
- mutation behavior: append-only or versioned where the source requires it

### Source Material

- category: durable artifact
- canonical posture: file or structured payload plus SQLite metadata
- mutation behavior: immutable or versioned depending on source

### Ingestion-Stage Artifact

- category: durable artifact
- canonical posture: file or structured payload plus SQLite metadata

### Chart Follow-Up

- category: durable artifact
- canonical posture: file or Markdown plus SQLite metadata
- mutation behavior: versioned when materially revised

### Research Brief

- category: durable artifact
- canonical posture: Markdown plus SQLite metadata
- mutation behavior: versioned artifact

### Desk Note

- category: persisted publication object
- canonical posture: Markdown plus SQLite metadata
- mutation behavior: immutable once issued

### Research Request

- category: workflow record
- canonical posture: SQLite record

### Signal Request

- category: workflow record
- canonical posture: SQLite record

### Topic

- category: workflow record
- canonical posture: SQLite record

### Editorial Assignment

- category: workflow record
- canonical posture: SQLite record

### Draft

- category: durable artifact
- canonical posture: file plus SQLite metadata
- mutation behavior: versioned by milestone revision

### Publication Item

- category: durable artifact
- canonical posture: file plus SQLite metadata
- mutation behavior: immutable once published

## Grounding

Analytical and editorial outputs may be grounded by supporting material in retained artifacts where needed.

Important:
- Axis does not require dense structured linking for every analytical relationship
- structured links should be reserved mainly for provenance, attribution, workflow lineage, and revision lineage

## Retrieval Posture

Not all records should be treated equally for retrieval.

Prefer high-value retrieval over:
- `Expert Surface`
- `Current State Surface`
- `Desk Note`
- `Research Brief`
- report parses
- transcripts
- retained signals where signal-side retrieval is the real need
