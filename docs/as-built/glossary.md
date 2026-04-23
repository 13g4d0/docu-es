# Glossary

| Term | Meaning in this solution |
|------|-------------------------|
| **IdentiaRAG** | Python package and FastAPI application for multi-stage RAG (query expansion → embeddings → Vespa → LLM answer). Evolved from upstream **nyrag** naming in parts of the codebase. |
| **Vespa** | Search engine used for hybrid / vector retrieval (`pyvespa`, ranking profiles). |
| **Open-WebUI** | Self-hosted chat UI and API hub (fork). Frontend: SvelteKit; backend: FastAPI + SQLAlchemy + optional Redis. |
| **LiteLLM** | OpenAI-compatible **gateway**: model aliases, routing, fallbacks, often backed by PostgreSQL when `STORE_MODEL_IN_DB` is enabled. |
| **OpenRouter** | Cloud model aggregator; typical **fallback** upstream behind LiteLLM. |
| **LM Studio** | Desktop inference runtime exposing an OpenAI-compatible `/v1` API on a configurable port. |
| **LM Link** | LM Studio ecosystem features for remote operation; often paired with private network reachability. |
| **Tailscale** | Mesh VPN providing stable private IPs (`100.64.0.0/10` range) between nodes (e.g. VPS ↔ workstation). |
| **Hermes Agent** | Separate container image for agent / messaging integrations (e.g. WhatsApp); optional HTTP API alongside the main app port. |
| **dev-stack.sh** | Bash orchestration in the IdentiaRAG repo for Open-WebUI Docker lifecycle and IdentiaRAG process control. |
| **Logical model alias** | User-facing model name resolved by the gateway (e.g. `lm-auto`) to one or more upstream deployments plus fallback rules. |
