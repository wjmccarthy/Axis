# Axis Signal Desk Operating Guide

## Purpose

This document defines the minimal implementation rule set for Signal Desk.

It governs:
- what Signal Desk owns
- how Signal Desk relates to collection subagents
- what Signal Desk must emit into the rest of Axis
- how Signal Desk fulfills bounded `Signal Requests`

It does not add new workflow.

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Canonical Role

Signal Desk is the collection coordination layer for Axis.

Signal Desk:
- coordinates source-specific collection subagents
- normalizes heterogeneous source outputs into canonical `Signals`
- assigns initial signal rank
- routes normalized `Signals` to `Experts`
- fulfills valid `Signal Requests` from `Analytical Desks`

Signal Desk does not own final interpretation.

## Collection Subagents

Signal Desk may coordinate many collection subagents with different behavior.

Those subagents may differ in:
- source type
- collection method
- parsing method
- staging behavior
- artifact shape
- watch cadence

Examples include:
- `Report Watch`
- `YouTube Watch`
- `X Watch`
- market, policy, or other source-specific collectors

Important:
- subagents do not define their own downstream analytical contract
- they must all normalize into canonical `Signals` and related retained artifacts

## Canonical Output Requirement

The rest of Axis should receive canonical `Signals`, not watch-specific downstream objects.

That means:
- source-specific collection diversity is allowed
- downstream signal semantics must remain consistent

When Signal Desk emits additional retained artifacts such as `Source Material` or `Chart Follow-Up` outputs, those should remain linked to canonical `Signals` rather than acting as a parallel attention system.

## Routing Rule

Signals route to `Experts`, not directly to `Analytical Desks`.

Routing basis:
- expert remit
- current strategist guidance

Signal Desk should not route directly to:
- `Analytical Desks` as first-order signal consumers
- channel editors
- `Topics`
- `Editorial Assignments`

Routing creates expert awareness and optional expert review. Desk-level synthesis happens later through expert `Calls`, expert `Contributions`, and desk deliberation.

## Signal Requests

Signal Desk may fulfill bounded `Signal Requests` from `Analytical Desks`.

A `Signal Request` is for signal-side retrieval, not new research work.

It may ask for:
- a specific time range
- filter criteria
- a bounded dump or search result over retained signals and signal-side artifacts where useful

Signal Desk returns signal-side results, not `Research Briefs`.

## Ranking Rule

Signal Desk assigns initial signal rank based on:
- quality
- novelty
- timeliness
- corroboration
- expected significance
- fit to current routing guidance

Experts then apply remit-specific judgment within their own scope.

## Non-Goals

Signal Desk should not be implemented as:
- a final interpretation desk
- a desk that produces `Desk Notes`
- a direct editorial workflow router
- a bundle of unrelated watch pipelines with incompatible downstream contracts

## Implementation Guardrail

If an implementation choice would make Signal Desk behave like:
- a set of watch-specific outputs with no canonical signal layer
- a desk that routes primary signal flow directly into analytical desks
- a desk that bypasses experts as the interpretive routing target

that implementation is drifting from the canonical Axis design.
