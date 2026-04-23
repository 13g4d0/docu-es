# Solution documentation (as-built)

This site describes the **current** integration of:

- **IdentiaRAG** — RAG pipeline (Vespa, embeddings, FastAPI UI/API).
- **Open-WebUI** — forked self-hosted chat platform (SvelteKit frontend + FastAPI backend).
- **Inference gateway** — OpenAI-compatible routing (e.g. LiteLLM), optional local inference (e.g. LM Studio) and cloud providers (e.g. OpenRouter), with private mesh transport (e.g. Tailscale) where deployed.
- **Hermes Agent** — optional messaging/agent stack (separate compose lifecycle).

Documentation is written for a **private** GitHub repository. **Do not** embed API keys, tokens, or environment-specific hostnames in tracked pages.

## How to read

| Section | Audience | Content |
|---------|----------|---------|
| [Glossary](as-built/glossary.md) | Everyone | Terms and product names. |
| [C4 — System context](as-built/c4-context.md) | Architects / leads | External actors and trust boundaries. |
| [C4 — Containers](as-built/c4-containers.md) | DevOps / backend | Runnable units and ports (logical). |
| [IdentiaRAG](as-built/identiarag-software.md) | Backend | Pipeline, APIs, compose services. |
| [Open-WebUI](as-built/open-webui-software.md) | Full-stack | Monolith structure, extension points. |
| [Inference gateway](as-built/inference-gateway.md) | Platform | Hybrid local + cloud model routing. |
| [Hermes Agent](as-built/hermes-agent.md) | Integrations | Agent container, API surface (high level). |
| [Deployment patterns](as-built/deployment-patterns.md) | DevOps | Compose vs `docker run`, env patterns. |
| [Request sequences](as-built/sequence-requests.md) | All | End-to-end Mermaid sequences. |

## Milestones

Progress is tracked in [ROADMAP-MILESTONES.md](ROADMAP-MILESTONES.md). Git pushes to `origin` are batched **per milestone**; see [PRIVATE-REPO-AND-PUSH.md](PRIVATE-REPO-AND-PUSH.md).

## Build locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs serve
```

Static HTML: `.venv/bin/mkdocs build` → output in `site/` (gitignored).
