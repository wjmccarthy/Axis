# Axis Research Desk Operating Guide

## Purpose

This document defines the minimal implementation rule set for Research Desk.

It governs:
- how research work begins
- what Research Desk produces
- what Research Desk does not own

It does not add new workflow.

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Canonical Role

Research Desk is a support function.

Research Desk:

- responds to valid Research Requests
- produces Research Briefs
- does not produce final domain interpretation
- does not produce final published content

## How Research Begins

- All new research work enters through a Research Request.
- A Research Request may be opened only by a Domain Desk.
- Research Desk does not open Research Requests on its own.
- Strategist-directed research must still enter through a Domain Desk Research Request.

## What Research Desk Produces

Research Desk produces:

- Research Briefs
- reusable support materials associated with those Research Briefs

Research Desk does not produce:

- Desk Notes
- Desk Theses
- Desk Views
- Theme Theses
- Theme Views

## What a Research Brief Is

A Research Brief is:

- a bounded reusable research product
- a response to a Research Request
- support for later interpretation and execution

A Research Brief is not:

- final domain analysis
- the desk's living current state
- a replacement for Desk Notes, Desk Views, or Theme Views

## Major Requests

- A Research Request is major when it is cross-domain in scope or expected to incur excessive cost.
- Research Desk may identify major status where the spec says it may do so.
- Strategist approval is required for major Research Requests.

## Implementation Guardrail

If an implementation choice would make Research Desk behave like:

- a parallel interpretation desk
- a desk that initiates its own research agenda outside Research Requests
- a source of Desk Notes or current desk posture

that implementation is drifting from the canonical Axis design.
