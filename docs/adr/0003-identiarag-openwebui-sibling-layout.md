# ADR 0003 — Sibling checkout layout for `dev-stack.sh`

- **Status:** Accepted  
- **Date:** 2026-04-23  

## Context

`dev-stack.sh` resolves `OPEN_WEBUI_ROOT` relative to the IdentiaRAG checkout (`../open-webui` by default). Operators may override with environment variables.

## Decision

Standardise on a **sibling directory layout** (`IdentiaRAG` next to `open-webui`) for development hosts, documented rather than hard-coded absolute paths in automation.

## Consequences

- **Positive:** Predictable relative paths; easier onboarding.
- **Negative:** Clones in non-standard locations must export `OPEN_WEBUI_ROOT` explicitly.
