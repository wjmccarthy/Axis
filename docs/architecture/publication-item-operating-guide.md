# Axis Draft and Publication Item Guide

## Purpose

This document defines the minimal implementation rule set for Drafts and Publication Items.

It governs:
- what a Draft is
- what a Publication Item is
- who owns them
- how attribution readiness applies before publication

It does not add new publication workflow.

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Canonical Role

Drafts and Publication Items are channel-specific editorial output objects.

- A Draft is working editorial output under active execution.
- A Publication Item is the publication object that Strategist reviews for approval and that is ultimately distributed externally for that assignment.
- A channel editor may create the Publication Item at any point after the Editorial Assignment begins.
- The exact timing and representation of the Publication Item may vary by channel implementation.

## Ownership

- Channel editors own Drafts for their Assignments.
- Channel editors own the resulting Publication Items for their Assignments until publication approval and distribution steps defined in the spec are complete.

These objects are not owned by:

- Analytical Desks
- Research Desk
- Signal Desk

Those desks may support execution, but they do not own the output objects themselves.

## Inputs

Drafts and Publication Items may be built from the routed assignment-relevant analytical subset, including:

- current-state surfaces
- desk notes
- relevant Research Brief

They may also incorporate attributable source material so long as attribution and provenance requirements are preserved.

## Attribution Readiness

If a Draft or Publication Item includes attributable source material, the publication path must preserve explicit source linkage as defined in [/Users/wjm/Code/Axis/docs/architecture/publication-attribution.md](/Users/wjm/Code/Axis/docs/architecture/publication-attribution.md).

This matters especially for:

- quotes
- visuals
- reproduced or directly referenced charts
- reproduced or directly referenced tables
- other externally attributable source material

## What Drafts Are Not

Drafts are not:

- the desk's analytical state
- a Research Brief
- a Desk Note
- a substitute for the underlying analytical inputs

## What Publication Items Are Not

Publication Items are not:

- raw research artifacts
- raw analytical state
- exempt from attribution requirements

## Implementation Guardrail

If an implementation choice would make Drafts or Publication Items behave like:

- ungrounded channel text disconnected from routed analytical input
- desk-owned analytical artifacts
- publishable output that can include attributable source material without preserved source linkage

that implementation is drifting from the canonical Axis design.
