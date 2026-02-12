# SSOT DATABASE SYSTEM - Complete Guide

**Single Source of Truth linking everything together**  
**Created:** November 4, 2025

---

## 🎯 What This Database Does

Links **SSOTs → eTextbooks → Chapters → Lessons → Content → Assets → Specifications** in a single, queryable system.

### The 7 Levels of Truth

```
LEVEL 1: SSOT (Single Source of Truth)
   ↓
LEVEL 2: eTextbook (Collection of chapters)
   ↓
LEVEL 3: Chapter (Section within eTextbook)
   ↓
LEVEL 4: Lesson (Teaching unit)
   ↓
LEVEL 5: Content Block (Granular content)
   ↓
LEVEL 6: Asset (Media file)
   ↓
LEVEL 7: Specification (Technical requirement)
```

---

## 📊 Database Schema

### Core Tables (7 Levels)

#### LEVEL 1: SSOTs
```sql
ssots (
    ssot_id TEXT PRIMARY KEY,
    ssot_type TEXT,              -- CURRICULUM, ETEXTBOOK, LESSON, UNIT, MODULE
    title TEXT,
    description TEXT,
    grade_level INTEGER,
    subject TEXT,
    version TEXT,
    status TEXT,                 -- DRAFT, ACTIVE, ARCHIVED
    file_path TEXT
)
```

**Example:**
- `SSOT-MESO-G3` → "MESO Grade 3 Curriculum"

---

#### LEVEL 2: eTextbooks
```sql
etextbooks (
    etextbook_id TEXT PRIMARY KEY,
    ssot_id TEXT → ssots,
    title TEXT,
    subtitle TEXT,
    grade_level INTEGER,
    isbn TEXT,
    page_count INTEGER,
    format TEXT,                 -- PDF, EPUB, HTML
    cover_image TEXT
)
```

**Example:**
- `EBOOK-G3-CIRCLES` → "Circles in Mesopotamian Geometry"

---

#### LEVEL 3: Chapters
```sql
chapters (
    chapter_id TEXT PRIMARY KEY,
    etextbook_id TEXT → etextbooks,
    chapter_number INTEGER,
    title TEXT,
    page_start INTEGER,
    page_end INTEGER,
    duration_minutes INTEGER,
    chapter_type TEXT,           -- INTRO, MYTH, GEOMETRY, ACTIVITY, ASSESSMENT
    learning_objectives TEXT
)
```

**Example:**
- `CHAP-G3-01B` → "The Sun & Circle of Sharing" (pages 21-40)

---

#### LEVEL 4: Lessons
```sql
lessons (
    lesson_id TEXT PRIMARY KEY,
    chapter_id TEXT → chapters,
    ssot_id TEXT → ssots,
    lesson_key TEXT,             -- meso_G3_1B
    lesson_name TEXT,
    grade INTEGER,
    deity_name TEXT,
    geometric_concept TEXT,
    math_standard TEXT,
    duration_minutes INTEGER,
    standards TEXT,
    estimated_images INTEGER
)
```

**Example:**
- `G3-1B` → "The Sun & Circle of Sharing"

---

#### LEVEL 5: Content Blocks
```sql
content_blocks (
    content_id INTEGER PRIMARY KEY,
    lesson_id TEXT → lessons,
    chapter_id TEXT → chapters,
    block_type TEXT,             -- TEXT, MYTH, IMAGE, VIDEO, ACTIVITY, DIAGRAM
    block_order INTEGER,
    section_name TEXT,
    body_text TEXT,
    duration_seconds INTEGER,
    interactivity_level TEXT     -- LOW, MEDIUM, HIGH
)
```

**Example:**
- Content Block #2: "The Myth" (180 seconds, MEDIUM interactivity)

---

#### LEVEL 6: Assets
```sql
assets (
    asset_id TEXT PRIMARY KEY,
    lesson_id TEXT → lessons,
    chapter_id TEXT → chapters,
    content_id INTEGER → content_blocks,
    asset_type TEXT,             -- IMG, VID, AUD, DOC, OVL
    subtype TEXT,                -- ILL, PHO, ART, DGM
    filename TEXT,
    usage_role TEXT,             -- myth, diagram, overlay, worksheet
    format TEXT,                 -- PNG, JPG, SVG, MP4
    width_px INTEGER,
    height_px INTEGER,
    alt_text TEXT,
    tags TEXT
)
```

**Example:**
- `meso_G3_1B-IMG-ILL_myth_01_sun_river` → myth illustration PNG

---

#### LEVEL 7: Specifications
```sql
specifications (
    spec_id INTEGER PRIMARY KEY,
    asset_id TEXT → assets,
    spec_type TEXT,              -- DIMENSION, FORMAT, COLOR, QUALITY, ACCESSIBILITY
    spec_name TEXT,
    spec_value TEXT,
    required BOOLEAN,
    priority TEXT,               -- LOW, MEDIUM, HIGH, CRITICAL
    validation_rule TEXT
)
```

**Example:**
- Width: 3840 (CRITICAL, required)
- Alt Text Length: 80-140 (CRITICAL, required)

---

### Supporting Tables

#### Sections (within Lessons)
```sql
sections (
    section_id INTEGER PRIMARY KEY,
    lesson_id TEXT → lessons,
    section_number INTEGER,
    section_name TEXT,
    duration_minutes INTEGER,
    slide_range TEXT
)
```

#### Slides (Presentation Elements)
```sql
slides (
    slide_id INTEGER PRIMARY KEY,
    lesson_id TEXT → lessons,
    section_id INTEGER → sections,
    slide_number INTEGER,
    slide_title TEXT,
    speaker_notes TEXT,
    asset_ids TEXT,
    layout_type TEXT
)
```

#### Overlays (Geometric Annotations)
```sql
overlays (
    overlay_id INTEGER PRIMARY KEY,
    lesson_id TEXT → lessons,
    asset_id TEXT → assets,
    category TEXT,
    overlay_code TEXT,
    svg_path TEXT,
    color_hex TEXT,
    animation_type TEXT
)
```

#### Standards (Educational Standards)
```sql
standards (
    standard_id INTEGER PRIMARY KEY,
    standard_code TEXT,          -- 3.G.A.1
    grade_level INTEGER,
    domain TEXT,
    description TEXT
)
```

#### Tags (Controlled Vocabulary)
```sql
tags (
    tag_id INTEGER PRIMARY KEY,
    tag_name TEXT,               -- grade-3, deity-shamash
    tag_category TEXT
)
```

#### Dependencies (Relationships)
```sql
dependencies (
    dependency_id INTEGER PRIMARY KEY,
    source_type TEXT,            -- SSOT, ETEXTBOOK, CHAPTER, LESSON, ASSET
    source_id TEXT,
    target_type TEXT,
    target_id TEXT,
    dependency_type TEXT,        -- REQUIRES, REFERENCES, DERIVES_FROM
    required BOOLEAN
)
```

#### Production Status (Workflow)
```sql
production_status (
    status_id INTEGER PRIMARY KEY,
    entity_type TEXT,
    entity_id TEXT,
    stage TEXT,                  -- PLANNING, DRAFTING, REVIEW, PRODUCTION, QA
    status TEXT,                 -- NOT_STARTED, IN_PROGRESS, COMPLETED
    assigned_to TEXT,
    due_date TIMESTAMP
)
```

---

## 🔗 Complete Hierarchy Example

```
SSOT-MESO-G3: "MESO Grade 3 Curriculum"
  └─ EBOOK-G3-CIRCLES: "Circles in Mesopotamian Geometry"
      ├─ CHAP-G3-01A: "Shamash & The Circle" (pages 1-20)
      │   └─ G3-1A: Lesson on radius/diameter
      │       ├─ Content Block 1: Opening image
      │       ├─ Content Block 2: Myth reading
      │       └─ Content Block 3: Activity
      │           ├─ Asset: meso_G3_1A-IMG-ART_shamash_tablet.jpg
      │           │   ├─ Spec: Width 3840px (CRITICAL)
      │           │   ├─ Spec: Format JPG (HIGH)
      │           │   └─ Spec: Alt text 80-140 chars (CRITICAL)
      │           └─ Asset: meso_G3_1A-OVL-center_dot.svg
      │               └─ Spec: Format SVG (CRITICAL)
      │
      └─ CHAP-G3-01B: "The Sun & Circle of Sharing" (pages 21-40)
          └─ G3-1B: Lesson on halves/fourths
              ├─ Content Block 1: Look and Wonder (120s)
              ├─ Content Block 2: The Myth (180s)
              ├─ Content Block 3: Geometry diagrams (300s)
              ├─ Content Block 4: Circle collage (600s)
              └─ Content Block 5: Worksheet (480s)
                  ├─ Asset: meso_G3_1B-IMG-ILL_myth_01.png
                  │   ├─ Spec: 3840×2160 px (CRITICAL)
                  │   ├─ Spec: PNG format (HIGH)
                  │   ├─ Spec: sRGB color space (MEDIUM)
                  │   ├─ Spec: 300 DPI (HIGH)
                  │   └─ Spec: Alt text length 80-140 (CRITICAL)
                  └─ Asset: meso_G3_1B-OVL-center_CENTER_Dot.svg
                      ├─ Spec: SVG format (CRITICAL)
                      └─ Spec: Scalable vector (HIGH)
```

---

## 📋 Query Examples

### 1. Get Full Hierarchy for a Lesson

```python
from SSOT_DATABASE_SYSTEM import SSOTDatabase

db = SSOTDatabase()
db.connect()

hierarchy = db.query_full_hierarchy('G3-1B')
print(f"SSOT: {hierarchy['ssot_title']}")
print(f"eTextbook: {hierarchy['etextbook_title']}")
print(f"Chapter: {hierarchy['chapter_title']}")
print(f"Lesson: {hierarchy['lesson_name']}")
print(f"Content Blocks: {hierarchy['content_blocks']}")
print(f"Assets: {hierarchy['assets']}")
print(f"Specifications: {hierarchy['specifications']}")
```

**Output:**
```
SSOT: MESO Grade 3 Curriculum
eTextbook: Circles in Mesopotamian Geometry
Chapter: The Sun & Circle of Sharing
Lesson: The Sun & Circle of Sharing
Content Blocks: 5
Assets: 2
Specifications: 8
```

---

### 2. Export Complete Manifest

```python
db.export_complete_manifest('G3-1B', 'manifest.json')
```

**Creates JSON with:**
- SSOT data
- eTextbook data
- Chapter data
- Lesson data
- All content blocks
- All assets with specifications
- All dependencies
- Complete hierarchy

---

### 3. Generate Asset Specification Report

```python
db.generate_asset_spec_report('G3-1B')
```

**Output:**
```
meso_G3_1B-IMG-ILL_myth_01_sun_river.png
  Type: IMG | Format: PNG
  Size: 3840×2160 px
  Alt: A bright round sun rises over a blue river at dawn.
  Specs: Width: 3840 (CRITICAL), Height: 2160 (CRITICAL),
         Format: PNG (HIGH), DPI: 300 (HIGH),
         Alt Text Length: 80-140 (CRITICAL)
```

---

### 4. Custom SQL Queries

```sql
-- Get all assets for a lesson with their specs
SELECT 
    a.asset_id,
    a.filename,
    a.format,
    a.width_px,
    a.height_px,
    GROUP_CONCAT(s.spec_name || ': ' || s.spec_value) as specs
FROM assets a
LEFT JOIN specifications s ON a.asset_id = s.asset_id
WHERE a.lesson_id = 'G3-1B'
GROUP BY a.asset_id;

-- Get dependency chain for a lesson
SELECT 
    d.source_type,
    d.source_id,
    d.dependency_type,
    d.target_type,
    d.target_id
FROM dependencies d
WHERE d.target_id = 'G3-1B'
   OR d.source_id = 'G3-1B';

-- Get all content blocks with their assets
SELECT 
    cb.section_name,
    cb.title,
    cb.block_type,
    cb.duration_seconds,
    COUNT(a.asset_id) as asset_count
FROM content_blocks cb
LEFT JOIN assets a ON cb.content_id = a.content_id
WHERE cb.lesson_id = 'G3-1B'
GROUP BY cb.content_id;
```

---

## 🎯 Use Cases

### 1. Content Production Pipeline

**Track production status for each entity:**

```sql
INSERT INTO production_status (
    entity_type, entity_id, stage, status, assigned_to, due_date
) VALUES (
    'ASSET',
    'meso_G3_1B-IMG-ILL_myth_01_sun_river',
    'PRODUCTION',
    'IN_PROGRESS',
    'Designer A',
    '2025-11-10'
);
```

Query production pipeline:
```sql
SELECT 
    ps.entity_type,
    ps.entity_id,
    ps.stage,
    ps.status,
    ps.assigned_to,
    ps.due_date
FROM production_status ps
WHERE ps.status != 'COMPLETED'
ORDER BY ps.due_date;
```

---

### 2. Specification Validation

**Check if all critical specs are met:**

```sql
SELECT 
    a.asset_id,
    a.filename,
    COUNT(CASE WHEN s.priority = 'CRITICAL' AND s.required = 1 THEN 1 END) as critical_specs,
    COUNT(CASE WHEN s.priority = 'HIGH' THEN 1 END) as high_specs
FROM assets a
LEFT JOIN specifications s ON a.asset_id = s.asset_id
WHERE a.lesson_id = 'G3-1B'
GROUP BY a.asset_id;
```

---

### 3. Dependency Management

**Find all assets required by a lesson:**

```sql
SELECT DISTINCT
    a.asset_id,
    a.filename,
    a.asset_type,
    d.dependency_type
FROM dependencies d
JOIN assets a ON d.source_id = a.asset_id
WHERE d.target_type = 'LESSON'
  AND d.target_id = 'G3-1B'
  AND d.required = 1;
```

---

### 4. Content Reuse

**Find assets that can be reused across lessons:**

```sql
SELECT 
    a.asset_id,
    a.filename,
    GROUP_CONCAT(DISTINCT a2.lesson_id) as used_in_lessons
FROM assets a
JOIN assets a2 ON a.filename = a2.filename
WHERE a2.lesson_id != a.lesson_id
GROUP BY a.asset_id;
```

---

## 📦 Data Flow

### Adding a New Lesson (Complete Flow)

```python
# 1. Ensure SSOT exists
cursor.execute("""
    INSERT OR IGNORE INTO ssots (ssot_id, ssot_type, title, grade_level)
    VALUES ('SSOT-MESO-G3', 'CURRICULUM', 'MESO Grade 3', 3)
""")

# 2. Ensure eTextbook exists
cursor.execute("""
    INSERT OR IGNORE INTO etextbooks (etextbook_id, ssot_id, title, grade_level)
    VALUES ('EBOOK-G3-CIRCLES', 'SSOT-MESO-G3', 'Circles', 3)
""")

# 3. Add Chapter
cursor.execute("""
    INSERT INTO chapters (chapter_id, etextbook_id, chapter_number, title)
    VALUES ('CHAP-G3-01C', 'EBOOK-G3-CIRCLES', 3, 'New Chapter')
""")

# 4. Add Lesson
cursor.execute("""
    INSERT INTO lessons (lesson_id, chapter_id, ssot_id, lesson_key, lesson_name, grade)
    VALUES ('G3-1C', 'CHAP-G3-01C', 'SSOT-MESO-G3', 'meso_G3_1C', 'New Lesson', 3)
""")

# 5. Add Content Blocks
cursor.execute("""
    INSERT INTO content_blocks (lesson_id, block_type, block_order, title)
    VALUES ('G3-1C', 'MYTH', 1, 'Opening Story')
""")

# 6. Add Assets
cursor.execute("""
    INSERT INTO assets (asset_id, lesson_id, asset_type, filename, format)
    VALUES ('meso_G3_1C-IMG-myth_01', 'G3-1C', 'IMG', 'myth_01.png', 'PNG')
""")

# 7. Add Specifications
cursor.execute("""
    INSERT INTO specifications (asset_id, spec_type, spec_name, spec_value, priority)
    VALUES ('meso_G3_1C-IMG-myth_01', 'DIMENSION', 'Width', '3840', 'CRITICAL')
""")

# 8. Add Dependencies
cursor.execute("""
    INSERT INTO dependencies (source_type, source_id, target_type, target_id, dependency_type)
    VALUES ('LESSON', 'G3-1C', 'CHAPTER', 'CHAP-G3-01C', 'REQUIRES')
""")
```

---

## 🔍 Validation Queries

### Check Completeness

```sql
-- Lessons without assets
SELECT l.lesson_id, l.lesson_name
FROM lessons l
LEFT JOIN assets a ON l.lesson_id = a.lesson_id
WHERE a.asset_id IS NULL;

-- Assets without specifications
SELECT a.asset_id, a.filename
FROM assets a
LEFT JOIN specifications s ON a.asset_id = s.asset_id
WHERE s.spec_id IS NULL;

-- Content blocks without assets
SELECT cb.content_id, cb.title
FROM content_blocks cb
LEFT JOIN assets a ON cb.content_id = a.content_id
WHERE cb.block_type IN ('IMAGE', 'VIDEO', 'DIAGRAM')
  AND a.asset_id IS NULL;

-- Missing critical specifications
SELECT 
    a.asset_id,
    a.filename,
    COUNT(s.spec_id) as spec_count
FROM assets a
LEFT JOIN specifications s ON a.asset_id = s.asset_id AND s.priority = 'CRITICAL'
GROUP BY a.asset_id
HAVING spec_count < 3;  -- Assuming minimum 3 critical specs
```

---

## 📊 Statistics Queries

```sql
-- Lesson statistics
SELECT 
    l.lesson_id,
    l.lesson_name,
    COUNT(DISTINCT cb.content_id) as content_blocks,
    COUNT(DISTINCT a.asset_id) as assets,
    COUNT(DISTINCT s.spec_id) as specifications,
    SUM(cb.duration_seconds) as total_duration_seconds
FROM lessons l
LEFT JOIN content_blocks cb ON l.lesson_id = cb.lesson_id
LEFT JOIN assets a ON l.lesson_id = a.lesson_id
LEFT JOIN specifications s ON a.asset_id = s.asset_id
GROUP BY l.lesson_id;

-- Asset type distribution
SELECT 
    asset_type,
    format,
    COUNT(*) as count,
    AVG(file_size_kb) as avg_size_kb
FROM assets
GROUP BY asset_type, format;

-- Production status summary
SELECT 
    stage,
    status,
    COUNT(*) as count
FROM production_status
GROUP BY stage, status;
```

---

## ✅ Benefits

1. **Single Source of Truth**: All curriculum data in one place
2. **Complete Traceability**: Track any asset back to its SSOT
3. **Specification Enforcement**: Validate technical requirements
4. **Dependency Management**: Understand relationships
5. **Production Tracking**: Monitor workflow status
6. **Content Reuse**: Find and reuse existing assets
7. **Quality Assurance**: Automated validation checks
8. **Reporting**: Generate comprehensive reports

---

## 🚀 Next Steps

1. **Run the system:**
   ```bash
   python3 SSOT_DATABASE_SYSTEM.py
   ```

2. **Query the database:**
   ```python
   from SSOT_DATABASE_SYSTEM import SSOTDatabase
   db = SSOTDatabase()
   db.connect()
   hierarchy = db.query_full_hierarchy('G3-1B')
   ```

3. **Add more lessons:**
   - Follow the data flow example
   - Link to existing eTextbooks/chapters
   - Add assets with specifications

4. **Export manifests:**
   ```python
   db.export_complete_manifest('G3-1B', 'output.json')
   ```

5. **Generate reports:**
   ```python
   db.generate_asset_spec_report('G3-1B')
   ```

---

**Status:** ✅ COMPLETE  
**Database:** `meso_ssot_complete.db`  
**Tables:** 14 (7 core + 7 supporting)  
**Sample Data:** Grade 3 Lessons 1A & 1B ready  
**Ready For:** Production tracking, asset management, quality assurance
