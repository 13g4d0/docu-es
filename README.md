# docu

Technical documentation for the IdentiaRAG + Open-WebUI + Hermes (+ gateway) stack, aligned with the as-built codebase and deployment.

- **Remote:** `https://github.com/13g4d0/docu` (expected to be **private**)
- **Working copy:** clone to any machine your team uses for authoring; keep secrets and customer-specific paths out of tracked files.

## Layout (planned)

| Path | Purpose |
|------|---------|
| `docs/as-built/` | System as implemented (C4, deployment, APIs, ops). |
| `docs/tor-gap/` | TdR traceability, gap analysis, documentation roadmap (uses a local-only TdR PDF under `incoming/`). |
| `incoming/` | Local-only inputs (e.g. TdR PDF). **Not committed** (see `.gitignore`). |

## Documentation milestones

See [`docs/ROADMAP-MILESTONES.md`](docs/ROADMAP-MILESTONES.md).

## Related sources (internal)

Reference materials may live in sibling checkouts on the same host (paths differ per environment). Do **not** copy API keys, `.env` contents, or provider credentials into this repo.

## TdR PDF (local only)

Place the Terms of Reference PDF under `incoming/` using **your** organisation’s approved transfer method (SFTP, secure share, etc.). Example shape only — replace placeholders:

```bash
scp <path-to-local>/tdr.pdf <user>@<host>:<path-to-repo>/incoming/tdr.pdf
```

Never commit keys, tokens, or production connection strings. The PDF stays **gitignored** unless you deliberately change `.gitignore` and policy.

## Git commit messages (no Cursor trailer)

This repo uses a local `commit-msg` hook under `.githooks/` that **strips** an accidental `Made-with: Cursor` line from commit messages (some environments inject it).

**After clone** (once per working copy):

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

See [`.githooks/README.md`](.githooks/README.md). One-off bypass (only if you really need it): `git -c core.hooksPath=/dev/null commit …`

## Private repo & pushing (milestones)

See [`docs/PRIVATE-REPO-AND-PUSH.md`](docs/PRIVATE-REPO-AND-PUSH.md). Commits to `origin` are intended **once per documentation milestone**, not on every small edit.

## MkDocs site

Use a **virtualenv** (PEP 668 on Debian/Ubuntu):

```bash
cd /opt/documentation
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs serve    # local preview
.venv/bin/mkdocs build    # static output in site/
```

Contributor rules: [CONTRIBUTING.md](CONTRIBUTING.md).

## CI

GitHub Actions builds the site with `mkdocs build --strict` on pushes and PRs to `main` (see `.github/workflows/docs.yml`). Artefact: `site/` zip per run.

Publishing steps: [docs/PUBLISHING.md](docs/PUBLISHING.md).
