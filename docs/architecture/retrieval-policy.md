# Axis Retrieval Policy

## Purpose

This document defines how Axis should retrieve relevant state and artifacts.

It governs:
- when to use metadata filters
- when to use lexical search
- when to use semantic retrieval
- how decay and recency should affect ranking
- how current state should be preferred over historical material
- how Signal Desk should fulfill bounded Signal Requests

It does not govern:
- OpenClaw runtime behavior
- Gateway behavior
- plugin or hook lifecycle behavior

Those remain governed by official OpenClaw documentation.

## Core Principle

Retrieval is a support layer, not the source of truth.

Axis should retrieve candidate context from:
- current state
- artifacts
- indexes

But canonical truth still lives in:
- SQLite state/metadata
- files
- versioned records

This document is primarily implementation guidance for retrieval over retained Axis state and artifacts.

Its first concrete operational use is Signal Desk fulfillment of Domain-Desk-sponsored Signal Requests.

## Retrieval Layers

### 1. Direct State Lookup

Use when the task concerns:
- current Beliefs
- current Theme List
- current Signal Feed
- current Desk Scratchpad
- current Editors Feed
- current Editors Scratchpad
- current Strategist Feed History
- current Strategist Scratchpad
- active Topic
- active Editorial Assignment

This should be preferred over search whenever the relevant current object is already known.

### 2. Metadata Filtering

Use when the task can be narrowed by structured fields such as:
- object type
- desk
- theme
- source/watch type
- recency window
- workflow status
- topic/assignment linkage

This is the first retrieval pass for high-volume or highly structured records.

This is also the default first pass for Signal Requests.

### 3. Lexical Search

Use when:
- exact terminology matters
- identifier lookup matters
- titles, names, source labels, or repeated phrases matter
- semantic retrieval would be too expensive or noisy

Recommended implementation:
- SQLite FTS over selected textual fields

### 4. Semantic Retrieval

Use when:
- conceptually related prior material matters
- the wording may differ from the current query
- interpretive similarity matters more than exact string match

Recommended implementation:
- LanceDB over selected text-heavy artifacts and narrative state fields

## What Should Be Retrieved First

Default preference order:

1. current Beliefs
2. current Theme List and other current working-memory documents where relevant
3. directly linked recent supporting artifacts
4. recent Desk Notes / Research Briefs
5. semantically similar historical artifacts
6. cold archival material

This order matters because Axis is a living interpretive system, not a generic document search engine.

## Embedding Policy

### Embed

- Beliefs sections
- report parses
- transcripts
- Research Briefs
- Desk Notes
- milestone drafts
- Publication Items

### Do Not Embed by Default

- raw Signals
- Topics
- Editorial Assignments
- purely structured metadata records

## Ranking Policy

Ranking should consider:
- explicit current-state priority
- recency
- whether a view or thesis still appears in current Beliefs
- object importance
- semantic relevance
- lexical match quality

## Historical Retrieval

Historical retrieval is valid, but it should not outrank current live state without reason.

Historical material should generally be:
- available
- linked
- rankable
- but lower in default priority unless strongly relevant

## Signal Retrieval Rule

Do not treat raw Signals as the primary semantic retrieval corpus by default.

Prefer:
- normalized signal records
- daily/weekly rollups
- report parses
- related Desk Notes

Use raw signal artifacts mainly for:
- provenance
- detailed backtracking
- corroboration

## Signal Request Fulfillment

When Signal Desk fulfills a Signal Request, it should prefer:

1. metadata filtering over retained normalized Signals
2. time-range filtering
3. supporting signal-side artifacts where they materially improve retrieval quality
4. semantic retrieval only when lexical and metadata filtering are insufficient

Signal Request fulfillment should return a bounded signal-search result or signal dump, not a Research Brief.

## Draft Retrieval Rule

Do not retrieve every draft revision equally.

Prefer:
- milestone drafts
- publication-ready drafts
- final Publication Items

## Output of Retrieval

Retrieval should return:
- object identity
- object type
- concise reason for relevance
- structured links where available
- enough metadata to trace back to canonical artifacts

## Open Questions

These still need later implementation detail:

1. Exact ranking formula or heuristic weights
2. How many results to mix from state vs artifacts
3. Whether some workflows should bypass semantic retrieval entirely
4. Whether desk/theme-specific retrieval policies are needed later
