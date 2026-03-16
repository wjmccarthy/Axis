# Axis Domain Desk Operating Guide

## Purpose

This document defines how a Domain Desk should operate inside Axis.

It governs:
- what a Domain Desk works from
- what a Domain Desk receives
- what a Domain Desk maintains
- what a Domain Desk shares with editorial and theme leads
- what a Domain Desk is not required to formalize

It does not govern:
- topic approval authority
- editorial assignment authority
- OpenClaw runtime behavior

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md) and official OpenClaw documentation.

## Canonical Role

A Domain Desk is the system's domain-specific interpretive authority for its mandate.

A Domain Desk does not operate as:

- a raw-signal inbox
- a note-production machine
- a single-view object

A Domain Desk operates from its current synthesized understanding.

## What a Domain Desk Receives

A Domain Desk receives:

- routed External Signals
- relevant Viewpoint Signals
- Research Briefs produced in response to its Research Requests
- existing desk understanding
- relevant collaborator-desk views and notes where needed
- editorial requests for interpretation, clarification, or support

## What a Domain Desk Maintains

A Domain Desk maintains:

- its current Beliefs
- its current Signal Feed
- its current Desk Scratchpad

If the desk leads one or more themes, it also maintains:

- Theme Theses and Theme Views for those themes inside its current Beliefs

Important:
- a Domain Desk does not operate from one single Desk View
- the desk's current understanding is represented through the current Beliefs container
- Desk Notes do not fully represent the desk's current understanding
- Signal Feed and Desk Scratchpad are desk-local working memory, not shared analytical output

## What a Domain Desk Works From

A Domain Desk works from its current synthesized understanding.

That current synthesized understanding may draw on:

- the current Beliefs
- the current Signal Feed
- the current Desk Scratchpad
- reviewed signals
- Research Briefs
- prior desk understanding
- relevant collaborator-desk views and notes
- current editorial demand

Implementation should not collapse this into a requirement that the desk always acts from one single object.

The intended default shape is:

- one current Beliefs file per desk
- one current Signal Feed document per desk holding the last `N` relevant routed signals
- one current Desk Scratchpad document per desk with archived history over time
- Desk Thesis, Desk Views, Theme Theses, and owned Theme Views represented inside the Beliefs file
- internal sections or subviews inside the Beliefs file where needed

Implementation should not default to many peer current-state documents for the same desk unless later implementation pressure proves that necessary.

## Signal Handling

When a signal is routed to a Domain Desk:

- the desk receives a persistent desk-local routed-signal record
- that record is marked only by whether it has been reviewed
- the desk may review the signal immediately or later

Important:
- a reviewed signal does not require a Desk Note
- a reviewed signal may affect desk understanding without producing a new outward artifact
- Axis does not require a per-signal mutation ledger for desk-state changes
- repeated or resurfacing signals may accumulate in Signal Feed and Desk Scratchpad before they justify Beliefs changes

## View and Thesis Evolution

Domain Desks may evolve their Beliefs from reviewed signals and other valid inputs.

Important:
- not every internal change requires a new formal artifact
- not every reviewed signal requires a note
- not every view change needs explicit per-signal linkage

Desk Theses and Theme Theses are the more durable conviction layer inside Beliefs.

Desk Views and Theme Views are the current evolving interpretation layer inside Beliefs.

Update pattern:
- thesis changes should be less frequent and should reflect durable conviction changes
- view changes may happen more frequently as current interpretation, weighting, or emphasis changes
- a restatement may refresh wording or emphasis without changing underlying meaning
- a revision changes current Beliefs substantively
- older state does not need to remain live inside current Beliefs once it is no longer current
- historical state remains recoverable through archived daily Beliefs

Current desk state should remain explicit inside Beliefs.

Desks may age out views by removing them from current Beliefs when those views no longer belong in current standing state.

## Desk-Local Working Memory

Domain Desks need temporal working memory in addition to Beliefs.

That working memory should remain desk-local and should not be treated as shared analytical output.

The intended default shape is:

- `Signal Feed`
  - one current desk-local document
  - holds the last `N` routed signals most relevant to the desk
  - exists so repeated ignored signals, recurrence, and short-horizon pattern pressure do not disappear immediately

- `Desk Scratchpad`
  - one current desk-local document
  - holds developing views, unresolved patterns, repeated motifs, and pre-Beliefs thinking
  - should preserve archived history over time

Important:
- Beliefs is the desk's current shared analytical state
- Signal Feed and Desk Scratchpad are working memory, not shared state
- implementation should not force a rigid schema onto Signal Feed or Desk Scratchpad beyond these role boundaries

## Desk Notes

Desk Notes are:

- fast explicit outward expressions of desk judgment
- point-in-time analytical artifacts
- generally less authoritative than the current views once those views are updated

Desk Notes are not:

- the full internal state of the desk
- mandatory outputs of signal review
- required before editorial can use the desk's current analytical state

In fast-moving situations, a Desk Note may surface before the more authoritative current view has been updated.

## Research Interaction

A Domain Desk may open a Research Request when existing knowledge is not sufficient.

The resulting Research Brief is used by the requesting desk as a research product.

Research Briefs may inform:

- Beliefs
- Desk Notes

Research Briefs are not themselves the desk's current standing analytical state.

## Worked Example: Assignment Support and Strategist Correction

This example is implementation guidance, not a new workflow object.

1. A channel editor working on an active Editorial Assignment requests story help from a relevant Domain Desk.
2. The Domain Desk responds with a Desk Note.
3. That Desk Note is part of the desk's analytical output and is therefore received by Strategist and Editors Desk.
4. Strategist disagrees with the posture implied by that Desk Note and issues a Viewpoint Signal.
5. The Domain Desk updates its current understanding in light of that Viewpoint Signal.
6. Because there is an active Assignment and the desk's outward judgment has now materially changed, the Domain Desk would typically issue a new Desk Note.
7. Editors Desk routes that refreshed assignment-relevant Desk Note to the channel editor.

Important:
- the second Desk Note is still the desk's own outward judgment after incorporating the Strategist's Viewpoint Signal
- the desk is not simply forwarding the Viewpoint Signal directly to the channel editor
- no extra coordination layer is required for this flow

## Theme Interaction

If a Domain Desk leads a theme:

- it owns that theme's Theme Thesis and Theme View
- the Theme View must remain anchored in and consistent with the lead desk's Desk View
- the Theme Thesis must remain anchored in and consistent with the lead desk's Desk Thesis
- no separate theme-coordination object or extra theme-update mechanism is required

If a Domain Desk collaborates on a theme led by another desk:

- its views and notes may be shared with the lead desk
- the lead desk owns the resulting Theme Thesis and Theme View

## What a Domain Desk Shares

A Domain Desk shares the following analytical surfaces into the system:

- Desk Thesis
- Desk View
- Theme Thesis
- Theme View
- Desk Note
- relevant Research Brief

Distribution should follow role relationships:

- Strategist receives current desk and theme analytical output across the system.
- Domain Desks send their editorial-facing analytical output to Editors Desk by default for Topic generation and sequencing.
- Channel editors receive the subset relevant to their current Assignments, routed through Editors Desk.
- A collaborator desk may also selectively share relevant views and notes with a lead desk when it is collaborating on a theme led elsewhere.

## What Is Not Required

Axis does not require:

- one Desk Note per reviewed signal
- one reviewed signal per Desk Note
- a single monolithic Desk View as the desk's only working surface
- explicit signal-to-view mutation records for every internal adjustment
- a separate theme-collaboration update object
- Strategist acting as the day-to-day theme operator

## Implementation Guardrail

If an implementation choice would cause a Domain Desk to behave like:

- a queue processor that must externalize every reviewed signal
- a system that only works from one current view object
- a note-driven layer where desk understanding is reduced to Desk Notes

that implementation is drifting from the canonical Axis design.

If an implementation choice would make theme ownership depend on:

- a separate coordination layer
- a special collaborator-update object
- Strategist acting as the day-to-day theme operator

that implementation is also drifting from the canonical Axis design.
