#!/usr/bin/env python3
"""
auto_summarize.py

Scan 01_INPUT/processed/ for .md/.txt/.pdf and create Research Notes in 03_WORK/drafts/ with:
- Summary
- TOC (if parseable)
- Highlights: important vs. irrelevant (heuristic)
- Recommendations/placement hints
- Guiding prompt scaffold (as provided)

Notes:
- PDF support here is minimal (text-extraction only if plain text; for complex PDFs, integrate a proper extractor).
- Non-destructive: source files remain in 01_INPUT/processed/.
- This is a simple heuristic summarizer; extend with model calls if desired.
"""
from pathlib import Path
import re
import hashlib
from datetime import datetime

BASE = Path("/Users/samimajeed/Documents/Obsidian - Main Vault")
PROCESSED = BASE / "01_INPUT/processed"
DRAFTS = BASE / "03_WORK/drafts"
DRAFTS.mkdir(parents=True, exist_ok=True)

GUIDING_PROMPT = """Metaphor of [ ] narrated in [ ] visualized by [geo elem] found in [myth art] and in [rituals] needing [material objects with shape + design]. How to draw [myth art]. Some of [myth+geo elem] appear in architecture/civic projects like [bridge]. Myth narrates visual semiotics metaphorically (Day A review) and functionally. [geo element] has [math properties]. When [transformation] → [scientific event]. Optional: combined with [prior discovery] → [process]. Review math/problem set; project."""

def hash_path(p: Path) -> str:
    return hashlib.md5(str(p).encode("utf-8")).hexdigest()[:8]

def summarize_text(text: str):
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    head = " ".join(lines[:5])
    summary = head[:500] + ("..." if len(head) > 500 else "")
    toc = []
    important = []
    irrelevant = []
    recs = []
    # Simple heuristics: detect headings (#) and key terms
    for ln in lines:
        if ln.startswith("#"):
            toc.append(ln.strip("# ").strip())
        if any(k in ln.lower() for k in ["myth", "ritual", "element", "geometry", "math", "innovation"]):
            important.append(ln)
        if any(k in ln.lower() for k in ["todo", "irrelevant", "skip"]):
            irrelevant.append(ln)
    if not important:
        important = lines[:3]
    if not toc:
        toc = [f"Section {i+1}" for i in range(min(5, len(lines)))]
    recs.append("Place myth/ritual/material culture content in Day A sections; function/system/physics in Day B.")
    recs.append("Attach candidate images from assets manifest to relevant sections.")
    return summary, toc, important[:5], irrelevant[:3], recs

def process_file(p: Path):
    if p.suffix.lower() not in {".md", ".txt"}:
        return False
    text = p.read_text(encoding="utf-8", errors="ignore")
    summary, toc, important, irrelevant, recs = summarize_text(text)
    out = DRAFTS / f"Research_{p.stem}_{hash_path(p)}.md"
    body = []
    body.append(f"# Research Note for {p.name}")
    body.append("")
    body.append("## Summary")
    body.append(summary)
    body.append("")
    body.append("## TOC")
    for t in toc:
        body.append(f"- {t}")
    body.append("")
    body.append("## Highlights: Important")
    for imp in important:
        body.append(f"- {imp}")
    body.append("")
    body.append("## Highlights: Irrelevant/To Skip")
    for irr in irrelevant:
        body.append(f"- {irr}")
    body.append("")
    body.append("## Recommendations / Placement")
    for r in recs:
        body.append(f"- {r}")
    body.append("")
    body.append("## Guiding Prompt")
    body.append(GUIDING_PROMPT)
    body.append("")
    body.append("## Notes")
    body.append("")
    out.write_text("\n".join(body), encoding="utf-8")
    return True

def main():
    processed = 0
    for p in PROCESSED.iterdir():
        if p.is_file():
            if process_file(p):
                processed += 1
    print(f"Created {processed} research notes in {DRAFTS}")

if __name__ == "__main__":
    main()
