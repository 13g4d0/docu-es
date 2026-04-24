# Documentación de la solución (as-built)

Este sitio describe la integración **actual** de:

- **Servicio RAG** — pipeline RAG (VectorDB, embeddings, FastAPI UI/API).
- **Interfaz web de chat** — plataforma de chat autohospedada derivada de fork (frontend SvelteKit + backend FastAPI).
- **Pasarela de inferencia** — enrutado compatible OpenAI (pasarela unificada), inferencia local opcional (runtime en escritorio) y proveedores en la nube (API agregadora de modelos), con transporte privado en malla (VPN entre nodos) donde aplique.
- **Servicio de agentes** — pila opcional de mensajería/agentes (ciclo de vida Compose independiente).

La documentación está pensada para un repositorio **privado** en GitHub. **No** incrustes claves API, tokens ni nombres de host específicos del entorno en páginas versionadas.

## Cómo leer

| Sección | Audiencia | Contenido |
|---------|-----------|-----------|
| [Glosario](as-built/glossary.md) | Todos | Términos y equivalencias funcionales. |
| [C4 — Contexto del sistema](as-built/c4-context.md) | Arquitectos / líderes | Actores externos y límites de confianza. |
| [C4 — Contenedores](as-built/c4-containers.md) | DevOps / backend | Unidades ejecutables y puertos (lógicos). |
| [Servicio RAG](as-built/identiarag-software.md) | Backend | Pipeline, APIs, servicios Compose. |
| [Interfaz web de chat](as-built/open-webui-software.md) | Full-stack | Estructura monolito, puntos de extensión. |
| [Pasarela de inferencia](as-built/inference-gateway.md) | Plataforma | Enrutado híbrido local + nube. |
| [Servicio de agentes](as-built/agent-service.md) | Integraciones | Contenedor de agentes, superficie API (alto nivel). |
| [Routers HTTP](as-built/open-webui-routers.md) | Backend | Mapa de prefijos FastAPI. |
| [Datos y almacenamiento](as-built/data-and-storage.md) | Backend / DBA | Bases, volúmenes, prioridades de backup. |
| [Red y seguridad](as-built/network-security-matrix.md) | Seguridad | Matriz de flujos y clases de puerto. |
| [Patrones de despliegue](as-built/deployment-patterns.md) | DevOps | Compose frente a `docker run`, patrones de entorno. |
| [Runbook operativo](as-built/operations-runbook.md) | DevOps | `ops.sh` / operaciones Compose. |
| [Observabilidad](as-built/observability.md) | DevOps | Healthchecks, logs, brechas conocidas. |
| [Secuencias de peticiones](as-built/sequence-requests.md) | Todos | Secuencias Mermaid extremo a extremo. |
| [ADRs](adr/README.md) | Arquitectos | Decisiones aceptadas. |
| [Referencias internas](meta/internal-references.md) | Equipo | Punteros al tablero devops (sin secretos). |

## Guía de usuario

| Página | Audiencia |
|--------|-----------|
| [Uso básico de la interfaz de chat](user-guide/open-webui-basics.md) | Usuarios finales |
| [Modelos y pasarela](user-guide/models-and-gateway.md) | Usuarios y administradores del espacio de trabajo |
| [Servicio RAG para analistas](user-guide/identiarag-for-analysts.md) | Analistas / operadores |

## Desarrollo

| Página | Audiencia |
|--------|-----------|
| [Incorporación](developer/onboarding.md) | Ingenieros que se unen al proyecto |
| [Política de fork y upstream](developer/fork-upstream-policy.md) | Mantenedores |

## TdR y brechas (fase 3)

| Página | Audiencia |
|--------|-----------|
| [Índice TdR y brechas](tor-gap/index.md) | PM / líder técnico |
| [Resumen ejecutivo TdR](tor-gap/tdr-executive-summary.md) | Stakeholders |
| [Criterios (tablero)](tor-gap/criteria-from-dashboard.md) | Evaluadores |
| [Cuaderno de brechas](tor-gap/gap-analysis-workbook.md) | Equipo de entrega |
| [Hoja de ruta documental](tor-gap/documentation-roadmap-from-gaps.md) | Redactor técnico / líder |
| [Notas del organizador](tor-gap/organizer-notes.md) | Uso interno (revisar antes de commit) |
| [Publicación](PUBLISHING.md) | DevOps |

## Hitos

El avance se sigue en [ROADMAP-MILESTONES.md](ROADMAP-MILESTONES.md). Los push a `origin` van agrupados **por hito**; ver [PRIVATE-REPO-AND-PUSH.md](PRIVATE-REPO-AND-PUSH.md).

## Build local

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs serve
```

HTML estático: `.venv/bin/mkdocs build` → salida en `site/` (gitignored).
