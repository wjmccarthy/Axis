# Report Watch

## Purpose

This document defines the Axis-native implementation posture for Report Watch.

It governs:
- the staged report-ingestion path
- the intended outputs of each stage
- reader and summary behavior
- the structural constraints implementation must preserve

It does not govern:
- OpenClaw runtime behavior
- Gateway behavior
- hook or plugin lifecycle behavior

Those remain governed by official OpenClaw documentation and [`OPENCLAW_PROGRAMMERS_GUIDE.md`](/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md).

## Role In Axis

Report Watch is a Signal Desk intake path for report-like source artifacts.

Its job is to:
- ingest reports as governed source artifacts
- allocate attention efficiently
- extract structured analytical outputs from reports that matter
- produce normalized signals and related downstream artifacts

Its job is not to:
- create Topics directly
- bypass Signal normalization
- collapse reports into a single mandatory topic
- replace Domain Desk interpretation

## Stage Model

Report Watch should use four stages:

1. `Raw Report`
- the original source artifact
- stored canonically with metadata and provenance

2. `Quick Read`
- cheap first-pass screening
- identifies likely value, likely document family, and whether deeper work is justified

3. `Deep Read Gate`
- batch or slice-level attention allocator
- decides what should receive full deep reading now

4. `Deep Read`
- section-aware analytical extraction for reports that cleared the gate

This preserves the intended operating shape:
- broad intake
- selective expensive reading
- auditable attention decisions

## Core Constraint

Report Watch must not collapse a reading too aggressively around a single dominant topic.

That kind of compression causes:
- one dominant topic slug per reading
- one dominant signal path per reading
- premature collapse of multi-section reports into one promoted line

In Axis, a Deep Read must be able to produce multiple downstream outputs when warranted.

Examples:
- multiple Signals
- multiple chart-followup candidates
- multiple company-node implications
- multiple theme implications
- event-context support

Topic formation happens later. It should not be the mandatory organizing key of the Deep Read itself.

## Reader Guidance

The Deep Read should follow these extraction rules:

- identify what the note is actually asserting, not what topics it merely mentions
- prefer authored conclusion language, explicit analyst judgment, and direct takeaways
- distinguish the note's primary thesis from the best standalone extracted claim when they differ
- extract claims that can stand alone as complete sentences
- prefer conclusion sections and analyst judgments over wrappers, meeting descriptions, headers, or agenda language
- do not extract bylines, disclosures, table rows, chart captions, exhibit labels, or valuation grids as the thesis or claim
- if the note is mostly tables or model detail, extract the analyst's actual conclusion rather than the numbers block
- tie each implication to the specific extracted claim that supports it
- downgrade weak or generic notes rather than inventing a strong claim

## Quick Read Guidance

The Quick Read should follow these screening rules:

- this is a screening pass, not a full-note summary
- wrappers, audio notes, chart packs, pure data dumps, recaps, and repeated siblings should be treated conservatively
- `always_read` is reserved for the clearest marquee notes
- `deep_read` is for notes that likely justify a full read once the whole slice is considered
- `light_read` is for notes worth keeping near the top of the queue without yet justifying a full read
- `cataloged_only` is for searchable notes that do not justify immediate reading
- `deferred_but_searchable` is for unreadable or clearly low-value items
- screen summaries should say what the note is actually about, not just restate the title
- when a note is not promoted, the Quick Read should still say what would justify a deeper read

## Deep Read Gate Guidance

The Deep Read Gate should follow these allocation rules:

- shallow recommendations are advisory, not binding
- selection is based on the whole slice, not rigid quotas
- some slices justify many deep reads; some justify very few
- preserve breadth when multiple distinct areas matter
- wrappers, repeated siblings, data-heavy updates, and duplicated house families should not crowd out stronger distinct notes
- flagship macro or live-event synthesis notes should not be demoted simply because related wrappers also exist

## Stage Outputs

### Raw Report

Should produce:
- canonical stored source artifact
- normalized source metadata
- provenance to inbox or watch source

### Quick Read

Should produce:
- bounded screening artifact
- document-family and source-character hints
- attention recommendation
- rationale for why a deeper read is or is not warranted

Important behavior:
- wrappers, repeated siblings, audio notes, pure data dumps, and recap notes should be screened conservatively
- weak previews should not be over-promoted

### Deep Read Gate

Should produce:
- batch-level or slice-level attention decisions
- final deep-read allocation for the current slice

Important behavior:
- no rigid quotas
- some slices may justify many deep reads
- preserve breadth when multiple distinct areas matter
- prevent duplicate family inflation
- keep flagship macro or live-event synthesis notes when they are genuinely the best synthesis of the slice

### Deep Read

Should produce:
- a section-aware reading artifact
- explicit evidence anchors
- theme and driver mappings
- relevance assessment
- promotion guidance
- one-to-many downstream Signals and related artifacts when warranted

Possible downstream outputs include:
- Signals
- Chart Follow-Up artifacts
- company-node implications
- theme implications
- event-context support

Important behavior:
- extract what the note is actually asserting, not what it merely mentions
- prefer authored judgment and section conclusions
- suppress headers, tables, agenda language, and descriptive filler
- tie implications to specific extracted claims

## Summary Behavior

Report Watch should support a slice-level summary shaped roughly around these sections:

- highest-relevance report views
- strategic company coverage
- macro and market context that matters
- active event contexts
- theme shifts and emerging convergence
- views worth tracking over time
- theme implications
- chart follow-ups

This section taxonomy should be preserved unless runtime evidence shows a better structure.

## Event Context

Report Watch should support explicit live-event context handling.

Purpose:
- stop note-level interpretation from being routed through the wrong adjacent theme
- give the slice a shared interpretation frame when a dominant live event is present

This should remain:
- supportive
- auditable
- non-authoritative

It should not:
- replace source reading
- invent evidence
- replace later desk interpretation

## Chart Follow-Ups

Chart follow-ups are a valid first-class downstream output of Report Watch.

They should exist when a report surfaces:
- a chartable bottleneck
- a comparative capacity question
- a financing or sanctioning question
- a strategic company bridge into a larger theme

They should be generated from extracted claims, not from generic topic templates alone.

Report Watch does not need a dedicated chart-clipping subagent in the first slice.

The minimum requirement is:
- detect that a chart follow-up is warranted
- preserve the supporting claim and source provenance
- make later clipping, extraction, or reconstruction possible

Actual chart clipping from PDFs may be added later as a bounded helper capability rather than a required primary agent.

## Tracking Over Time

Report Watch may maintain source or publisher tracking outputs when useful.

These are helpful for:
- longitudinal institutional stance tracking
- house or desk drift over time
- identifying recurring thematic emphasis

But they should remain secondary artifacts, not the primary memory layer of Axis.

## Integration Rules

Report Watch outputs must integrate cleanly with:
- the Axis signal model
- the Axis memory model
- the Axis linking model
- Desk Views and Theme Views downstream

It must not:
- bypass normalized Signal records
- create a separate workflow architecture
- create hidden topic objects at the ingestion layer

## Implementation Guidance

When implementing Report Watch:

1. Start from the reader and summary behavior defined here.
2. Preserve the staged attention model.
3. Remove one-reading-to-one-topic compression.
4. Keep report-derived outputs explicitly linked back to the source artifact and deep-read evidence anchors.
5. Keep topic formation downstream from extracted report outputs.

## Acceptance Direction

A good first Report Watch slice should prove:
- report intake works on sample inputs
- Quick Read and Deep Read Gate allocate attention sensibly
- Deep Read can extract multiple downstream candidates from one report when warranted
- outputs enter Axis as normalized signals and related artifacts rather than topic-first objects
