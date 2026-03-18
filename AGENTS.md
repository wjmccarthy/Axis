# Repository expectations

This repo is part of a long-lived system, not a demo. Optimize for correctness, operational durability, and continuity.

## Environment

- Primary host: Apple Silicon macOS
- Default shell: zsh
- Daily workflow may run under a non-admin account
- Source control: GitHub
- Secrets: 1Password plus gitignored local env files
- Runtime host: openclaw
- prefer openclaw patterns, built-in functionality, skills, and tools to build our own


## Canonical files

Use these if they exist and are relevant to the task:

- `ROADMAP.md`
- `BUILD_LOG.md`
- relevant runbooks under `docs/` or `docs/runbooks/`
- relevant architecture docs under `docs/architecture/`
- relevant implementation docs under `docs/implementation/`

Rules:
- `ROADMAP.md` is for objectives, sequencing, dependencies, and proof criteria.
- `BUILD_LOG.md` is for current execution state, blockers, decisions, and next step.
- Do not create parallel planning docs if these already exist.
- Do not create `ROADMAP.md` or `BUILD_LOG.md` in third-party or throwaway repos unless explicitly asked.

## Before working

- Identify the authoritative acceptance surface for the task.
- Find the repo’s actual run, test, lint, and build commands before improvising.
- Keep changes aligned with the roadmap when one exists.
- If the task is analysis only, do not edit files or runtime state unless explicitly asked.

## Command discovery order

Use commands from the first applicable source:

1. `README.md`
2. repo runbooks in `docs/`
3. `justfile` or `Makefile`
4. `package.json`
5. `pyproject.toml`
6. scripts already present in the repo

If commands are missing or contradictory, say so plainly instead of guessing.

## Verification order

Unless the user says otherwise, rank evidence like this:

1. user-defined acceptance surface
2. live runtime behavior
3. health, API, or control-plane surfaces
4. integration-level end-to-end behavior
5. repo-declared tests
6. build, lint, or typecheck
7. static config or file contents

Rules:
- Treat config as intent, not proof.
- Do not claim success because a file changed if runtime behavior still fails.
- If UI, runtime, or API disagree with config, trust the live surface first.

## Change discipline

- Prefer minimal diffs.
- Do not add new services, persistence layers, wrappers, or background processes unless required.
- Do not commit secrets, tokens, private keys, or filled local env files.
- Keep implementation, runtime reality, and planning artifacts aligned.
- If a supported operational path exists, prefer it over manual file surgery unless verified evidence says otherwise.

## Definition of done

Work is done only when:
- the requested change is implemented,
- the authoritative acceptance surface has been checked,
- relevant checks for the touched area were run or explicitly judged not applicable,
- `BUILD_LOG.md` was updated if the work was substantive,
- `ROADMAP.md` was updated only if strategy or sequencing materially changed,
- any remaining uncertainty is stated explicitly.

## Build log update style

Keep `BUILD_LOG.md` compact:
- what was attempted
- what changed
- what was verified
- what failed or remains unresolved
- exact next rational step