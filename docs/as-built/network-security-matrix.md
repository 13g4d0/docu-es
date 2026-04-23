# Red y matriz de seguridad

Solo flujos **lógicos**. Sustituye nombres de interfaz y CIDR por los estándares de tu organización.

## Matriz llamador → llamado

```mermaid
flowchart TB
  subgraph clients [Clientes]
    BR[Navegador]
  end

  subgraph edge [Borde]
    RP[Reverse proxy / TLS]
  end

  subgraph apps [Capa de aplicación]
    OW[Interfaz web de chat]
    IR[Servicio RAG]
    GW[Pasarela de inferencia]
  end

  subgraph data [Capa de datos]
    V[Vespa]
    PG[(Postgres)]
    RD[(Redis opcional)]
  end

  subgraph mesh [Malla privada]
    TS[VPN en malla]
  end

  subgraph ext [APIs externas]
    CL[Proveedores LLM en la nube]
    LOC[Inferencia en estación]
  end

  BR --> RP --> OW
  BR --> RP --> IR
  OW --> GW
  OW --> IR
  GW --> TS --> LOC
  GW --> CL
  IR --> V
  OW --> PG
  OW --> RD
  GW --> PG
```

## Clases de puerto

| Clase | Ejemplos | Endurecimiento |
|-------|----------|----------------|
| **HTTPS público** | *Reverse proxy* → interfaz / servicio RAG | TLS 1.2+, WAF opcional, autenticación obligatoria. |
| **Solo interno** | Pasarela ↔ Postgres, interfaz ↔ Redis | Enlazar a loopback o red Docker privada; sin exposición WAN. |
| **Solo malla** | Pasarela → inferencia en estación | ACL en la malla; el proceso de inferencia no debe confiar en Internet público. |
| **Egreso a proveedor** | Pasarela → API agregadora / OpenAI | Lista blanca saliente; cuotas por clave. |

## Secretos (política)

| Tipo de secreto | Dónde guardarlo | Nunca |
|-----------------|-----------------|-------|
| Clave maestra de pasarela | Gestor de secretos / `.env` en servidor | En git, pegado en docs. |
| Claves API de proveedor | Entorno de pasarela o *vault* | En clientes de navegador salvo por proxy servidor. |
| Contraseñas DB | Compose env / *vault* | En logs en claro. |

## Relacionado

- [Pasarela de inferencia](inference-gateway.md)
- [Runbook operativo](operations-runbook.md)
