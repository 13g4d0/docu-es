# Documentation roadmap — milestone index

Suggested order. Treat each milestone as a shippable slice (PR-sized where possible).

**Status (rolling):** M0.* in progress in-repo; dashboard / TdR gap phases start after as-built baseline is stable.

## Phase 0 — Bootstrap

| ID | Milestone | Status |
|----|-----------|--------|
| M0.1 | Repository layout, naming, language policy, doc generator choice (MkDocs / Docusaurus / other). | **Done** — MkDocs + Material + mermaid2 in `docu`. |
| M0.2 | Glossary + repo map (`IdentiaRAG`, `open-webui`, `devops`, Hermes). | **Done** — see `docs/as-built/glossary.md`, `repo-map.md`. |
| M0.3 | “How to read this site” + links to `dashboard.html` and architecture references. | **Partial** — home `docs/index.md`; link dashboard only from secure internal runbooks (not in public examples). |

## Phase 1 — As-built (code + runtime truth)

| ID | Milestone | Status |
|----|-----------|--------|
| M1.1 | Product / solution context (short; grounded in what exists). | **Partial** — `docs/index.md`, inference gateway page. |
| M1.2 | C4 Level 1 — **System context**: actors, external systems, trust boundaries. | **Done** — `as-built/c4-context.md`. |
| M1.3 | C4 Level 2 — **Containers**: services (LiteLLM, Open-WebUI, Hermes, RAG, DBs, queues if any). | **Done** — `as-built/c4-containers.md`. |
| M1.4 | C4 Level 3 — **Components** (per critical service or repo): main modules and dependencies. | **Partial** — `identiarag-software.md`, `open-webui-software.md`. |
| M1.5 | **Deployment**: Docker/Compose, Hostinger, volumes, env var *reference* (no secrets). | **Partial** — `deployment-patterns.md`. |
| M1.6 | **Network & security**: Tailscale, ports, TLS paths, caller/callee matrix. | **Partial** — inside gateway + context; matrix TODO. |
| M1.7 | **Data**: logical schemas, retention, backups (only what is evidenced in code/config). | **Todo** |
| M1.8 | **APIs**: OpenAI-compatible routes, Hermes endpoints, health checks — tables + sequence diagrams. | **Partial** — `sequence-requests.md`. |
| M1.9 | **Operations**: runbooks (start/stop, upgrade, common incidents). | **Todo** |
| M1.10 | **Observability**: logs, metrics, traces — or explicit “not implemented” gaps. | **Todo** |
| M1.11 | **ADRs**: key decisions inferred from the repos (lightweight). | **Todo** |

## Phase 2 — Users & developers

| ID | Milestone |
|----|-----------|
| M2.1 | End-user guides (Open-WebUI usage, models, policies as deployed). |
| M2.2 | Developer onboarding: clone, build, test, PR conventions. |
| M2.3 | Fork vs upstream boundaries (`open-webui`, etc.). |

## Phase 3 — TdR & gap (after solid as-built)

| ID | Milestone |
|----|-----------|
| M3.1 | TdR executive summary (requirements & scope cited from `incoming/tdr.pdf`). |
| M3.2 | **TdR ↔ implementation** matrix (full / partial / missing / N/A). |
| M3.3 | **Technical gap report** (risk, effort, dependencies). |
| M3.4 | **Documentation roadmap** derived from gaps (what to write next). |
| M3.5 | Alignment with `dashboard.html` indicators. |

## Phase 4 — Published docs site (`docs.domain.com`)

| ID | Milestone |
|----|-----------|
| M4.1 | Static site generator + theme + navigation. |
| M4.2 | CI: build + link check; optional deploy to `docs` subdomain. |
| M4.3 | Versioning policy (per release vs date-stamped). |

## Phase 5 — Debt & maintenance

| ID | Milestone |
|----|-----------|
| M5.1 | “Doc debt” checklist for meaningful code changes. |
| M5.2 | Quarterly review: diagrams vs reality, broken links, secret rotation notes. |
