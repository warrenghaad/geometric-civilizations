---
note_type: ontology-glossary
tags: [ontology, tagging-system, metadata-structure, magic-framework]
source_of_truth: scripts/auto_annotate.py
---

# Tagging System Master (MAGIC-Aligned)

Canonical tags (what the watcher will keep) and approved synonyms (what the watcher will normalize). Semiotics and Comptroller are included.

## Canonical Tags by Category
- **MAGIC domains**: `math-domain`, `aesthetics-domain`, `geometric-element-domain`, `ideology-domain`, `comptroller-domain`
- **Stages**: `ontology-stage-1`, `ontology-stage-2`, `ontology-stage-3`
- **Semiotics**: `visual-semiotics`, `semiotic-sign`, `semiotic-system`
- **Day A (Embodied Aesthetics / Material)**: `day-a`, `myth`, `mythic-art`, `material-objects`, `cylinder-seals`, `textiles`, `pottery`, `architecture`, `tools`, `ornaments`, `ritual-ceremonial`, `ritual-everyday`, `embodied-cognition`, `artistic-decomposition`
- **Day B (Disembodied Systems / Innovation)**: `day-b`, `mathematics`, `engineering`, `architecture`, `technology`, `design-thinking`, `innovation`, `historical-causation`, `mathematical-decomposition`
- **Bridge**: `architecture-bridge`, `form-and-function`, `aesthetics-math-bridge`
- **Lesson components**: `hands-on-activity`, `sel-integration`, `archetype-role`, `transformation-verb`
- **Status**: `draft`, `reviewed`, `ready`, `approved`, `taught`
- **Base/meta**: `magic-framework`

## Approved Synonyms (auto-normalized)
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

## Grade Levels and Status
- Grades (fixed set): `K-2`, `3-5`, `6-8`, `9-12`
- Status (fixed set): `draft`, `reviewed`, `ready`, `approved`, `taught`

## How the Watcher Uses This
- It prompts Claude with the canonical list above.
- It normalizes synonyms to canonical slugs and drops anything outside this list.
- It always adds `magic-framework`.
- Grade levels are constrained to the fixed set above; unknowns fall back to `unknown`.
- Status is normalized to the fixed set above; unknowns fall back to `draft`.

## Keeping Script and Glossary in Sync
If you edit this glossary, also update `scripts/auto_annotate.py` (`MAGIC_TAGS` and `TAG_SYNONYMS`) so the watcher enforces the same values.

---

## Image Tags (shared IDs; keep separate from MAGIC)
Use these when you want Obsidian notes to line up with the image ontology. The `geo-*` slugs are the bridge (see `GEOMETRIC_ELEMENT_LINKS.md`). This does not merge the ontologies—just a reference list.

- **Dimensions**: `dim-0d`, `dim-1d`, `dim-2d`, `dim-3d`, `dim-4d`
- **Dimension mappings**: `map-1d-on-2d`, `map-1d-on-3d`, `map-1d-builds-2d-on-2d`, `map-2d-on-2d`, `map-2d-on-3d`, `map-2d-to-3d`, `map-3d-objects`, `map-3d-versions-of-2d`
- **Geometric elements (shared)**: `geo-point`, `geo-line`, `geo-curve`, `geo-curvearea`, `geo-surface`, `geo-polygon`, `geo-circle`, `geo-polyhedron`, `geo-sphere`, `geo-cylinder`, `geo-cone`, `geo-archform`, `geo-relief`
- **Operations**: `op-symmetry`, `op-tiling`, `op-subdivide`, `op-param`, `op-project`, `op-extrude`, `op-revolve`, `op-emboss`, `op-section`, `op-weave`
- **Cultural contexts**: `civ-meso`, `civ-egypt`, `civ-islam`, `civ-renaissance`, `civ-greece`, `civ-medieval-eu`, `civ-china`, `civ-india`, `civ-andes`
- **Pattern/material/technique** (from image system as needed): e.g., `pat-rosace`, `pat-wallpaper`, `mat-stone`, `tech-carving`, `tech-weaving`
- **Math concepts** (as needed): e.g., `math-symmetry`, `math-proportion`, `math-trig`

Optional frontmatter for image-aligned notes:
```yaml
image_type: [artifact | overlay | reference]
dimension_mapping: [map-2d-on-3d]
dimensions: [dim-2d, dim-3d]
geometric_elements: [geo-archform, geo-polygon]
operations: [op-symmetry, op-tiling]
pattern_type: [pat-rosace]
material: [mat-stone]
technique: [tech-carving]
cultural_context: [civ-meso]
math_concepts: [math-symmetry]
```
