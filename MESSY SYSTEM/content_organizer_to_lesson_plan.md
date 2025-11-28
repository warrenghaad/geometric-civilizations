---
title: content organizer to lesson plan
document_type: content-draft
subject: 
grade_levels: [3]
element: TBD
scope: all-three
status: drafting
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

# Content Organizer → Lesson Plan Formatter (Main Vault)

Use this to track raw content and promote it into structured lesson plans. Fill frontmatter in each content note; Dataview tables below help you filter and copy into your lesson template.

## Frontmatter template for content drafts
```yaml
---
title: [Working title]
subject: [Math|Art|History|Myth|Music|SEL|...]     # or #subject/...
grade_levels: [3,4,5]                               # array
element: [circle|triangle|square|spiral|radial|polygon|grid|fractal|TBD]
document_type: content-draft
scope: [ontology-myth-and-art|ontology-material-culture|ontology-innovation|all-three|TBD]
duration_minutes: 45
standards: ["3.G.A.1", "RI.3.3"]
status: drafting                                    # drafting|ready|needs-images|needs-ritual|needs-function
key_points:
  - ""
  - ""
images:
  - id: ""
    desc: ""
    placement: ""
    why: ""
links:
  - "[[related_note]]"
tags: [#content, #lesson/candidate]
attachments:
  - "path/to/source.pdf"
  - "path/to/slides.pptx"
---
```

## Frontmatter template for lesson plans (target format)
```yaml
---
title: [Lesson Title]
document_type: lesson-plan
grade_levels: [3]
element: [ ]
scope: [ontology-myth-and-art|ontology-innovation|...]
duration_minutes: 50
lesson_day: [DayA|DayB]
status: drafting
standards: ["3.G.A.1"]
sections:
  - name: Myth Retelling
    minutes: 5
    text: ""
  - name: Material Culture (core)
    minutes: 12
    text: ""
  - name: Technique
    minutes: 7
    text: ""
  - name: Hands-On
    minutes: 10
    text: ""
  - name: Wrap
    minutes: 5
    text: ""
  - name: Exit Ticket
    minutes: 3
    text: ""
images:
  - id: ""
    desc: ""
    placement: ""
    why: ""
tags: [#lesson/plan]
---
```

## Dataview: Content candidates by status
```dataview
TABLE status, subject, grade_levels AS Grades, element, scope, key_points, file.link AS Note
FROM ""
WHERE document_type = "content-draft"
SORT status ASC, file.name ASC
```

## Dataview: Ready-to-format drafts (drafting → ready)
```dataview
TABLE subject, grade_levels AS Grades, element, scope, key_points, images, file.link AS Note
FROM ""
WHERE document_type = "content-draft" AND (status = "ready" OR status = "drafting")
SORT file.name ASC
```

## Dataview: Source PDFs/PPTs in this vault (reference)
```dataview
TABLE file.name AS File, file.folder AS Folder, file.size AS Size
FROM ""
WHERE endswith(lower(file.name), ".pdf") OR endswith(lower(file.name), ".pptx") OR endswith(lower(file.name), ".ppt")
SORT file.name ASC
```

## Dataview: Lesson plans (target format)
```dataview
TABLE lesson_day AS Day, grade_levels AS Grades, element, scope, duration_minutes AS Min, standards, file.link AS Lesson
FROM ""
WHERE document_type = "lesson-plan"
SORT file.name ASC
```

## Minimal workflow
1) Capture raw content as a note with `document_type: content-draft` using the content template above.
2) Fill subject/element/grade/scope/status; add key_points and image stubs.
   - Include attachments to PDFs/PPTs in the `attachments` list for quick reference.
3) When ready, create a lesson-plan note using the lesson plan template and copy key_points/images into the structured sections.
4) Track progress via the tables: move status from `drafting` → `ready` → (once converted) keep as reference or mark `used`.
