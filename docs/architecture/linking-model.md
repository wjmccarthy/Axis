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
- Axis does not require explicit per-signal mutation records for Desk View or Theme View changes
- Axis does not require dense analytical support links across theses, views, notes, briefs, topics, and drafts
- desks may evolve Beliefs from reviewed signals without a cognitive event ledger

Practical distinction:
- signal-side linking should be relatively strong because it answers where a Signal came from and what source material supports it
- editorial and workflow linking should remain minimal and should exist mainly for attribution and lineage

## Required Linking Cases

Structured links are required when published output includes attributable source material such as:

- quotes
- visuals
- reproduced or directly referenced charts
- reproduced or directly referenced tables
- other externally attributable source material

In those cases, the relevant Draft or Publication Item should preserve explicit Source Material linkage for attribution and provenance.

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
- Beliefs
- Signal Feed
- Desk Scratchpad
- Theme List
- Editors Feed
- Editors Scratchpad
- Strategist Feed History
- Strategist Scratchpad
- Research Request
- Signal Request
- Signal
- Source Material
- Desk-Local Routed-Signal Record
- Report Artifact
- Report Parse
- Chart Follow-Up
- Transcript
- Research Brief
- Desk Note
- Topic
- Editorial Assignment
- Draft
- Publication Item

Desk Theses, Desk Views, Theme Theses, and Theme Views may also carry stable internal IDs where useful inside Beliefs, but they are not required to behave like separate top-level persisted current-state records.

## Link Categories

### 1. Provenance Links

Meaning:
- the source was derived from, extracted from, or supported by the target source artifact

Examples:
- Signal -> Report Parse
- Report Parse -> Report Artifact
- Signal -> Source Material
- Source Material -> Report Artifact
- Source Material -> Transcript
- Chart Follow-Up -> Report Parse

### 2. Attribution Links

Meaning:
- the published or publication-bound object uses attributable source material that must remain traceable

Examples:
- Draft -> Source Material
- Publication Item -> Source Material

### 3. Workflow Links

Meaning:
- the source and target are connected through workflow state

Examples:
- Topic -> Editorial Assignment
- Editorial Assignment -> Draft
- Editorial Assignment -> Publication Item

### 4. Revision Links

Meaning:
- the source supersedes, revises, or snapshots the target

Examples:
- archived Beliefs -> prior archived Beliefs
- Draft v3 -> Draft v2
- Publication Item v2 -> Publication Item v1

### 5. Corroboration Links

Meaning:
- two or more records independently support the same interpreted development

Examples:
- Signal -> Signal
- Report Artifact -> Transcript

## High-Value Relationship Defaults

### Signal may link to

- raw source artifacts
- Source Material
- Report Parse
- Chart Follow-Up
- Transcript
- other corroborating Signals

### Source Material may link to

- Report Artifact
- Report Parse
- Transcript
- Signal where relevant
- Research Brief where included
- Desk Note where included
- Draft
- Publication Item

### Desk-Local Routed-Signal Record may link to

- Signal
- destination desk

### Research Brief may link to

- Signals
- Source Material
- Report Artifacts
- Report Parses
- Transcripts

### Chart Follow-Up may link to

- Report Artifact
- Report Parse
- Signal

### Topic may link to

- Editorial Assignments

### Editorial Assignment may link to

- Topic
- Drafts
- Publication Items

### Draft may link to

- Editorial Assignment
- Topic
- Source Material
- prior Drafts
- Publication Item

### Publication Item may link to

- Draft
- Editorial Assignment
- Topic
- Source Material
- prior Publication Items where version lineage matters

## Directionality Rule

Links should be directional.

The system may expose reverse lookups, but implementation should preserve the semantic direction of the original relationship.

Examples:
- `Topic has_assignment EditorialAssignment` is not the same as `EditorialAssignment has_topic Topic`
- `PublicationItem derived_from Draft` is not the same as `Draft derived_from PublicationItem`

## Minimal Link Metadata

Every structured link should support at least:
- source ID
- source type
- target ID
- target type
- link type
- created time
- optional explanation or note

Later implementation may add:
- confidence
- provenance class
- manual vs automated creation source

## Revision Lineage

Archived Beliefs, Drafts, and Publication Items should preserve explicit predecessor/successor relationships where version lineage matters.

This is important for:
- reconstructing change over time
- tracing when a conviction shifted
- understanding editorial evolution

## What Is Not Required

Implementation should not assume that Axis requires:
- a per-signal view-update ledger
- explicit support links from reviewed Signals into Desk Views or Theme Views
- structured analytical links from Topics, Assignments, Drafts, or Publication Items into theses, views, notes, or briefs by default
- a full cognitive lineage graph for every internal desk-state adjustment
- dense support-link capture where the maintenance cost exceeds the attribution, provenance, or lineage value

## Compaction Rule

Compaction and rollups should not destroy important provenance, attribution, or lineage links.

If a rollup becomes the preferred retrieval surface, the underlying artifact links should still remain recoverable.

## Open Questions

These still need later implementation detail:

1. Exact enumerated link types
2. Whether some links should carry weights or confidence
3. Whether some link pairs should be forbidden
4. Whether corroboration should be a first-class record or only a link type
