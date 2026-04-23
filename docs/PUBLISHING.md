# Publicar el sitio de documentación

MkDocs genera HTML estático en `site/`. Este repo está preparado para **GitHub Pages** con **GitHub Actions** (sin S3 ni buckets).

## GitHub Pages (URL por defecto)

Con el repositorio `13g4d0/docu-es`, el sitio se sirve en:

**https://13g4d0.github.io/docu-es/**

`site_url` en `mkdocs.yml` coincide con esa base para que enlaces y búsqueda funcionen bien.

### Configuración única en GitHub (interfaz)

1. Abre el repo en GitHub → **Settings** → **Pages**.  
2. En **Build and deployment** → **Source**, elige **GitHub Actions** (no «Deploy from a branch» salvo que cambiéis de workflow más adelante).  
3. Guarda. Tras la primera ejecución correcta en `main`, la URL del sitio aparece en **Pages** y en la salida del job **deploy** del workflow.

### Si solo ves el `README.md` (texto plano, sin menú Material)

Casi siempre significa que Pages está sirviendo la **raíz del repo** (o la carpeta `/docs` con Jekyll), **no** el artefacto `site/` del workflow.

1. **Settings → Pages → Source** debe ser **GitHub Actions**, no *Deploy from a branch*.  
2. Si antes elegiste **Branch: `main` / folder: `/ (root)`** o **`/docs`**, cámbialo a **GitHub Actions** y guarda.  
3. En **Actions**, espera a que terminen en verde **`docs`** y **`pages build and deployment`**.  
4. Abre de nuevo **https://13g4d0.github.io/docu-es/** (mejor recarga forzada **Ctrl+F5**).

El sitio MkDocs correcto tiene **barra superior con pestañas** (Inicio, As-built, …) y **menú lateral**; la portada es el título configurado en `site_name` de `mkdocs.yml`, no el encabezado `#` del README del repo.

El workflow **copia `.nojekyll` a `site/`** tras `mkdocs build` para que, si Pages mezclara Jekyll, no procese los HTML estáticos.

### Diagramas Mermaid

Los diagramas usan la **configuración nativa de Material** (`pymdownx.superfences` + `custom_fences` para `mermaid`). No uses el plugin `mkdocs-mermaid2` a la vez: rompe el renderizado.

Si tras publicar no ves los diagramas: recarga forzada (**Ctrl+F5**) y revisa en las herramientas de desarrollador (**Consola**) si un bloqueador o CSP impide cargar el script de Mermaid (Material lo incluye en el bundle / CDN según versión).

El workflow está en `.github/workflows/docs.yml`: en cada **push** a `main` ejecuta `mkdocs build --strict`, luego **upload-pages-artifact** + **deploy-pages**.

### Repositorio público

Este sitio (`docu-es`) está pensado como repositorio **público**: cualquiera puede clonar y ver el historial. No incluyas secretos ni datos personales. La documentación en **inglés** puede vivir en un repo hermano (`docu` u otro) con su propia URL de Pages.

## Build local

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs build --strict
# salida: ./site/
```

## Pull requests

Cada **pull request** contra `main` ejecuta solo el job de **build** (sin despliegue), de modo que enlaces rotos o errores estrictos de MkDocs fallen en CI antes del merge.

## Dominio personalizado (opcional)

1. Añade DNS: **CNAME** `docs` → `<usuario>.github.io` (o registros **A** / **AAAA** según la doc de dominio personalizado de Pages).  
2. En **Settings → Pages**, define **Custom domain** (p. ej. `docs.example.com`).  
3. Actualiza `site_url` en `mkdocs.yml` a esa URL HTTPS y vuelve a desplegar.

## Lista de comprobación de seguridad

| Comprobar | Motivo |
|-----------|--------|
| No publicar `incoming/*.pdf` ni `_extracted/` | Legal / confidencialidad. |
| Revisar que el contenido sea adecuado para repo público | Historial Git y Issues son visibles. |

## Relacionado

- [Git y política de push](PRIVATE-REPO-AND-PUSH.md)
