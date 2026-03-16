# Guide Authoring Rules

## Purpose

This document defines how implementation-facing architecture guides for Axis should be written.

The goal is to prevent Axis-specific documentation from accidentally redefining OpenClaw framework behavior or steering implementation with incorrect system assumptions.

## Scope Rule

Every implementation guide must state:
- what Axis-specific behavior it governs
- what it does not govern
- where OpenClaw framework authority still applies

Axis guides are overlays on top of OpenClaw, not replacements for OpenClaw documentation.

## Authority Rule

Use this authority order:

1. official OpenClaw documentation for framework/runtime behavior
2. [`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md) for Axis system behavior
3. Axis architecture docs for implementation-facing product-layer decisions

If an Axis architecture guide appears to conflict with official OpenClaw documentation on framework behavior, the OpenClaw documentation wins.

## What Axis Guides May Define

Axis guides may define:
- Axis memory model
- Axis artifact model
- Axis linking model
- Axis retrieval policy
- Axis signal ingestion behavior
- Axis view/thesis update behavior
- Axis storage conventions for Axis-owned state and artifacts
- Axis-specific recovery, compaction, and archival policies

## What Axis Guides Must Not Redefine Without Citation

Axis guides must not redefine or improvise:
- Gateway behavior
- session/runtime memory semantics
- workspace bootstrapping conventions
- plugin lifecycle or packaging rules
- hook lifecycle behavior
- tool-loading rules
- protocol/control-plane behavior
- sandbox semantics

If a guide needs to mention one of these, it should:
- cite the relevant official OpenClaw documentation
- or explicitly say that implementation must follow official OpenClaw docs here

## Citation Rule

If a guide depends on OpenClaw framework behavior, it should cite the official documentation directly.

Do not restate framework behavior from memory when the exact rule matters.

## Design Rule

Prefer the smallest Axis-specific rule that solves the product problem.

Do not:
- create parallel framework concepts when OpenClaw already has one
- prescribe custom runtime plumbing without a verified need
- write speculative implementation detail as if it were framework fact

## Memory Rule

Axis-owned product memory may be defined by Axis architecture docs.

OpenClaw runtime/operator memory should remain governed by official OpenClaw documentation and local runtime conventions.

Do not blur those two layers in implementation guides.

## Review Rule

Before adding a new implementation guide, check:
- Is this documenting Axis product behavior or OpenClaw framework behavior?
- If framework behavior is involved, is there an official citation?
- Could this text cause an implementer to bypass a standard OpenClaw path?
- Is this better as a note in an existing guide rather than a new guide?

## Current OpenClaw References

- [OpenClaw Memory](https://docs.openclaw.ai/concepts/memory)
- [OpenClaw Plugins](https://docs.openclaw.ai/tools/plugin)
- [OpenClaw Skills](https://docs.openclaw.ai/skills)
- [OpenClaw Hooks](https://docs.openclaw.ai/automation/hooks)
- [OpenClaw Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
