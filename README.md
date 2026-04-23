# Documentación técnica (sitio MkDocs)

Documentación del stack **servicio RAG + interfaz web de chat + servicio de agentes + pasarela de inferencia**, alineada con el código *as-built* y el despliegue.

- **Remoto:** `https://github.com/13g4d0/docu-es` (**público** — documentación en español para GitHub Pages).
- **Versión en inglés:** puede mantenerse en un repo aparte (p. ej. `13g4d0/docu`) con su propia URL de Pages.
- **Copia de trabajo:** clonar en cualquier máquina; no versionar secretos ni rutas propias de clientes.

## Estructura (prevista)

| Ruta | Uso |
|------|-----|
| `docs/as-built/` | Sistema tal como está implementado (C4, despliegue, APIs, ops). |
| `docs/tor-gap/` | Trazabilidad TdR, análisis de brechas, hoja de ruta documental (TdR PDF local bajo `incoming/`). |
| `incoming/` | Entradas solo locales (p. ej. PDF TdR). **No versionado** (ver `.gitignore`). |

## Hitos documentales

Ver [`docs/ROADMAP-MILESTONES.md`](docs/ROADMAP-MILESTONES.md).

## Fuentes relacionadas (internas)

Los materiales de referencia pueden vivir en checkouts hermanos en el mismo host (las rutas varían). **No** copies claves API, contenido de `.env` ni credenciales de proveedor en este repo.

## PDF TdR (solo local)

Coloca el PDF de los términos de referencia bajo `incoming/` con el método aprobado por tu organización (SFTP, enlace seguro, etc.). Ejemplo de forma (sustituye marcadores):

```bash
scp <ruta-local>/tdr.pdf <usuario>@<host>:<ruta-al-repo>/incoming/tdr.pdf
```

No versiones claves, tokens ni cadenas de conexión de producción. El PDF permanece **gitignored** salvo que cambiéis `.gitignore` y la política.

## Mensajes de commit (sin remolque de herramienta)

Este repo usa un hook local `commit-msg` bajo `.githooks/` que **elimina** una línea accidental `Made-with: Cursor` del mensaje (algunos entornos la inyectan).

**Tras clonar** (una vez por copia de trabajo):

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

Ver [`.githooks/README.md`](.githooks/README.md). Bypass puntual (solo si hace falta): `git -c core.hooksPath=/dev/null commit …`

## Repo privado y push (hitos)

Ver [`docs/PRIVATE-REPO-AND-PUSH.md`](docs/PRIVATE-REPO-AND-PUSH.md). Los commits a `origin` están pensados **una vez por hito** documental, no en cada edición pequeña.

## Sitio MkDocs

Usa un **virtualenv** (PEP 668 en Debian/Ubuntu):

```bash
cd /opt/documentacion
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs serve    # vista previa local
.venv/bin/mkdocs build    # salida estática en site/
```

Normas para colaboradores: [CONTRIBUTING.md](CONTRIBUTING.md).

## CI y GitHub Pages

GitHub Actions (`.github/workflows/docs.yml`):

- **Pull requests:** `mkdocs build --strict` + artefacto `site/`.
- **Push a `main`:** mismo build y despliegue a **GitHub Pages** en **https://13g4d0.github.io/docu-es/** (activar **Settings → Pages → Source: GitHub Actions** una vez).

Detalle: [docs/PUBLISHING.md](docs/PUBLISHING.md).
