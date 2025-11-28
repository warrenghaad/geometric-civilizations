#!/usr/bin/env python3
"""
Asset indexer: find curriculum-related images, build a manifest, and (optionally) organize symlinks by tag.

Usage (edit base dirs as needed):
  python3 asset_indexer.py \
    --base "/Users/samimajeed/Documents/Obsidian - Main Vault/05_DELIVERABLES/_archive_startover_2025-12-19_MD_Lessons" \
    --base "/Users/samimajeed/Documents" \
    --out "/Users/samimajeed/Documents/Obsidian - Main Vault/05_DELIVERABLES/assets_manifest" \
    --symlinks "/Users/samimajeed/Documents/Obsidian - Main Vault/05_DELIVERABLES/assets_by_tag"

Defaults (if no args): scans current working directory.
Safe: read-only unless --symlinks is provided (creates symlinks, no moves).
"""

import argparse
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path
from datetime import datetime

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".gif", ".bmp", ".webp"}

# Tokens that indicate curriculum relevance. Expand as needed.
KEYWORDS = {
    "g1", "g2", "g3", "g4", "g5",
    "lesson", "unit", "module",
    "circle", "triangle", "square", "spiral", "radial", "polygon", "grid", "fractal",
    "shamash", "ishtar", "sin", "nanna", "enlil", "enki", "axis", "ziggurat", "pyramid",
    "arch", "seal", "cylinder", "star", "rosette", "meander", "tessellation",
    "mesopotamia", "babylon", "assyria", "sumer", "egypt", "maya", "rome", "greece",
    "math", "geometry", "pattern", "design", "artifact", "artifacts",
}

def hash_path(p: Path) -> str:
    return hashlib.md5(str(p).encode("utf-8")).hexdigest()[:8]

def infer_tags(name: str) -> list:
    base = name.lower()
    tags = set()
    for kw in KEYWORDS:
        if kw in base:
            tags.add(kw)
    return sorted(tags)

def is_relevant(path: Path) -> bool:
    # Relevant if keyword appears in any part of the path
    tokens = re.split(r"[\\/_\\-\\s]+", path.as_posix().lower())
    return any(kw in tokens or kw in path.name.lower() for kw in KEYWORDS)

def scan(base_dirs, out_dir, symlink_dir=None):
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for base in base_dirs:
        base_path = Path(base).expanduser().resolve()
        if not base_path.exists():
            continue
        for p in base_path.rglob("*"):
            if not p.is_file():
                continue
            if p.suffix.lower() not in IMAGE_EXT:
                continue
            if not is_relevant(p):
                continue  # skip non-curriculum images
            tags = infer_tags(p.name)
            entry = {
                "id": f"{p.stem}_{hash_path(p)}",
                "filename": p.name,
                "path": str(p),
                "tags": tags,
                "size_bytes": p.stat().st_size,
                "modified": datetime.fromtimestamp(p.stat().st_mtime).isoformat(),
            }
            manifest.append(entry)
            if symlink_dir:
                for t in tags or ["uncategorized"]:
                    dest_dir = Path(symlink_dir) / t
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest = dest_dir / p.name
                    if dest.exists():
                        if dest.is_symlink() and dest.resolve() == p.resolve():
                            continue
                        dest = dest_dir / f"{p.stem}_{hash_path(p)}{p.suffix}"
                    try:
                        dest.symlink_to(p)
                    except FileExistsError:
                        pass
    # Write manifest
    json_path = out_dir / "asset_manifest.json"
    csv_path = out_dir / "asset_manifest.csv"
    with json_path.open("w", encoding="utf-8") as jf:
        json.dump(manifest, jf, indent=2)
    with csv_path.open("w", encoding="utf-8", newline="") as cf:
        writer = csv.DictWriter(cf, fieldnames=list(manifest[0].keys()) if manifest else [])
        if manifest:
            writer.writeheader()
            writer.writerows(manifest)
    # Summary
    summary = [
        f"Total images indexed: {len(manifest)}",
        f"Output: {json_path}",
        f"CSV: {csv_path}",
    ]
    if symlink_dir:
        summary.append(f"Symlinks: {symlink_dir}")
    (out_dir / "asset_index_summary.txt").write_text("\n".join(summary), encoding="utf-8")
    return manifest

def main():
    parser = argparse.ArgumentParser(description="Index curriculum-related images and build a manifest.")
    parser.add_argument("--base", action="append", help="Base directory to scan (can be used multiple times).", required=False)
    parser.add_argument("--out", help="Output directory for manifest files.", required=False)
    parser.add_argument("--symlinks", help="Optional directory to create symlinks organized by tag.", required=False)
    args = parser.parse_args()

    base_dirs = args.base or ["."]
    out_dir = Path(args.out or "./asset_manifest").expanduser().resolve()
    symlink_dir = Path(args.symlinks).expanduser().resolve() if args.symlinks else None

    manifest = scan(base_dirs, out_dir, symlink_dir)
    print(f"Indexed {len(manifest)} images.")

if __name__ == "__main__":
    main()
