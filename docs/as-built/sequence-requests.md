# Secuencias de peticiones

Vistas extremo a extremo sin incrustar URLs específicas del entorno.

## Pregunta RAG (UI del servicio RAG)

```mermaid
sequenceDiagram
  autonumber
  actor U as Usuario
  participant UI as FastAPI servicio RAG
  participant V as Vespa
  participant L as API LLM

  U->>UI: Enviar pregunta
  UI->>L: Generar consultas extra (opcional)
  L-->>UI: Consultas expandidas
  UI->>UI: Incrustar consultas
  UI->>V: Búsqueda nearestNeighbor
  V-->>UI: Chunks rankeados
  UI->>L: Respuesta solo con contexto recuperado
  L-->>UI: Respuesta final
  UI-->>U: Render / stream
```

## Chat vía interfaz web de chat a través de la pasarela

```mermaid
sequenceDiagram
  autonumber
  actor U as Usuario
  participant W as Interfaz web de chat
  participant G as Pasarela
  participant P as Upstream primario
  participant F as Upstream fallback

  U->>W: Mensaje
  W->>G: /v1/chat/completions
  alt primario OK
    G->>P: Reenvío
    P-->>G: Completion
  else fallo primario
    G->>F: Política fallback
    F-->>G: Completion
  end
  G-->>W: Respuesta
  W-->>U: Stream UI
```

## Opcional: la interfaz llama al servicio RAG para funciones RAG

```mermaid
sequenceDiagram
  participant W as Interfaz web de chat
  participant R as Servicio RAG
  participant V as Vespa

  W->>R: HTTP por función
  R->>V: Recuperación
  V-->>R: Chunks
  R-->>W: JSON / contexto parcial
```

Las rutas exactas dependen de la configuración del fork; rastrea llamadas desde los routers backend de la interfaz que referencian `IDENTIARAG_BASE_URL`.
