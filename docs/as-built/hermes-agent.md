# Servicio de agentes

Es un desplegable **separado** del servicio RAG y de la interfaz web de chat. Empaqueta un runtime de agente (incluye canales de mensajería opcionales con proveedores de terceros) en una imagen de contenedor publicada por la pila del proveedor de alojamiento.

## Patrón Compose (observado)

De un `docker-compose.yml` representativo en el servidor de aplicaciones:

```yaml
# Ilustrativo — no copiar secretos del .env real
services:
  hermes-agent:
    image: <registro>/<imagen-agente>:latest
    ports:
      - "8642:8642"   # superficie HTTP API opcional
    env_file: [.env]
    volumes:
      - ./hermes:/opt/hermes    # montaje para git / actualizaciones de código
      - ./data:/opt/data
```

Las etiquetas de *reverse proxy* (p. ej. Traefik en `4860`) pueden enrutar la **UI** HTTP principal; el mapeo **8642** suele usarse para API o *health* — confirma con el contenedor en ejecución y `.env`.

```mermaid
flowchart TB
  subgraph HC["Proyecto Compose del servicio de agentes"]
    H["Contenedor del servicio de agentes"]
    data[("Volumen de datos en el host")]
    code["Montaje de código del agente en el host"]
    H --> data
    H --> code
  end

  user["Usuarios externos"] -->|"Mensajería"| H
  admin["Operadores"] -->|"HTTP API o health"| H
```

## Relación con la pila de chat

- **Ortogonal** a la conexión OpenAI por defecto de la interfaz web de chat: el servicio de agentes **no** sustituye a la pasarela de inferencia salvo que cableéis integraciones explícitas.
- Patrón futuro opcional: enrutar las llamadas LLM del servicio de agentes por la misma **pasarela** para cuotas y registro unificados.

## Operaciones (alto nivel)

- Montar `./hermes` sobre un checkout git del código del agente cuando necesitéis actualizaciones tipo `git pull` dentro del layout de la imagen.
- Mantener `.env` fuera de git; rotar las claves API del agente de forma independiente de las de la pasarela.

## Relacionado

- [C4 — Contenedores](c4-containers.md) para resumen de puertos.
- [Patrones de despliegue](deployment-patterns.md) para Compose frente a la pila de UI.
