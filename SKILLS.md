# Axis Skills Registry

## Purpose

This file is the curated list of external skills approved for use with Axis.

Use this file for:
- approved external marketplace skills
- optional external skills under consideration
- notes on why a skill is allowed or constrained

Do not use this file for:
- general OpenClaw framework rules
- implementation architecture
- task planning

Those belong in:
- [`docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md`](/Users/wjm/Code/Axis/docs/architecture/OPENCLAW_PROGRAMMERS_GUIDE.md)
- [`SPECIFICATION.md`](/Users/wjm/Code/Axis/SPECIFICATION.md)
- [`ROADMAP.md`](/Users/wjm/Code/Axis/ROADMAP.md)

## External Skills Approved

### Primary

- `1password`
  - Purpose: local 1Password CLI integration via `op`
  - Role in Axis: secret access and operator auth flows

- `brave-search`
  - Purpose: web search and content extraction
  - Role in Axis: search-driven research and source discovery

- `agent-browser`
  - Purpose: agent-first browser automation
  - Role in Axis: interactive browsing, authenticated sessions, JS-heavy pages, screenshots, and extraction

- `youtube-api-skill`
  - Purpose: YouTube Data API integration with managed OAuth
  - Role in Axis: YouTube Watch search, channel data, playlist data, comments, and API-native video discovery

- `blogwatcher`
  - Purpose: blog and RSS/Atom monitoring
  - Role in Axis: feed-based source monitoring for Signal Desk

### Secondary / Optional

- `playwright-mcp`
  - Purpose: Playwright-based browser automation via MCP
  - Role in Axis: fallback or alternative browser automation path

- `brave`
  - Purpose: Brave Browser control and debugging workflows
  - Role in Axis: browser-specific workflows when Brave behavior matters

- `peekaboo`
  - Purpose: macOS UI automation
  - Role in Axis: fallback for GUI workflows outside normal browser automation

## External Skills Under Consideration

- None yet.

## Selection Notes

- This registry should favor a small number of high-value external skills.
- Add a new external skill here only after reviewing fit, install model, and operational risk.
