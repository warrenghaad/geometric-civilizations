---
note_type: howto
title: Smart Connections Setup (Annotations + Lessons)
tags: [smart-connections, howto, automation]
---

# Smart Connections Setup (Annotations → Table → Lessons)

Wire Claude JSON → lesson table (CSV) → lesson notes in one action.

## Prerequisites
- Obsidian Smart Connections plugin installed/enabled.
- Python 3 available.
- Vault root: `/Users/samimajeed/Documents/Obsidian - Main Vault`

## Script in use
- `scripts/ingest_annotation.py` (ingests JSON, updates CSV, writes note)
- CSV: `00_SYSTEM/lesson_table.csv`
- Output notes: `00_SYSTEM/Annotations/`

## Action 1: Ingest Claude JSON (selection → stdin)
Use when Claude JSON is in the clipboard/selection.

**Command:**  
`python3 "{{vault}}/scripts/ingest_annotation.py"`

In Smart Connections, set “pass selection as stdin” if available. Otherwise, use Action 2 with a saved file.

## Action 2: Ingest Claude JSON file
Use when you saved Claude output to a file.

**Command:**  
`python3 "{{vault}}/scripts/ingest_annotation.py" --json "{{file_path}}"`

Run this on a selected JSON file in Obsidian’s file explorer.

## Expected Claude JSON keys
`week, lesson_code, civ, subject, grade_band, status, lesson_title, geo_elements (list), dimension_mapping, objectives (list), standards (list), materials (list), image_refs (list), day_a_activities (list), day_b_activities (list)`

Tell Claude: “Return JSON only with those keys.”

## What happens
- Updates/creates a row in `00_SYSTEM/lesson_table.csv` (keyed by week + lesson_code).
- Writes/updates a lesson note in `00_SYSTEM/Annotations/` with frontmatter + Day A/B activities.
- Dataview tables pointed at `00_SYSTEM/Annotations` will show the note immediately.

## Quick Dataview to verify
```dataview
TABLE week, lesson_code, civ, subject, grade_band, status
FROM "01_INPUT/AI_Outputs_Raw"
SORT file.mtime DESC
LIMIT 200
```

## Optional gap checks
See `IMAGE_TAG_GAPS.md` (adjusted to `01_INPUT/AI_Outputs_Raw`).
