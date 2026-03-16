# Axis Publication Attribution Guide

## Purpose

This document defines the minimal implementation rule set for attribution and source-use in published output.

It governs:
- what counts as attributable published material
- when explicit source linkage is required
- what must be preserved for auditability and publication hygiene

It does not add new publication workflow.

Those remain governed by [/Users/wjm/Code/Axis/SPECIFICATION.md](/Users/wjm/Code/Axis/SPECIFICATION.md).

## Core Rule

If a publication uses attributable source material, the publication path must preserve explicit source linkage for attribution and provenance.

That attributable material should be treated as `Source Material` for implementation purposes.

This applies to:

- quotes
- visuals
- reproduced or directly referenced charts
- reproduced or directly referenced tables
- other externally attributable source material

## What Must Be Preserved

For attributable published material, implementation should preserve:

- the source identity
- the relevant Source Material record or equivalent retained representation
- enough provenance to show where the published material came from

Where applicable, this should also preserve:

- page, section, timestamp, or similar locator information
- the intermediate artifact used to derive the published material

Important:

- `Source Material` is the preferred attribution object when Axis retains attributable material in reusable form.
- `equivalent retained representation` is a bounded exception for editorially sourced material that has not yet been normalized into `Source Material`.
- that exception does not remove the requirement to preserve source identity, provenance, and enough locator detail for attribution and later verification.
- if editorially sourced attributable material becomes reusable inside Axis, implementation should normally normalize it into `Source Material`.

## Where Linking Matters Most

Attribution linking matters most for:

- Drafts
- Publication Items
- Source Material used in publication

Source Material may be:

- referenced by a Signal
- included in a Research Brief
- included in a Desk Note
- sourced directly by editorial outside the signal infrastructure

The purpose is:

- correct attribution
- auditability
- later source verification
- publication defensibility

## What Is Not Required

Axis does not require:

- dense internal attribution-style links for every analytical relationship
- exhaustive linkage for non-attributable internal synthesis
- publication-time linkage for every internal desk judgment that is not itself attributable source material

## Implementation Guardrail

If an implementation choice would allow published quotes, visuals, charts, tables, or other attributable material to appear without preserved linkage to the Source Material used in publication, that implementation is drifting from the intended Axis publication standard.
