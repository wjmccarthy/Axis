# OpenClaw Programmer's Guide for Axis

## Purpose

This file is a condensed project-local guide for implementing Axis in ways that are native to OpenClaw. It is not a substitute for the official docs, but it should prevent future sessions from drifting into non-standard patterns.

## Core Rules

- OpenClaw Gateway is the single control plane and source of truth for sessions, routing, and channel connections.
- Do not build a parallel control plane, bridge, or node transport for Axis if the OpenClaw Gateway protocol already covers the need.
- Use OpenClaw workspace, memory, and sandbox conventions by default.
- Treat OpenClaw protocol/schema definitions as authoritative where they exist.
- If Axis needs behavior that does not fit standard OpenClaw patterns, stop and resolve that explicitly before implementing.

## Gateway and Protocol

- Run with one long-lived Gateway per host unless there is a deliberate multi-gateway isolation reason.
- Clients and nodes should use the Gateway WebSocket protocol, not the legacy TCP bridge.
- The first frame on a Gateway connection must be `connect`.
- OpenClaw uses typed protocol schemas as the source of truth; do not hand-roll divergent protocol contracts if an official schema already exists.

## Workspace and Memory

- The agent workspace is the default working directory and the home for project files and agent memory.
- `~/.openclaw/` is for OpenClaw config, credentials, and sessions, not project logic.
- OpenClaw memory is Markdown on disk, not implicit model state.
- Default memory layers:
  - `memory/YYYY-MM-DD.md` for daily logs
  - `MEMORY.md` for curated long-term memory
- Axis project docs should stay in the repo; OpenClaw operational memory should stay in OpenClaw memory files.

## Bootstrap Files

According to the official OpenClaw [Agent Runtime](https://docs.openclaw.ai/concepts/agent) and [Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace) docs, the workspace bootstrap file set includes:

- `AGENTS.md`
- `SOUL.md`
- `TOOLS.md`
- `BOOTSTRAP.md` on first-run flows
- `IDENTITY.md`
- `USER.md`

Axis should not fight these conventions. Project-specific guidance belongs in repo docs unless it clearly belongs in workspace bootstrap or memory.

## Sandboxing and Tooling

- Use OpenClaw sandbox configuration if isolation is needed.
- Do not simulate sandboxing with custom wrappers if standard OpenClaw sandbox settings are sufficient.
- Remember that sandbox workspace access can be `none`, `ro`, or `rw`; design file access assumptions accordingly.
- Additional host directory access should use documented bind-mount configuration, not hidden path assumptions.

## Practical Axis Guidance

- Build Axis as an OpenClaw-native system, not as a generic app that merely happens to run inside OpenClaw.
- Keep Axis implementation guides focused on current product behavior. Do not introduce framework-level assumptions that are not grounded in official OpenClaw docs.
- For any transport, session, memory, or sandbox decision, prefer the documented OpenClaw pattern first.
- When in doubt, consult the official docs before introducing a new subsystem.

## ClawHub Skill Policy for Axis

- Treat ClawHub skills as untrusted by default and review them like executable third-party code.
- Do not depend on marketplace skills for essential workflow logic unless their role has been explicitly approved in project docs.
- Reject skills that require pasted shell commands, remote bootstrap scripts, force installs, or unclear prerequisites.

## Official References

- [OpenClaw docs home](https://docs.openclaw.ai/)
- [Gateway Architecture](https://docs.openclaw.ai/architecture)
- [Gateway Protocol](https://docs.openclaw.ai/gateway/protocol)
- [Agent Runtime](https://docs.openclaw.ai/concepts/agent)
- [Agent Workspace](https://docs.openclaw.ai/agent-workspace)
- [Memory](https://docs.openclaw.ai/concepts/memory)
- [Sandboxing](https://docs.openclaw.ai/sandboxing)
- [TypeBox / protocol source of truth](https://docs.openclaw.ai/concepts/typebox)
