# Publishing `docs.<your-domain>` (Phase 4)

MkDocs emits static files under `site/`. Host them on any static file host (NGINX, S3+CloudFront, GitHub Pages, Cloudflare Pages, etc.).

## Build artefact

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs build
# output: ./site/
```

## Recommended checks before go-live

| Check | Command / action |
|-------|------------------|
| Internal links | `mkdocs build` already fails on some broken refs; optionally add `lychee` or `markdown-link-check` in CI. |
| Search scope | Large gitignored files are excluded; do not copy `incoming/*.pdf` into `site/`. |
| Access control | If the TdR extract is ever copied into `docs/`, keep the site **private** or behind SSO. |

## DNS

1. Create hostname `docs.example.com` (replace with your domain).  
2. Point CNAME/A record to the static host.  
3. Configure TLS at the edge (Let’s Encrypt, managed cert, etc.).

## `site_url` in MkDocs

Uncomment and set in `mkdocs.yml`:

```yaml
site_url: https://docs.example.com
```

This fixes canonical URLs and OpenGraph when you enable social cards later.

## Related

- [Private repo & push](PRIVATE-REPO-AND-PUSH.md)  
- CI workflow: repository file `.github/workflows/docs.yml` (build on every push to `main`).
