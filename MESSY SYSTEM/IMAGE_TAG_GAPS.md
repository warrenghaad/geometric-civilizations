---
note_type: helper
title: Image Tag Gaps
tags: [ontology, helper, dataview]
---

# Image Tag Gaps (quick checks)

Use these Dataview snippets to see what’s missing and to assign dimension/image tags.

## Files missing any `geo-*` tag
```dataview
TABLE file.mtime AS "Modified"
FROM "01_INPUT/AI_Outputs_Raw"
WHERE !contains(regexmatch("^geo-", join(tags, " ")), true)
SORT file.mtime DESC
LIMIT 100
```

## Files missing a dimension mapping
```dataview
TABLE file.mtime AS "Modified"
FROM "01_INPUT/AI_Outputs_Raw"
WHERE !dimension_mapping
SORT file.mtime DESC
LIMIT 100
```

## Files missing cultural context
```dataview
TABLE file.mtime AS "Modified"
FROM "01_INPUT/AI_Outputs_Raw"
WHERE !cultural_context
SORT file.mtime DESC
LIMIT 100
```

## Recent files with image fields (sanity check)
```dataview
TABLE dimension_mapping, geometric_elements, operations, cultural_context
FROM "01_INPUT/AI_Outputs_Raw"
WHERE dimension_mapping
SORT file.mtime DESC
LIMIT 50
```

## Frontmatter fields to use (image-aligned)
```yaml
dimension_mapping: [map-2d-on-3d]
dimensions: [dim-2d, dim-3d]
geometric_elements: [geo-archform]
operations: [op-symmetry]
cultural_context: [civ-meso]
pattern_type: [pat-rosace]
material: [mat-stone]
technique: [tech-carving]
math_concepts: [math-symmetry]
```
