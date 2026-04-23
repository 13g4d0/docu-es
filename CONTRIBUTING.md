# Contribuir al sitio de documentación

## Seguridad

- No versiones claves API, tokens, archivos `.env`, claves privadas ni nombres de host / IP propios de clientes.
- Usa marcadores en ejemplos: `<host-pasarela>`, `<usuario>@<host>`, etc.
- El PDF TdR va bajo `incoming/` (gitignored para `*.pdf`). El **extracto de texto** `docs/tor-gap/_extracted/tdr-extract.txt` también está **gitignored**; regenéralo con `python scripts/extract_tdr_pdf.py` tras revisar política legal de redistribución.

## Hooks de Git

Tras clonar:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

## Builds de documentación

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs serve
```

## Ritmo por hitos

Agrupa cambios sustantivos y haz push a `origin` cuando un hito del roadmap esté cerrado. Ver `docs/PRIVATE-REPO-AND-PUSH.md`.
