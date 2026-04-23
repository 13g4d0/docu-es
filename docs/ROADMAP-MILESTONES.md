# Roadmap documental — índice de hitos

Orden sugerido. Trata cada hito como un entregable acotado (tamaño PR cuando sea posible).

**Estado (rodante):** fase **3** en gran parte cerrada (página M3.4 de *backlog* doc añadida); fase **4** con CI de build — despliegue y política de versionado aún abiertos.

## Fase 0 — Arranque

| ID | Hito | Estado |
|----|------|--------|
| M0.1 | Estructura del repo, nombres, política de idioma, elección del generador estático (MkDocs / Docusaurus / otro). | **Hecho** — MkDocs + Material + Mermaid nativo en Material. |
| M0.2 | Glosario + mapa de repos (servicio RAG, fork interfaz chat, devops, servicio de agentes). | **Hecho** — `docs/as-built/glossary.md`, `repo-map.md`. |
| M0.3 | «Cómo leer este sitio» + enlaces a `dashboard.html` y referencias de arquitectura. | **Hecho** — `meta/internal-references.md` + tabla de inicio (rutas relativas al checkout devops, sin URLs de producción). |

## Fase 1 — As-built (código + verdad de ejecución)

| ID | Hito | Estado |
|----|------|--------|
| M1.1 | Contexto producto / solución (breve; anclado en lo que existe). | **Hecho** — `docs/index.md` + páginas de pasarela / contexto. |
| M1.2 | C4 nivel 1 — **Contexto del sistema**: actores, sistemas externos, límites de confianza. | **Hecho** — `as-built/c4-context.md`. |
| M1.3 | C4 nivel 2 — **Contenedores**: servicios (pasarela, interfaz de chat, servicio de agentes, RAG, bases, colas si las hay). | **Hecho** — `as-built/c4-containers.md`. |
| M1.4 | C4 nivel 3 — **Componentes** (por servicio o repo crítico): módulos principales y dependencias. | **Hecho** — `identiarag-software.md`, `open-webui-software.md`, `open-webui-routers.md`. |
| M1.5 | **Despliegue**: Docker/Compose, proveedor de alojamiento, volúmenes, referencia de variables de entorno (sin secretos). | **Hecho** — `deployment-patterns.md` (+ delegación ops). |
| M1.6 | **Red y seguridad**: VPN en malla, puertos, rutas TLS, matriz llamador/llamado. | **Hecho** — `network-security-matrix.md`. |
| M1.7 | **Datos**: esquemas lógicos, retención, copias de seguridad (solo lo evidenciado en código/config). | **Hecho** — `data-and-storage.md`. |
| M1.8 | **APIs**: rutas compatibles OpenAI, endpoints del servicio de agentes, healthchecks — tablas + diagramas de secuencia. | **Hecho** — `open-webui-routers.md` + `sequence-requests.md` + tabla de salud en `observability.md`. |
| M1.9 | **Operaciones**: runbooks (arranque/parada, actualización, incidentes frecuentes). | **Hecho** — `operations-runbook.md` (alto nivel; runbooks profundos en devops). |
| M1.10 | **Observabilidad**: logs, métricas, trazas — o brechas explícitas «no implementado». | **Hecho** — `observability.md` (métricas/trazas marcadas como brechas). |
| M1.11 | **ADRs**: decisiones clave inferidas de los repos (ligeras). | **Hecho** — `docs/adr/0001–0003`. |

## Fase 2 — Usuarios y desarrolladores

| ID | Hito | Estado |
|----|------|--------|
| M2.1 | Guías de usuario final (uso de la interfaz de chat, modelos, políticas desplegadas). | **Hecho** — `user-guide/open-webui-basics.md`, `models-and-gateway.md`, `identiarag-for-analysts.md`. |
| M2.2 | Incorporación desarrolladores: clone, build, test, convenciones de PR. | **Hecho** — `developer/onboarding.md`. |
| M2.3 | Límites fork vs *upstream* (interfaz de chat, etc.). | **Hecho** — `developer/fork-upstream-policy.md`. |

## Fase 3 — TdR y brechas (tras as-built sólido)

| ID | Hito | Estado |
|----|------|--------|
| M3.1 | Resumen ejecutivo TdR (requisitos y alcance citados desde `incoming/tdr.pdf`). | **Hecho** — `tor-gap/tdr-executive-summary.md` + script de extracto. |
| M3.2 | Matriz **TdR ↔ implementación** (completa / parcial / ausente / N/A). | **Plantilla** — `tor-gap/gap-analysis-workbook.md` (rellenar por criterio). |
| M3.3 | **Informe técnico de brechas** (riesgo, esfuerzo, dependencias). | **Plantilla** — sección 2 del cuaderno. |
| M3.4 | **Hoja de ruta documental** derivada de brechas (qué escribir después). | **Hecho** — `tor-gap/documentation-roadmap-from-gaps.md` (matriz inicial; rellenar tras taller). |
| M3.5 | Alineación con indicadores de `dashboard.html`. | **Parcial** — instantánea de criterios + sección de mapeo en el cuaderno. |

## Fase 4 — Sitio publicado (`docs.dominio.com`)

| ID | Hito | Estado |
|----|------|--------|
| M4.1 | Generador estático + tema + navegación. | **Hecho** (igual que M0.1). |
| M4.2 | CI: build + comprobación de enlaces; despliegue opcional al subdominio `docs`. | **Hecho (GitHub)** — workflow construye en PR; **deploy-pages** en `main` → `https://13g4d0.github.io/docu-es/`. Comprobación de enlaces aún opcional. |
| M4.3 | Política de versionado (por release vs fechado). | **Pendiente** |

## Fase 5 — Deuda y mantenimiento

| ID | Hito |
|----|------|
| M5.1 | Lista de comprobación de «deuda doc» ante cambios de código significativos. |
| M5.2 | Revisión trimestral: diagramas vs realidad, enlaces rotos, notas de rotación de secretos. |
