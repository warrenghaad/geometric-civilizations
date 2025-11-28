# Curriculum Pipeline (Obsidian Main Vault)

This is a minimal, reproducible flow for turning raw research into structured lessons.

## Folders (aligned to steps)
- Input: `01_INPUT/unprocessed/` (drop raw files) → then move to `01_INPUT/processed/` after initial tagging/frontmatter
- Static DB: `02_DATABASE/` (reference/archival only; do not edit here)
- Work: `03_WORK/drafts/` for content-draft notes, `03_WORK/lessons/` for lesson-plan notes
- Templates/SSOTs: `03_PRODUCTION/Templates and SSOTs/`
- Output: `04_OUTPUT/` (finished lesson plans, exports; HTML in `04_OUTPUT/html_exports/`)
- Assets: `05_DELIVERABLES/assets_manifest/` (manifest), `05_DELIVERABLES/assets_by_tag/` (symlinks already built)

## Step 1 — Input
- Drop files into `01_INPUT/staging/`.
- For PDFs/PPTs, note the path in `attachments`.

## Step 2 — Tagging (frontmatter)
Add to each new note:
```yaml
---
title: [Working title]
document_type: content-draft
subject: 
grade_levels: [3]
element: TBD
scope: all-three
status: drafting      # drafting|ready|needs-images|needs-ritual|needs-function
key_points:
  - ""
  - ""
attachments:
  - ""
images:
  - id: ""
    desc: ""
    placement: ""
    why: ""
tags: [#content, #lesson/candidate]
---
```

## Step 3 — Sort drafts
- Use `03_PRODUCTION/Templates and SSOTs/lesson_pipeline_dashboard.md` (Dataview) to see drafts by status.
- Set `status: ready` when key_points and assets are set.

## Step 4 — Concept outline (in the draft)
- Expand key_points into Myth, Ritual/Objects, Technique, Hands-On, System/Function.

## Step 5 — Table (Week/Lesson map)
- Use a simple table to map Day A/B sections:
```markdown
| Week / Lesson / Day      | Section 1 | Section 2 | Section 3 | Section 4 | Section 5 | Section 6 | Section 7 | Section 8 |
|--------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| Week Thesis (overall)    |           |           |           |           |           |           |           |           |
| Lesson: [Title] — Day A  |           |           |           |           |           |           |           |           |
| Lesson: [Title] — Day B  |           |           |           |           |           |           |           |           |
```

## Step 6 — Lesson plans (use existing shells)
- For each lesson, use the `_DayA.md` and `_DayB.md` shells (or duplicate templates in `03_PRODUCTION/Templates and SSOTs/`):
  - Day A: Myth Retelling; Myth in Art; Material Culture (justify ritual+objects, freq/radius, embodied action; preface/end why it belongs); Technique; Practice; Hands-On; Wrap; Exit Ticket.
  - Day B: Bridge; Myth as organizing story; Design-in-Use (function + transformations + physics + adoption); Structural Decomposition; Practice; Hands-On Model/Test; Wrap; Exit Ticket.
- Update frontmatter: `document_type: lesson-plan`, fill element/grade_levels/scope/standards, set `status: ready`.

## Step 7 — Export (HTML)
- Convert finished lesson plans to HTML into `05_DELIVERABLES/html_exports/` (use your existing export script or pandoc/markdown lib).

## SSOT Checkpoint: eTextbook (Master)
- Use `03_PRODUCTION/Templates and SSOTs/eTextbook_Chapter_Master.md` as the SSOT structure.
- Compile Day A/B sections, labs, assessments, image manifest into the eTextbook chapter per element.
- Final output is the eTextbook chapter (master SSOT) from which all derivatives are made.

## Tools/Notes
- Asset manifest: already built at `05_DELIVERABLES/assets_manifest/asset_manifest.{json,csv}`; symlinks at `05_DELIVERABLES/assets_by_tag/`.
- Templates: `03_PRODUCTION/Templates and SSOTs/DayA_Lesson Table.md`, `DayB_Lesson Table.md`, `Element_Template.md`, etc.
- Dashboard: `03_PRODUCTION/Templates and SSOTs/lesson_pipeline_dashboard.md` (Dataview).
