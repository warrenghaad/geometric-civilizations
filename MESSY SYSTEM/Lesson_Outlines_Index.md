# Lesson Outlines Index - Auto-Generated from Database
**Purpose:** Automated view of all curriculum content organized by week
**How it Works:** Dataview queries pull content based on YAML tags
**Last Updated:** Auto-updates when database changes

---

## HOW TO USE THIS FILE

**This file automatically shows you:**
1. What content exists for each week
2. Which sections content belongs in
3. What's missing (gaps to fill)
4. Quick links to full database entries

**To build a lesson:**
1. Navigate to your week below
2. Click links to open full content
3. Copy relevant sections
4. Paste into lesson template
5. Differentiate for grades 3, 4, 5

---

## QUICK NAVIGATION

[[#Week 1 Circle - Shamash|Week 1]] • [[#Week 2|Week 2]] • [[#Week 3|Week 3]] • [[#Week 4|Week 4]] • [[#Week 5|Week 5]] • [[#Week 6|Week 6]] • [[#Week 7|Week 7]] • [[#Week 8|Week 8]] • [[#Week 9|Week 9]] • [[#Week 10|Week 10]] • [[#Week 11|Week 11]] • [[#Week 12|Week 12]] • [[#Week 13|Week 13]] • [[#Week 14|Week 14]] • [[#Week 15|Week 15]] • [[#Week 16|Week 16]]

---

# Week 1: Circle - Shamash

## Week 1 Overview

**Geometric Element:** Circle
**Deity:** Shamash (Sun God)
**Core Metaphor:** Circle = Impartial Justice (reaches all equally from center)
**Primary Myth:** Epic of Gilgamesh - Eight Winds Episode

---

## 📖 MYTHS (Day A Section 1)

```dataview
TABLE
  title AS "Myth Title",
  primary_source AS "Source",
  duration AS "Duration",
  geometric_elements AS "Geometric Focus",
  file.link AS "Full Content"
FROM "02_DATABASE/Myths"
WHERE week_number = 1
  AND status = "ready"
SORT day_a_section ASC
```

**If empty:** No myths tagged for Week 1 yet. Create myth entry with `week_number: 1`

---

## 🏺 ARTIFACTS (Day A Sections 3-4)

### Day A Section 3: Iconography (Mythic Art)

```dataview
TABLE
  artifact_name AS "Material Object",
  primary_element AS "Geometric Element",
  semiotic_meaning AS "Metaphor/Meaning",
  visual_clarity AS "Image Quality",
  file.link AS "Details"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND day_a_section = 3
  AND status = "ready"
SORT visual_clarity DESC
```

### Day A Section 4: Visual Saturation (Material Culture)

#### 4A: Sacred Architecture

```dataview
TABLE
  artifact_name AS "Structure",
  location AS "Location",
  geometric_elements AS "Geometric Features",
  file.link AS "Details"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND day_a_section = 4
  AND contains(tags, "sacred-architecture")
  AND status = "ready"
```

#### 4B: Ritual Objects

```dataview
TABLE
  artifact_name AS "Object",
  catalog_number AS "ID",
  ritual_function AS "Used In",
  file.link AS "Details"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND day_a_section = 4
  AND contains(tags, "ritual-object")
  AND status = "ready"
```

#### 4C: Economic/Agricultural Objects

```dataview
TABLE
  artifact_name AS "Object",
  economic_function AS "Purpose",
  file.link AS "Details"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND day_a_section = 4
  AND contains(tags, "economic-object")
  AND status = "ready"
```

#### 4D: Domestic Objects

```dataview
TABLE
  artifact_name AS "Object",
  domestic_message AS "Daily Message",
  file.link AS "Details"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND day_a_section = 4
  AND contains(tags, "domestic-object")
  AND status = "ready"
```

---

## 🏛️ ARCHITECTURAL BRIDGE (Day A Section 7)

```dataview
TABLE
  artifact_name AS "Structure",
  form_meaning AS "Form (Symbolic)",
  function_engineering AS "Function (Practical)",
  file.link AS "Full Analysis"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 1
  AND day_a_section = 7
  AND contains(tags, "architecture-bridge")
  AND status = "ready"
```

---

## 🔬 STEM INNOVATIONS (Day B)

### Day B Section 1: Architectural Innovation

```dataview
TABLE
  innovation_name AS "Innovation",
  problem_solved AS "Problem Solved",
  geometric_principle AS "Geometric Principle Used",
  file.link AS "Full Content"
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 1
  AND day_b_section = 1
  AND status = "ready"
```

### Day B Section 2: Mathematical Principles

```dataview
TABLE
  innovation_name AS "Mathematical Discovery",
  mesopotamian_calculation AS "How They Did It",
  modern_formula AS "Modern Expression",
  file.link AS "Full Content"
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 1
  AND day_b_section = 2
  AND status = "ready"
```

### Day B Section 3: Technological Inventions

```dataview
TABLE
  innovation_name AS "Invention",
  date_period AS "When Invented",
  impact AS "How It Changed Things",
  file.link AS "Full Content"
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 1
  AND day_b_section = 3
  AND status = "ready"
```

### Day B Section 5: Modern Legacy

```dataview
TABLE
  innovation_name AS "Ancient Innovation",
  modern_application AS "Modern Version",
  still_same AS "Why Still Works",
  file.link AS "Full Content"
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 1
  AND day_b_section = 5
  AND status = "ready"
```

---

## 🖼️ IMAGES INVENTORY (All Sections)

### Day A Images

```dataview
TABLE
  image_name AS "Image",
  source_artifact AS "From",
  day_a_section AS "Section",
  file.link AS "View"
FROM "02_DATABASE/Images"
WHERE week_number = 1
  AND day_a_section != null
  AND status = "ready"
SORT day_a_section ASC
```

### Day B Images

```dataview
TABLE
  image_name AS "Image",
  source_artifact AS "From",
  day_b_section AS "Section",
  file.link AS "View"
FROM "02_DATABASE/Images"
WHERE week_number = 1
  AND day_b_section != null
  AND status = "ready"
SORT day_b_section ASC
```

---

## ⚠️ GAPS - What's Missing for Week 1?

```dataview
TABLE
  title AS "Incomplete Item",
  content_type AS "Type",
  status AS "Current Status",
  file.link AS "Link"
FROM "02_DATABASE"
WHERE week_number = 1
  AND status != "ready"
SORT content_type ASC, status ASC
```

**How to fix gaps:**
1. Click link to incomplete item
2. Fill in missing information
3. Change `status: ready`
4. Item will appear in queries above

---

## 📊 COMPLETION STATUS for Week 1

```dataview
TABLE
  length(rows) AS "Count"
FROM "02_DATABASE"
WHERE week_number = 1
  AND status = "ready"
GROUP BY content_type
```

**Target Numbers:**
- Myths: 1-2 ✓
- Artifacts: 15-20 ✓
- STEM Innovations: 6-10 ✓
- Images: 40-50 ✓

---

---

# Week 2: Triangle - Sacred Mountain

## Week 2 Overview

**Geometric Element:** Triangle
**Deity:** {TBD - Possibly Enlil/An (mountain gods)}
**Core Metaphor:** Triangle = Hierarchical Ascension / Divine Realm
**Primary Myth:** {TBD - Creation myths, ziggurat symbolism}

---

## 📖 MYTHS (Day A Section 1)

```dataview
TABLE
  title AS "Myth Title",
  primary_source AS "Source",
  duration AS "Duration",
  geometric_elements AS "Geometric Focus",
  file.link AS "Full Content"
FROM "02_DATABASE/Myths"
WHERE week_number = 2
  AND status = "ready"
SORT day_a_section ASC
```

---

## 🏺 ARTIFACTS (Day A Sections 3-4)

### Iconography & Material Culture

```dataview
TABLE
  artifact_name AS "Artifact",
  catalog_number AS "Museum ID",
  day_a_section AS "Section",
  geometric_elements AS "Features",
  file.link AS "Details"
FROM "02_DATABASE/Artifacts"
WHERE week_number = 2
  AND status = "ready"
SORT day_a_section ASC
```

---

## 🔬 STEM INNOVATIONS (Day B)

```dataview
TABLE
  innovation_name AS "Innovation",
  day_b_section AS "Day B Section",
  geometric_principle AS "Geometric Principle",
  file.link AS "Full Content"
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 2
  AND status = "ready"
SORT day_b_section ASC
```

---

## ⚠️ GAPS - What's Missing for Week 2?

```dataview
TABLE
  title AS "Incomplete Item",
  content_type AS "Type",
  status AS "Current Status",
  file.link AS "Link"
FROM "02_DATABASE"
WHERE week_number = 2
  AND status != "ready"
```

---

---

# Week 3: Square - Ordered Earth

## Week 3 Overview

**Geometric Element:** Square/Rectangle
**Deity:** Marduk (Creator, establishes order)
**Core Metaphor:** Square = Bounded Order / Stable Foundation
**Primary Myth:** Enuma Elish (Creation Epic)

---

## 📖 MYTHS

```dataview
TABLE title, file.link
FROM "02_DATABASE/Myths"
WHERE week_number = 3 AND status = "ready"
```

## 🏺 ARTIFACTS

```dataview
TABLE artifact_name, catalog_number, day_a_section, file.link
FROM "02_DATABASE/Artifacts"
WHERE week_number = 3 AND status = "ready"
SORT day_a_section ASC
```

## 🔬 STEM INNOVATIONS

```dataview
TABLE innovation_name, day_b_section, file.link
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 3 AND status = "ready"
SORT day_b_section ASC
```

## ⚠️ GAPS

```dataview
TABLE title, content_type, status, file.link
FROM "02_DATABASE"
WHERE week_number = 3 AND status != "ready"
```

---

---

# Week 4: Eight-Pointed Star - Venus Cycle

## Week 4 Overview

**Geometric Element:** Eight-Pointed Star
**Deity:** Inanna/Ishtar (Love, War, Venus)
**Core Metaphor:** 8-Star = Divine Feminine Power / Cyclical Time
**Primary Myth:** Descent of Inanna

---

## 📖 MYTHS

```dataview
TABLE title, file.link
FROM "02_DATABASE/Myths"
WHERE week_number = 4 AND status = "ready"
```

## 🏺 ARTIFACTS

```dataview
TABLE artifact_name, catalog_number, day_a_section, file.link
FROM "02_DATABASE/Artifacts"
WHERE week_number = 4 AND status = "ready"
SORT day_a_section ASC
```

## 🔬 STEM

```dataview
TABLE innovation_name, day_b_section, file.link
FROM "02_DATABASE/STEM_Innovations"
WHERE week_number = 4 AND status = "ready"
SORT day_b_section ASC
```

## ⚠️ GAPS

```dataview
TABLE title, content_type, status, file.link
FROM "02_DATABASE"
WHERE week_number = 4 AND status != "ready"
```

---

---

# Weeks 5-16: Template Structure

_Copy structure from Weeks 1-4 for remaining weeks_

---

## Week 5: Crescent - Moon Cycles
## Week 6: Hexagon - Sacred Geometry
## Week 7: Spiral - Growth Patterns
## Week 8: Rosette - Cosmic Flower
## Week 9: Composite Shapes - Complex Integration
## Week 10: Tessellations - Infinite Patterns
## Week 11: Symmetry - Balance and Order
## Week 12: Proportion - Mathematical Ratios
## Week 13: Angles - Directional Meaning
## Week 14: Curves - Fluid vs Fixed
## Week 15: Three-Dimensional Forms - Depth
## Week 16: Integration - All Elements Combined

---

---

# GLOBAL QUERIES (All Weeks)

## All Ready Content by Type

```dataview
TABLE
  length(rows) AS "Count",
  list(rows.file.link) AS "Items"
FROM "02_DATABASE"
WHERE status = "ready"
GROUP BY content_type
```

---

## All Incomplete Content (Needs Work)

```dataview
TABLE
  week_number AS "Week",
  content_type AS "Type",
  status AS "Status",
  file.link AS "Link"
FROM "02_DATABASE"
WHERE status != "ready"
SORT week_number ASC, content_type ASC
```

---

## Images by Week (Count)

```dataview
TABLE
  length(rows) AS "Image Count"
FROM "02_DATABASE/Images"
WHERE status = "ready"
GROUP BY week_number
SORT week_number ASC
```

---

## Artifacts by Museum

```dataview
TABLE
  length(rows) AS "Count",
  list(rows.catalog_number) AS "Catalog Numbers"
FROM "02_DATABASE/Artifacts"
WHERE status = "ready"
GROUP BY museum
```

---

## STEM Innovations by Category

```dataview
TABLE
  length(rows) AS "Count"
FROM "02_DATABASE/STEM_Innovations"
WHERE status = "ready"
GROUP BY category
```

---

# QUICK STATS DASHBOARD

## Overall Progress

```dataview
TABLE
  length(rows.week_number) AS "Weeks with Content"
FROM "02_DATABASE"
WHERE status = "ready"
GROUP BY "Total Weeks Covered"
```

## Content Breakdown

```dataview
TABLE WITHOUT ID
  content_type AS "Content Type",
  length(rows) AS "Ready Items",
  length(filter(rows, (r) => r.status = "draft")) AS "Draft Items",
  length(filter(rows, (r) => r.status = "needs_images")) AS "Needs Images"
FROM "02_DATABASE"
GROUP BY content_type
```

---

# MAINTENANCE NOTES

## How to Keep This Working

### When Adding New Content:
1. Create database entry with template
2. Add REQUIRED tags:
   - `week_number: X`
   - `content_type: {type}`
   - `geometric_element: {element}`
   - `day_a_section: X` or `day_b_section: X`
   - `status: ready` (when complete)
3. Save to correct folder in `02_DATABASE/`
4. This file auto-updates (no manual editing needed!)

### If Queries Show Empty:
- Check that files are in `02_DATABASE/` folders
- Check that YAML tags exist and are spelled correctly
- Check that `status: ready` is set
- Check that `week_number` matches week you're viewing

### Common Issues:
- **"No results"** → Files not tagged properly
- **"Wrong section"** → `day_a_section` or `day_b_section` incorrect
- **"Missing items"** → `status` not set to "ready"
- **"Can't find week"** → `week_number` not set or wrong

---

**Next Steps:**
1. Create database templates with correct YAML structure
2. Populate Week 1 content as proof of concept
3. Verify all queries work
4. Replicate for 16 weeks

---

**Related Files:**
- [[DATABASE_SCHEMA]] - Database structure explanation
- [[WORKFLOW_INPUT_TO_LESSON]] - Full workflow documentation
- [[Week_Template_Outline]] - Lesson template to fill from this outline
