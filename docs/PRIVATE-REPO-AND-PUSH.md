# Git y política de push

## Objetivos

- Este repositorio (`docu-es`) es **público**: el historial y el contenido son visibles para cualquiera. **No** subas claves API, tokens, valores de `.env` ni datos personales.
- **Agrupa cambios por hitos** cuando sea posible (rodajas de documentación acordadas), en lugar de un micro-commit por línea.
- La documentación **en inglés** puede vivir en otro repo (p. ej. `docu`) con su propio flujo y URL de Pages.

## Autenticación para `git push`

Los colaboradores usan la autenticación habitual de GitHub (SSH, `gh auth login`, PAT con alcance mínimo, etc.). Para **CI** que despliegue solo HTML, el workflow de Pages usa `GITHUB_TOKEN` (no hace falta PAT en el repo para el deploy estándar).

Si en el futuro un agente automatizado necesita **push de commits** al repo, usa **Deploy key** o **PAT** con alcance mínimo y guarda el secreto solo en el host o en **GitHub Actions secrets** — nunca en el Markdown versionado.

## Ritmo por hitos (recomendado)

1. Acumula cambios doc en local o en rama hasta cerrar un **hito** de `ROADMAP-MILESTONES.md`.
2. Revisa el diff: sin secretos (`Bearer`, `sk-`, IPs internas si tu política lo prohíbe, etc.).
3. Commit(s) con mensaje claro (p. ej. `docs(M3.2): plantilla de matriz TdR`).
4. `git push origin main`.

## Si el repo pasa de privado a público (o al revés)

- Revisa `git log` y archivos por contenido que no deba ser público (defensa en profundidad).
- Actualiza enlaces en otros repos (devops, README del servicio RAG) que apunten a la URL de Pages correcta.
