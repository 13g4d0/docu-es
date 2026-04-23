# Referencias internas (fuera de este repo)

Tipos de artefactos que viven en repositorios hermanos en el mismo host documental. **No** pegues URLs de producción, claves API ni nombres de host de clientes en el sitio MkDocs.

## Repositorio devops

| Ruta relativa (dentro del checkout devops) | Uso |
|--------------------------------------------|-----|
| `docs/*.md` | Arquitectura y runbooks (cableado pasarela, VPN en malla, interfaz de chat). |
| `map/dashboard.html` | Tablero de deuda / progreso (rúbrica `CRITERIA` + persistencia local). Instantánea reflejada en el sitio → [Criterios desde el tablero](../tor-gap/criteria-from-dashboard.md). |
| `incoming/tdr.pdf` (en el checkout **de documentación**) | PDF oficial TdR — extraer localmente con `python scripts/extract_tdr_pdf.py` → `docs/tor-gap/_extracted/tdr-extract.txt` (gitignored). |
| `ops.sh` | Delega en `dev-stack.sh` del servicio RAG para el ciclo de vida de la pila. |

El layout de clones es por organización; configura `DEVOPS_STACK_SCRIPT` o `DEVOPS_IDENTIARAG_ROOT` si las rutas difieren.

## Repositorio del servicio RAG

| Ruta | Uso |
|------|-----|
| `dev-stack.sh` | Orquestación interfaz de chat + servicio RAG. |
| `compose.yml` | Vespa + UI + agent-embed opcional. |
| `documentation/` | Árbol de docs *upstream* del servicio RAG (distinto de este sitio MkDocs). |

## Relación con M0.3

- **Este sitio MkDocs** = documentación *as-built* curada + roadmap de la solución combinada.
- **HTML del tablero** = seguimiento operativo / deuda; mantenlo en **devops** y enlázalo internamente vía wiki o host estático con acceso controlado — sin URLs de producción hardcodeadas en git.

## Relacionado

- [Runbook operativo](../as-built/operations-runbook.md)
