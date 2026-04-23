# Contributing to `docu`

## Security

- Never commit API keys, tokens, `.env` files, private keys, or customer-specific hostnames/IP addresses.
- Use placeholders in examples: `<gateway-host>`, `<user>@<host>`, etc.
- The TdR PDF stays under `incoming/` (gitignored for `*.pdf`). The **full-text extract** `docs/tor-gap/_extracted/tdr-extract.txt` is also **gitignored**; regenerate with `python scripts/extract_tdr_pdf.py` after legal review of redistribution policy.

## Git hooks

After clone:

```bash
git config core.hooksPath .githooks
chmod +x .githooks/commit-msg
```

## Documentation builds

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-docs.txt
.venv/bin/mkdocs serve
```

## Milestone cadence

Batch substantive changes and push to `origin` when a roadmap milestone is complete. See `docs/PRIVATE-REPO-AND-PUSH.md`.
