# Copilot Instructions for Geometric Civilizations

## Repository Overview

**Geometric Civilizations** is an educational curriculum project that teaches geometry concepts for **Grades 3–5** through the lens of ancient Mesopotamian civilization. It covers a **96-lesson curriculum** spanning Grades 3–5 (32 lessons per grade) with two interwoven tracks:

1. **Mesopotamian Geometric Civilization Studies** (48 lessons) — Geometry through ancient Mesopotamian culture, artifacts, deities, and architecture.
2. **Comprehensive Math Curriculum** (48 lessons) — Standards-aligned mathematics covering place value, operations, fractions, measurement, geometry, and data.

The project generates **PowerPoint presentations**, **e-textbooks**, and **interactive HTML** content. Assets are sourced from major museum APIs (British Museum, Metropolitan Museum, Louvre, etc.).

---

## Repository Structure

```
/                                          # Root directory
├── .github/
│   └── copilot-instructions.md            # This file
├── CURRICULUM_SYSTEM_ORGANIZED/
│   ├── 01_ETEXTBOOK_PIPELINE/             # E-textbook generation pipeline scripts
│   └── 02_VISUAL_ASSETS_PIPELINE/         # Visual asset download/processing scripts
├── Geometric Civilizations - Interactive Home Page (1).html  # Interactive HTML home page
├── MESOPOTAMIAN_CURRICULUM_MAPPING_FOR_PERPLEXITY.md         # Curriculum research guide for image sourcing
├── script_cross_reference.py              # Python pipeline orchestrator
└── shell_script_manager.sh               # Bash script manager
```

**Key source files:**
- `script_cross_reference.py` — Defines the full Python script dependency graph and execution order for the curriculum pipeline. Run with `python3 script_cross_reference.py validate|run-all|run <script>`.
- `shell_script_manager.sh` — Manages Bash lesson setup scripts (`setup-G3-Lesson-*.sh`, `setup-G4-Lesson-*.sh`). Run with `bash shell_script_manager.sh status|validate|run-all|run <script>|create-missing|complete-system`.
- `CURRICULUM_SYSTEM_ORGANIZED/01_ETEXTBOOK_PIPELINE/` — Intended to contain Python scripts for converting PowerPoints to e-textbooks.
- `CURRICULUM_SYSTEM_ORGANIZED/02_VISUAL_ASSETS_PIPELINE/` — Intended to contain scripts for downloading and inserting images.

---

## Languages & Technologies

- **Python 3** — Primary scripting language for curriculum building, image downloading, PowerPoint generation, and e-textbook conversion.
- **Bash** — Lesson setup scripts and system orchestration.
- **HTML/CSS/JavaScript** — Interactive home page.
- **PowerPoint (`.pptx`)** — Generated output format for lessons (via `python-pptx`).
- **JSON** — Lesson data source format (used by `build_all.py` and related scripts).

---

## Build & Validation

### Python Environment

There is no `requirements.txt` or `setup.py` checked in. Key Python dependencies used across scripts include:
- `python-pptx` — PowerPoint generation
- `requests` — Image downloading from museum APIs
- `Pillow` — Image processing
- `firebase-admin` — Firebase museum database uploads (optional)

Set up a virtual environment before running scripts:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install python-pptx requests Pillow
```

### Validate Script References

```bash
python3 script_cross_reference.py validate
```

This checks that all Python scripts referenced in the dependency map exist on disk. Most referenced scripts are **not yet created** — they represent the intended pipeline architecture.

### Run Shell Script Status Check

```bash
bash shell_script_manager.sh status
```

This shows which lesson setup shell scripts (`setup-G3-Lesson-*.sh`, etc.) exist on disk.

### Create Missing Lesson Scripts

```bash
bash shell_script_manager.sh create-missing
```

This generates missing Grade 3 and Grade 4 lesson setup scripts from the Grade 3 Lesson A template.

### Run Complete System

```bash
bash shell_script_manager.sh complete-system
```

This runs validation, then all shell scripts, then the Python pipeline.

---

## Curriculum Architecture

- **Lesson naming**: `G3-Lesson-A` through `G3-Lesson-H` (Grade 3), `G4-Lesson-A` through `G4-Lesson-H` (Grade 4), similarly for Grade 5. Each letter (A–H) corresponds to one math or Mesopotamian topic; only 8 of the planned 32 per grade are scaffolded in the existing shell scripts. The remaining lessons will follow the same `setup-G{grade}-Lesson-{letter}.sh` pattern as additional scripts are created.
- **Setup scripts**: `setup-G{grade}-Lesson-{letter}.sh` create the directory and file structure for each lesson.
- **Build scripts**: Python `build_all.py` (not yet created) reads JSON lesson data and generates PowerPoint files.
- **Image pipeline**: Downloads images from museum APIs (British Museum, Met, Louvre) and inserts them into slide decks.
- **E-textbook pipeline**: `ppt_to_etextbook_converter.py` (not yet created) converts PowerPoints to HTML/web format.

---

## Important Notes

- Many Python scripts referenced in `script_cross_reference.py` and `shell_script_manager.sh` **do not yet exist**. They define the intended pipeline; actual script files need to be created.
- The `.DS_Store` files in `CURRICULUM_SYSTEM_ORGANIZED/` are macOS artifacts and should be ignored.
- There are **no automated tests or CI pipelines** in this repository.
- When creating new lesson scripts, follow the naming convention `setup-G{grade}-Lesson-{letter}.sh` and place them in the repository root.
- Always use `#!/usr/bin/env bash` and `set -euo pipefail` in new shell scripts.
- Always use `#!/usr/bin/env python3` in new Python scripts.
