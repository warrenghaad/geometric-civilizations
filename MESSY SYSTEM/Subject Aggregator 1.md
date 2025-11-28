# Subject Aggregator

Use this note to surface all files by **subject**. Pick one of these conventions:
- Frontmatter field: `subject: Math` (or Art, History, Myth, etc.)
- Tag convention: `#subject/math` (or `#subject/art`, `#subject/history`, etc.)

## By Frontmatter `subject`
```dataview
TABLE
  subject AS Subject,
  document_type AS Type,
  element AS Element,
  scope AS Scope,
  grade_levels AS Grades,
  status AS Status,
  file.link AS Note
FROM ""
WHERE subject
SORT subject ASC, file.name ASC
```

## By Tag `#subject/<name>`
```dataview
TABLE
  replace(t, "#subject/", "") AS Subject,
  document_type AS Type,
  element AS Element,
  scope AS Scope,
  grade_levels AS Grades,
  status AS Status,
  file.link AS Note
FROM ""
FLATTEN filter(file.tags, (t) => startswith(lower(t), "#subject/")) AS t
WHERE t
SORT Subject ASC, file.name ASC
```

Notes:
- If a note has both a `subject` field and a `#subject/...` tag, it will appear in both tables.
- Adjust the field names if your frontmatter uses different keys. The queries are non-destructive and can be edited in-place.
