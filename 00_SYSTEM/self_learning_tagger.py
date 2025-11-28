#!/usr/bin/env python3
"""
self_learning_tagger.py
Context-aware tagging with simple co-occurrence learning.

What it does (non-destructive):
- Scans text files in 01_INPUT/processed and 02_WORK/drafts.
- Uses vocab lists (elements, deities, motifs, media, etc.) from vocab_egypt.json (extend as needed).
- Finds known tokens; collects nearby unknown tokens; counts co-occurrence.
- Suggests new candidate terms when they co-occur often enough.
- Writes a report to 00_SYSTEM/learning_state.json and learning_report.json.
- Does NOT modify your notes.

How to run:
  python3 self_learning_tagger.py

You can extend vocab_egypt.json or add more vocab files and tweak thresholds below.
"""

import json
import re
from pathlib import Path
from collections import defaultdict, Counter

BASE = Path("/Users/samimajeed/Documents/Obsidian - Main Vault")
INPUT_PROCESSED = BASE / "01_INPUT/processed"
DRAFTS = BASE / "02_WORK/drafts"
VOCAB_FILES = [
    BASE / "00_SYSTEM/vocab_egypt.json",
    BASE / "00_SYSTEM/vocab_mesopotamia.json"
]
STATE_FILE = BASE / "00_SYSTEM/learning_state.json"
REPORT_FILE = BASE / "00_SYSTEM/learning_report.json"

# Settings
WINDOW_SIZE = 5          # words around known tokens to inspect
SUGGEST_THRESHOLD = 3    # occurrences to suggest a new candidate term

def load_vocab():
    keys = [
        "elements",
        "deities",
        "motifs",
        "media",
        "myth_terms",
        "ritual_terms",
        "languages",
        "math_terms",
        "social_status",
        "design_terms",
        "ritual_objects",
        "verbs",
        "fashion_textiles",
        "agriculture",
        "inventions",
        "time_periods",
        "hairstyles",
        "colors",
        "famous_artworks",
        "science_discoveries",
        "phrases"
    ]
    vocab = {k: [] for k in keys}
    for vf in VOCAB_FILES:
        if vf.exists():
            data = json.loads(vf.read_text(encoding="utf-8"))
            for k in keys:
                vocab[k].extend([w.lower() for w in data.get(k, [])])
    # dedupe
    for k in vocab:
        vocab[k] = sorted(set(vocab[k]))
    return vocab

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"cooccurrence": {}, "suggested": {}}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

def tokenize(text):
    return re.findall(r"[a-zA-Z'][a-zA-Z']+", text.lower())

def process_text(text, vocab_sets, co_counts):
    tokens = tokenize(text)
    known_positions = []
    for i, tok in enumerate(tokens):
        for cat, words in vocab_sets.items():
            if tok in words:
                known_positions.append((i, cat, tok))
                break
    for pos, cat, tok in known_positions:
        start = max(0, pos - WINDOW_SIZE)
        end = min(len(tokens), pos + WINDOW_SIZE + 1)
        for j in range(start, end):
            if j == pos:
                continue
            cand = tokens[j]
            if len(cand) < 4:
                continue
            # skip if already known
            if any(cand in words for words in vocab_sets.values()):
                continue
            co_counts[cat][cand] += 1

def scan_files(vocab):
    vocab_sets = {k: set(v) for k, v in vocab.items()}
    co_counts = {k: Counter() for k in vocab_sets}
    for folder in [INPUT_PROCESSED, DRAFTS]:
        if not folder.exists():
            continue
        for p in folder.rglob("*.md"):
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            process_text(text, vocab_sets, co_counts)
    return co_counts

def build_report(co_counts, state, vocab):
    suggestions = defaultdict(list)
    for cat, counter in co_counts.items():
        for term, count in counter.most_common():
            if count >= SUGGEST_THRESHOLD:
                if term not in vocab[cat]:
                    suggestions[cat].append({"term": term, "count": count})
    state["cooccurrence"] = {k: dict(v) for k, v in co_counts.items()}
    state["suggested"] = suggestions
    save_state(state)
    REPORT_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return suggestions

def main():
    vocab = load_vocab()
    state = load_state()
    co_counts = scan_files(vocab)
    suggestions = build_report(co_counts, state, vocab)
    print("Context tagging complete.")
    for cat, items in suggestions.items():
        if items:
            top = ", ".join([f"{d['term']}({d['count']})" for d in items[:5]])
            print(f"Suggested new {cat}: {top}")

if __name__ == "__main__":
    main()
