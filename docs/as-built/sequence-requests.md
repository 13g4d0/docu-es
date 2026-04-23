# Request sequences

End-to-end views without embedding environment-specific URLs.

## RAG question (IdentiaRAG UI)

```mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant UI as IdentiaRAG FastAPI
  participant V as Vespa
  participant L as LLM API

  U->>UI: Submit question
  UI->>L: Generate extra queries (optional)
  L-->>UI: Expanded queries
  UI->>UI: Embed queries
  UI->>V: nearestNeighbor search
  V-->>UI: Ranked chunks
  UI->>L: Answer with retrieved context only
  L-->>UI: Final answer
  UI-->>U: Render / stream
```

## Chat via Open-WebUI through gateway

```mermaid
sequenceDiagram
  autonumber
  actor U as User
  participant W as Open-WebUI
  participant G as LiteLLM
  participant P as Primary upstream
  participant F as Fallback upstream

  U->>W: Message
  W->>G: /v1/chat/completions
  alt primary OK
    G->>P: Forward
    P-->>G: Completion
  else primary fails
    G->>F: Fallback policy
    F-->>G: Completion
  end
  G-->>W: Response
  W-->>U: UI stream
```

## Optional: Open-WebUI calls IdentiaRAG for RAG features

```mermaid
sequenceDiagram
  participant W as Open-WebUI
  participant R as IdentiaRAG
  participant V as Vespa

  W->>R: Feature-specific HTTP call
  R->>V: Retrieval
  V-->>R: Chunks
  R-->>W: JSON / partial context
```

Exact paths depend on fork configuration; trace calls starting at Open-WebUI backend routers that reference `IDENTIARAG_BASE_URL`.
