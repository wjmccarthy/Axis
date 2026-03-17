# Report Watch

## Purpose

This document defines the Axis-native implementation posture for `Report Watch`.

It governs:
- the staged report-ingestion path
- the intended outputs of each stage
- reader and summary behavior
- the structural constraints implementation must preserve

It does not govern:
- OpenClaw runtime behavior
- Gateway behavior
- hook or plugin lifecycle behavior

Those remain governed by official OpenClaw documentation and [/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md](/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md).

## Role In Axis

`Report Watch` is a Signal Desk intake path for report-like source artifacts.

Its job is to:
- ingest reports as governed source artifacts
- allocate attention efficiently
- extract structured report-side outputs from reports that matter
- produce canonical `Signals` and related retained artifacts

Its job is not to:
- create `Topics` directly
- bypass signal normalization
- replace expert interpretation
- replace analytical desk synthesis

## Stage Model

`Report Watch` should preserve a staged attention model:

1. `Raw Report`
2. `Quick Read`
3. `Deep Read Gate`
4. `Deep Read`

This preserves:
- broad intake
- selective expensive reading
- auditable attention decisions

## Core Constraint

`Report Watch` must not collapse one report into one mandatory downstream analytical line.

A deep read must be able to produce multiple downstream outputs when warranted.

Possible downstream outputs include:
- multiple `Signals`
- `Chart Follow-Up` artifacts
- company- or asset-specific implications
- strategic implications
- event-context support

Topic formation happens later.

## Reader Guidance

Deep reading should:
- identify what the note is actually asserting
- prefer authored judgment and direct takeaways
- distinguish the primary authored thesis from the best standalone extracted claim when they differ
- extract claims that can stand alone as complete statements
- downgrade weak or generic notes rather than inventing a strong claim

Deep reading should not:
- treat wrappers, headers, tables, disclosures, or agenda text as the core claim
- compress a multi-claim report into one forced downstream output

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

### Deep Read Gate

Should produce:
- attention-allocation decision for the current slice or batch
- reason for deep-read promotion or non-promotion

### Deep Read

Should produce:
- section-aware reading artifact
- explicit evidence anchors
- relevance assessment
- promotion guidance
- one-to-many downstream `Signals` and related artifacts when warranted

## Summary Behavior

`Report Watch` may support slice-level summary outputs when useful.

Useful summary sections include:
- highest-relevance report views
- strategic company coverage
- macro and market context that matters
- active event contexts
- views worth tracking over time
- strategic implications
- chart follow-ups

These summaries are support artifacts for signal-side awareness.
They do not replace normalized signals or later expert and desk interpretation.

## Event Context

`Report Watch` may support explicit live-event context handling when a dominant event shapes many reports in the same slice.

This should remain:
- supportive
- auditable
- non-authoritative

It should not:
- replace source reading
- invent evidence
- replace later expert or desk interpretation

## Chart Follow-Ups

`Chart Follow-Up` artifacts are valid first-class downstream outputs of `Report Watch`.

They should exist when a report surfaces:
- a chartable bottleneck
- a comparative capacity question
- a financing or sanctioning question
- a strategic company or asset bridge worth later extraction or reconstruction

They should be grounded in extracted claims and source provenance.

## Integration Rules

`Report Watch` outputs must integrate cleanly with:
- the Axis signal model
- the Axis memory model
- the Axis linking model
- downstream expert and analytical-desk consumption

It must not:
- bypass normalized `Signal` records
- create a separate workflow architecture
- create hidden topic objects at the ingestion layer

## Acceptance Direction

A good first `Report Watch` slice should prove:
- report intake works on sample inputs
- screening and gating allocate attention sensibly
- deep reading can extract multiple downstream outputs from one report when warranted
- outputs enter Axis as canonical `Signals` and related retained artifacts rather than as topic-first or alternate-framing objects
