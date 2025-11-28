# Messy System → Clean Pipeline (Hand-off Guide)

Use this to triage messy content into the new pipeline so another CLI can take over smoothly.

## Folder map (clean system)
- Input: `01_INPUT/unprocessed/` → `01_INPUT/processed/` (raw files, then tagged)
- Static DB: `02_DATABASE/` (reference/archival only; do not edit)
- Work: `03_WORK/drafts/` (content-draft), `03_WORK/etextbook_sections/` (structured sections for the eTextbook; use Day A/B shells as section scaffolds, but not “lessons”)
- Templates/SSOTs: `03_PRODUCTION/Templates and SSOTs/`
- Output: `04_OUTPUT/` (exports; HTML in `04_OUTPUT/html_exports/`)
- Assets: `05_DELIVERABLES/assets_manifest/` (manifest) and `assets_by_tag/` (symlinks)

## Triage steps
1) Drop any messy MD/txt/pdf/ppt into `01_INPUT/unprocessed/`.
2) Run auto-tag to add frontmatter and move to drafts:
   ```bash
   python3 "/Users/samimajeed/Documents/Obsidian - Main Vault/00_SYSTEM/auto_tag.py"
   ```
   - This writes frontmatter and moves files to `03_WORK/drafts/`.
3) (Optional) Run the self-learning tagger to suggest new terms:
   ```bash
   python3 "/Users/samimajeed/Documents/Obsidian - Main Vault/00_SYSTEM/self_learning_tagger.py"
   ```
   - Reports are in `00_SYSTEM/learning_state.json` and `learning_report.json`. Non-destructive.
4) Link images using the asset manifest:
   - Manifest: `05_DELIVERABLES/assets_manifest/asset_manifest.json`
   - Symlinks by tag: `05_DELIVERABLES/assets_by_tag/`
   - Add `images:` entries to frontmatter as needed (id/desc/placement/why).
5) Promote drafts into eTextbook sections:
- Copy content into Day A/B section shells from `03_PRODUCTION/Templates and SSOTs/` (store structured sections in `03_WORK/etextbook_sections/`).
- Update frontmatter: `document_type: etextbook-section`, fill element/grades/scope/standards, set `status: ready`.
6) Export:
- Compile eTextbook sections to HTML into `04_OUTPUT/html_exports/` (pandoc or Python markdown converter).

## Status check
- Use `03_PRODUCTION/Templates and SSOTs/lesson_pipeline_dashboard.md` (Dataview) to see draft/section statuses.
- Frontmatter keys expected: `document_type`, `subject`, `grade_levels`, `element`, `scope`, `status`, `key_points`, `attachments`, `images`.

## Scripts
- Auto-tag: `00_SYSTEM/auto_tag.py` (md/txt only; uses vocab from `00_SYSTEM/vocab_*.json`)
- Self-learning suggestions: `00_SYSTEM/self_learning_tagger.py`
- Asset indexer (already run): `05_DELIVERABLES/assets_manifest/` + `assets_by_tag/`

## Notes
- Keep `02_DATABASE` static (reference only).
- Active editing happens in `03_WORK/*`.
- If new vocab is needed (e.g., new deities/elements), add to `00_SYSTEM/vocab_*.json` and re-run the self-learning tagger.
