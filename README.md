# Geometric Civilizations Curriculum
## Quarter 2 Pilot: Grades 3–5 Integrated Geometry–Myth–Art Curriculum

**54 lessons total** | 18 per grade | Single-source-of-truth architecture

---

## 📚 Overview

This project implements a comprehensive interdisciplinary curriculum that integrates:
- **Mathematics** (place value, fractions, ratios, measurement)
- **Geometry** (circles, tessellations, symmetry, star polygons)
- **Mythology** (cross-cultural creation stories and symbolism)
- **Art** (pattern-making, construction, cultural artifacts)

### Pedagogical Framework

**Line → Square → Cube → Tesseract**

- Rejects rigid developmental stages as prescriptive
- Treats complexity as **additive and networked**, not hierarchical
- Exposure to abstraction *creates* abstract thinkers

---

## 🏗️ Architecture

### Single Source of Truth (SSOT)

```
curriculum_master.csv          ← High-level curriculum map
        ↓
generate_curriculum.py         ← Generates 54 lesson JSONs
        ↓
lessons/G*.json               ← Detailed lesson specifications
        ↓
    ┌───┴──────┬──────────┬──────────┐
    ↓          ↓          ↓          ↓
overlays   images   etextbook   slides/videos
```

All content derives from lesson JSON files—**never edit generated files directly**.

---

## 📁 Project Structure

```
geometric-civilizations/
├── curriculum_master.csv           # Master curriculum map (54 lessons)
├── build_all.sh                    # Main build script
│
├── schemas/
│   ├── design_system.json          # Typography, colors, layouts
│   └── lesson_schema.json          # Lesson structure definition
│
├── lessons/
│   ├── G3-01.json                  # Grade 3, Lesson 1 (SSOT)
│   ├── G3-02.json
│   ├── ...
│   └── G5-18.json
│
├── scripts/
│   ├── generate_curriculum.py      # Generate lesson JSONs from CSV
│   ├── overlay_generator.py        # Create SVG geometric overlays
│   ├── image_sourcer.py            # Fetch images from Met API / Wikimedia
│   └── etextbook_generator.py      # Build interactive HTML textbook
│
├── assets/
│   ├── artifacts/                  # Cultural artifact images
│   ├── overlays/                   # SVG geometric overlays
│   ├── characters/                 # Character illustrations
│   ├── diagrams/                   # Bridge diagrams
│   └── worksheets/                 # PDF worksheets
│
├── output/
│   ├── slides/                     # PowerPoint slides
│   └── videos/                     # Lesson videos
│
├── etextbook/
│   └── index.html                  # Interactive e-textbook
│
└── docs/
    └── video_workflow.md           # Video generation guide
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Ensure Python 3.8+ is installed
python3 --version

# Run the build script (creates venv and installs packages)
./build_all.sh
```

### 2. Generate Curriculum

```bash
# Generate 54 lesson JSONs + e-textbook
./build_all.sh

# Generate with placeholder images
./build_all.sh --placeholders

# Source real images from museums (slow, requires internet)
./build_all.sh --images
```

### 3. View E-Textbook

```bash
# Open in your browser
open etextbook/index.html
```

---

## 🛠️ Build Options

### Full Build

```bash
./build_all.sh --images --slides --videos
```

### Individual Lesson

```bash
./build_all.sh --lesson G3-01
```

### Development Mode (fast iteration)

```bash
# Generate curriculum + e-textbook only (no images/videos)
./build_all.sh
```

---

## 📖 Lesson Structure

Each lesson JSON contains:

```json
{
  "lessonId": "G3-1",
  "metadata": { "grade": 3, "weekNumber": 1, ... },
  "sel": { "prompt": "...", "duration": 5, ... },
  "hook": { "character": {...}, "narrative": "...", ... },
  "myth": { "title": "...", "scenes": [...], ... },
  "artifacts": [
    {
      "artifactId": "artifact-01",
      "title": "Newgrange Triple Spiral",
      "imageUrl": "assets/artifacts/...",
      "overlays": [
        {
          "overlayId": "overlay-01",
          "type": "circles",
          "elements": [
            { "shape": "circle", "coordinates": {...}, "label": "..." }
          ]
        }
      ],
      "metadata": { "source": "Wikimedia", "license": "CC0 1.0", ... }
    }
  ],
  "mathActivity": {...},
  "artActivity": {...},
  "geometryActivity": {...},
  "bridge": {...},
  "exit": {...},
  "assessments": {...},
  "extensions": {...},
  "teacherNotes": {...}
}
```

See `schemas/lesson_schema.json` for complete specification.

---

## 🎨 Design System

All visual specs are defined in `schemas/design_system.json`:

- **Typography**: Font families, sizes (grade-specific)
- **Colors**: Palettes for each grade + civilization colors
- **Layouts**: Slide layouts (title, SEL, hook, myth, artifact, activity, bridge, exit)
- **Overlays**: SVG styling for geometric annotations
- **Video**: Transition specs, narration timing, pan/zoom settings

### Grade-Specific Palettes

- **Grade 3**: Vibrant Wonder (high contrast, engaging)
- **Grade 4**: Scholarly Discovery (balanced, precise)
- **Grade 5**: Mature Inquiry (sophisticated, parametric)

---

## 🖼️ Image Sourcing

### Automatic Sourcing

```bash
# Fetch from Met Museum API and Wikimedia Commons
./build_all.sh --images
```

### Manual Curation

1. Edit `lessons/G3-01.json`
2. Update `artifacts[].imageUrl` with your image path
3. Add metadata: `source`, `museum`, `accessionNumber`, `license`

### Supported Sources

- **Met Museum**: Open Access API (CC0 1.0)
- **Wikimedia Commons**: High-resolution images (various licenses)
- **Custom uploads**: Place in `assets/artifacts/`

---

## 🎥 Video Generation

### Workflow

```
Lesson JSON
    ↓
PowerPoint slides (python-pptx)
    ↓
Export to PNG (LibreOffice headless)
    ↓
Composite SVG overlays
    ↓
Generate narration (OpenAI TTS)
    ↓
Assemble video (FFmpeg)
```

### Implementation Status

- [x] Lesson JSON structure
- [x] Overlay SVG generation
- [x] Image sourcing pipeline
- [ ] PowerPoint generation (see `docs/video_workflow.md`)
- [ ] Slide export automation
- [ ] Narration TTS
- [ ] Video assembly

**See `docs/video_workflow.md` for detailed implementation guide.**

---

## 📝 Curriculum Map

### Grade 3 (18 lessons)

| Week | Math Concept | Geometric Concept | Civilization | Artifacts |
|------|--------------|-------------------|--------------|-----------|
| 1 | Place value, compare/order | Circle partitions | Prehistoric | Newgrange triple spiral, Chauvet handprints |
| 1 | Rounding | Nearest ring/sector | Egypt | Karnak lotus capitals |
| 2 | Multiplication arrays | Tessellation tiles | Greece | Amphora meander borders |
| 2 | Division/fair shares | Radial equal shares | Mesopotamia | Rosette cylinder seals |
| ... | ... | ... | ... | ... |

### Grade 4 (18 lessons)

| Week | Math Concept | Geometric Concept | Civilization | Artifacts |
|------|--------------|-------------------|--------------|-----------|
| 1 | Place value (millions) | Coordinate grids | Egypt | Temple axes, gridded figures |
| 1 | Compare/order | Symmetry ranking | Greece | Greek architectural orders |
| 2 | Model fractions/decimals | Sector partitions | Byzantine | Cross-in-square, rose windows |
| ... | ... | ... | ... | ... |

### Grade 5 (18 lessons)

| Week | Math Concept | Geometric Concept | Civilization | Artifacts |
|------|--------------|-------------------|--------------|-----------|
| 1 | Ratios | r:d and ring ratios | Mesopotamia | Shamash disks |
| 1 | Equivalent ratios (tables) | Tessellation repeats | Islamic | Zellige 8/10-point modules |
| 2 | Graphs of equivalent ratios | Star polygons {n/k} | Islamic | Topkapi scroll constructions |
| ... | ... | ... | ... | ... |

**See `curriculum_master.csv` for complete map.**

---

## 🧩 Extending the Curriculum

### Add a New Lesson

1. Edit `curriculum_master.csv`
2. Add a row with lesson details
3. Run `./build_all.sh`
4. Manually enrich generated JSON in `lessons/`
5. Add artifact images to `assets/artifacts/`

### Customize a Lesson

1. Edit `lessons/G3-01.json` directly
2. Update myth scenes, artifact overlays, activities
3. Regenerate e-textbook: `python3 scripts/etextbook_generator.py`

### Add Overlay Types

1. Edit `schemas/design_system.json` → `overlayStyles`
2. Add new geometric annotation styles
3. Update `scripts/overlay_generator.py` with new shape handlers

---

## 📊 Standards Alignment

### Common Core State Standards (CCSS)

- **Grade 3**: 3.NBT, 3.MD, 3.G
- **Grade 4**: 4.NBT, 4.NF, 4.MD, 4.G
- **Grade 5**: 5.NF, 5.MD, 5.G

### National Core Arts Standards (NCAS)

- **Creating**: VA:Cr2.1, VA:Cr2.3
- **Presenting**: VA:Pr4.1
- **Responding**: VA:Re7.2, VA:Re8.1
- **Connecting**: VA:Cn10.1, VA:Cn11.1

---

## 🤝 Contributing

### Reporting Issues

- Lesson content errors → Edit `lessons/G*.json`
- Design system updates → Edit `schemas/design_system.json`
- Curriculum map changes → Edit `curriculum_master.csv`

### Pull Request Workflow

1. Make changes to SSOT files (`curriculum_master.csv`, `lessons/*.json`, `schemas/*.json`)
2. Regenerate outputs: `./build_all.sh`
3. Commit changes to version control
4. Submit PR with clear description

---

## 📜 License

### Curriculum Content

- Original lesson plans, activities, and teacher notes: **CC BY-SA 4.0**

### Cultural Artifacts

- Met Museum images: **CC0 1.0** (Public Domain)
- Wikimedia Commons images: Various (see individual image metadata)
- Always check `artifacts[].metadata.license` in lesson JSON

### Code

- Build scripts, generators, and automation: **MIT License**

---

## 🔗 Resources

- **Met Museum API**: https://metmuseum.github.io/
- **Wikimedia Commons**: https://commons.wikimedia.org/
- **Common Core Standards**: http://www.corestandards.org/
- **NCAS**: https://www.nationalartsstandards.org/

---

## 📞 Contact

For questions, feedback, or collaboration:

- **Email**: [your-email@example.com]
- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)

---

## 🙏 Acknowledgments

- Museum partners: Metropolitan Museum of Art, British Museum, Louvre
- Cultural consultants for accurate representation of civilizations
- Educators who piloted and refined the curriculum

---

**Built with ❤️ for educators who believe students deserve rich, interconnected knowledge**
