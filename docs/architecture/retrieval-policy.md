# Axis Retrieval Policy

## Purpose

This document defines how Axis should retrieve relevant state and artifacts.

It governs:
- when to use direct state lookup
- when to use metadata filters
- when to use lexical search
- when to use semantic retrieval
- how current state should be preferred over historical material
- how Signal Desk should fulfill bounded `Signal Requests`

It does not govern:
- OpenClaw runtime behavior
- Gateway behavior
- plugin or hook lifecycle behavior

Those remain governed by official OpenClaw documentation.

## Core Principle

Retrieval is a support layer, not the source of truth.

Axis should retrieve candidate context from:
- current state
- publication objects
- durable artifacts
- indexes

Canonical truth still lives in persisted state, workflow records, and retained artifacts.

## Retrieval Layers

### 1. Direct State Lookup

Use when the task concerns a known current object such as:
- `Expert Surface`
- `Current State Surface`
- expert-local state where explicitly needed
- desk-local state where explicitly needed
- `Editorial Agenda`
- `Editors Feed`
- `Editors Scratchpad`
- `Strategist Feed History`
- `Strategist Scratchpad`
- active `Topic`
- active `Editorial Assignment`

This should be preferred over search whenever the relevant current object is already known.

### 2. Metadata Filtering

Use when the task can be narrowed by structured fields such as:
- object type
- expert
- desk
- source or watch type
- recency window
- workflow status
- topic or assignment linkage

This is the first retrieval pass for high-volume or highly structured records.

This is also the default first pass for `Signal Requests`.

### 3. Lexical Search

Use when:
- exact terminology matters
- identifier lookup matters
- titles, names, source labels, or repeated phrases matter

### 4. Semantic Retrieval

Use when:
- conceptually related prior material matters
- wording may differ from the current query
- interpretive similarity matters more than exact string match

## What Should Be Retrieved First

Default preference order:

1. relevant current publication object
   - `Current State Surface`
   - `Expert Surface`
2. relevant current working-memory object where the task is explicitly internal
3. directly linked recent supporting artifacts
4. recent `Desk Notes` and `Research Briefs`
5. semantically similar historical artifacts
6. cold archival material

This order matters because Axis is a living interpretive system, not a generic document search engine.

## Embedding Policy

### Embed

- `Expert Surface`
- `Current State Surface`
- report parses
- transcripts
- `Research Briefs`
- `Desk Notes`
- milestone drafts
- `Publication Items`

### Do Not Embed By Default

- raw workflow records
- purely structured metadata records

Raw `Signals` may be embedded later if signal-side retrieval quality proves it necessary, but they should not be assumed to be the primary semantic corpus by default.

## Ranking Policy

Ranking should consider:
- explicit current-state priority
- recency
- object importance
- semantic relevance
- lexical match quality

## Historical Retrieval

Historical material should generally remain:
- available
- linked
- rankable

But it should not outrank current live state without reason.

## Signal Retrieval Rule

Signal-side retrieval should prefer:
- retained normalized `Signals`
- signal-side derived artifacts
- report parses
- transcripts
- rollups where present

Signal Desk fulfillment of `Signal Requests` should return:
- bounded signal-search results
- bounded signal dumps

It should not return a `Research Brief`.

## Output Of Retrieval

Retrieval should return:
- object identity
- object type
- concise reason for relevance
- structured links where available
- enough metadata to trace back to canonical retained artifacts or state

## Open Questions

These still need later implementation detail:
- exact ranking formula or heuristic weights
- how many results to mix from current state versus artifacts
- where semantic retrieval should be bypassed entirely
