# Axis Artifact Model

## Purpose

This document defines the major Axis-owned state and artifact classes that implementation must support.

It governs:
- what the major Axis records are
- what category each record belongs to
- which records are mutable state versus durable artifacts
- what the canonical storage posture is for each class

It does not govern:
- OpenClaw runtime memory behavior
- Gateway behavior
- plugin lifecycle behavior
- hook lifecycle behavior

Those remain governed by official OpenClaw documentation.

## Categories

Axis records fall into three main categories:

### 1. Mutable State

These represent the system's current evolving synthesized understanding.

- Beliefs
- current Signal Feed
- current Desk Scratchpad
- current Theme List
- current Editors Feed
- current Editors Scratchpad
- current Strategist Feed History
- current Strategist Scratchpad

### 2. Durable Artifacts

These represent observed inputs, analytical outputs, editorial outputs, and published outputs.

- Signal
- Source Material
- report artifact
- report parse
- Chart Follow-Up
- transcript
- Research Request
- Signal Request
- Research Brief
- Desk Note
- Topic
- Editorial Assignment
- draft
- Publication Item

### 3. Operational/Derived Records

These support retrieval, compaction, or archival behavior but are not the primary truth objects themselves.

- desk-local routed-signal record
- daily signal rollup
- weekly signal rollup
- retrieval index entry
- link record

## Canonical Storage Posture

### Beliefs

- category: mutable state
- canonical posture: Markdown file owned by the desk
- update behavior: current persisted desk analytical state
- contains: Desk Thesis, Desk Views, Theme Theses, and owned Theme Views
- historical tracking: archived daily as part of the desk's state history

### Signal Feed

- category: mutable desk-local working state
- canonical posture: desk-owned working document
- update behavior: rolling last `N` relevant routed signals for the desk
- purpose: recent signal-flow and short-horizon temporal memory distinct from Beliefs

### Desk Scratchpad

- category: mutable desk-local working state
- canonical posture: desk-owned working document
- update behavior: evolving notebook for developing views, recurrence, and unresolved signal pressure
- historical tracking: archived over time

### Theme List

- category: mutable editorial working state
- canonical posture: Editors-Desk-owned Markdown file
- update behavior: current thematic framing, topic-development context, and sequencing context

### Editors Feed

- category: mutable editorial working state
- canonical posture: Editors-Desk-owned working document
- update behavior: rolling last `N` feed items most relevant to Topic generation and sequencing

### Editors Scratchpad

- category: mutable editorial working state
- canonical posture: Editors-Desk-owned working document
- update behavior: evolving notebook for topic ideas, theme/trend pairings, and sequencing thoughts
- historical tracking: archived over time

### Strategist Feed History

- category: mutable strategist working state
- canonical posture: Strategist-owned working document
- update behavior: rolling recent feed history most relevant to synthesis, prioritization, and override decisions

### Strategist Scratchpad

- category: mutable strategist working state
- canonical posture: Strategist-owned working document
- update behavior: evolving notebook for cross-domain synthesis, unresolved tensions, and pre-signal or pre-decision reasoning
- historical tracking: archived over time

### Signal

- category: durable artifact
- canonical posture: SQLite metadata with file/JSON payload when needed
- mutation behavior: append-only

### Source Material

- category: durable artifact
- canonical posture: file or structured payload plus SQLite metadata
- mutation behavior: immutable or versioned depending on source

Source Material is the implementation-level class for attributable supporting material such as:

- quotes
- visuals
- charts
- tables
- excerpts
- clips
- other attributable source-derived material

Source Material may sit behind Signals, Research Briefs, Desk Notes, Drafts, and Publication Items.

Some Source Material, such as standing-watch charts or other routable observed material, may also be emitted or referenced through Signals when it is meant to enter the system's attention and routing flow.

Source Material is not:

- a replacement for the origin source artifact
- automatically a Signal
- automatically a publication asset

When Source Material itself is meant to be noticed, routed, and consumed by the system, it should also be emitted or referenced through a canonical Signal rather than remaining buried only as support material.

Source Material should normally preserve provenance back to an origin or retained source representation such as:

- a report artifact
- a report parse
- a transcript
- another retained source representation

### Desk-Local Routed-Signal Record

- category: operational/derived record
- canonical posture: SQLite record
- mutation behavior: persistent record with `reviewed` flag for each destination desk

### Report Artifact

- category: durable artifact
- canonical posture: file plus SQLite metadata

### Report Parse

- category: durable artifact
- canonical posture: file/JSON plus SQLite metadata

### Chart Follow-Up

- category: durable artifact
- canonical posture: Markdown/file plus SQLite metadata
- mutation behavior: versioned artifact when materially revised

### Transcript

- category: durable artifact
- canonical posture: file plus SQLite metadata

### Research Brief

- category: durable artifact
- canonical posture: Markdown plus SQLite metadata
- mutation behavior: versioned artifact

### Research Request

- category: durable workflow artifact
- canonical posture: SQLite record

### Signal Request

- category: durable workflow artifact
- canonical posture: SQLite record

### Desk Note

- category: durable artifact
- canonical posture: Markdown plus SQLite metadata
- mutation behavior: immutable once issued

### Topic

- category: durable workflow artifact
- canonical posture: SQLite record

### Editorial Assignment

- category: durable workflow artifact
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

Desk theses and views may be grounded by supporting material in narrative or retained state where needed.

Important:
- Axis does not require dense structured linking for analytical relationships among theses, views, notes, and briefs
- structured links should be reserved mainly for provenance, attribution, workflow lineage, and revision lineage
- the sparse-linking rules in [`linking-model.md`](/Users/wjm/Code/Axis/docs/architecture/linking-model.md) control how far this should go in practice

## Retrieval Posture

Artifacts and state should not all be treated equally for retrieval.

### Embed for semantic retrieval

- Beliefs sections
- report parses
- transcripts
- Research Briefs
- Desk Notes
- milestone drafts
- Publication Items

### Do not embed by default

- raw Signals
- Topics
- Editorial Assignments
- purely structured metadata records

## Current-State Retention Posture

- Beliefs is the current-state container.
- Signal Feed and Desk Scratchpad are desk-local working-memory surfaces.
- Theme List is the current editorial working document.
- Editors Feed and Editors Scratchpad are Editors-Desk working-memory surfaces.
- Strategist Feed History and Strategist Scratchpad are strategist working-memory surfaces.
- Desks may explicitly age out views by removing them from current Beliefs.
- Historical tracking comes from archived daily Beliefs rather than from keeping every old view active in current state.

## Open Questions

These still need later implementation decisions:

1. Exact fields for each record class
2. Exact stable ID format
3. Exact hot/warm/cold thresholds by class
