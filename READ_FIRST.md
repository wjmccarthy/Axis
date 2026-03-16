# Read First

## Canonical Rule

[`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md) is canonical.

If any implementation doc, roadmap entry, or other project note conflicts with the spec, the spec wins.

## Required Change Order

When changing the system design or implementation guidance:

1. Update [`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md) first.
2. Validate internal consistency inside the spec before touching other docs.
3. Update subordinate implementation docs under [`docs/architecture/`](/Users/wjm/Code/Axis/docs/architecture/) to match the spec.
4. Validate those implementation docs against the full existing doc set for consistency.
5. Update [`ROADMAP.md`](/Users/wjm/Code/Axis/ROADMAP.md) last if sequencing, proof criteria, or stage boundaries changed.
6. Run a full consistency check across the full documentation set.
7. Run a full implementation simulation.
8. Find and fix any errors that would lead an implementer off course.
9. Repeat the consistency-check and simulation loop until that class of error is gone.

## Implementation Guardrail

Do not change subordinate docs first and then reinterpret the spec afterward.

Do not treat “close enough” wording as acceptable if it could cause implementation drift.
