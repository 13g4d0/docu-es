# TdR — executive summary (M3.1)

Synthesised from the PDF extract (`incoming/tdr.pdf` → `scripts/extract_tdr_pdf.py`) and the dashboard masthead. **Not** a substitute for legal review of the official document.

## Programme identity (extract)

| Field | Value (from document) |
|-------|------------------------|
| Programme | MAP–BID — *Programa de Mejora a la Eficiencia del Servicio Civil de la República Dominicana* |
| Reference | DR-L1142 (loan / programme context in TdR text) |
| Component | Component 2 — optimisation of MAP infrastructure & technology solutions |
| Subject | **TdR** — *Plataforma IA Jurídica Institucional* |
| Contract modality | **BOT** (Build–Operate–Transfer) |
| Document dates | March / April 2026 (cover pages vary) |

## Objectives (high level)

1. **Knowledge base** — Enable institutional legal knowledge (laws, regulations, manuals, etc.) for the public employment framework, initial period noted in TdR (e.g. first **3 months** for certain milestones).
2. **Agentic assistant** — Expert agent that researches, drafts, and audits drafts (resolution-style work) within a similar early window.
3. **Usage quota** — Provide at least **5,000** conversational RAG queries **per month** for a period of **18 months** (12+6) as stated in the extract.
4. **Operate & maintain** — Run the intelligent platform for **18 months** after go-live.
5. **Exit plan** — Detailed exit plan so MAP can migrate to another provider without loss of information or vendor lock-in (deadline tied to month **21** in extract).

## Procurement context (dashboard)

The gap dashboard (`dashboard.html`) states (verify against your official copy):

- **Expediente:** DR-L1142-P00100 · SBC  
- **Envelope:** **USD 200,000** · **24 months** · BOT modality  
- **Pre-technical-test threshold:** **63 / 90** points (70%) on experience + methodology + personnel groupings  
- **EOI deadline (as coded in dashboard):** 28 April 2026  

If any field differs in your final tender notice, update **both** the dashboard constants and this summary.

## Scope keywords (extract)

- Cloud-hosted **legal AI platform** with **web UI** and **conversational assistant** using **RAG**.  
- **Digital agents** for investigate → draft → audit workflows.  
- Emphasis on **normative systematication** for public employment law.  
- Later sections of the TdR (see extract) cover **DPA**, **model versioning**, **technical test**, **users**, **deliverables**, and **minimum team**.

## Where to go next

1. Regenerate `docs/tor-gap/_extracted/tdr-extract.txt` whenever the PDF changes.  
2. Fill [Gap analysis workbook](gap-analysis-workbook.md).  
3. Keep scoring evidence in the dashboard UI or export Markdown/CSV from the dashboard buttons.

## Related

- [Criteria from dashboard](criteria-from-dashboard.md)  
- [Tor-gap hub](index.md)
