#!/usr/bin/env python3
"""
replace_safe.py

Safely replace a file in 02_DATABASE with a vetted copy from 03_WORK, creating a backup.

Usage:
  python3 replace_safe.py --src "/path/to/03_WORK/..." --dst "/Users/samimajeed/Documents/Obsidian - Main Vault/02_DATABASE/..."

Behavior:
- Copies src to dst after creating a timestamped backup of dst (if it exists) under 02_DATABASE/_backup/YYYYMMDD_HHMMSS/.
- Will refuse to run if dst is not under 02_DATABASE.
- Prints actions; does not delete any source.
"""
import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path

VAULT = Path("/Users/samimajeed/Documents/Obsidian - Main Vault")
DB_ROOT = VAULT / "02_DATABASE"

def main():
    parser = argparse.ArgumentParser(description="Safely replace a DB file with a vetted work copy.")
    parser.add_argument("--src", required=True, help="Source file (e.g., under 03_WORK).")
    parser.add_argument("--dst", required=True, help="Destination in 02_DATABASE to replace.")
    args = parser.parse_args()

    src = Path(args.src).expanduser().resolve()
    dst = Path(args.dst).expanduser().resolve()

    if DB_ROOT not in dst.parents:
        print("Refusing: destination must be under 02_DATABASE.")
        sys.exit(1)
    if not src.exists():
        print(f"Source does not exist: {src}")
        sys.exit(1)
    if not dst.parent.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)

    # Backup if dst exists
    if dst.exists():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = DB_ROOT / "_backup" / ts
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_dst = backup_dir / dst.name
        shutil.copy2(dst, backup_dst)
        print(f"Backed up {dst} -> {backup_dst}")

    shutil.copy2(src, dst)
    print(f"Replaced {dst} with {src}")

if __name__ == "__main__":
    main()
