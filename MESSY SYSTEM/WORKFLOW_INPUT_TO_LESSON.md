# AUTOMATED WORKFLOW: Input → Database → Outline → Lesson
**Purpose:** Automated pipeline from research to ready-to-teach lessons
**Last Updated:** 2025-11-24

---

## THE COMPLETE PIPELINE

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW OVERVIEW                         │
└─────────────────────────────────────────────────────────────┘

STAGE 1: INPUT
└─> Raw materials land in 01_INPUT/
    - PDFs, images, notes, web exports
    - No organization required yet

STAGE 2: EXTRACTION & TAGGING
└─> Create database entries with metadata
    - Use templates for myths, artifacts, deities, etc.
    - Add YAML tags: week, geometric_element, deity, etc.
    - Place in 02_DATABASE/ organized folders

STAGE 3: AUTOMATED QUERIES
└─> Lesson outlines auto-populate from database
    - Dataview queries pull tagged content
    - Organized by week number
    - Shows what exists, what's missing

STAGE 4: LESSON ASSEMBLY
└─> Fill lesson template from outline
    - Copy queried content into sections
    - Differentiate for grades 3, 4, 5
    - Add teaching notes

STAGE 5: EXPORT TO DELIVERABLES
└─> Final lesson ready for classroom
    - Move to 05_DELIVERABLES/
    - Generate slides, worksheets, handouts
```

---

## STAGE 1: INPUT

### What Lands Here:
- **Location:** `01_INPUT/AI_Outputs_Raw/`
- **Content:** PDFs, research notes, images, web exports
- **No organization needed:** Just drop it here

### Example Files:
- Mesopotamia research paper (PDF)
- Museum catalog images
- Myth translation (text file)
- Architectural diagrams

---

## STAGE 2: EXTRACTION & TAGGING

### Process:

For each piece of INPUT content:

#### Step 1: Identify Content Type
**What is this?**
- [ ] Myth narrative
- [ ] Artifact description
- [ ] Deity information
- [ ] STEM innovation
- [ ] Image

#### Step 2: Use Appropriate Template
**Create new database entry:**

**For MYTH:**
```bash
Location: 02_DATABASE/Myths/
Template: Myth_Template.md
```

**For ARTIFACT:**
```bash
Location: 02_DATABASE/Artifacts/
Template: Artifact_Template.md
```

**For DEITY:**
```bash
Location: 02_DATABASE/Deities/
Template: Deity_Template.md
```

**For STEM:**
```bash
Location: 02_DATABASE/STEM_Innovations/
Template: Innovation_Template.md
```

**For IMAGE:**
```bash
Location: 02_DATABASE/Images/
Template: Image_Metadata_Template.md
```

#### Step 3: Fill Template with CRITICAL TAGS

**REQUIRED YAML TAGS (these enable automation):**

```yaml
---
# Week Assignment (REQUIRED)
week_number: 1  # Which week does this belong to?
weeks_used: [1, 8]  # If used in multiple weeks

# Geometric Element (REQUIRED)
geometric_element: circle  # circle, triangle, square, etc.
geometric_elements: [circle, radial-symmetry]  # If multiple

# Deity (REQUIRED if applicable)
deity: Shamash
deities: [Shamash, Ishtar]  # If multiple

# Content Type (REQUIRED)
content_type: myth  # myth, artifact, deity, stem_innovation, image

# Day Usage (REQUIRED)
day_a_usage: true  # Use in Day A?
day_b_usage: false  # Use in Day B?
day_a_section: 1  # Which Day A section? (1-7)
day_b_section: null  # Which Day B section? (1-6)

# MAGIC Category (REQUIRED)
magic_category: myth  # myth, artifact, geometric_element, innovation, ceremonial

# Status (REQUIRED)
status: ready  # draft, ready, needs_images, needs_verification

# Tags for Search (REQUIRED)
tags: [myth, circle, shamash, epic-of-gilgamesh, eight-winds, week-1]
---
```

---

## STAGE 3: AUTOMATED QUERIES (The Magic!)

### Lesson Outlines Auto-Populate

**Location:** `00_SYSTEM/Lesson_Outlines_Index.md`

This file uses **Dataview queries** to automatically pull content from database based on tags.

---

### Example Query Structure:

```markdown
# Week 1: Circle - Shamash

## MYTH CONTENT

```dataview
TABLE
  title AS "Myth",
  day_a_section AS "Day A Section",
  file.link AS "Link"
FROM "02_DATABASE/Myths"
WHERE week_number = 1
  AND geometric_element = "circle"
  AND status = "ready"
SORT day_a_section ASC
```

## ARTIFACTS CONTENT

```dataview
TABLE
  artifact_name AS "Artifact",
  catalog_number AS "Museum ID",
  day_a_section AS "Section",
  visual_clarity AS "Quality",
  file.link AS "Link"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND contains(geometric_elements, "circle")
  AND status = "ready"
SORT day_a_section ASC, visual_clarity DESC
```

## STEM INNOVATIONS

```dataview
TABLE
  innovation_name AS "Innovation",
  category AS "Type",
  day_b_section AS "Day B Section",
  file.link AS "Link"
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 1
  AND contains(geometric_elements, "circle")
  AND status = "ready"
SORT day_b_section ASC
```

## IMAGES INVENTORY

```dataview
TABLE
  image_name AS "Image",
  source_museum AS "Source",
  day_a_section AS "Day A",
  day_b_section AS "Day B",
  file.link AS "Link"
FROM "02_DATABASE/Images"
WHERE week_number = 1
SORT day_a_section ASC, day_b_section ASC
```

## GAPS - WHAT'S MISSING?

```dataview
TABLE
  title AS "Incomplete Item",
  status AS "Status",
  file.link AS "Link"
FROM "02_DATABASE"
WHERE week_number = 1
  AND status != "ready"
SORT content_type ASC
```
```

---

### What This Gives You:

When you open `Lesson_Outlines_Index.md`, you instantly see:

✅ **All myths for Week 1** (ready to use)
✅ **All artifacts for Week 1** (with museum IDs)
✅ **All STEM content for Week 1** (organized by Day B section)
✅ **All images for Week 1** (showing which section they go in)
✅ **What's missing** (gaps to fill)

**No manual searching!** Tags do the work.

---

## STAGE 4: LESSON ASSEMBLY

### Using the Outline to Build Lessons

#### Step 1: Open Lesson Outline
```
File: 00_SYSTEM/Lesson_Outlines_Index.md
Navigate to: Week 1 section
```

Dataview shows you all Week 1 content automatically.

#### Step 2: Create New Lesson File
```
Location: 03_PRODUCTION/Outlines/
Filename: Week-01-Circle-Shamash-LESSON.md
Template: Use Week_Template_Outline.md
```

#### Step 3: Click Through and Copy Content

**For Day A Section 1 (Myth):**
1. Dataview shows: [[Epic-of-Gilgamesh-Eight-Winds]]
2. Click link to open full myth
3. Copy narrative text
4. Paste into Day A Section 1 of lesson

**For Day A Section 3 (Iconography):**
1. Dataview shows: [[Tablet-of-Shamash-BM-91000]]
2. Click link to open artifact entry
3. Copy artifact description
4. Paste into Day A Section 3

**For Day A Section 4 (Visual Saturation):**
1. Dataview shows: All artifacts tagged with week_number=1
2. Click through each
3. Copy examples for sacred architecture, ritual objects, etc.
4. Paste into appropriate subsections

**For Day B Section 1 (Architecture):**
1. Dataview shows STEM innovations tagged day_b_section=1
2. Click through
3. Copy engineering explanations
4. Paste into Day B Section 1

**Repeat for all sections.**

---

#### Step 4: Differentiate for Grades

Each database entry includes:
```yaml
grade_3_usage: "Simple observation"
grade_4_usage: "Basic calculations"
grade_5_usage: "Advanced formulas"
```

Copy appropriate version into lesson.

---

#### Step 5: Add Images

Dataview shows all images for Week 1 with tags indicating which section.

```dataview
TABLE image_name, day_a_section, file.link
FROM "02_DATABASE/Images"
WHERE week_number = 1 AND day_a_section = 1
```

Shows you exactly which images go in Day A Section 1.

Copy image paths into lesson.

---

## STAGE 5: EXPORT TO DELIVERABLES

### Finalize and Move

Once lesson is complete:

```bash
FROM: 03_PRODUCTION/Outlines/Week-01-Circle-Shamash-LESSON.md
TO: 05_DELIVERABLES/Lesson_Plans_Final/Grade3/Week_01_Circles/
```

### Generate Artifacts:
- Export markdown to PDF
- Generate slides from lesson sections
- Create worksheets from activities
- Package all Week 1 materials together

---

## THE POWER OF THIS SYSTEM

### Before (Manual):
1. Search for Week 1 content across folders ❌
2. Remember which artifacts have good images ❌
3. Find that one myth you saved somewhere ❌
4. Check if you have STEM content ❌
5. Manually assemble everything ❌
6. Miss something important ❌

**Time:** Hours of frustration

### After (Automated):
1. Open Lesson_Outlines_Index.md ✅
2. Dataview shows ALL Week 1 content automatically ✅
3. Click links, copy content ✅
4. Paste into template ✅
5. Differentiate for grades ✅
6. Export ✅

**Time:** 30-45 minutes

---

## KEY SUCCESS FACTORS

### 1. TAG CONSISTENTLY

Every database entry MUST have:
```yaml
week_number: X
geometric_element: {element}
content_type: {type}
day_a_section: X  # or null
day_b_section: X  # or null
status: ready  # or draft
```

**If you forget tags, content won't appear in queries!**

---

### 2. USE STANDARD VALUES

Don't vary tag values:

**✅ CORRECT:**
```yaml
geometric_element: circle
geometric_element: triangle
geometric_element: square
```

**❌ WRONG:**
```yaml
geometric_element: Circle  # Capital
geometric_element: circles  # Plural
geometric_element: round shape  # Different term
```

Use the EXACT same value every time or queries break.

---

### 3. ASSIGN SECTIONS ACCURATELY

Day A has 7 sections, Day B has 6 sections.

Tag with correct section number so content appears in right place.

**Example:**
- Myth → `day_a_section: 1`
- SEL prompts → `day_a_section: 2`
- Iconography → `day_a_section: 3`
- Visual saturation → `day_a_section: 4`
- Decomposition → `day_a_section: 5`
- Hands-on → `day_a_section: 6`
- Bridge → `day_a_section: 7`

---

### 4. MARK STATUS

Only items with `status: ready` appear in main queries.

Use `status: draft` for incomplete items.

Separate query shows gaps.

---

## TEMPLATES FOR EACH DATABASE TYPE

### Myth Template:
```
Location: 02_DATABASE/Myths/Myth_Template.md
Use for: Narrative texts
Tags needed: week_number, geometric_element, deity
```

### Artifact Template:
```
Location: 02_DATABASE/Artifacts/Artifact_Template.md
Use for: Museum objects
Tags needed: week_number, geometric_elements, catalog_number
```

### Deity Template:
```
Location: 02_DATABASE/Deities/Deity_Template.md
Use for: God/goddess information
Tags needed: associated_geometric_elements, primary_myth
```

### STEM Template:
```
Location: 02_DATABASE/STEM_Innovations/Innovation_Template.md
Use for: Inventions, math, engineering
Tags needed: week_number, geometric_element, day_b_section
```

### Image Metadata Template:
```
Location: 02_DATABASE/Images/Image_Template.md
Use for: Every image
Tags needed: week_number, day_a_section, day_b_section, source_artifact
```

---

## DAILY WORKFLOW

### When New Content Arrives:

**Morning (15 min):**
1. Check `01_INPUT/` for new materials
2. Identify content type
3. Create database entry with template
4. Add YAML tags
5. Save to appropriate folder

**Afternoon (30 min):**
1. Open `Lesson_Outlines_Index.md`
2. Check which weeks are complete
3. Identify gaps
4. Prioritize what to research next

**Weekly (2 hours):**
1. Pick one week to complete
2. Use outline queries to check what exists
3. Fill gaps in database
4. Assemble lesson from outline
5. Differentiate for grades
6. Export to deliverables

---

## NEXT STEPS TO IMPLEMENT

### Phase 1: Create Templates (30 min)
- [ ] Create Myth_Template.md
- [ ] Create Artifact_Template.md
- [ ] Create Deity_Template.md
- [ ] Create Innovation_Template.md
- [ ] Create Image_Template.md

### Phase 2: Set Up Folders (10 min)
- [ ] Create 02_DATABASE/Myths/
- [ ] Create 02_DATABASE/Artifacts/
- [ ] Create 02_DATABASE/Deities/
- [ ] Create 02_DATABASE/STEM_Innovations/
- [ ] Create 02_DATABASE/Images/

### Phase 3: Create Automated Outlines (20 min)
- [ ] Create Lesson_Outlines_Index.md
- [ ] Add Dataview queries for each week
- [ ] Test queries with sample data

### Phase 4: Populate One Complete Week (3-4 hours)
- [ ] Choose Week 1 (Circle - Shamash)
- [ ] Create 5-8 database entries (myth, artifacts, deity, STEM)
- [ ] Tag everything correctly
- [ ] Verify queries work
- [ ] Assemble complete lesson

### Phase 5: Replicate for 16 Weeks (ongoing)
- [ ] Weeks 2-16 follow same process
- [ ] Each week gets faster as you internalize workflow

---

Would you like me to:
1. Create the actual template files now?
2. Set up the Lesson_Outlines_Index with Dataview queries?
3. Populate Week 1 as a complete working example?

Let me know what you've gathered and we'll start implementing!
