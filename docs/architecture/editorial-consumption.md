# Axis Editorial Consumption Guide

## Purpose

This document defines how editorial components consume analytical output from Domain Desks.

It governs:
- which analytical surfaces editorial consumes
- which surfaces are more authoritative versus faster
- how editorial workflow uses analytical input without dense analytical linking

It does not govern:
- topic approval authority
- assignment lifecycle authority
- OpenClaw runtime behavior

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md) and official OpenClaw documentation.

## Canonical Rule

The editorial layer may consume all of the following from Domain Desks:

- Desk Thesis
- Desk View
- Theme Thesis
- Theme View
- Desk Note
- Research Brief

Editorial does not consume raw signals as its primary analytical surface.

Important distribution distinction:
- Strategist receives current desk and theme analytical output across the system.
- Domain Desks send the analytical surfaces below to Editors Desk by default.
- Signal Desk may also route designated trend-oriented canonical Signals directly to Editors Desk for Topic generation and sequencing.
- Editors Desk uses that full editorial-facing analytical surface for Topic generation and sequencing.
- Channel editors receive the subset relevant to their current Assignments, routed through Editors Desk.
- Editors Desk maintains its own working memory distinct from Topics and Assignments.

## Authority and Timing

The analytical surfaces are not equal.

- Desk Views and Theme Views are the authoritative current analytical state.
- Desk Theses and Theme Theses are the more durable conviction layer behind that current state.
- Desk Notes are faster point-in-time expressions of judgment and may surface before the more authoritative views are updated in fast-moving situations.
- Research Briefs are research products used when evidence, background, or deeper support is needed.

Important:
- Desk Notes do not displace Desk Views or Theme Views as the standing analytical authority.
- In fast-moving situations, a newer Desk Note may be the current tactical read until the authoritative view catches up.

## Editors Desk

Editors Desk maintains:

- its current Theme List
- its current Editors Feed
- its current Editors Scratchpad

Important:
- Theme List is the Editors-Desk working document for current thematic framing and sequencing context
- Editors Feed and Editors Scratchpad are Editors-Desk-local working memory, not workflow objects
- Topics remain the canonical editorial workflow object

### From Domain Desks

Editors Desk receives by default:

- Desk Thesis
- Desk View
- Theme Thesis
- Theme View
- Desk Note
- relevant Research Brief

### From Signal Desk

Editors Desk may also receive designated trend-oriented canonical Signals from Signal Desk for Topic generation and sequencing.

Editors Desk uses these to:

- create and refine Topics
- manage backlog, slate, sequencing, and reuse planning
- maintain continuity across channels
- pair what is trending with what Axis thinks
- generate Topics that fit both the analytical realm and audience attention
- improve sequencing and framing

Editors Desk should not treat Desk Notes as the sole or default analytical substrate.
Editors Desk should not treat designated trend-oriented canonical Signals as substitutes for domain analytical authority.

Axis does not require:

- channel editors to consume designated trend-oriented canonical Signals directly by default
- designated trend-oriented canonical Signals to serve as final interpretation
- every trend signal to become a Topic

## Editors Desk Working Memory

Editors Desk needs local working memory in addition to Topics and Assignments.

The intended default shape is:

- `Theme List`
  - one current Editors-Desk document
  - holds current thematic framing, development context, and sequencing context
  - is distinct from Topics as workflow objects

- `Editors Feed`
  - one current Editors-Desk document
  - holds the last `N` feed items most relevant to Topic generation and sequencing
  - may include domain analytical output and designated trend-oriented canonical Signals

- `Editors Scratchpad`
  - one current Editors-Desk document
  - holds developing topic ideas, trend/theme pairings, sequencing thoughts, and pre-Topic working material
  - should preserve archived history over time

Important:
- Theme List is the current editorial working document, not a workflow object
- Editors Feed and Editors Scratchpad are working memory, not shared final workflow state
- implementation should not force a rigid schema onto these working documents beyond these role boundaries

## Channel Editors

Channel editors consume the subset relevant to their current Assignments from:

- Desk Thesis
- Desk View
- Theme Thesis
- Theme View
- Desk Note
- relevant Research Brief

Channel editors use these to:

- interpret the current analytical state
- execute Editorial Assignments
- request clarification through the relevant Domain Desk when needed

Channel editors should not treat Desk Notes as the only valid analytical input.
Channel editors do not need blanket receipt of all desk output across the system.
Editors Desk is the normal routing layer for what channel editors receive for a given Assignment.

## How Editorial Should Read the Surfaces

### Desk Thesis

Use when editorial needs the desk's more durable domain conviction.

This is useful for:
- continuity
- structural framing
- deciding whether a development fits an existing long-running domain belief

### Desk View

Use when editorial needs the desk's current domain interpretation.

This is usually the most authoritative current desk-level analytical input.

### Theme Thesis

Use when editorial needs the durable conviction behind a theme.

This is useful for:
- continuity across time
- strategic framing
- connecting current developments back to the longer-running theme logic

### Theme View

Use when editorial needs the current interpretation of a theme.

This is usually the most authoritative current theme-level analytical input.

### Desk Note

Use when editorial needs a fast explicit judgment artifact.

This is especially useful in:
- fast-moving situations
- moments where a bounded point-in-time interpretation is needed quickly

Desk Notes may be newer than the standing views, but they are generally less authoritative than current views once those views are updated.

### Research Brief

Use when editorial needs:
- additional evidence
- deeper factual support
- reusable research output relevant to the current execution

Research Briefs support interpretation and execution, but they are not the current standing analytical state.

## Workflow Anchoring

Editorial workflow objects should not require dense analytical linking into desk state.

The explicit downstream links that matter are:

- workflow lineage between Topic, Editorial Assignment, Draft, and Publication Item
- Source Material linkage where attribution or provenance materially matters

Implementation should not force Topics, Editorial Assignments, Drafts, or Publication Items to carry structured links to desk theses, desk views, theme theses, theme views, desk notes, or research briefs by default.

## Worked Example: Assignment Support Update

This example shows the intended routing behavior during active execution.

1. A channel editor asks a relevant Domain Desk for help on an active Assignment.
2. The Domain Desk issues a Desk Note.
3. Strategist receives that Desk Note as part of the desk's default analytical output.
4. If Strategist needs to change current posture, Strategist issues a Viewpoint Signal.
5. The Domain Desk updates its current understanding and, if the changed posture should be expressed outwardly for the active Assignment, issues a new Desk Note.
6. Editors Desk routes that refreshed assignment-relevant Desk Note to the channel editor.

This is an event-based flow.

It does not require:
- a separate coordination layer
- direct raw Viewpoint Signal delivery to the channel editor
- the original Desk Note to remain the operative tactical read once the desk has issued the refreshed note

## What Is Not Required

Axis does not require:

- Desk Notes to exist before editorial can use current views or theses
- Research Briefs to exist before editorial can act when current domain understanding is sufficient
- editorial to choose exactly one analytical surface per Topic or Assignment
- Desk Notes to be treated as more authoritative than current views

## Implementation Guardrail

If an implementation choice would cause editorial behavior to collapse back to:

- Desk Notes plus Research Briefs only
- or Desk Notes as the sole analytical authority

that implementation is drifting from the canonical Axis design.

If an implementation choice would make designated trend-oriented canonical Signals behave like:

- final analytical authority
- direct channel-editor input by default
- a replacement for Domain Desk interpretation

that implementation is also drifting from the canonical Axis design.
