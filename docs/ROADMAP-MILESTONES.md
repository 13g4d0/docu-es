# Documentation roadmap — milestone index

Suggested order. Treat each milestone as a shippable slice (PR-sized where possible).

**Status (rolling):** Phases **0–2** complete in `docu`; next focus is **Phase 3** (TdR gap vs `incoming/tdr.pdf`) when you are ready to extract text from the PDF on a secure workstation.

## Phase 0 — Bootstrap

| ID | Milestone | Status |
|----|-----------|--------|
| M0.1 | Repository layout, naming, language policy, doc generator choice (MkDocs / Docusaurus / other). | **Done** — MkDocs + Material + mermaid2 in `docu`. |
| M0.2 | Glossary + repo map (`IdentiaRAG`, `open-webui`, `devops`, Hermes). | **Done** — see `docs/as-built/glossary.md`, `repo-map.md`. |
| M0.3 | “How to read this site” + links to `dashboard.html` and architecture references. | **Done** — `meta/internal-references.md` + home table (paths relative to devops checkout, no production URLs). |

## Phase 1 — As-built (code + runtime truth)

| ID | Milestone | Status |
|----|-----------|--------|
| M1.1 | Product / solution context (short; grounded in what exists). | **Done** — `docs/index.md` + gateway/context pages. |
| M1.2 | C4 Level 1 — **System context**: actors, external systems, trust boundaries. | **Done** — `as-built/c4-context.md`. |
| M1.3 | C4 Level 2 — **Containers**: services (LiteLLM, Open-WebUI, Hermes, RAG, DBs, queues if any). | **Done** — `as-built/c4-containers.md`. |
| M1.4 | C4 Level 3 — **Components** (per critical service or repo): main modules and dependencies. | **Done** — `identiarag-software.md`, `open-webui-software.md`, `open-webui-routers.md`. |
| M1.5 | **Deployment**: Docker/Compose, Hostinger, volumes, env var *reference* (no secrets). | **Done** — `deployment-patterns.md` (+ ops delegation). |
| M1.6 | **Network & security**: Tailscale, ports, TLS paths, caller/callee matrix. | **Done** — `network-security-matrix.md`. |
| M1.7 | **Data**: logical schemas, retention, backups (only what is evidenced in code/config). | **Done** — `data-and-storage.md`. |
| M1.8 | **APIs**: OpenAI-compatible routes, Hermes endpoints, health checks — tables + sequence diagrams. | **Done** — `open-webui-routers.md` + `sequence-requests.md` + health table in `observability.md`. |
| M1.9 | **Operations**: runbooks (start/stop, upgrade, common incidents). | **Done** — `operations-runbook.md` (high level; deep runbooks stay in devops). |
| M1.10 | **Observability**: logs, metrics, traces — or explicit “not implemented” gaps. | **Done** — `observability.md` (metrics/tracing called out as gaps). |
| M1.11 | **ADRs**: key decisions inferred from the repos (lightweight). | **Done** — `docs/adr/0001–0003`. |

## Phase 2 — Users & developers

| ID | Milestone | Status |
|----|-----------|--------|
| M2.1 | End-user guides (Open-WebUI usage, models, policies as deployed). | **Done** — `user-guide/open-webui-basics.md`, `models-and-gateway.md`, `identiarag-for-analysts.md`. |
| M2.2 | Developer onboarding: clone, build, test, PR conventions. | **Done** — `developer/onboarding.md`. |
| M2.3 | Fork vs upstream boundaries (`open-webui`, etc.). | **Done** — `developer/fork-upstream-policy.md`. |

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
