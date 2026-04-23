# ADR 0003 — Carpetas hermanas para `dev-stack.sh`

- **Estado:** Aceptado  
- **Fecha:** 2026-04-23  

## Contexto

`dev-stack.sh` resuelve `OPEN_WEBUI_ROOT` relativo al checkout del servicio RAG (`../open-webui` por defecto). Los operadores pueden sobrescribir con variables de entorno.

## Decisión

Estandarizar un **layout en directorios hermanos** (servicio RAG junto al fork `open-webui`) en hosts de desarrollo, documentado en lugar de rutas absolutas fijas en la automatización.

## Consecuencias

- **Positivo:** Rutas relativas predecibles; *onboarding* más simple.
- **Negativo:** Clones en ubicaciones no estándar deben exportar `OPEN_WEBUI_ROOT` explícitamente.
