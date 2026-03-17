# Axis Term Boundaries

## Purpose

This note defines the minimal term boundaries most likely to cause implementation drift.

It is not a full glossary.

## Signal

A `Signal` is a normalized observation or Strategist-generated guidance object in the signal layer.

It is used for:
- routing
- ranking
- attention
- monitoring

It is not:
- a Research Brief
- a Desk Note
- a Topic
- a publication object

## Viewpoint Signal

A `Viewpoint Signal` is a Strategist-generated signal used to express priorities, judgments, or system-level interpretive direction.

It is not:
- a desk note
- a research product
- a desk-owned current-state object

## Source Material

`Source Material` is attributable retained material referenced by the system.

Examples:
- quotes
- visuals
- charts
- tables
- excerpts
- clips

It is not:
- automatically a `Signal`
- automatically a publication asset
- a replacement for the underlying retained source artifact

## Expert

An `Expert` is a permanent system-level interpretive agent with a standing remit.

It is:
- the primary routing target for signals
- assignable to one or more Analytical Desks
- the owner of expert-local state and an `Expert Surface`

It is not:
- a desk
- a producer-side consumer
- a workflow object

## Expert Feed

`Expert Feed` is the expert-local recent-signal working surface.

It is:
- expert-local
- signal-rooted
- recent-input working memory

It is not:
- shared current analytical state
- a desk feed

## Expert Watchlist

`Expert Watchlist` is the expert-local tracked set derived from expert feed.

It is:
- a distilled tracked layer
- inclusive of selected feed items and derived/calculated items
- part of what the expert exposes outwardly

It is not:
- the full feed
- the desk’s adopted state

## Expert Ideas

`Expert Ideas` are tentative expert interpretations in the expert’s own scope.

They are:
- narrower than desk ideas
- curated by the expert
- eligible to inform calls and contributions

They are not:
- desk-level adopted state

## Expert Beliefs

`Expert Beliefs` are the expert’s condensed standing knowledge in its own remit.

They are:
- slower-moving than expert ideas
- exposed on the expert surface
- one input into desk-level synthesis

They are not:
- desk beliefs
- strategist-owned state

## Expert Calls

`Expert Calls` are desk-directed interventions created by an expert.

They may:
- propose a new desk idea
- support an existing desk idea
- challenge an existing desk idea
- support an existing desk belief
- challenge an existing desk belief

They are not:
- the same thing as ordinary contributions
- desk-owned state

## Contribution

A `Contribution` is an expert’s participation inside ongoing desk deliberation.

It is:
- desk-directed
- lighter-weight than a call
- part of active desk debate

It is not:
- the same thing as an `Expert Call`
- adopted desk state by itself

## Expert Surface

`Expert Surface` is the expert’s persisted current-state publication object.

It contains:
- watchlist
- beliefs
- selected ideas
- active calls

It is not:
- the full expert memory
- a desk surface

## Analytical Desk

An `Analytical Desk` is the top analytical synthesis unit in Axis.

It is:
- composed from assigned experts
- the layer where mixture-of-experts reasoning is implemented
- the owner of desk-level ideas, beliefs, debates, and current-state publication

It is not:
- a first-order signal inbox
- a single expert
- a separate strategic-framing object

## Desk Feed

`Desk Feed` is the desk-local feed of expert calls, expert contributions, and other relevant desk input.

It is:
- desk-local
- the intake surface for desk deliberation
- distinct from direct signal routing

It is not:
- raw signal flow
- the desk’s published current state

## Desk Ideas

`Desk Ideas` are the desk’s live debated claims.

They are:
- the short-cycle frontier of desk thinking
- eligible to become beliefs
- persistent when needed

They are not:
- the same thing as desk notes
- the same thing as desk beliefs

## Desk Beliefs

`Desk Beliefs` are adopted desk-level claims with enough agreement to count as current desk position.

They are:
- the longer-cycle adopted desk layer
- part of the desk’s standing current state

They are not:
- all of desk state by themselves
- equivalent to a point-in-time desk note

## Desk Debates

`Desk Debates` are the internal deliberative memory around desk ideas and beliefs.

They are:
- internal
- part of desk state
- the reasoning context behind support, challenge, and movement

They are not:
- exposed current state
- a producer-facing surface

## Current State Surface

`Current State Surface` is the desk’s persisted current-state publication object.

It contains:
- core position
- current beliefs
- selected ideas

It is:
- inspectable across the system
- the main standing desk-state interface

It is not:
- the desk’s full internal memory
- the same thing as a desk note

## Desk Note

A `Desk Note` is a point-in-time outward expression of desk judgment.

It is:
- bounded
- explicit
- faster than the current-state surface in some situations

It is not:
- the desk’s full current understanding
- mandatory for every development
- a replacement for standing current state

## Editorial Agenda

`Editorial Agenda` is the Editors-Desk working document for current editorial framing and sequencing context.

It is:
- editorial working state
- distinct from Topics as workflow objects

It is not:
- a Topic
- an Editorial Assignment
- a published output

## Editors Feed

`Editors Feed` is the Editors-Desk recent-input working document.

It is:
- editorial working memory
- recent analytical/editorial input flow

It is not:
- a workflow object
- shared final editorial state

## Editors Scratchpad

`Editors Scratchpad` is the Editors-Desk notebook for developing topic ideas and sequencing thoughts.

It is:
- working memory
- editorial and developmental

It is not:
- a Topic
- an Editorial Assignment

## Strategist Feed History

`Strategist Feed History` is Strategist’s recent-input working document.

It is:
- strategist working memory
- recent cross-desk input context

It is not:
- a formal signal object
- shared current analytical state

## Strategist Scratchpad

`Strategist Scratchpad` is Strategist’s notebook for developing synthesis and pre-decision reasoning.

It is:
- strategist working memory
- developmental and cross-domain

It is not:
- a formal signal
- a workflow object

## Research Request

A `Research Request` is a bounded request from an Analytical Desk for new research support.

It is:
- desk-opened
- routed to Research Desk
- used when existing desk knowledge is insufficient

It is not:
- a Signal Request
- a Research Brief

## Signal Request

A `Signal Request` is a bounded request from an Analytical Desk to Signal Desk for signal-side search over retained signals.

It is used for:
- time-bounded search
- filtered retrieval
- bounded signal dumps for desk use

It is not:
- new research work
- a Research Brief

## Research Brief

A `Research Brief` is a bounded reusable research product produced by Research Desk.

It is:
- evidence and findings support
- reusable
- an input into later desk and producer work

It is not:
- desk current state
- final desk interpretation

## Chart Follow-Up

A `Chart Follow-Up` is a retained downstream artifact created when a source surfaces a chart-worthy claim or comparison worth later extraction, clipping, or reconstruction.

It is:
- signal-side support material
- grounded in a retained source and extracted claim

It is not:
- a desk note
- a publication object by default

## Topic

A `Topic` is the shared editorial subject tracked by Editors Desk through its lifecycle.

It is:
- editorial
- cross-channel
- the parent of zero or more Editorial Assignments

It is not:
- a signal
- an assignment

## Editorial Assignment

An `Editorial Assignment` is the instruction to turn an approved Topic into channel-specific output.

It is:
- channel-specific
- owned by the relevant channel editor

It is not:
- the Topic itself
- the final Publication Item

## Draft

A `Draft` is working channel-specific editorial output under active execution.

It is not:
- desk state
- the final published asset

## Publication Item

A `Publication Item` is the publication-ready or final externally distributed output object.

It is not:
- a Draft
- a raw research artifact
- exempt from attribution requirements
