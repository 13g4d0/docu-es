# Publishing the documentation site

MkDocs writes static HTML to `site/`. This repo is set up for **GitHub Pages** using **GitHub Actions** (no S3/buckets).

## GitHub Pages (default URL)

With repository `13g4d0/docu`, the site is served at:

**https://13g4d0.github.io/docu/**

`site_url` in `mkdocs.yml` matches that base so links and search behave correctly.

### One-time setup in GitHub (UI)

1. Open the repo on GitHub → **Settings** → **Pages**.  
2. Under **Build and deployment** → **Source**, choose **GitHub Actions** (not “Deploy from a branch” unless you switch workflows later).  
3. Save. After the first successful run on `main`, the site URL appears in **Pages** and in the workflow job **deploy** output.

### Si solo ves el `README.md` (texto plano, sin menú Material)

Eso casi siempre significa que Pages está sirviendo la **raíz del repo** (o la carpeta `/docs` con Jekyll), **no** el artefacto `site/` del workflow.

1. **Settings → Pages → Source** debe ser **GitHub Actions**, no *Deploy from a branch*.  
2. Si antes elegiste **Branch: `main` / folder: `/ (root)`** o **`/docs`**, cámbialo a **GitHub Actions** y guarda.  
3. En **Actions**, espera a que terminen en verde **`docs`** y **`pages build and deployment`**.  
4. Abre de nuevo **https://13g4d0.github.io/docu/** (mejor recarga forzada **Ctrl+F5**).

El sitio MkDocs correcto tiene **barra superior con pestañas** (Home, As-built, …) y **menú lateral**; la portada es **“Solution documentation”**, no el título del README `# docu`.

El workflow **copia `.nojekyll` a `site/`** tras `mkdocs build` para que, si Pages mezclara Jekyll, no procese los HTML estáticos.

The workflow file is `.github/workflows/docs.yml`: on every **push** to `main` it runs `mkdocs build --strict`, then **upload-pages-artifact** + **deploy-pages**.

### Private repository note

Visibility of a **private** repo’s GitHub Pages site depends on your GitHub plan and product (e.g. Enterprise). Confirm in [GitHub Docs — GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) who can view the published site. If the site must be internal-only, consider Enterprise or an alternative host with SSO.

## Local build

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs build --strict
# output: ./site/
```

## Pull requests

Every **pull request** against `main` runs the **build** job only (no deploy), so broken links or strict MkDocs errors fail CI before merge.

## Custom domain later (optional)

1. Add DNS: **CNAME** `docs` → `<user>.github.io` (or **A** / **AAAA** records per GitHub Pages custom domain docs).  
2. In **Settings → Pages**, set **Custom domain** (e.g. `docs.example.com`).  
3. Update `site_url` in `mkdocs.yml` to that HTTPS URL and redeploy.

## Safety checklist

| Check | Why |
|-------|-----|
| Do not publish `incoming/*.pdf` or `_extracted/` | Legal / confidentiality. |
| Keep repo access aligned with who may read Pages | Especially for private repos. |

## Related

- [Private repo & push](PRIVATE-REPO-AND-PUSH.md)
