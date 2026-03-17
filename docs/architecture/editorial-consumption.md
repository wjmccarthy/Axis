# Axis Editorial Consumption Guide

## Purpose

This document defines how producer-side editorial components consume analytical output from Analytical Desks.

It governs:
- what editorial may inspect
- what editorial may subscribe to
- how editorial should treat current state versus notes
- what working memory Editors Desk maintains

It does not govern:
- topic approval authority
- assignment lifecycle authority
- OpenClaw runtime behavior

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Canonical Rule

Editorial consumes analytical output, not the raw signal firehose.

The primary editorial-facing inputs are:
- `Current State Surface`
- `Desk Note`
- direct desk answers to questions
- `Research Brief` where deeper support is needed

Editorial does not depend on:
- raw signals as its main interpretive input
- desk-internal debates
- expert-internal memory surfaces as the normal producer-facing interface

## Current State Vs Desk Note

These surfaces are not the same.

`Current State Surface`:
- is the standing current desk state
- contains core position, beliefs, and selected ideas
- is the main desk state interface editorial should inspect

`Desk Note`:
- is a point-in-time published communication
- may surface faster in fast-moving situations
- does not replace standing current state permanently

Editorial rule:
- use `Current State Surface` as the standing analytical baseline
- use `Desk Notes` as bounded pushed updates, alerts, or framing artifacts
- in a fast-moving situation, a newer `Desk Note` may be the current tactical read until current state catches up

## Editors Desk

Editors Desk may:
- inspect the `Current State Surface` of Analytical Desks
- subscribe to `Desk Notes`
- ask direct questions of Analytical Desks

Editors Desk uses these inputs to:
- create and refine `Topics`
- manage backlog, slate, sequencing, and reuse planning
- maintain continuity across channels
- request new bounded analytical output when needed through desk questions

Editors Desk working memory includes:
- `Editorial Agenda`
- `Editors Feed`
- `Editors Scratchpad`

Role of each:
- `Editorial Agenda`
  - current editorial framing and sequencing context
- `Editors Feed`
  - recent incoming editorially relevant analytical material
- `Editors Scratchpad`
  - working editorial development memory before material becomes Topic state

These are working-memory surfaces, not workflow objects.

## Channel Editors

Channel editors normally consume a routed subset of:
- current-state surfaces
- desk notes
- relevant research briefs

That subset is routed through Editors Desk for active assignments.

Channel editors may work through the relevant Analytical Desk for:
- interpretation
- clarification
- assignment support
- escalation into research when needed

Channel editors should not be treated as first-order consumers of the full internal analytical surface across the system.

## Research Support

When editorial needs deeper support:
- the request goes to the relevant Analytical Desk
- the desk decides whether existing knowledge is sufficient
- if not, the desk opens a `Research Request`

Research support remains desk-mediated.

Editorial does not open `Research Requests` directly.

## What Editorial Should Not Treat As Canonical

Editorial should not treat any of the following as the main analytical authority:
- raw signals
- desk-internal debates
- expert feed/watchlist state
- desk notes alone

Editorial should also not rebuild an obsolete layered analytical model in its own working memory.

## Workflow Anchoring

Editorial workflow should remain anchored in:
- `Topic`
- `Editorial Assignment`
- `Publication Item`

Analytical inputs support those workflow objects, but workflow objects should not require dense analytical linking by default.

The important explicit links remain:
- workflow lineage
- attribution and provenance where needed

## Worked Example

1. Editors Desk inspects the current state of a relevant Analytical Desk.
2. Editors Desk asks a direct question about a developing story angle.
3. The desk decides that a bounded outward answer is warranted and publishes a `Desk Note`.
4. Editors Desk uses the current-state surface plus that note to refine a `Topic`.
5. A channel editor later receives the assignment-relevant subset of that analytical material.

## Implementation Guardrail

If an implementation choice would make editorial behave like:
- a raw-signal consumer
- a desk-note-only consumer
- a system that rebuilds obsolete shadow analytical objects in the producer layer

that implementation is drifting from the canonical Axis design.
