# Internal references (outside this repo)

This page lists **types** of artefacts that live in sibling repositories on the same documentation host. **Do not** paste production URLs, API keys, or customer hostnames into `docu`.

## Devops repository

| Relative path (inside devops checkout) | Purpose |
|----------------------------------------|---------|
| `docs/*.md` | Branded architecture and gateway runbooks (LiteLLM, Tailscale, Open-WebUI wiring). |
| `map/dashboard.html` | Technical-debt / progress dashboard consumed in the browser from your internal deployment. |
| `ops.sh` | Delegates to IdentiaRAG `dev-stack.sh` for stack lifecycle. |

Clone layout is organisation-specific; configure `DEVOPS_STACK_SCRIPT` or `DEVOPS_IDENTIARAG_ROOT` if paths differ.

## IdentiaRAG repository

| Path | Purpose |
|------|---------|
| `dev-stack.sh` | Open-WebUI + IdentiaRAG orchestration. |
| `compose.yml` | Vespa + UI + optional agent-embed. |
| `documentation/` | Upstream IdentiaRAG docs tree (distinct from this MkDocs site). |

## How this relates to M0.3

- **MkDocs (`docu`)** = curated as-built + roadmap for the combined solution.
- **Dashboard HTML** = operational / debt tracking; keep it in **devops** and link internally via your wiki or password-protected static host — not via hard-coded production URLs in git.

## Related

- [Operations runbook](../as-built/operations-runbook.md)
