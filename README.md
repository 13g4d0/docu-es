# docu

Technical documentation for the IdentiaRAG + Open-WebUI + Hermes (+ gateway) stack, aligned with the as-built codebase and deployment.

- **Remote:** https://github.com/13g4d0/docu.git  
- **Canonical workspace on server:** `/opt/documentation`

## Layout (planned)

| Path | Purpose |
|------|---------|
| `docs/as-built/` | System as implemented (C4, deployment, APIs, ops). |
| `docs/tor-gap/` | TdR traceability, gap analysis, documentation roadmap (uses local `incoming/tdr.pdf`). |
| `incoming/` | Local-only inputs (e.g. `tdr.pdf`). **Not pushed** to this public repo by default. |

## Documentation milestones

See [`docs/ROADMAP-MILESTONES.md`](docs/ROADMAP-MILESTONES.md).

## Related sources (on server)

- Technical debt dashboard: `/opt/devops/map/dashboard.html`
- Branded architecture reference: `/opt/devops/docs/BRANDED_PRIVATE_MESH_ARCHITECTURE.md`

## TdR PDF (local)

Place the Terms of Reference PDF on the server (already typical path):

`scp /path/to/tdr.pdf root@31.97.145.146:/opt/documentation/incoming/tdr.pdf`

It stays out of git for this **public** repo unless you explicitly choose to publish it.

## Git commit messages (no Cursor trailer)

This repo uses a local `commit-msg` hook under `.githooks/` that **strips** an accidental `Made-with: Cursor` line from commit messages (some environments inject it). That keeps `main` history readable on GitHub.

**After clone** (once per working copy):

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

See [`.githooks/README.md`](.githooks/README.md). One-off bypass (only if you really need it): `git -c core.hooksPath=/dev/null commit …`
