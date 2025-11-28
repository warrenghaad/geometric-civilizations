---
note_type: ontology-archive
tags: [archive, ontology, tagging-system, metadata-structure, magic-framework]
---

# MAGIC Ontology & Metadata System (Consolidated)

This is the archived copy of the consolidated ontology (canonical tags/synonyms/grade-status + directions/templates). Current/operable files were removed from the main tree per request.

## Canonical Tags (enforced)
- **MAGIC domains**: `math-domain`, `aesthetics-domain`, `geometric-element-domain`, `ideology-domain`, `comptroller-domain`
- **Stages**: `ontology-stage-1`, `ontology-stage-2`, `ontology-stage-3`
- **Semiotics**: `visual-semiotics`, `semiotic-sign`, `semiotic-system`
- **Day A (Embodied Aesthetics / Material)**: `day-a`, `myth`, `mythic-art`, `material-objects`, `cylinder-seals`, `textiles`, `pottery`, `architecture`, `tools`, `ornaments`, `ritual-ceremonial`, `ritual-everyday`, `embodied-cognition`, `artistic-decomposition`
- **Day B (Disembodied Systems / Innovation)**: `day-b`, `mathematics`, `engineering`, `architecture`, `technology`, `design-thinking`, `innovation`, `historical-causation`, `mathematical-decomposition`
- **Bridge**: `architecture-bridge`, `form-and-function`, `aesthetics-math-bridge`
- **Lesson components**: `hands-on-activity`, `sel-integration`, `archetype-role`, `transformation-verb`
- **Status**: `draft`, `reviewed`, `ready`, `approved`, `taught`
- **Base/meta**: `magic-framework`

## Approved Synonyms
- `math` → `math-domain`
- `aesthetics` → `aesthetics-domain`
- `geometry`, `geometric-element` → `geometric-element-domain`
- `ideology` → `ideology-domain`
- `comptroller`, `power` → `comptroller-domain`
- `semiotics`, `semiotic` → `visual-semiotics`
- `sign` → `semiotic-sign`
- `material`, `objects` → `material-objects`
- `seals` → `cylinder-seals`
- `daya` → `day-a`
- `dayb` → `day-b`
- `bridge` → `architecture-bridge`

## Grades and Status
- Grades: `K-2`, `3-5`, `6-8`, `9-12`
- Status: `draft`, `reviewed`, `ready`, `approved`, `taught`

---

# Directions & Templates (from a priori doc)

## Core Pedagogical Philosophy (Front Matter for Master Index)
```yaml
curriculum_name: Geometric Elements - Myth to Innovation
pedagogical_model: Form + Function Integration
core_thesis: |
  Geometric elements are visual semiotics that:
  1. Emerge from myth and sacred art (FORM - metaphorical meaning)
  2. Become institutionalized through material culture, ritual, and embodied cognition (INTERNALIZATION)
  3. Enable innovative design thinking for mathematical, scientific, architectural, and civic solutions (FUNCTION - practical application)

  Integration Point: Architecture bridges Form (Day A) and Function (Day B)

structure: Two-day weekly modules (Day A: Myth→Material Culture; Day B: STEM Innovation)
tags: [curriculum, geometric-semiotics, myth-to-innovation]
```

## Weekly Module Template (YAML)
```yaml
# WEEK IDENTIFIER
week_number: [1-12]
geometric_element: [Circle/Triangle/Square/Pentagon/Hexagon/etc.]
element_type: [atomic/complex]
complexity_level: [foundational/intermediate/advanced]

# PEDAGOGICAL STRUCTURE
day_a_focus: Myth → Material Culture → Embodied Cognition
day_b_focus: STEM Innovation → Design Thinking → Problem Solving

# CORE ONTOLOGY TAGS
ontology_stage_1: myth-and-art
ontology_stage_2: institutionalization
ontology_stage_3: innovation

# FORM & FUNCTION
form_category: [visual-semiotic, symbolic-meaning, sacred-geometry]
function_category: [mathematical-principle, architectural-application, technological-innovation]

# LINKING
primary_myth: "[[Myth Name]]"
related_elements: [list of related geometric elements]
architectural_bridge: "[[Architecture Case Study]]"
stem_innovations: [list of innovations]

# IMAGE TRACKING
image_count: [total number]
myth_art_images: [count]
material_culture_images: [count]
ritual_images: [count]
innovation_images: [count]

# ASSESSMENT
learning_objectives: |
  - Understand [element] as metaphor from myth
  - Recognize [element] in material culture
  - Explain how [element] enables [specific innovation]
tags: [week-X, element-name, myth-to-material, stem-innovation, day-a, day-b]
```

## Folder Structure (summary)
```
Geometric Elements Curriculum/
├── 00-MASTER-INDEX.md
├── 01-ONTOLOGY-SYSTEM/
├── 02-MYTHS-DATABASE/
├── 03-WEEKLY-MODULES/
│   ├── Week-01-Circle/ (OVERVIEW, Day A/B, Images, Assessment)
│   └── Week-02-Triangle/ (etc.)
├── 04-MATERIAL-CULTURE-DATABASE/
├── 05-STEM-INNOVATIONS-DATABASE/
├── 06-ARCHITECTURAL-BRIDGES/
└── 07-TEACHING-RESOURCES/
```

## Day A Note Template (key frontmatter)
```yaml
day: A
week: [X]
element: [Name]
focus: Form - Myth to Material Culture
ontology_stages: [myth-and-art, institutionalization]
lecture_duration: 50-75 minutes
image_heavy: true
tags: [day-a, week-X, element-name, myth, material-culture, embodied-cognition, ritual]
```

## Day B Note Template (key frontmatter)
```yaml
day: B
week: [X]
element: [Name]
focus: Function - STEM Innovation & Design Thinking
ontology_stage: innovation
lecture_duration: 50-75 minutes
demonstration_heavy: true
tags: [day-b, week-X, element-name, stem, mathematics, engineering, architecture, innovation]
```

---

*Archived for reference; not the active source in the main tree.*
