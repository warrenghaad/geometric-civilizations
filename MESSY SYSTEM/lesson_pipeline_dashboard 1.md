# Lesson Pipeline Dashboard

## Content drafts (to promote)
```dataview
TABLE status, subject, grade_levels AS Grades, element, scope, key_points, attachments, file.link AS Note
FROM ""
WHERE document_type = "content-draft"
SORT status ASC, file.name ASC
```

## Ready-to-format drafts (drafting → ready)
```dataview
TABLE subject, grade_levels AS Grades, element, scope, key_points, images, attachments, file.link AS Note
FROM ""
WHERE document_type = "content-draft" AND (status = "ready" OR status = "drafting")
SORT file.name ASC
```

## Lesson plans (Day A/B)
```dataview
TABLE lesson_day AS Day, grade_levels AS Grades, element, scope, duration_minutes AS Min, standards, file.link AS Lesson
FROM ""
WHERE document_type = "lesson-plan"
SORT file.name ASC
```

## Source PDFs/PPTs (reference)
```dataview
TABLE file.name AS File, file.folder AS Folder, file.size AS Size
FROM ""
WHERE endswith(lower(file.name), ".pdf") OR endswith(lower(file.name), ".pptx") OR endswith(lower(file.name), ".ppt")
SORT file.name ASC
```

## Minimal promotion snippet (copy key points into Day A/B)
1) Open your content draft (`document_type: content-draft`).
2) Copy relevant key_points/images into the Day A/B shell:
   - Day A: Myth Retelling; Myth in Art; **Material Culture (core: element→myth→ritual→object/form→embodied action; freq/radius; why it belongs)**; Technique; Practice; Hands-On; Wrap; Exit Ticket.
   - Day B: Bridge; Myth as organizing story; **Design-in-Use (functionality + transformations + physics + adoption)**; Structural Decomposition; Practice; Hands-On Model/Test; Wrap; Exit Ticket.
3) Update frontmatter (element, grade_levels, scope, standards, status) on the lesson plan.
