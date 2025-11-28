---
note_type: ontology-crosswalk
title: Geometric Element Links (Obsidian ↔ Image Ontology)
tags: [ontology, crosswalk, geometric-elements]
---

# Geometric Element Crosswalk

Shared IDs (`geo-*`) to use in BOTH systems so notes and images can find each other. Keep these slugs in frontmatter/tags in Obsidian and they’ll line up with the image ontology (see `ONTOLOGY_IMAGE_SYSTEM.md`, `IMAGE_ORGANIZATION_COMPLETE_2025-11-10.md`).

## Shared `geo-*` IDs
- `geo-point`
- `geo-line`
- `geo-curve`
- `geo-curvearea`
- `geo-surface`
- `geo-polygon`
- `geo-circle`
- `geo-polyhedron`
- `geo-sphere`
- `geo-cylinder`
- `geo-cone`
- `geo-archform`
- `geo-relief`

## How to use
- In Obsidian notes (annotation, artifact, lecture), add the relevant `geo-*` slug to tags or frontmatter alongside your MAGIC tags.
- In the image system, the same `geo-*` slugs already index images; use them to query/filter there.

## Adding a new geometric element
1) Pick a new slug: `geo-<name>` (lowercase, hyphenated).
2) Add it here under “Shared `geo-*` IDs”.
3) Add it to the image ontology lists in `ONTOLOGY_IMAGE_SYSTEM.md` and `IMAGE_ORGANIZATION_COMPLETE_2025-11-10.md` (and your JSON if applicable).
4) Use the same slug in Obsidian frontmatter/tags and in image metadata.

## Where each system lives
- Obsidian tagging: `00_SYSTEM/Ontology/Tagging-System-Master.md` (MAGIC tags + any shared `geo-*` you add).
- Image ontology: `.../Geometric Elements/Cultural Artifacts/Ontology/ONTOLOGY_TO_PIPELINE_MAPPING.md` and `.../Research/Python Scripts 1112/IMAGE_ORGANIZATION_COMPLETE_2025-11-10.md`.
