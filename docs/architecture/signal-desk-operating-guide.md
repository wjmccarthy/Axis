# Axis Signal Desk Operating Guide

## Purpose

This document defines the minimal implementation rule set for Signal Desk.

It governs:
- what Signal Desk owns
- how Signal Desk relates to collection subagents
- what Signal Desk must emit into the rest of Axis
- how Signal Desk fulfills bounded Signal Requests

It does not add new workflow.

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Canonical Role

Signal Desk is the collection coordination layer for Axis.

Signal Desk:

- coordinates specialized collection subagents
- normalizes heterogeneous source outputs into canonical Signals
- assigns initial signal rank
- routes normalized Signals to Domain Desks
- fulfills valid Signal Requests from Domain Desks

Signal Desk does not own final interpretation.

## Collection Subagents

Signal Desk may coordinate many collection subagents with very different behavior.

Those subagents may differ in:

- source type
- collection method
- parsing method
- staging behavior
- artifact shape
- watch cadence

Examples include:

- Report Watch
- YouTube Watch
- X Watch
- market or policy collection jobs
- other source-specific collectors

Important:
- these subagents do not define their own downstream analytical contract
- they all must produce output that can be normalized into canonical Axis Signals

## Canonical Output Requirement

No matter how different the collection subagents are, the rest of Axis should receive canonical Signals rather than watch-specific downstream objects.

That means:

- source-specific collection diversity is allowed
- downstream signal semantics must remain consistent

Signal Desk is the layer that makes heterogeneous collection behavior legible to the rest of the system.

Signal Desk may also have standing instructions to generate Source Material, such as charts for specific commodities or other tracked subjects.

When that Source Material is meant to be noticed, routed, and consumed as part of system attention, it should also be emitted or referenced through canonical Signals rather than remaining buried only as support material.

Some designated trend-oriented canonical Signals, especially from X Watch, YouTube Watch, or selected web-trend/query collection, may also be routed directly to Editors Desk for Topic generation and sequencing.

Those direct editorial trend inputs:

- remain canonical Signals rather than special watcher-specific downstream objects
- help Editors Desk understand what is currently attracting attention
- do not replace Desk Views, Theme Views, Desk Notes, or other domain analytical authority
- do not imply that channel editors should consume the raw signal firehose

## Routing Rule

- Signals route to Domain Desks, not to themes.
- Themes guide routing but are not themselves consumers.
- Routing creates a desk-local routed-signal record with a `reviewed` flag for each destination desk.

Signal Desk should not route directly to:

- channel editors
- Topics
- Editorial Assignments
- themes as consumers

## Signal Requests

Signal Desk may fulfill bounded Signal Requests from Domain Desks.

A Signal Request is for signal-side retrieval, not new research work.

It should allow a requesting desk to ask for:

- a specific time range
- filter criteria
- a bounded dump or search result over retained signals

Signal Desk should return signal-side results, not a Research Brief.

## Ranking Rule

Signal Desk assigns the initial signal rank based on:

- quality
- novelty
- timeliness
- corroboration
- expected significance
- fit to current themes and desk mandates

Domain Desks then apply relevance ranking within their own mandates.

## Non-Goals

Signal Desk should not be implemented as:

- a final interpretation desk
- a desk that produces Desk Notes
- a desk that owns Desk Views or Theme Views
- a set of source-specific downstream contracts with no canonical signal layer

## Implementation Guardrail

If an implementation choice would make Signal Desk behave like:

- a bundle of unrelated watch pipelines with incompatible downstream outputs
- a final analytical desk
- a system that routes directly from watches to editorial workflow objects

that implementation is drifting from the canonical Axis design.
