# Axis Memory Model

## Purpose

This document defines the implementation-facing memory model for Axis.

It exists to clarify:
- what Axis must remember
- which memory layers exist
- what the canonical source of truth is for each kind of state or artifact
- how retrieval should work
- how compaction and retention should work

This document should guide implementation choices without changing the behavioral contract in [`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Design Goals

- Keep the memory model low-risk, low-cost, and local-first.
- Avoid inventing a custom memory engine when standard files, SQLite, and selective retrieval are sufficient.
- Keep mutable state separate from durable artifacts.
- Keep retrieval/index layers separate from canonical storage.
- Preserve provenance and revision history where it materially matters.
- Allow old information to cool out of hot retrieval without losing the underlying truth.
- Keep this document limited to memory/storage/retention decisions rather than reopening object design that is already settled elsewhere.

## Memory Layers

### 1. Runtime Memory

Purpose:
- Agent/runtime continuity
- operator preferences
- setup and runbook knowledge
- lightweight working continuity across sessions

Expected implementation posture:
- Use native OpenClaw runtime memory conventions
- Do not use this as the primary store for Axis domain state or high-volume artifacts

### 2. Domain Memory

Purpose:
- The evolving synthesized understanding of the system

Includes:
- Beliefs
- current Signal Feed
- current Desk Scratchpad

Characteristics:
- mixed narrative and structured
- mutable current state
- historically tracked through archived daily Beliefs
- not reducible to Research Briefs or Desk Notes
- includes desk-local working memory distinct from shared Beliefs

### 2A. Editorial Memory

Purpose:
- The current working memory of Editors Desk for Topic generation and sequencing

Includes:
- current Theme List
- current Editors Feed
- current Editors Scratchpad

Characteristics:
- mixed narrative and structured
- mutable current working state
- distinct from Topics and Editorial Assignments as workflow objects
- includes archived scratch history where useful

### 2B. Strategist Working Memory

Purpose:
- The current working memory of Strategist for cross-domain synthesis, prioritization, and override decisions

Includes:
- current Strategist Feed History
- current Strategist Scratchpad

Characteristics:
- mixed narrative and structured
- mutable current working state
- distinct from formal signals, approvals, and workflow objects
- includes archived scratch history where useful

### 3. Artifact Memory

Purpose:
- Durable records of what entered, what was produced, and what was published

Includes:
- incoming signal artifacts
- normalized signal records
- desk-local routed-signal records
- Source Material
- report files and parses
- Chart Follow-Ups
- transcripts
- Research Requests
- Signal Requests
- Research Briefs
- Desk Notes
- Topics
- Editorial Assignments
- working drafts
- revision drafts
- Publication Items
- published output history

Characteristics:
- mostly durable
- provenance-sensitive
- often append-only or versioned

### 4. Retrieval Layer

Purpose:
- recall relevant artifacts or prior context
- support semantic and lexical discovery

Characteristics:
- never the source of truth
- derived from canonical state/artifacts
- may include lexical and semantic indexes

### 5. Compaction and Archive Layer

Purpose:
- control cost and complexity over time
- reduce hot retrieval pressure
- preserve old information without keeping everything equally active

Characteristics:
- hot / warm / cold tiers
- rollups and summaries as derived artifacts
- no destructive replacement of canonical records by summaries

## Core Principle: Canonical Truth vs Retrieval

Axis should distinguish clearly between:

- canonical truth
  - files
  - structured records
  - versioned state

- retrieval support
  - search indexes
  - embeddings
  - rollups
  - summaries

The retrieval layer may help the system find relevant information, but it must not become the only copy of that information.

This document names the memory/storage posture.

It should not reopen:
- object ownership already defined in the spec
- object meaning already defined in the spec
- workflow behavior already defined in the spec
- detailed retrieval behavior already governed by [`retrieval-policy.md`](/Users/wjm/Code/Axis/docs/architecture/retrieval-policy.md)
- detailed linking behavior already governed by [`linking-model.md`](/Users/wjm/Code/Axis/docs/architecture/linking-model.md)

## Canonical Storage Principles

Default stack:
- flat Markdown for low-frequency, low-volume human-readable records
- JSON or similar structured files for machine-generated or higher-volume artifacts
- SQLite for metadata, workflow state, relationships, statuses, revision history, and structured queries
- SQLite FTS for lexical search
- LanceDB as the local semantic retrieval layer for selected semantically useful text

General rules:
- Large artifacts should live as files rather than database blobs by default.
- SQLite should hold the structured metadata and linking layer.
- Vector indexes should be treated as rebuildable derived infrastructure.

Within Axis, the canonical storage posture is already decided at a useful level:
- Beliefs: desk-owned Markdown files
- Signal Feed: desk-owned working document
- Desk Scratchpad: desk-owned working document with archived history
- Theme List: Editors-Desk-owned Markdown file
- Editors Feed: Editors-Desk-owned working document
- Editors Scratchpad: Editors-Desk-owned working document with archived history
- Strategist Feed History: Strategist-owned working document
- Strategist Scratchpad: Strategist-owned working document with archived history
- signals and workflow records: SQLite-centered metadata records, with file/JSON payload where needed
- durable artifacts such as reports, transcripts, notes, briefs, drafts, and publication items: files plus SQLite metadata

This document should not restate those storage choices as if they were still unresolved.

## Object Categories

### Mutable State

These represent current evolving understanding:

- Beliefs
- current Signal Feed
- current Desk Scratchpad
- current Theme List
- current Editors Feed
- current Editors Scratchpad
- current Strategist Feed History
- current Strategist Scratchpad

Current decisions:
- Beliefs are the canonical current-state container for each desk.
- Beliefs are represented canonically as Markdown files owned by desks.
- Signal Feed is a desk-local working document holding the last `N` relevant routed signals for the desk.
- Desk Scratchpad is a desk-local working document for developing views, unresolved patterns, and temporal signal pressure that does not yet belong in Beliefs.
- Theme List is the Editors-Desk-owned working document for current thematic framing and sequencing context.
- Editors Feed is an Editors-Desk-local working document holding the last `N` feed items most relevant to Topic generation and sequencing.
- Editors Scratchpad is an Editors-Desk-local working document for developing themes, topic ideas, trend/theme pairings, and sequencing thoughts that do not yet belong in Theme List or Topics.
- Strategist Feed History is a Strategist-local working document holding recent feed history relevant to synthesis, prioritization, and override decisions.
- Strategist Scratchpad is a Strategist-local working document for developing cross-domain synthesis, unresolved tensions, and pre-signal or pre-decision reasoning.
- Desk Theses and Theme Theses are the durable conviction layer.
- Desk Views and Theme Views are the current evolving interpretation layer.
- Desk Views are built on top of Desk Theses.
- Theme Views are built on top of Theme Theses.
- Desk Theses, Desk Views, Theme Theses, and Theme Views are represented canonically inside Beliefs.
- Beliefs is the only canonical current-state object for a desk.
- Historical tracking comes from archived daily Beliefs.
- Desks may age out views explicitly by removing them from current Beliefs.
- Older Beliefs remain the historical record rather than keeping every prior view equally alive in current state.
- Signal Feed and Desk Scratchpad are desk-local working memory rather than shared analytical output.
- Desk Scratchpad should preserve archived history over time.
- Theme List is the current editorial working document rather than a workflow object.
- Editors Feed and Editors Scratchpad are Editors-Desk working memory rather than workflow state.
- Editors Scratchpad should preserve archived history over time.
- Strategist Feed History and Strategist Scratchpad are strategist working memory rather than workflow state.
- Strategist Scratchpad should preserve archived history over time.

Memory-model consequence:
- current desk state lookup means loading current Beliefs
- near-term desk temporal-memory lookup may mean loading current Signal Feed
- developing-pattern lookup may mean loading current or archived Desk Scratchpad
- current editorial working-state lookup may mean loading current Theme List
- current editorial input-flow lookup may mean loading current Editors Feed
- developing editorial-pattern lookup may mean loading current or archived Editors Scratchpad
- strategist recent-input lookup may mean loading current Strategist Feed History
- strategist developing-synthesis lookup may mean loading current or archived Strategist Scratchpad
- historical desk-state lookup means loading archived Beliefs
- desks do not need a separate current-state store for theses or views outside Beliefs

### Durable Signal, Request, and Analytical Artifacts

- Signals
- desk-local routed-signal records
- Source Material
- report parses
- Chart Follow-Ups
- transcripts
- Signal Requests
- Research Requests
- Research Briefs
- Desk Notes

Current decisions:
- Signals are stored canonically as SQLite metadata plus file/JSON payload when needed.
- Desk-local routed-signal records are stored canonically as SQLite records with a `reviewed` flag per destination desk.
- Source Material is stored canonically as file or structured payload plus SQLite metadata, with provenance back to an origin or retained source representation.
- Report artifacts and parses are stored canonically as files plus SQLite metadata.
- Chart Follow-Ups are stored canonically as Markdown/file plus SQLite metadata.
- Transcripts are stored canonically as files plus SQLite metadata.
- Research Requests are stored canonically as SQLite workflow records.
- Signal Requests are stored canonically as SQLite workflow records.
- Research Briefs are stored canonically as Markdown plus SQLite metadata.
- Desk Notes are stored canonically as Markdown plus SQLite metadata.
- Signals are append-only.
- Desk Notes are immutable once issued.
- Research Briefs are versioned artifacts and should not be silently edited.
- Some Source Material may also be emitted or referenced through Signals when it is meant to enter the system's attention and routing flow.
- Publication attribution may depend on Source Material even when that material did not enter through the signal path.

### Editorial Artifacts

- Topics
- Editorial Assignments
- working drafts
- review drafts
- final Publication Items

Current decisions:
- Topics are stored canonically in SQLite.
- Editorial Assignments are stored canonically in SQLite.
- Drafts are stored canonically as files plus SQLite metadata.
- Publication Items are stored canonically as files plus SQLite metadata.
- Drafts are retained at milestone revisions rather than every small edit.
- Milestone draft revisions include:
  - first complete draft
  - major structural rewrite
  - domain-review draft
  - strategist/publication-review draft
  - approved/publishable draft
- Publication Items are immutable once published.

## Retrieval Policy

Recommended default:

- lexical search for:
  - metadata-rich records
  - known identifiers
  - source names
  - titles
  - structured filters

- semantic retrieval for:
  - Beliefs sections
  - report text
  - Source Material where direct source recall is valuable
  - transcript text
  - Chart Follow-Ups
  - Research Briefs
  - Desk Notes
  - draft text where reuse/search value is high
  - final Publication Items

Do not default to embedding:
- every raw signal row
- purely structured records
- every tiny intermediate artifact
- Topics
- Editorial Assignments
- desk-local routed-signal records
- Source Material records that are primarily structured attribution containers rather than semantically useful text

Current decisions:
- Use LanceDB as the local semantic retrieval layer.
- Use SQLite FTS for lexical retrieval.
- Embed:
  - Beliefs sections
  - report parses
  - transcripts
  - Research Briefs
  - Desk Notes
  - milestone drafts
  - Publication Items
- Do not embed raw Signals by default.

This section is only the memory-model posture for what gets embedded.

Detailed retrieval order, ranking, and fallback behavior remain governed by [`retrieval-policy.md`](/Users/wjm/Code/Axis/docs/architecture/retrieval-policy.md).

## Compaction Policy

Compaction should create higher-level derived artifacts, not replace canonical artifacts.

Recommended pattern:

- hot tier
  - current Beliefs
  - current Signal Feed and Desk Scratchpad
  - current Theme List, Editors Feed, and Editors Scratchpad
  - current Strategist Feed History and Strategist Scratchpad
  - recent signals
  - active Topics and Assignments
  - active drafts

- warm tier
  - recent but not active artifacts
  - daily/weekly rollups
  - still queryable and partially indexed

- cold tier
  - archived canonical artifacts
  - minimal hot indexing
  - rehydrated on demand

Questions still to finalize:
- hot/warm/cold thresholds by artifact class

Current decisions:
- Desks archive Beliefs daily to preserve the historical record.
- Signal streams retain raw canonical records.
- Signal Desk produces daily source/watch rollups.
- Signal Desk produces weekly source/watch rollups.
- Source/watch is the primary canonical compaction axis for signals.
- Desk/theme rollups may be derived later when useful rather than serving as the first canonical compaction layer.
- Editorial drafts compact by milestone rather than by every small edit.
- Desks may age out views explicitly by removing them from current Beliefs.

## Open Questions For Implementation

1. Whether later implementation should standardize a shared internal Beliefs template across desks
2. What daily Beliefs archive retention policy should be used across hot/warm/cold storage?
3. What are the hot/warm/cold thresholds?
4. How are stable IDs assigned across linked artifacts?
5. How should Axis memory interact with OpenClaw runtime memory without duplicating it?

## Linking and Identity

Current decisions:
- Every Beliefs, Signal Feed, Desk Scratchpad, Theme List, Editors Feed, Editors Scratchpad, Strategist Feed History, Strategist Scratchpad, Research Request, Signal Request, signal, brief, note, topic, assignment, draft, and publication item should have a stable ID.
- Theses and views may also carry stable internal IDs where useful inside Beliefs, but Beliefs is the canonical state object that must always have one.
- Structured links should be kept explicit where attribution, provenance, or revision lineage materially matters.
- Signal-side provenance links should be relatively strong.
- Publication-time attribution links should point to Source Material actually used in Drafts or Publication Items.
- Archived Beliefs, Drafts, and Publication Items should preserve revision lineage where it materially matters.

Detailed link categories and relationship rules remain governed by [`linking-model.md`](/Users/wjm/Code/Axis/docs/architecture/linking-model.md).

## Current Recommendation

Proceed with a conservative architecture:

- OpenClaw memory for runtime/operator continuity
- Axis-owned domain memory through desk-owned Beliefs and desk-local working memory
- Axis-owned editorial and strategist working memory through Theme List, feed documents, and scratchpads
- Axis-owned artifact memory for signals, Source Material, research, and editorial outputs
- SQLite as the structured control metadata layer
- files as the canonical artifact layer
- selective vector retrieval over chosen text-heavy artifacts
- compaction through rollups and tiering, not destructive summarization
