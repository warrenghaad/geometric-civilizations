#!/usr/bin/env python3
"""
auto_tag.py - Context-aware tagging pass.
Scans 01_INPUT/unprocessed/, infers metadata from filenames and content, writes frontmatter, moves to 02_WORK/drafts/.
Uses keywords and simple sentence/context checks; you can extend keyword lists as needed.
"""
import re
import shutil
from pathlib import Path
from datetime import datetime

BASE = Path("/Users/samimajeed/Documents/Obsidian - Main Vault")
UNPROCESSED = BASE / "01_INPUT/unprocessed"
DRAFTS = BASE / "03_WORK/drafts"
DRAFTS.mkdir(parents=True, exist_ok=True)

# Keywords map to elements/subjects/scopes; extend as needed.
ELEMENT_MAP = {
    "circle": "circle", "triangle": "triangle", "square": "square",
    "spiral": "spiral", "radial": "radial", "polygon": "polygon",
    "grid": "grid", "fractal": "fractal", "hexagon": "hexagon", "hex": "hexagon",
    "star": "star8", "rosette": "star8", "arch": "arch", "ziggurat": "ziggurat",
    "pyramid": "pyramid", "seal": "frieze", "frieze": "frieze", "tessellation": "tessellation",
}
SUBJECT_MAP = {
    "math": "Math", "geometry": "Math", "pattern": "Math",
    "myth": "Myth", "ritual": "Myth", "story": "Myth",
    "art": "Art", "design": "Art", "artifact": "History", "history": "History",
}
SCOPE_MAP = {
    "myth": "ontology-myth-and-art",
    "ritual": "ontology-material-culture",
    "material": "ontology-material-culture",
    "tech": "ontology-innovation",
    "physics": "ontology-innovation",
    "system": "ontology-innovation",
}

GRADE_HINTS = {
    "g3": "3", "g4": "4", "g5": "5", "grade3": "3", "grade4": "4", "grade5": "5"
}

def infer_from_text(text: str, fname: str):
    blob = (fname + " " + text[:2000]).lower()
    element = None
    for k, v in ELEMENT_MAP.items():
        if k in blob:
            element = v
            break
    subject = None
    for k, v in SUBJECT_MAP.items():
        if k in blob:
            subject = v
            break
    scope = None
    for k, v in SCOPE_MAP.items():
        if k in blob:
            scope = v
            break
    grades = []
    for k, v in GRADE_HINTS.items():
        if k in blob:
            grades.append(v)
    grades = sorted(set(grades)) or []
    return element, subject, scope, grades

def build_frontmatter(title, element, subject, scope, grades):
    fm = []
    fm.append("---")
    fm.append(f"title: {title}")
    fm.append("document_type: content-draft")
    fm.append(f"subject: {subject or ''}")
    fm.append(f"grade_levels: [{', '.join(grades) if grades else '3'}]")
    fm.append(f"element: {element or 'TBD'}")
    fm.append(f"scope: {scope or 'all-three'}")
    fm.append("status: drafting")
    fm.append("key_points:")
    fm.append("  - \"\"")
    fm.append("  - \"\"")
    fm.append("attachments:")
    fm.append("  - \"\"")
    fm.append("images:")
    fm.append("  - id: \"\"")
    fm.append("    desc: \"\"")
    fm.append("    placement: \"\"")
    fm.append("    why: \"\"")
    fm.append("tags: [#content, #lesson/candidate]")
    fm.append("---\n")
    return "\n".join(fm)

def process_file(path: Path):
    if path.suffix.lower() not in {".md", ".txt"}:
        return False
    text = path.read_text(encoding="utf-8", errors="ignore")
    element, subject, scope, grades = infer_from_text(text, path.name)
    fm = build_frontmatter(path.stem.replace("_", " "), element, subject, scope, grades)
    new_text = fm + text
    out = DRAFTS / path.name
    out.write_text(new_text, encoding="utf-8")
    path.unlink()
    return True

def main():
    processed = 0
    for p in UNPROCESSED.iterdir():
        if p.is_file():
            if process_file(p):
                processed += 1
    print(f"Processed {processed} files from unprocessed → drafts")

if __name__ == "__main__":
    main()
