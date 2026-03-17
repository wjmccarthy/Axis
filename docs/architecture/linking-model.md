# Axis Linking Model

## Purpose

This document defines the minimal structured relationship model between Axis state and artifacts.

It governs:
- where structured links are required
- where structured links are useful but optional
- how links should be treated for attribution, provenance, workflow lineage, and revision lineage

It does not govern:
- OpenClaw runtime behavior
- Gateway behavior
- plugin or hook lifecycle behavior

Those remain governed by official OpenClaw documentation.

## Core Principle

Axis should keep structured linking sparse by default.

The point of linking is not to create a dense internal graph.

The point of linking is to preserve:
- source provenance
- publication attribution
- workflow lineage
- revision lineage where it materially matters

Important limitations:
- Axis does not require a per-signal mutation ledger for expert or desk state changes
- Axis does not require dense analytical support links across expert state, desk state, notes, briefs, topics, and drafts

## Required Linking Cases

Structured links are required when published or publication-bound output includes attributable source material such as:
- quotes
- visuals
- reproduced or directly referenced charts
- reproduced or directly referenced tables
- other externally attributable source material

In those cases, the relevant draft or `Publication Item` should preserve explicit `Source Material` linkage for attribution and provenance.

## Optional Linking Cases

Outside attribution, provenance, workflow lineage, and revision lineage, structured linking should remain selective.

Implementation should not create dense link debt for low-value internal relationships that do not materially improve:
- attribution
- auditability
- revision tracking
- publication grounding

## Stable Identity Rule

Every important Axis state or artifact record should have a stable ID.

This applies to:
- `Expert`
- `Expert Feed`
- `Expert Watchlist`
- `Expert Ideas`
- `Expert Beliefs`
- `Expert Calls`
- `Expert Surface`
- `Analytical Desk`
- `Desk Feed`
- `Desk Ideas`
- `Desk Beliefs`
- `Desk Debates`
- `Current State Surface`
- `Editorial Agenda`
- `Editors Feed`
- `Editors Scratchpad`
- `Strategist Feed History`
- `Strategist Scratchpad`
- `Research Request`
- `Signal Request`
- `Signal`
- `Source Material`
- report artifacts
- report parses
- ingestion-stage artifacts
- `Chart Follow-Up`
- transcripts
- `Research Brief`
- `Desk Note`
- `Topic`
- `Editorial Assignment`
- `Draft`
- `Publication Item`

## Link Categories

### 1. Provenance Links

Meaning:
- the source was derived from, extracted from, or supported by the target artifact

Examples:
- `Signal -> Report Parse`
- `Report Parse -> Report Artifact`
- `Signal -> Source Material`
- `Source Material -> Report Artifact`
- `Chart Follow-Up -> Report Parse`

### 2. Attribution Links

Meaning:
- the publication-bound object uses attributable source material that must remain traceable

Examples:
- `Draft -> Source Material`
- `Publication Item -> Source Material`

### 3. Workflow Links

Meaning:
- the source and target are connected through workflow state

Examples:
- `Topic -> Editorial Assignment`
- `Editorial Assignment -> Draft`
- `Editorial Assignment -> Publication Item`

### 4. Revision Links

Meaning:
- the source supersedes, revises, or snapshots the target

Examples:
- later state snapshot -> prior state snapshot
- `Draft v3 -> Draft v2`
- `Publication Item v2 -> Publication Item v1`

### 5. Corroboration Links

Meaning:
- two or more records independently support the same interpreted development

Examples:
- `Signal -> Signal`
- `Report Artifact -> Transcript`

## High-Value Relationship Defaults

### Signal may link to

- source artifacts
- `Source Material`
- report parses
- `Chart Follow-Up`
- transcripts
- corroborating `Signals`

### Source Material may link to

- report artifacts
- report parses
- transcripts
- `Signal` where relevant
- `Research Brief` where included
- `Desk Note` where included
- `Draft`
- `Publication Item`

### Research Brief may link to

- `Signals`
- `Source Material`
- report artifacts
- report parses
- transcripts

### Chart Follow-Up may link to

- report artifact
- report parse
- `Signal`

### Desk Note may link to

- relevant `Research Briefs`
- supporting `Signals`
- `Source Material` where needed

### Editorial workflow objects may link to

- each other through workflow lineage
- `Source Material` where attribution or provenance materially matters

## Minimal Link Metadata

Every structured link should support at least:
- source ID
- source type
- target ID
- target type
- link type
- created time

## What Is Not Required

Implementation should not assume that Axis requires:
- dense structured analytical support links among expert and desk state objects
- explicit support links from every reviewed signal into every resulting expert or desk state change
- structured analytical links from `Topic`, `Editorial Assignment`, `Draft`, or `Publication Item` into all desk state by default
- a full cognitive lineage graph for every internal adjustment

## Compaction Rule

Compaction and rollups should not destroy important provenance, attribution, or lineage links.

If a rollup becomes the preferred retrieval surface, underlying artifact links should still remain recoverable.
