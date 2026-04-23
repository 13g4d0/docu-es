# Open-WebUI — HTTP routers (component view)

This page maps **FastAPI routers** registered in `backend/open_webui/main.py` (fork snapshot). Feature flags may omit some routers (e.g. SCIM, admin analytics).

## Router diagram

```mermaid
flowchart TB
  subgraph transport [Transport]
    APP[FastAPI app]
    WS["/ws WebSocket"]
  end

  subgraph integrations [Model runners]
    OLL["/ollama"]
    OAI["/openai"]
  end

  subgraph api [Versioned REST /api/v1]
    PIP[pipelines]
    TSK[tasks]
    IMG[images]
    AUD[audio]
    RET[retrieval]
    CFG[configs]
    AUTH[auths]
    USR[users]
    CHN[channels]
    CHT[chats]
    NTE[notes]
    MDL[models]
    KNO[knowledge]
    PRM[prompts]
    TOL[tools]
    SKL[skills]
    MEM[memories]
    FLD[folders]
    GRP[groups]
    FIL[files]
    FUN[functions]
    EVL[evaluations]
    ANA[analytics optional]
    UTL[utils]
    TRM[terminals]
    SCM[scim optional]
  end

  APP --> WS
  APP --> OLL
  APP --> OAI
  APP --> PIP
  APP --> TSK
  APP --> IMG
  APP --> AUD
  APP --> RET
  APP --> CFG
  APP --> AUTH
  APP --> USR
  APP --> CHN
  APP --> CHT
  APP --> NTE
  APP --> MDL
  APP --> KNO
  APP --> PRM
  APP --> TOL
  APP --> SKL
  APP --> MEM
  APP --> FLD
  APP --> GRP
  APP --> FIL
  APP --> FUN
  APP --> EVL
  APP --> ANA
  APP --> UTL
  APP --> TRM
  APP --> SCM
```

## Prefix table

| Prefix | Purpose (summary) |
|--------|---------------------|
| `/ws` | Real-time / streaming channel (see `socket` package). |
| `/ollama` | Ollama-compatible endpoints. |
| `/openai` | OpenAI-compatible proxying and tool calls toward external gateways. |
| `/api/v1/pipelines` | Pipeline plugins. |
| `/api/v1/tasks` | Background tasks. |
| `/api/v1/images` | Image generation / editing integrations. |
| `/api/v1/audio` | STT/TTS routes. |
| `/api/v1/retrieval` | RAG retrieval configuration and execution. |
| `/api/v1/configs` | Runtime configuration. |
| `/api/v1/auths` | Sign-in, tokens, OAuth. |
| `/api/v1/users` | User profiles and admin operations. |
| `/api/v1/channels` | Channel / workspace constructs. |
| `/api/v1/chats` | Chat sessions and messages. |
| `/api/v1/notes` | Notes feature. |
| `/api/v1/models` | Model list and metadata. |
| `/api/v1/knowledge` | Knowledge collections. |
| `/api/v1/prompts` | Saved prompts. |
| `/api/v1/tools` | Tool definitions. |
| `/api/v1/skills` | Skills (structured tool bundles). |
| `/api/v1/memories` | Long-term memory store. |
| `/api/v1/folders` | Folder hierarchy for chats/files. |
| `/api/v1/groups` | RBAC groups. |
| `/api/v1/files` | Uploaded files. |
| `/api/v1/functions` | Python functions exposed to models. |
| `/api/v1/evaluations` | Evaluation flows. |
| `/api/v1/analytics` | Admin analytics (optional flag). |
| `/api/v1/utils` | Miscellaneous helpers. |
| `/api/v1/terminals` | Web terminal integration. |
| `/api/v1/scim/v2` | SCIM provisioning (optional flag). |

## SQLAlchemy models (`backend/open_webui/models/`)

Representative modules: `chats`, `chat_messages`, `users`, `auths`, `knowledge`, `files`, `groups`, `memories`, `tools`, `functions`, … — see [Data & storage](data-and-storage.md).

## Related

- [Open-WebUI — software](open-webui-software.md)
- [Sequence diagrams](sequence-requests.md)
