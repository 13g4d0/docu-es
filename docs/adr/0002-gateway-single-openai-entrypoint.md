# ADR 0002 — Single OpenAI-compatible gateway for chat models

- **Status:** Accepted  
- **Date:** 2026-04-23  

## Context

Open-WebUI can talk to many providers directly, but operations need unified routing, fallback, and secrets that should not live in every browser session.

## Decision

Route primary chat model traffic through a **single OpenAI-compatible gateway** (LiteLLM in the reference deployment). Local inference (e.g. LM Studio) attaches as an upstream reachable via **private mesh** networking.

## Consequences

- **Positive:** Centralised policy (`lm-auto`-style aliases), fallback, and key rotation.
- **Negative:** Additional moving part; gateway DB must be backed up when `STORE_MODEL_IN_DB` is enabled.
