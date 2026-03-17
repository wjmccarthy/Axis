# Axis Analytical Desk Operating Guide

## Purpose

This document defines how an Analytical Desk should operate inside Axis.

It governs:
- what an Analytical Desk is for
- what an Analytical Desk receives
- what state an Analytical Desk maintains
- what an Analytical Desk shares with the rest of the system
- how an Analytical Desk relates to Experts, Strategist, and support desks

It does not govern:
- workflow authority already defined in [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md)
- OpenClaw runtime behavior
- storage implementation details beyond the architectural model

## Canonical Role

An Analytical Desk is the top analytical synthesis unit in Axis.

An Analytical Desk:
- is composed from assigned Experts
- synthesizes expert input into desk-level understanding
- answers direct questions from Strategist, Producer Desks, and other desks
- publishes current state and Desk Notes for downstream consumers
- may open Research Requests when assigned experts cannot answer sufficiently
- may open Signal Requests when bounded retained-signal retrieval is needed

An Analytical Desk is not:
- a raw-signal inbox
- a monolithic single-agent interpreter
- a note-only publication layer
- a replacement for Expert-level interpretation

## Relationship To Experts

Signals route to Experts, not directly to Analytical Desks.

Experts are system-level permanent agents with standing remits.

Analytical Desk composition rules:
- desk assignment is desk-controlled
- membership is fluid
- assigned experts are expected to contribute
- experts may participate in multiple desks

Analytical Desks implement the mixture-of-experts pattern by:
- receiving Calls and Contributions from assigned Experts
- deliberating over that input
- maintaining desk-level Ideas and Beliefs

## What An Analytical Desk Receives

An Analytical Desk receives:
- Expert Calls
- Expert Contributions
- relevant Research Briefs returned against its Research Requests
- bounded retained-signal results returned against its Signal Requests
- relevant Desk Notes from other Analytical Desks as informational context
- Viewpoint Signals as strategist guidance
- direct questions from Strategist, Producer Desks, and other desks

Important:
- desks do not receive first-order signal routing as their primary input path
- incoming notes from other desks are usually informational context rather than automatic desk-state change
- debate and desk-state movement should be driven primarily by expert input and desk judgment

## Desk State

Each Analytical Desk maintains:
- `Desk Feed`
- `Desk Ideas`
- `Desk Beliefs`
- `Desk Debates`
- one persisted `Current State Surface`

Role of each layer:
- `Desk Feed`
  - collects Calls, Contributions, and other desk-relevant incoming context
- `Desk Ideas`
  - the live short-cycle frontier of desk thinking
- `Desk Beliefs`
  - the adopted longer-cycle desk position
- `Desk Debates`
  - internal deliberative memory around Ideas and Beliefs
- `Current State Surface`
  - the outward-facing persisted current-state publication object for the desk

`Current State Surface` contains:
- core position
- current beliefs
- selected ideas

`Desk Debates` are internal only.

## How A Desk Works

An Analytical Desk works from:
- its current `Desk Beliefs`
- its current `Desk Ideas`
- its current `Desk Feed`
- its current `Desk Debates`
- current relevant `Expert Surface` state from assigned experts
- current `Research Briefs` and bounded signal-search results where relevant
- current strategist guidance

Calls create desk-directed pressure on current desk state.

The desk remains in control of what happens next:
- merge debate
- defer it
- suppress it
- close it
- force a vote

Ordinary Contributions participate inside desk deliberation but do not by themselves define the desk’s adopted state.

## Desk Governance

The desk governs its own debates.

Desk governance rules:
- every assigned Expert gets a vote in desk decisions
- Strategist participates in every analytical desk
- Strategist has one normal vote plus veto over belief adoption
- Strategist may stop debate but may not unilaterally force belief adoption
- an `Idea` becomes a `Belief` only with unanimity of desk votes and absent strategist veto
- a `Belief` returns to `Idea` status when challenge reaches at least a `2/3` majority of desk votes

Calls do not force one fixed handling path.
The desk retains control over how deliberation is managed.

## Questions And Support

Analytical Desks accept direct questions from:
- Strategist
- Producer Desks
- other desks

The desk may respond by:
- answering directly
- updating its `Current State Surface`
- publishing a `Desk Note`
- opening a `Research Request`
- opening a `Signal Request`
- doing nothing yet

Questions do not create a separate architectural object beyond the valid downstream workflow the desk chooses.

## Desk Notes

`Desk Notes` are point-in-time published communications to subscribers.

They are:
- bounded
- outward-facing
- flexible in form
- cumulative rather than replacing prior notes automatically

They are not:
- the desk’s full current state
- a required output of every reviewed development
- the only way editorial or Strategist can consume desk understanding

In fast-moving situations, a newer `Desk Note` may be the current tactical read until the `Current State Surface` catches up.

## What An Analytical Desk Shares

The outward analytical surfaces shared by an Analytical Desk are:
- `Current State Surface`
- `Desk Notes`
- direct answers to questions
- relevant `Research Briefs` where needed

Default consumers:
- Strategist
- Producer Desks
- selectively subscribed Analytical Desks

Other desks may inspect current state before deciding whether to subscribe.

## What Is Not Required

Axis does not require:
- direct signal routing into desks as the normal analytical path
- a separate layered analytical object stack above desk ideas and beliefs
- a separate strategic-framing runtime object
- one note per reviewed development
- dense per-signal mutation lineage for desk-state changes
- exposing desk debates as shared current state

## Implementation Guardrail

If an implementation choice would make an Analytical Desk behave like:
- a direct signal inbox
- a single-agent interpreter instead of a synthesis layer
- a note-only layer with no standing current state
- a rebuild of an obsolete layered analytical model

that implementation is drifting from the canonical Axis design.
