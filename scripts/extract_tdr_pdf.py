#!/usr/bin/env python3
"""Extract plain text from incoming/tdr.pdf into docs/tor-gap/_extracted/tdr-extract.txt.

Requires: pip install pypdf (see requirements-docs.txt)

Usage (from repo root):
  python3 scripts/extract_tdr_pdf.py
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError as e:  # pragma: no cover
    print("Install pypdf: pip install pypdf", file=sys.stderr)
    raise SystemExit(1) from e


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    pdf = root / "incoming" / "tdr.pdf"
    out_dir = root / "docs" / "tor-gap" / "_extracted"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "tdr-extract.txt"

    if not pdf.is_file():
        print(f"Missing PDF: {pdf}", file=sys.stderr)
        raise SystemExit(2)

    reader = PdfReader(str(pdf))
    chunks: list[str] = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        chunks.append(f"\n--- PAGE {i + 1} ---\n{text}")
    out.write_text("".join(chunks), encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size} bytes, {len(reader.pages)} pages)")


if __name__ == "__main__":
    main()
