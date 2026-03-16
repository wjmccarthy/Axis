# Axis Term Boundaries

## Purpose

This note defines the minimal term boundaries most likely to cause implementation drift.

It is not a full glossary.

## Signal

A `Signal` is a normalized observation or Strategist-generated guidance object in the system's signal layer.

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

## Source Material

`Source Material` is attributable material retained and referenced by the system.

Examples:

- quotes
- visuals
- charts
- tables
- excerpts
- clips

It is not the same thing as:

- the root source artifact itself
- automatically a Signal
- automatically a publication asset

## Research Brief

A `Research Brief` is a bounded reusable research product produced by Research Desk in response to a Research Request.

It is used for:

- evidence
- findings
- support
- reuse

It is not:

- current desk state
- final domain interpretation
- a Desk Note

## Signal Request

A `Signal Request` is a bounded request from a Domain Desk to Signal Desk for signal-side search over retained signals.

It is used for:

- time-bounded signal search
- filtered signal retrieval
- signal dumps for desk interpretation

It is not:

- a Research Request
- a Research Brief
- new research work

## Desk Note

A `Desk Note` is a point-in-time outward expression of selected desk judgment.

It is:

- faster
- bounded
- explicit

It is not:

- the desk's full current understanding
- mandatory for every reviewed signal
- more authoritative than current views once those views are updated

## Beliefs

`Beliefs` is the desk-owned container for a desk's current analytical state.

It is:

- the canonical current-state object for a desk
- represented canonically as a Markdown file
- the container for Desk Thesis, Desk Views, Theme Theses, and owned Theme Views

It is not:

- just one Desk View
- a Desk Note
- a Research Brief

## Signal Feed

`Signal Feed` is the desk-local recent-signal working document.

It is:

- a rolling last-`N` signal surface
- temporal working memory over recent routed signal flow
- desk-local

It is not:

- Beliefs
- a Desk Note
- shared analytical output

## Desk Scratchpad

`Desk Scratchpad` is the desk-local notebook for developing patterns and pre-Beliefs thinking.

It is:

- working memory
- temporal and developmental
- archived over time

It is not:

- Beliefs
- shared analytical output
- a formal Desk Note

## Theme List

`Theme List` is the Editors-Desk working document for current thematic framing and sequencing context.

It is:

- editorial working state
- current thematic context for Topic generation
- distinct from Topics as workflow objects

It is not:

- a Topic
- an Editorial Assignment
- a published output

## Editors Feed

`Editors Feed` is the Editors-Desk recent-input working document.

It is:

- a rolling last-`N` feed-items surface
- editorial working memory over current analytical and trend inputs
- desk-local

It is not:

- a Topic
- a workflow object
- shared final editorial state

## Editors Scratchpad

`Editors Scratchpad` is the Editors-Desk notebook for developing topic ideas and sequencing thoughts.

It is:

- working memory
- editorial and developmental
- archived over time

It is not:

- a Topic
- an Editorial Assignment
- a formal publication object

## Strategist Feed History

`Strategist Feed History` is the Strategist recent-input working document.

It is:

- a rolling recent-feed surface
- strategist working memory over current cross-domain inputs
- local to Strategist

It is not:

- a formal signal object
- a workflow object
- shared analytical state

## Strategist Scratchpad

`Strategist Scratchpad` is the Strategist notebook for developing synthesis and pre-decision reasoning.

It is:

- working memory
- cross-domain and developmental
- archived over time

It is not:

- a formal signal
- an approval object
- a workflow object

## Desk Thesis

A `Desk Thesis` is the desk's more durable conviction layer.

It is:

- slower-moving
- structural
- part of the basis for current Desk Views

It is not:

- a Strategist Thesis Signal
- the same thing as a Desk View

## Desk View

A `Desk View` is the desk's current evolving interpretation layer.

It is:

- more current than a Desk Thesis
- more authoritative than a Desk Note as standing analytical state
- built on top of the current Desk Thesis

It is not:

- the same thing as a Desk Note
- required to map one-to-one to signals

## Theme Thesis

A `Theme Thesis` is the durable conviction layer for a theme.

It is:

- owned by the lead desk
- slower-moving
- anchored in the lead desk's Desk Thesis

It is not:

- owned day-to-day by Strategist
- the same thing as a Theme View

## Theme View

A `Theme View` is the current evolving interpretation of a theme.

It is:

- owned by the lead desk
- anchored in the lead desk's Desk View
- subject to Strategist override or reprioritization

It is not:

- a separate theme-coordination mechanism
- the same thing as the Theme definition itself

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

An `Editorial Assignment` is the instruction to turn an approved Topic and its supporting materials into channel-specific output.

It is:

- channel-specific
- owned by the relevant channel editor

It is not:

- the Topic itself
- the final Publication Item

## Draft

A `Draft` is working channel-specific editorial output under active execution.

It is not:

- the analytical state
- the final published asset

## Publication Item

A `Publication Item` is the publication-ready or final externally distributed output object.

It is not:

- a Draft
- a raw research artifact
- exempt from attribution requirements
