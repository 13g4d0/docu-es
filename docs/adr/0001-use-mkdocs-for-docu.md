# ADR 0001 — Use MkDocs Material for the `docu` site

- **Status:** Accepted  
- **Date:** 2026-04-23  

## Context

We need a static documentation site that can later publish to `docs.<domain>`, with search, navigation, and Mermaid diagrams.

## Decision

Use **MkDocs** with the **Material** theme and **mermaid2** plugin, built via a local Python virtual environment (PEP 668 safe).

## Consequences

- **Positive:** Fast authoring in Markdown, good default UX, CI-friendly `mkdocs build`.
- **Negative:** MkDocs 2.x upstream changes will require migration planning when upgrading.
