# Axis Deferred Implementation Boundaries

## Purpose

This note defines implementation areas that are intentionally not fully specified yet.

It exists to prevent implementing agents from filling in channel-specific or premature detail as if it were already part of the design.

## Rule

If the canonical spec does not define a channel-specific execution detail yet, implementation should not invent a universal model for it prematurely.

## Deferred Areas

The following areas are intentionally deferred until later channel-editor implementation work:

- channel-specific assignment types
- publication schedules and cadence by channel
- exact assignment-start packaging rules by channel
- exact retrieval heuristics by channel
- exact trend-input thresholds for Topic creation
- exact editorial formatting and production conventions by channel

## What Is Already Defined

The following are already defined and should be implemented consistently:

- Topics are owned by Editors Desk
- Editorial Assignments are created only from approved Topics
- Channel editors own their Assignments
- Editors Desk routes assignment-relevant analytical subsets to channel editors
- Channel editors work through the relevant Analytical Desk for interpretation, clarification, and research support

## Implementation Guardrail

If an implementation choice would:

- create a universal channel-execution model before channel-editor design is complete
- hard-code one channel's assignment pattern as the general Axis rule
- treat deferred channel-specific behavior as if it were already canonically specified

that implementation is drifting from the intended Axis design.
