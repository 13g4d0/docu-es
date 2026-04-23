# Documentation roadmap — milestone index

Suggested order. Treat each milestone as a shippable slice (PR-sized where possible).

## Phase 0 — Bootstrap

| ID | Milestone |
|----|-----------|
| M0.1 | Repository layout, naming, language policy, doc generator choice (MkDocs / Docusaurus / other). |
| M0.2 | Glossary + repo map (`IdentiaRAG`, `open-webui`, `devops`, Hermes). |
| M0.3 | “How to read this site” + links to `dashboard.html` and architecture references. |

## Phase 1 — As-built (code + runtime truth)

| ID | Milestone |
|----|-----------|
| M1.1 | Product / solution context (short; grounded in what exists). |
| M1.2 | C4 Level 1 — **System context**: actors, external systems, trust boundaries. |
| M1.3 | C4 Level 2 — **Containers**: services (LiteLLM, Open-WebUI, Hermes, RAG, DBs, queues if any). |
| M1.4 | C4 Level 3 — **Components** (per critical service or repo): main modules and dependencies. |
| M1.5 | **Deployment**: Docker/Compose, Hostinger, volumes, env var *reference* (no secrets). |
| M1.6 | **Network & security**: Tailscale, ports, TLS paths, caller/callee matrix. |
| M1.7 | **Data**: logical schemas, retention, backups (only what is evidenced in code/config). |
| M1.8 | **APIs**: OpenAI-compatible routes, Hermes endpoints, health checks — tables + sequence diagrams. |
| M1.9 | **Operations**: runbooks (start/stop, upgrade, common incidents). |
| M1.10 | **Observability**: logs, metrics, traces — or explicit “not implemented” gaps. |
| M1.11 | **ADRs**: key decisions inferred from the repos (lightweight). |

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
