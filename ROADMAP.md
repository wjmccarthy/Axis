# Roadmap

## Purpose

This roadmap defines the staged MVP build sequence for Axis.

The goal is to:

- build the system in minimum viable stages
- prove each stage is viable before adding major complexity
- make prerequisites explicit
- keep stage scope balanced in implementation effort and time
- delay downstream editorial execution until upstream intelligence is real

[`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md) remains canonical.

## Roadmap Rules

- Build from runtime and signal infrastructure toward expert interpretation, desk synthesis, editorial, then publication.
- Each MVP must prove a real operating behavior, not just scaffolding or file creation.
- Do not pull producer workflow forward before expert routing and analytical-desk synthesis are proven.
- Do not pull channel-specific behavior forward before Editors Desk topic generation is proven.
- Architecture guidance under [`docs/architecture/`](/Users/wjm/Code/Axis/docs/architecture) is subordinate to the spec and exists to reduce implementation drift.
- Current first-pass desk and expert implementation shape lives in [`docs/implementation/`](/Users/wjm/Code/Axis/docs/implementation/), not in this roadmap.

## MVP 1: Runtime Spine

### Goal

Get Axis alive inside the OpenClaw runtime with a working communications surface.

### Includes

- Assistant running inside the OpenClaw runtime
- Discord added as the communications channel

### Excludes

- signal collection
- watcher subagents
- expert interpretation
- analytical-desk behavior
- editorial behavior

### Why This Stage Exists

Axis must first exist as a working runtime system before any watcher, expert, desk, or editorial behavior matters.

### Prerequisites

- canonical spec
- OpenClaw-native implementation posture

### New Implementation Notes To Read

- [`docs/architecture/implementation-reading-order.md`](/Users/wjm/Code/Axis/docs/architecture/implementation-reading-order.md)
- [`docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md`](/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md)
- [`docs/architecture/guide-authoring-rules.md`](/Users/wjm/Code/Axis/docs/architecture/guide-authoring-rules.md)
- [`docs/architecture/deferred-implementation-boundaries.md`](/Users/wjm/Code/Axis/docs/architecture/deferred-implementation-boundaries.md)
- [`docs/architecture/term-boundaries.md`](/Users/wjm/Code/Axis/docs/architecture/term-boundaries.md)

### Proof Of Viability

- Assistant runs in the OpenClaw runtime
- Discord supports bidirectional command/control and thread routing as the communications surface

## MVP 2: First Signal Producers

### Goal

Prove that Axis can generate both external and strategist-generated signals.

### Includes

- Report Watch generating canonical `Signals`
- Strategist running and generating `Viewpoint Signals`

### Excludes

- broad watcher surface
- expert state
- analytical-desk synthesis
- editorial behavior

### Why This Stage Exists

Axis needs both incoming external signals and strategist-generated guidance before the interpretive system can become real.

### Prerequisites

- MVP 1
- Report Watch implementation guidance
- signal ingestion and Signal Desk guidance

### New Implementation Notes To Read

- [`docs/architecture/signal-desk-operating-guide.md`](/Users/wjm/Code/Axis/docs/architecture/signal-desk-operating-guide.md)
- [`docs/architecture/signal-ingestion.md`](/Users/wjm/Code/Axis/docs/architecture/signal-ingestion.md)
- [`docs/architecture/report-watch.md`](/Users/wjm/Code/Axis/docs/architecture/report-watch.md)
- [`docs/architecture/artifact-model.md`](/Users/wjm/Code/Axis/docs/architecture/artifact-model.md)
- [`docs/architecture/linking-model.md`](/Users/wjm/Code/Axis/docs/architecture/linking-model.md)

### Proof Of Viability

- Report Watch emits canonical `Signals`
- Strategist emits `Viewpoint Signals`

## MVP 3: Expert Routing And Expert State

### Goal

Prove that routed signals reach the right experts and that experts can maintain usable expert-local state.

### Includes

- signal routing to experts
- expert remit-driven consumption
- `Expert Feed`
- `Expert Watchlist`
- `Expert Ideas`
- `Expert Beliefs`
- `Expert Calls`
- `Expert Surface`

### Excludes

- analytical-desk synthesis
- desk current-state publication
- editorial behavior

### Why This Stage Exists

The new architecture depends on experts as the first-order consumers of signal flow. That layer has to be real before desk synthesis can be trusted.

The current first-pass expert roster and remit shape are maintained in [`docs/implementation/desk-and-expert-roster.md`](/Users/wjm/Code/Axis/docs/implementation/desk-and-expert-roster.md).

### Prerequisites

- MVP 2

### New Implementation Notes To Read

- [`docs/architecture/analytical-desk-operating-guide.md`](/Users/wjm/Code/Axis/docs/architecture/analytical-desk-operating-guide.md)
- [`docs/architecture/memory-model.md`](/Users/wjm/Code/Axis/docs/architecture/memory-model.md)
- [`docs/implementation/desk-and-expert-roster.md`](/Users/wjm/Code/Axis/docs/implementation/desk-and-expert-roster.md)

### Proof Of Viability

- routed signals reach the intended experts
- experts maintain usable expert-local state
- experts can surface active calls and selected ideas through `Expert Surface`

## MVP 4: Analytical Desk Synthesis Loop

### Goal

Prove that Analytical Desks can synthesize expert input into current desk state and outward analytical output.

### Includes

- desk composition from assigned experts
- `Desk Feed`
- `Desk Ideas`
- `Desk Beliefs`
- `Desk Debates`
- `Current State Surface`
- `Desk Note`
- strategist participation in desk deliberation
- desk question handling

### Excludes

- Research Desk
- producer-desk topic generation

### Why This Stage Exists

This is the first stage that proves Axis has real desk-level intelligence rather than only collection and expert-local interpretation.

The current first-pass analytical desk set, desk memberships, and desk explanation styles are maintained in [`docs/implementation/desk-and-expert-roster.md`](/Users/wjm/Code/Axis/docs/implementation/desk-and-expert-roster.md).

### Prerequisites

- MVP 3

### New Implementation Notes To Read

- [`docs/implementation/desk-and-expert-roster.md`](/Users/wjm/Code/Axis/docs/implementation/desk-and-expert-roster.md)

### Proof Of Viability

- analytical desks maintain usable desk state
- desks publish coherent current-state surfaces
- desks can issue desk notes when warranted
- strategist can consume and influence desk output without recreating an obsolete analytical layer

## MVP 5: Research Support Loop

### Goal

Prove that research support deepens the already-working expert and desk system.

### Includes

- `Research Request` creation by Analytical Desks
- Research Desk fulfillment
- `Research Brief` delivery back to the requesting desk

### Excludes

- Editors Desk
- channel-editor execution

### Why This Stage Exists

Research should deepen an already working intelligence system, not substitute for it.

### Prerequisites

- MVP 4

### New Implementation Notes To Read

- [`docs/architecture/research-desk-operating-guide.md`](/Users/wjm/Code/Axis/docs/architecture/research-desk-operating-guide.md)

### Proof Of Viability

- Analytical Desks can open valid `Research Requests`
- Research Desk can return usable `Research Briefs`
- desks can use those briefs without changing the core expert-plus-desk model

## MVP 6: Signal Retrieval Loop

### Goal

Prove that Analytical Desks can request bounded signal search from Signal Desk over retained signal history.

### Includes

- `Signal Request` creation by Analytical Desks
- Signal Desk fulfillment of bounded signal search
- signal-dump or bounded search-result return to the requesting desk

### Excludes

- Editors Desk
- channel-editor execution
- broad retrieval productization beyond signal-side search

### Why This Stage Exists

Before producer desks begin generating topics from the upstream system, Analytical Desks should be able to pull bounded signal history without confusing signal retrieval with research work.

### Prerequisites

- MVP 5

### New Implementation Notes To Read

- [`docs/architecture/retrieval-policy.md`](/Users/wjm/Code/Axis/docs/architecture/retrieval-policy.md)

### Proof Of Viability

- Analytical Desks can open valid `Signal Requests`
- Signal Desk can return bounded signal-search results for a specified time range and filter criteria
- desks can use those results without confusing them with `Research Briefs`

## MVP 7: Editors Desk Topic Generation

### Goal

Prove that Editors Desk can generate viable `Topics` from the upstream intelligence system.

### Includes

- Editors Desk running
- one current `Editorial Agenda`
- one current `Editors Feed`
- one current `Editors Scratchpad`
- inspection of analytical-desk current-state surfaces
- subscription to desk notes
- direct desk questions
- topic generation and topic management

### Excludes

- channel-specific publication execution
- broad channel scheduling complexity

### Why This Stage Exists

Editors Desk should appear only after signal production, expert interpretation, desk synthesis, and support loops are already real.

### Prerequisites

- MVP 6

### New Implementation Notes To Read

- [`docs/architecture/editorial-consumption.md`](/Users/wjm/Code/Axis/docs/architecture/editorial-consumption.md)

### Proof Of Viability

- Editors Desk can generate viable `Topics` from analytical-desk output
- Editors Desk maintains usable `Editorial Agenda`, `Editors Feed`, and `Editors Scratchpad`
- topic generation reflects current analytical state rather than a direct raw-signal firehose

## MVP 8: Single-Channel Publication Loop

### Goal

Prove the first full Topic-to-publication loop through one channel editor.

### Includes

- one channel editor
- approved `Topic` to `Editorial Assignment` flow
- draft creation
- `Publication Item` creation

### Excludes

- multiple channel types
- broad publication scheduling complexity

### Why This Stage Exists

Publication should be proven only after upstream signal, expert, desk, research, and editorial topic generation are already working.

### Prerequisites

- MVP 7

### New Implementation Notes To Read

- [`docs/architecture/publication-item-operating-guide.md`](/Users/wjm/Code/Axis/docs/architecture/publication-item-operating-guide.md)
- [`docs/architecture/publication-attribution.md`](/Users/wjm/Code/Axis/docs/architecture/publication-attribution.md)

### Proof Of Viability

- one channel editor can execute an approved `Topic` into a draft and `Publication Item`
- the publication loop uses routed analytical inputs rather than bypassing the upstream system

## MVP 9: Optional Watcher Expansion

### Goal

Add watcher breadth beyond Report Watch.

### Includes

- additional watcher subagents beyond Report Watch
- broader heterogeneous collection behavior under Signal Desk
- canonical `Signal` normalization across additional watcher types

### Excludes

- redesign of the already-proven core loop

### Why This Stage Exists

The first full Axis loop can run on Report Watch alone. Broader watcher expansion is valuable, but optional until the core system loop is proven.

### Prerequisites

- MVP 8

### New Implementation Notes To Read

- no new implementation notes by default

### Proof Of Viability

- additional watcher types emit canonical `Signals`
- Signal Desk coordinates them without downstream contract drift

## MVP 10: System Expansion

### Goal

Expand from the first proven publication loop to the full intended system.

### Includes

- more watcher depth
- more experts
- more analytical desks
- more producer surfaces
- more channel editors
- broader operational complexity once the core model is proven

### Excludes

- unnecessary redesign of already-proven earlier stages

### Why This Stage Exists

This stage expands a proven system rather than trying to discover the architecture at full complexity.

### Prerequisites

- MVP 9

### New Implementation Notes To Read

- no new implementation notes by default

### Proof Of Viability

- additional system surfaces can be added without breaking the proven core model
- Axis scales by extension rather than architectural reinvention
