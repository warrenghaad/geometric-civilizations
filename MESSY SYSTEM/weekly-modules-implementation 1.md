---
title: weekly-modules-implementation
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

# Weekly Modules Database Schema - Implementation Guide

## HOW THIS SCHEMA COMPLETES YOUR CURRICULUM OUTLINES

Your SQL schema creates the backbone for organizing what you've already outlined. Here's the practical mapping:

---

## TABLE 1: `weekly_modules`
**Purpose:** Master tracking for all 8 weeks × 3 grades = 24 unique module configurations

### Real Examples from Your Curriculum:

```sql
-- GRADE 3, WEEK 1: THE WHEEL
INSERT INTO weekly_modules (
  week_number, 
  geometric_element, 
  element_type, 
  complexity_level,
  day_a_focus,
  day_a_primary_myth,
  day_a_metaphor,
  day_a_image_count,
  day_b_focus,
  day_b_mathematical_principles,
  day_b_innovations,
  architectural_bridge
) VALUES (
  1, 
  'Circle',
  'atomic',
  'foundational',
  -- Day A Data
  'The Potter''s Wheel as Gift of Wisdom',
  'Enki invents the wheel to ease human labor; Anu, Enlil, and Enki debate which god provides the greatest gift to humanity',
  'Rotation as symbol of progress and interconnection; the wheel connects us across distances',
  8,  -- image count: The Hero with Two Faces (Enki), potter wheel diagrams, ancient Mesopotamian wheels, chariot wheels, etc.
  -- Day B Data
  'Circle geometry, rotation mechanics, radius/diameter/circumference relationships',
  '["radius definition: half the diameter", "diameter definition: widest point", "circumference = π × d", "axle alignment for stability", "rotational force distribution"]',
  '["Potter''s wheel (rotation technology)", "Chariot wheels (transportation)", "Pulley systems (mechanical advantage)", "Rotation in modern machinery"]',
  'Ziggurat as stack of receding circles (viewed from above); concentric temple chambers'
);

-- GRADE 4, WEEK 2: IRRIGATION
INSERT INTO weekly_modules VALUES (
  10,
  'Network/Flow',
  'complex',
  'intermediate',
  'Controlling Water = Controlling Life',
  'Enki (water god) teaches humans to channel rivers; narrative of co-creation and resource management',
  'Water as lifeblood; channels as veins of civilization; networks as nervous systems',
  12,
  'Canal geometry, angles for water flow, elevation calculations, network topology',
  '["flow rate physics", "gravity angle optimization", "elevation drop calculations", "intersection design", "junction angles for flow splitting"]',
  '["Canal systems (hydraulic engineering)", "Shaduf water lifts (mechanical engineering)", "Aqueducts (civil engineering)", "Modern irrigation networks"]',
  'Bridge: Canals connect ziggurats (temples receive water); channels create boundaries (square city grids)'
);

-- GRADE 5, WEEK 5: PYTHAGOREAN THEOREM (Historical Babylon)
INSERT INTO weekly_modules VALUES (
  37,
  'Right Triangle',
  'atomic',
  'advanced',
  'The Secret of Plimpton 322: Babylonian Mathematics 1000 Years Before Pythagoras',
  'Scribes in King Hammurabi''s court discover perfect mathematical relationships hidden in the stars and measured in land surveys',
  'The right angle as moment of perfect balance; theorem as proof that the universe obeys mathematical law',
  15,
  'Pythagorean theorem (a² + b² = c²), Pythagorean triples, right triangle identification, surveying applications',
  '["3-4-5 verification", "5-12-13 triple", "8-15-17 triple", "Plimpton 322 tablet analysis", "Proof via area decomposition"]',
  '["Land surveying (Si.427 tablet)", "Right angle construction", "Distance calculations", "Modern construction right-angles"]',
  'Bridge: Plimpton 322 proves cosmic order (same mathematical laws everywhere); connects to astronomy (Babylonian star charts)'
);
```

---

## TABLE 2: `ontology_stages`
**Purpose:** Track which stage each lesson/artifact belongs to across the 3-stage model

### How It Works:

```sql
-- STAGE 1: MYTH-AND-ART (Emotional/Narrative Foundation)
INSERT INTO ontology_stages (
  artifact_id,
  stage,
  stage_name,
  notes
) VALUES (
  1,  -- Grade 3, Week 1 Circle lesson
  1,
  'myth-and-art',
  'Enki myth establishes emotional connection to the wheel as gift and labor-saving device; 
   creates meaning frame for students before mathematical analysis'
);

-- STAGE 2: INSTITUTIONALIZATION (Formal Systems)
INSERT INTO ontology_stages VALUES (
  1,
  2,
  'institutionalization',
  'Formula (C = πd) becomes standardized; scribal tradition records measurements on clay tablets; 
   potter''s guild establishes wheel specifications and training protocols'
);

-- STAGE 3: INNOVATION (Extension & New Applications)
INSERT INTO ontology_stages VALUES (
  1,
  3,
  'innovation',
  'Chariot wheels enable transportation; pulley combinations multiply mechanical advantage; 
   modern rotational technology (motors, turbines, bearings) extends the principle 1000s of years later'
);
```

**THIS SOLVES YOUR IMMEDIATE PROBLEM:** Your curriculum already maps to these three stages; this database just ORGANIZES the data so you can query by stage.

---

## TABLE 3: `material_culture_categories`
**Purpose:** Organize the hundreds of Mesopotamian objects you're already researching

### Examples from Your Work:

```sql
-- From your Circle research (Mesopotamia document)
INSERT INTO material_culture_categories (
  name,
  category_type,
  description
) VALUES 
  ('Potter''s Wheel', 'architecture', 'Rotating ceramic tool; connects rotation principle to everyday craftsmanship; found in archaeological sites from Uruk period onward'),
  ('Cylinder Seals', 'ritual', 'Small carved cylinders rolled onto clay; circular impression creates continuous bands of imagery; both decorative and administrative'),
  ('Royal Headdress with Circular Ornaments', 'domestic', 'Queen Puabi''s crown from Royal Tombs of Ur; circular rosettes arranged in bands; demonstrates status through geometric perfection'),
  ('Chariot Wheels', 'economic', 'Mesopotamian innovations in wheel design (6-spoked, 8-spoked); enabled rapid military movement and trade; archaeological evidence from Mari and Ur'),
  ('Temple Rosette Decoration', 'ritual', '6, 8, or 12-pointed circular flower motif; symbol of Ishtar; appears on walls, vessels, jewelry; protective function in sacred spaces'),
  ('Shamash Sun Disk Symbol', 'ritual', 'Circle with four cardinal points and radiating lines; represents solar justice god; carved on boundary stones (kudurrus), seals, stelae');

-- Later query to organize your lessons:
SELECT * FROM material_culture_categories WHERE category_type = 'domestic'
-- Returns: objects for "Day A: Art & Craft" segment of lessons
```

---

## TABLE 4: `stem_innovations`
**Purpose:** Track the STEM innovations you've already mapped (but now queryable)

### Examples from Your 8-Week Structure:

```sql
-- GRADE 3 INNOVATIONS
INSERT INTO stem_innovations VALUES (NULL, 'Potter''s Wheel', 'technological', 'Circle', 'Rotation at fixed axle', 'Modern pottery, industrial turbines, bearings', 1);
INSERT INTO stem_innovations VALUES (NULL, 'Cuneiform Writing System', 'technological', 'Grid + Angle', 'Geometric compression of meaning; angles convey information', 'Alphabet, digital encoding, binary', 2);
INSERT INTO stem_innovations VALUES (NULL, 'Ziggurat Construction', 'architectural', 'Square', 'Stacking receding squares for stability', 'Modern setback buildings, pyramids, dome architecture', 3);

-- GRADE 4 INNOVATIONS
INSERT INTO stem_innovations VALUES (NULL, 'Irrigation Networks', 'engineering', 'Network', 'Optimal angle calculations for water flow', 'Modern hydroelectric systems, plumbing', 10);
INSERT INTO stem_innovations VALUES (NULL, 'Cylinder Seal Printing', 'technological', 'Circle + Grid', 'Rotational printing; first mass production method', 'Printing press, lithography, textile printing', 11);

-- GRADE 5 INNOVATIONS
INSERT INTO stem_innovations VALUES (NULL, 'Plimpton 322 Mathematics', 'mathematical', 'Right Triangle', 'Discovery of Pythagorean theorem 1000 years before Pythagoras', 'All right-angle engineering, surveying, architecture', 37);
INSERT INTO stem_innovations VALUES (NULL, 'Babylonian Astronomy Charts', 'mathematical', 'Circle + Coordinate', 'Prototypical coordinate system for tracking planets', 'Modern astronomy, GPS, satellite navigation', 38);
```

---

## HOW TO USE THESE TABLES TO FINISH YOUR OUTLINES

### Goal 1: Complete the Grade 4 & 5 Full Lessons
**You have:** Detailed week-by-week outlines with focus areas, myths, math  
**You need:** Full 100-minute lesson structures (like your Week 3 Square HTML slides)

```sql
-- Query: "Give me all Grade 5 weeks that need full lesson development"
SELECT week_number, geometric_element, day_a_focus, day_b_focus
FROM weekly_modules
WHERE complexity_level = 'advanced'  -- Grade 5
ORDER BY week_number;

-- Returns weeks 33-40 with all metadata needed to generate HTML slides
```

**Action:** Use these query results as structured input to Claude to generate Week 4-8 HTML presentations (same format as your Week 3 Square slides)

---

### Goal 2: Create Assessment Rubrics Tied to Ontology Stages
**You have:** Assessment ideas in Grade 5 TO-DO  
**You need:** Rubrics that explicitly measure progress through myth→institution→innovation stages

```sql
-- Create assessment map:
SELECT 
  wm.week_number,
  wm.geometric_element,
  os.stage_name,
  'What should students demonstrate?' as assessment_question
FROM weekly_modules wm
JOIN ontology_stages os ON wm.id = os.artifact_id
ORDER BY wm.week_number, os.stage;

-- Build rubric scoring around 3-stage progression
-- Stage 1 (Myth-Art): Can student explain emotional/narrative meaning?
-- Stage 2 (Institution): Can student apply formula and record data?
-- Stage 3 (Innovation): Can student extend principle to new context?
```

---

### Goal 3: Organize Your Massive Image & Resource Library
**You have:** 50+ images of Mesopotamian circles, 30+ architectural photos, hundreds of artworks  
**You need:** Systematic tagging so teachers can find "Show me an example of circular rosettes on textiles"

```sql
-- In your image metadata:
-- file: mesopotamian_jewelry_royal_tombs_ur_rosettes.jpg
-- artifact_type: 'jewelry'
-- category_id: (links to material_culture_categories)
-- week_number: 1  (fits into Circle week)
-- stage: 1  (myth-art stage, emotional impact)
-- alt_text: 'Queen Puabi''s circular gold rosettes arranged in concentric bands'

-- Query: "Get all images for Grade 3 Week 1 that show geometric precision in handcrafts"
SELECT image_file, alt_text
FROM images
WHERE week_number = 1 
  AND category_id IN (SELECT id FROM material_culture_categories WHERE category_type = 'domestic')
  AND stage = 1;
```

---

## IMMEDIATE NEXT STEPS

### Phase 1: Populate Your Database (1-2 days)
1. Run the 4 CREATE TABLE statements ✓
2. Manually insert data for weeks 1-8 (use examples above as templates)
3. Link your existing research to week numbers and stages

### Phase 2: Generate Missing HTML Slides (3-5 days)
1. Query database for Weeks 4-8 metadata
2. Feed to Claude with same template as Week 3 Square
3. Generate 5 × 20-slide presentations (16:9 format, visually rich)

### Phase 3: Build Assessment Framework (2-3 days)
1. Create rubrics for each stage (myth-art, institution, innovation)
2. Link to learning outcomes
3. Connect to Common Core standards

### Phase 4: Organize Resource Library (2-3 days)
1. Tag all 100+ images with metadata
2. Create image picker tool (optional but useful)
3. Build image galleries for each week

---

## THE BIG PICTURE

Your SQL schema doesn't just organize data—it **completes your pedagogical vision**:

✅ **Weekly Modules** = What you teach (content)  
✅ **Ontology Stages** = How it progresses (progression)  
✅ **Material Culture Categories** = Where meaning lives (objects)  
✅ **STEM Innovations** = Why it matters (impact)

Together, they ensure your curriculum is:
- **Coherent** (each piece connects to the whole)
- **Queryable** (teachers can find anything fast)
- **Scalable** (easy to add more grades/subjects)
- **Data-driven** (evidence of student progression)

---

## QUICK SQL TEMPLATE FOR YOUR NEXT FULL LESSON

Use this whenever generating Weeks 4-8 slides:

```sql
SELECT 
  'METADATA FOR WEEK ' || week_number || ': ' || geometric_element as week_title,
  day_a_focus as day_a_content,
  day_a_primary_myth as mythological_foundation,
  day_a_metaphor as emotional_anchor,
  day_b_focus as math_content,
  day_b_mathematical_principles as formulas,
  day_b_innovations as modern_applications,
  architectural_bridge as synthesis_concept,
  complexity_level as cognitive_level
FROM weekly_modules
WHERE week_number = ?;
-- Replace ? with 4, 5, 6, 7, or 8 for next lessons
```

**Ready to build your database and generate the remaining 5 weeks of HTML slides?**