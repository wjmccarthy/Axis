# Axis Implementation Reading Order

## Purpose

This note defines the intended reading order for implementing agents.

Its purpose is to reduce drift by making the authority hierarchy and doc roles explicit.

## Authority Order

Read and apply documents in this order:

1. [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md)
2. relevant notes in [/Users/wjm/Code/Axis/docs/architecture/](/Users/wjm/Code/Axis/docs/architecture)
3. relevant notes in [/Users/wjm/Code/Axis/docs/implementation/](/Users/wjm/Code/Axis/docs/implementation/)
4. [/Users/wjm/Code/Axis/ROADMAP.md](/Users/wjm/Code/Axis/ROADMAP.md) for sequencing only
5. [/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md](/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md) for OpenClaw-specific framework constraints

## Canonical Rule

`SPECIFICATION.md` is canonical.

The architecture docs are subordinate implementation guidance.

The implementation docs contain current first-pass implementation-shaping notes derived from the spec and architecture docs.

If an architecture doc appears to conflict with the spec, the spec wins.

If an implementation doc appears to conflict with the spec, the spec wins.

## Reading by Area

### System-wide implementation posture

Read:

- [/Users/wjm/Code/Axis/docs/architecture/guide-authoring-rules.md](/Users/wjm/Code/Axis/docs/architecture/guide-authoring-rules.md)
- [/Users/wjm/Code/Axis/docs/architecture/deferred-implementation-boundaries.md](/Users/wjm/Code/Axis/docs/architecture/deferred-implementation-boundaries.md)
- [/Users/wjm/Code/Axis/docs/architecture/term-boundaries.md](/Users/wjm/Code/Axis/docs/architecture/term-boundaries.md)

### Memory, storage, retrieval, and linking

Read:

- [/Users/wjm/Code/Axis/docs/architecture/memory-model.md](/Users/wjm/Code/Axis/docs/architecture/memory-model.md)
- [/Users/wjm/Code/Axis/docs/architecture/artifact-model.md](/Users/wjm/Code/Axis/docs/architecture/artifact-model.md)
- [/Users/wjm/Code/Axis/docs/architecture/retrieval-policy.md](/Users/wjm/Code/Axis/docs/architecture/retrieval-policy.md)
- [/Users/wjm/Code/Axis/docs/architecture/linking-model.md](/Users/wjm/Code/Axis/docs/architecture/linking-model.md)

### Signal-side behavior

Read:

- [/Users/wjm/Code/Axis/docs/architecture/signal-desk-operating-guide.md](/Users/wjm/Code/Axis/docs/architecture/signal-desk-operating-guide.md)
- [/Users/wjm/Code/Axis/docs/architecture/signal-ingestion.md](/Users/wjm/Code/Axis/docs/architecture/signal-ingestion.md)
- [/Users/wjm/Code/Axis/docs/architecture/report-watch.md](/Users/wjm/Code/Axis/docs/architecture/report-watch.md)

### Expert and desk interpretation

Read:

- [/Users/wjm/Code/Axis/docs/architecture/expert-reward-function.md](/Users/wjm/Code/Axis/docs/architecture/expert-reward-function.md)
- [/Users/wjm/Code/Axis/docs/architecture/analytical-desk-operating-guide.md](/Users/wjm/Code/Axis/docs/architecture/analytical-desk-operating-guide.md)
- [/Users/wjm/Code/Axis/docs/implementation/desk-and-expert-roster.md](/Users/wjm/Code/Axis/docs/implementation/desk-and-expert-roster.md)

### Historical context

Read only if needed:

- [/Users/wjm/Code/Axis/docs/implementation/THEMES_ARCHIVE.md](/Users/wjm/Code/Axis/docs/implementation/THEMES_ARCHIVE.md)

### Research behavior

Read:

- [/Users/wjm/Code/Axis/docs/architecture/research-desk-operating-guide.md](/Users/wjm/Code/Axis/docs/architecture/research-desk-operating-guide.md)

### Editorial behavior

Read:

- [/Users/wjm/Code/Axis/docs/architecture/editorial-consumption.md](/Users/wjm/Code/Axis/docs/architecture/editorial-consumption.md)
- [/Users/wjm/Code/Axis/docs/architecture/publication-attribution.md](/Users/wjm/Code/Axis/docs/architecture/publication-attribution.md)
- [/Users/wjm/Code/Axis/docs/architecture/publication-item-operating-guide.md](/Users/wjm/Code/Axis/docs/architecture/publication-item-operating-guide.md)

## Guardrail

Do not treat the architecture note set as a parallel spec.

Its purpose is to make the canonical design easier to implement without changing it.
