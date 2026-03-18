# Agent State

This tree holds the writable per-agent Axis state for agents.

Each agent state root lives at `agents/<agent-id>/` and currently includes only writable directories:

- `memory/`
- `state/`
- `state/scratchpad/`

This tree must not contain behavior-defining bootstrap files such as `AGENTS.md`, `IDENTITY.md`, or `TOOLS.md`.

Those live in the trusted workspace-definition tree under `/Users/wjm/Code/Axis/agent-definitions/`.
