# ADR 0001 — MkDocs Material para este sitio

- **Estado:** Aceptado  
- **Fecha:** 2026-04-23  

## Contexto

Necesitamos un sitio de documentación estático que más adelante pueda publicarse en `docs.<dominio>`, con búsqueda, navegación y diagramas Mermaid.

## Decisión

Usar **MkDocs** con el tema **Material** y Mermaid vía **Material / `pymdownx.superfences`** (sin el plugin `mkdocs-mermaid2` en paralelo, que entraba en conflicto), construido con un **virtualenv** local (seguro ante PEP 668).

## Consecuencias

- **Positivo:** Autoría rápida en Markdown, buena UX por defecto, `mkdocs build` amigable con CI.
- **Negativo:** Los cambios *upstream* de MkDocs 2.x exigirán plan de migración al actualizar.
