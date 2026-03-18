# Agent Workspaces And Definitions

This tree holds the canonical reviewed per-agent OpenClaw workspace files for Axis.

Each agent has a directory at `agents/<agent-id>/` containing:

- `AGENTS.md`
- `IDENTITY.md`
- `TOOLS.md`

These files define the canonical prompt, identity, and tool posture for the agent.

This tree is the trusted behavior-defining layer.

`agent-state/` is separate and exists only for writable runtime and Axis-owned state.
