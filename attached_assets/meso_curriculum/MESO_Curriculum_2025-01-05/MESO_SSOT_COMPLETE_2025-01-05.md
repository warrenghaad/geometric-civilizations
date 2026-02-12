# MESO Program - Single Source of Truth (SSOT)
## Complete Specification Document
**Version**: 1.0  
**Date**: 2025-01-05  
**Status**: AUTHORITATIVE  
**Scope**: Grades 3, 4, and 5 ONLY

---

## 🎯 EXECUTIVE SUMMARY

This document is the **Single Source of Truth** for the MESO (Mesopotamian Educational Standards Optimization) Program. It defines ALL standards, naming conventions, database schemas, asset specifications, and quality requirements for curriculum materials spanning Grades 3-5.

### Critical Constraints
- ✅ **Permitted Grades**: 3, 4, 5 ONLY
- ❌ **Prohibited**: Any Grade 1, Grade 2, or Grade 6+ content
- 🔄 **Legacy Content**: All existing Grade 1 materials are DEPRECATED and must be remapped to Grade 3-5

### Document Authority
This SSOT supersedes all previous specifications. Any conflicting documentation is deprecated. This document is the ONLY authoritative source for:
- File naming conventions
- Directory structure
- Database schemas
- Asset specifications
- Quality standards
- Accessibility requirements
- Canva integration

---

## 📐 SECTION 1: PROGRAM IDENTITY

### Program Overview
**Name**: MESO (Mesopotamian Educational Standards Optimization)  
**Educational Domain**: Ancient Mesopotamian civilization integrated with:
- Mathematics (geometry, measurement, fractions)
- Social-Emotional Learning (SEL)
- Cultural studies
- Arts integration

### Grade Specifications

#### Grade 3 (Foundation)
- **Focus**: Basic geometric shapes (circles, triangles, rectangles)
- **Concepts**: Perimeter, area fundamentals, symmetry
- **Mesopotamian Context**: Basic artifacts, simple myths
- **SEL Themes**: Sharing, fairness, community

#### Grade 4 (Development)
- **Focus**: Complex shapes, composite figures, fractions
- **Concepts**: Area of composite shapes, angles, rotational symmetry
- **Mesopotamian Context**: Architecture, measurement systems
- **SEL Themes**: Justice, balance, cooperation

#### Grade 5 (Mastery)
- **Focus**: Advanced geometry, coordinate systems, volume
- **Concepts**: 3D shapes, transformations, mathematical patterns
- **Mesopotamian Context**: Advanced mathematics, astronomy
- **SEL Themes**: Wisdom, leadership, interconnection

### Content Structure (Per Lesson)
Each lesson contains 7 pedagogical sections:
1. **Myth + SEL** (Image moral)
2. **Geometric Element + Link**
3. **Hands-on Build**
4. **Guided Practice**
5. **Workshop Application**
6. **Assessment Prompt**
7. **Reflection + Share**

---

## 🗂️ SECTION 2: DIRECTORY STRUCTURE (CANONICAL)

### Root Structure (Mandatory)
```
/MESO_Program/
├── Grade_3/
│   ├── G3_1A_SunCircleSharing/
│   ├── G3_1B_MoonCrescent/
│   └── [Additional G3 lessons...]
├── Grade_4/
│   ├── G4_1A_MardukSquare/
│   └── [Additional G4 lessons...]
├── Grade_5/
│   ├── G5_1A_GilgameshHexagon/
│   └── [Additional G5 lessons...]
├── _System/
│   ├── SSOT/
│   ├── Templates/
│   ├── Validation/
│   └── Archive/
└── _Documentation/
    ├── Standards_Alignment/
    ├── Accessibility_Compliance/
    └── Quality_Assurance/
```

### Individual Lesson Structure (Mandatory)
```
/Grade_X/GX_YZ_LessonName/
├── 01_eTextbook/
│   └── meso_GX_YZ_eTextbook_v##.pdf
├── 02_Slides/
│   └── meso_GX_YZ_Slides_v##.pptx
├── 03_TeacherScript/
│   └── meso_GX_YZ_TeacherScript_v##.pdf
├── 04_Worksheet/
│   └── meso_GX_YZ_Worksheet_v##.pdf
├── 05_Templates/
│   └── meso_GX_YZ_Templates_v##.pdf
├── 06_Rubrics/
│   └── meso_GX_YZ_RubricsExemplars_v##.pdf
├── 07_Attribution/
│   └── meso_GX_YZ_Attribution_v##.pdf
└── Assets/
    ├── Images/
    │   ├── Myth_Illustrations/
    │   ├── Geometric_Diagrams/
    │   ├── Artifact_Photos/
    │   ├── Student_Work_Examples/
    │   └── UI_Elements/
    ├── Overlays/
    │   ├── Geometric_Constructions/
    │   ├── Measurement_Tools/
    │   ├── Highlight_Layers/
    │   └── Animation_Guides/
    ├── Audio/
    │   ├── Narration/
    │   ├── Sound_Effects/
    │   └── Background_Music/
    ├── Video/
    │   ├── Standard_Motion/
    │   ├── Reduced_Motion/
    │   └── Static_Alternatives/
    └── Metadata/
        ├── Asset_Registry.csv
        ├── Sidecar_JSON/
        └── Version_History/
```

### Directory Naming Rules (Absolute)
- **Grade Folders**: Exactly "Grade_3", "Grade_4", "Grade_5"
- **Lesson Folders**: Format "GX_YZ_LessonName" where:
  - X = Grade number (3, 4, or 5)
  - Y = Unit number (1-99)
  - Z = Lesson letter (A-Z, uppercase)
  - LessonName = PascalCase, no spaces
- **Case Sensitivity**: All names are case-sensitive, must match exactly

---

## 🔤 SECTION 3: FILENAME GRAMMAR SPECIFICATION

### Master Filename Pattern (Absolute)
```
meso_{LessonKey}-S{SlideNumber}-{AssetRole}_{ContentDescriptor}-{SpecificationCode}-{ReferenceID}_v{VersionNumber}.{FileExtension}
```

### Token Definitions

#### Prefix Token
- **Format**: `meso_` (literal, always lowercase)
- **Purpose**: Universal identifier for MESO program

#### LessonKey Token
- **Format**: `G{Grade}_{Unit}{Letter}`
- **Grade**: 3, 4, or 5 ONLY
- **Unit**: 1-99 (no zero-padding)
- **Letter**: A-Z (uppercase)
- **Examples**: `G3_1A`, `G3_12B`, `G4_5C`, `G5_1A`

#### SlideNumber Token
- **Format**: `S{##}` (zero-padded two digits)
- **Range**: S00-S99
- **Special**:
  - S00 = Non-slide assets
  - S01-S40 = Standard lesson slides
  - S41-S99 = Extended content

#### AssetRole Token (Must be uppercase, 3 characters)
- **IMG**: Bitmap images (photos, illustrations, raster graphics)
- **OVL**: Vector overlays (geometric constructions, guides)
- **VID**: Video content (animations, demonstrations)
- **AUD**: Audio content (narration, sound effects, music)
- **DOC**: Document snippets (text blocks, citations)
- **UI**: User interface elements (buttons, bars, navigation)
- **TEX**: Textures and patterns (backgrounds, fills)

#### ContentDescriptor Token
- **Format**: kebab-case (lowercase, hyphens only)
- **Length**: 3-50 characters
- **Rules**: Describe subject matter, no underscores or spaces
- **Examples**: 
  - `myth-sun-over-river`
  - `center-dot-indicator`
  - `artifact-cylinder-seal`

#### SpecificationCode Token
- **Format**: UPPERCASE letters, numbers, hyphens
- **Length**: 3-15 characters
- **Examples**: `HD1X`, `HD2X`, `SVGA`, `PRINT-LTR`, `VID-1080p`

#### ReferenceID Token
- **Format**: `R{###}` (zero-padded three digits)
- **Range**: R001-R999 per lesson
- **Uniqueness**: Unique within each lesson only

#### VersionNumber Token
- **Format**: `v{##}` (zero-padded two digits)
- **Range**: v01-v99
- **Rules**: Always starts at v01, increment for content changes

#### FileExtension Token
- **Must be lowercase**
- **Permitted**: png, jpg, jpeg, svg, mp4, mp3, wav, pdf, txt

### Complete Filename Examples (Valid)
```
meso_G3_1A-S03-IMG_myth-sun-over-river-HD2X-R001_v01.png
meso_G3_1A-S08-OVL_center-dot-indicator-SVGA-R012_v01.svg
meso_G4_2B-S15-VID_geometric-construction-demo-VID-1080p-R033_v02.mp4
meso_G5_1C-S07-AUD_narration-ishtar-descent-AUD-48k-R021_v01.mp3
meso_G3_1A-S00-UI_navigation-button-set-UI-STD-R044_v01.png
```

### Invalid Filename Examples (Rejected)
```
❌ meso_G1_1A-S03-IMG_myth-sun-HD2X-R001_v01.png   (Grade 1 not permitted)
❌ meso_G3_1a-S03-IMG_myth-sun-HD2X-R001_v01.png   (Lowercase lesson letter)
❌ meso_G3_1A-S3-IMG_myth-sun-HD2X-R001_v01.png    (Slide not zero-padded)
❌ meso_G3_1A-S03-img_myth-sun-HD2X-R001_v01.png   (Lowercase role)
❌ meso_G3_1A-S03-IMG_myth_sun-HD2X-R001_v01.png   (Underscore in descriptor)
❌ meso_G3_1A-S03-IMG_myth-sun-HD2X-R001_v01.PNG   (Uppercase extension)
```

---

## 📊 SECTION 4: DATABASE SCHEMA

### Core Tables

#### Table: lessons
**Purpose**: Master registry of all lessons

| Column | Type | Description | Required | Constraints |
|--------|------|-------------|----------|-------------|
| lesson_key | TEXT | Primary key (G3_1A format) | ✅ | UNIQUE, NOT NULL |
| lesson_name | TEXT | Human-readable title | ✅ | 50 chars max |
| grade | INTEGER | Grade level | ✅ | Must be 3, 4, or 5 |
| unit | INTEGER | Unit number | ✅ | 1-99 |
| letter | TEXT | Lesson letter | ✅ | Single uppercase A-Z |
| deity | TEXT | Primary deity featured | ✅ | - |
| geometric_concept | TEXT | Primary geometry taught | ✅ | - |
| math_standard | TEXT | Aligned standard code | ✅ | - |
| sel_theme | TEXT | SEL theme | ✅ | - |
| estimated_duration | INTEGER | Duration in minutes | ✅ | Positive integer |
| status | TEXT | Current status | ✅ | DRAFT/REVIEW/APPROVED/PUBLISHED |
| last_modified | TEXT | ISO 8601 date | ✅ | YYYY-MM-DD format |
| created_by | TEXT | Author identifier | ✅ | - |

#### Table: sections
**Purpose**: Define pedagogical sections within lessons

| Column | Type | Description |
|--------|------|-------------|
| lesson_key | TEXT | Foreign key to lessons |
| section_number | INTEGER | 1-7 (fixed structure) |
| section_name | TEXT | Standardized name |
| section_description | TEXT | Detailed description |
| slide_range | TEXT | e.g., "S01-S08" |
| learning_objectives | TEXT | Comma-separated |
| materials | TEXT | Required materials |
| estimated_time | INTEGER | Minutes for section |

**Standardized Section Names**:
1. Myth + SEL (Image Moral)
2. Geometric Element + Link
3. Hands-on Build
4. Guided Practice
5. Workshop Application
6. Assessment Prompt
7. Reflection + Share

#### Table: assets
**Purpose**: Complete registry of all assets with metadata

**Key Columns**:
- asset_id (PRIMARY KEY)
- lesson_key (FOREIGN KEY)
- slide_number
- asset_role (IMG/OVL/VID/AUD/DOC/UI/TEX)
- content_descriptor
- specification_code
- reference_id
- version
- filename (full name following grammar)
- status
- file_size
- dimensions
- color_space
- alt_text (REQUIRED for accessibility)
- caption
- tags (semicolon-separated)
- overlay_codes
- source
- license
- quality_check
- accessibility_check
- approval_status

#### Table: overlays
**Purpose**: Registry of overlay types and specifications

| Column | Type | Description |
|--------|------|-------------|
| overlay_code | TEXT | Unique ID (e.g., CENTER_DOT) |
| category | TEXT | Major category |
| overlay_name | TEXT | Human-readable |
| description | TEXT | Purpose and appearance |
| visual_specification | TEXT | Drawing requirements |
| usage_guidelines | TEXT | When/how to use |
| color_requirements | TEXT | Color specs |
| size_requirements | TEXT | Size specs |
| accessibility_notes | TEXT | Special considerations |

#### Table: specifications
**Purpose**: Technical specifications for all asset types

| Column | Type | Description |
|--------|------|-------------|
| spec_code | TEXT | Code (e.g., HD1X, SVGA) |
| spec_type | TEXT | Image/Video/Audio/Document |
| dimensions | TEXT | Width×Height or duration |
| format | TEXT | File format |
| color_space | TEXT | sRGB, CMYK, etc. |
| quality_settings | TEXT | Compression, bitrate |
| use_cases | TEXT | When to use |
| file_size_target | TEXT | Target size range |

---

## 📐 SECTION 5: ASSET SPECIFICATIONS

### Image Specifications

#### HD1X - Standard Definition 1x
- **Dimensions**: 1920×1080 pixels
- **Color Space**: sRGB IEC61966-2.1
- **Format**: PNG (preferred) or JPEG (95+ quality)
- **Transparency**: Supported in PNG
- **Line Weight**: Minimum 3 pixels
- **Text Size**: Minimum 18 pixels for labels
- **Use Cases**: Standard slide images, diagrams, UI
- **File Size**: <2MB PNG, <1MB JPEG

#### HD2X - High Definition 2x
- **Dimensions**: 3840×2160 pixels
- **Color Space**: sRGB IEC61966-2.1
- **Format**: PNG for graphics, JPEG for photos
- **Transparency**: Supported in PNG
- **Line Weight**: Minimum 6 pixels
- **Text Size**: Minimum 36 pixels for labels
- **Use Cases**: Full-bleed myth illustrations, detailed diagrams
- **File Size**: <8MB PNG, <4MB JPEG

#### SVGA - Scalable Vector Graphics
- **Canvas Size**: 1920×1080 pixels (reference)
- **Format**: SVG 1.1 or 2.0
- **Color Space**: sRGB color intent
- **Stroke Width**: Minimum 3 pixels when rendered at 1920×1080
- **Text Handling**: Convert to outlines unless dynamic
- **Use Cases**: Geometric overlays, construction guides
- **Optimization**: Remove metadata, optimize paths

#### PRINT-LTR - US Letter Print
- **Dimensions**: 2550×3300 pixels (8.5×11" @ 300 DPI)
- **Color Space**: sRGB (CMYK at print time)
- **Format**: PDF (preferred) or PNG
- **Line Weight**: Minimum 1.5 points (0.5mm)
- **Text Size**: Minimum 12 points
- **Use Cases**: Worksheets, templates, printables
- **Bleed**: 0.125" (9 pixels) when required

#### PRINT-A4 - A4 Print
- **Dimensions**: 2480×3508 pixels (210×297mm @ 300 DPI)
- **Color Space**: sRGB (CMYK at print time)
- **Format**: PDF (preferred) or PNG
- **Line Weight**: Minimum 1.5 points (0.5mm)
- **Text Size**: Minimum 12 points
- **Use Cases**: International worksheets, templates
- **Bleed**: 3mm (35 pixels) when required

### Video Specifications

#### VID-1080p - Standard Video
- **Resolution**: 1920×1080 pixels
- **Frame Rate**: 30fps
- **Codec**: H.264 (AVC)
- **Bitrate**: 8-16 Mbps VBR
- **Audio**: AAC, 48kHz, stereo, 256 kbps
- **Container**: MP4
- **Color Space**: Rec. 709
- **Duration**: 5 seconds to 5 minutes per clip

#### VID-720p - Reduced Bandwidth
- **Resolution**: 1280×720 pixels
- **Frame Rate**: 30fps
- **Codec**: H.264 (AVC)
- **Bitrate**: 4-8 Mbps VBR
- **Audio**: AAC, 48kHz, stereo, 192 kbps
- **Use Cases**: Mobile optimization, lower bandwidth

### Audio Specifications

#### AUD-48k - High Quality Audio
- **Sample Rate**: 48kHz
- **Bit Depth**: 24-bit (source), 16-bit (delivery)
- **Format**: WAV (source), MP3 (delivery)
- **MP3 Encoding**: 256 kbps VBR or higher
- **Channels**: Mono or stereo
- **Loudness**: -23 LUFS integrated
- **Use Cases**: Narration, music, sound effects

#### AUD-STD - Standard Audio
- **Sample Rate**: 44.1kHz
- **Bit Depth**: 16-bit
- **Format**: MP3
- **Encoding**: 192 kbps VBR
- **Use Cases**: Basic sound effects, simple narration

---

## 🎨 SECTION 6: VISUAL OVERLAYS TAXONOMY

### Overlay Categories

#### CENTER Category
**CENTER_DOT** - Center Point Indicator
- Small filled circle, high contrast
- Size: 8-12 pixels diameter at HD1X
- Color: Black or white (contrasting)

**CENTER_CROSS** - Center Cross Indicator
- Small cross (+ symbol)
- Size: 16×16 pixels at HD1X
- Stroke: 2-3 pixels wide

#### LINE Category
**LINE_DIAMETER** - Single Diameter Line
- Straight line passing through center
- Stroke: 3-4 pixels wide at HD1X
- May extend slightly beyond circle

**LINE_RADIUS** - Radius Line
- Line from center to circumference
- Stroke: 3-4 pixels wide
- Optional arrowhead at circumference

**LINE_PERPENDICULAR** - Perpendicular Diameters
- Two lines crossing at 90° at center
- Stroke: 3-4 pixels wide
- Equal length

**LINE_AXES8** - Eight-Fold Symmetry Axes
- Eight lines radiating at 45° intervals
- Stroke: 2-3 pixels wide
- Exactly 45° between adjacent lines

#### HIGHLIGHT Category
**HIGH_HALVES** - Half Highlighting
- Semi-transparent color overlay
- Opacity: 20-30%
- Contrasting color

**HIGH_QUARTERS** - Quarter Highlighting
- Semi-transparent color overlay
- Opacity: 20-30%
- Sequential use to show all quarters

**HIGH_SEGMENT** - Arbitrary Segment
- Semi-transparent color overlay
- Opacity: 20-30%
- Clear boundary definition

#### MOTION Category
**MOTION_ORBIT** - Orbital Path Guide
- Dashed or dotted line showing circular motion
- Dash pattern: 10px dash, 5px gap at HD1X
- May be animated in video

**MOTION_ARROW** - Directional Motion Indicator
- Arrow or curved arrow
- Proportional to context
- May pulse or animate

#### MEASUREMENT Category
**MEAS_DIMENSION** - Dimension Lines
- Line with perpendicular end marks and text
- Font: Roboto, minimum 14px at HD1X
- Shows measurements with units

**MEAS_ANGLE** - Angle Measurement
- Arc with angle value in degrees
- Arc proportional to angle size
- Clear label

**MEAS_CALLOUT** - Measurement Callouts
- Leader line with text label
- Thin line: 1-2px wide
- Clear, high contrast text

---

## 🎨 SECTION 7: VISUAL DESIGN STANDARDS

### Color Palette (Authoritative)

#### Primary Palette
- **Sky Gold**: #FFD24A (RGB: 255, 210, 74)
- **River Blue**: #2B6CB0 (RGB: 43, 108, 176)
- **Clay**: #B56533 (RGB: 181, 101, 51)
- **Stone**: #6B7280 (RGB: 107, 114, 128)

#### Secondary Palette
- **Light Gold**: #FFF4CC (Sky Gold at 20% opacity)
- **Light Blue**: #E6F2FF (River Blue at 20% opacity)
- **Light Clay**: #F5E6D3 (Clay at 20% opacity)
- **Light Stone**: #F3F4F6 (Stone at 20% opacity)

#### Neutral Palette
- **Pure White**: #FFFFFF
- **Pure Black**: #000000
- **Dark Gray**: #374151
- **Medium Gray**: #9CA3AF
- **Light Gray**: #F9FAFB

#### Usage Guidelines
- **Sky Gold**: Highlights, emphasis, divine/celestial
- **River Blue**: Primary text, geometric elements, water
- **Clay**: Earth elements, artifacts, warm accents
- **Stone**: Secondary text, backgrounds, neutral

### Typography System

#### Font Hierarchy
1. **Display/Title**: Montserrat Bold, 24-48px
2. **Heading 1**: Montserrat SemiBold, 20-32px
3. **Heading 2**: Montserrat Medium, 18-24px
4. **Body Text**: Roboto Regular, 16-18px
5. **Caption**: Roboto Regular, 14-16px
6. **Label**: Roboto Medium, 14-18px

#### Line Height
- Headings: 1.2-1.3× font size
- Body Text: 1.4-1.6× font size
- Captions: 1.3-1.4× font size

#### Letter Spacing
- Display: -0.02em
- Headings: -0.01em
- Body: 0em (default)
- Labels: 0.01em

### Line Weight Standards
- **HD1X Scale (1920×1080)**: 3 pixels minimum
- **HD2X Scale (3840×2160)**: 6 pixels minimum
- **Print (300 DPI)**: 1.5 points (0.5mm) minimum
- **SVGA Vectors**: 3 pixels when rendered at 1920×1080

**Line Weight Hierarchy**:
- Primary Elements: 4-6 pixels (HD1X)
- Secondary Elements: 3-4 pixels (HD1X)
- Detail Lines: 2-3 pixels (HD1X, use sparingly)

**Stroke Endings**:
- Round caps for geometric elements
- Square caps for technical drawings
- Consistent within each asset

---

## ♿ SECTION 8: ACCESSIBILITY REQUIREMENTS

### Alt Text Standards
**Requirements**:
- **Mandatory**: All IMG, visible OVL, VID poster frames
- **Length**: 80-250 characters
- **Language**: Clear, concise, descriptive
- **Content**: Describe visual AND educational purpose

**Alt Text Formula**:
1. Identify the subject
2. Describe relevant details (colors, shapes, relationships)
3. State educational purpose
4. Avoid redundancy

**Good Examples**:
- "Two equal halves of a circle separated by straight diameter line, demonstrating concept of halves."
- "Eight-point star with symmetry axes in red at 45-degree intervals."

**Prohibited Phrases**:
- "Image of..."
- "Picture showing..."
- "Graphic depicting..."

### Reduced Motion Requirements
**Scope**: All video and animated elements

**Standard Motion**:
- Frame rate: 30fps
- Natural pacing for education

**Reduced Motion (RM) Variants Required**:
- Slower transitions (minimum 2 seconds per change)
- No parallax or 3D camera movement
- No rapid flashing or strobing
- No motion blur effects
- Static holds instead of continuous motion
- Fade transitions instead of slide/zoom

**RM Filename Convention**: Add "-RM" before version
```
Standard: meso_G3_1A-S03-VID_myth-sun-rising-VID-1080p-R001_v01.mp4
RM: meso_G3_1A-S03-VID_myth-sun-rising-VID-1080p-R001-RM_v01.mp4
```

### Color and Contrast Requirements
**WCAG Compliance**: AA minimum, AAA preferred

**Contrast Ratios**:
- Normal Text: 4.5:1 minimum
- Large Text (18pt+): 3:1 minimum
- Graphical Elements: 3:1 minimum
- UI Components: 3:1 minimum

**Color Usage Rules**:
- Never rely on color alone to convey information
- Provide pattern or texture alternatives
- Test in grayscale
- Use high contrast combinations from approved palette

### Font and Typography Requirements
**Approved Fonts**:
- Primary: Montserrat (headings, labels)
- Secondary: Roboto (body text, captions)
- Fallbacks: Arial, Helvetica, sans-serif

**Size Requirements**:
- Slide Labels: Minimum 18px at HD1X (36px at HD2X)
- Print Labels: Minimum 12pt at 300 DPI
- UI Text: Minimum 16px
- Caption Text: Minimum 14px

---

## 🖼️ SECTION 9: CANVA INTEGRATION

### Template Structure

#### Template 1: Myth Illustration Slide
**Canva ID**: [To be assigned]
**Dimensions**: 1920×1080 pixels (16:9)

**Layout Zones**:
- Header Zone (1920×150px): Lesson title, deity name
- Main Image Zone (1920×820px): Full-bleed myth illustration
- Footer Zone (1920×110px): Slide number, attribution

**Typography**:
- Title: Montserrat Bold, 48px, Sky Gold
- Subtitle: Montserrat Medium, 32px, River Blue
- Body: Roboto Regular, 24px, Stone

**Color Scheme**: Mesopotamian Warm
- Primary: Sky Gold #FFD24A
- Accent: Clay #B56533
- Text: Dark Gray #374151

#### Template 2: Lesson Presentation Slide
**Canva ID**: [To be assigned]
**Dimensions**: 1920×1080 pixels (16:9)

**Layout Zones**:
- Header (1920×150px): Section name
- Content Area (1400×700px, centered): Main content
- Sidebar (440×700px, right): Geometric diagrams/overlays
- Footer (1920×110px): Navigation, page numbers

**Typography**:
- Heading: Montserrat SemiBold, 36px
- Body: Roboto Regular, 20px
- Labels: Roboto Medium, 18px

**Color Scheme**: Mesopotamian Cool
- Primary: River Blue #2B6CB0
- Accent: Sky Gold #FFD24A
- Background: Light Gray #F9FAFB

### Export Specifications
**From Canva to MESO Format**:
- Export as PNG at 2× resolution (3840×2160)
- Color profile: sRGB
- Rename following MESO filename grammar
- Place in appropriate Assets folder

### Asset Naming in Canva
**Canva Project Names**:
```
MESO - G3_1A - Myth Slide 03 - Sun Over River
MESO - G3_1A - Presentation Slide 12 - Center Point Discovery
```

**Export Filenames** (before renaming):
```
MESO_G3_1A_Myth03_export.png
MESO_G3_1A_Pres12_export.png
```

**Final MESO Filenames** (after processing):
```
meso_G3_1A-S03-IMG_myth-sun-over-river-HD2X-R001_v01.png
meso_G3_1A-S12-IMG_pres-center-point-discovery-HD2X-R012_v01.png
```

---

## ✅ SECTION 10: QUALITY CONTROL

### Visual Quality Checklist
**Technical Quality**:
- [ ] Resolution meets specification exactly
- [ ] Correct color space (sRGB/CMYK)
- [ ] Appropriate file format
- [ ] Optimal quality/size balance
- [ ] No compression artifacts
- [ ] Clean, crisp edges on geometric elements
- [ ] Perfect alignment

**Design Quality**:
- [ ] Correct fonts, sizes, hierarchy
- [ ] Approved palette colors only
- [ ] WCAG AA contrast compliance
- [ ] Minimum line weights met
- [ ] Consistent with lesson visual style
- [ ] Clear educational purpose
- [ ] Culturally accurate

**Educational Quality**:
- [ ] Supports stated learning objective
- [ ] Age-appropriate for target grade
- [ ] Mathematically accurate
- [ ] Appropriate cultural context
- [ ] Supports SEL objectives
- [ ] Meets accessibility requirements

### Content Accuracy Standards
**Mathematical Accuracy**:
- Geometric shapes must be mathematically perfect
- Measurements accurate to specified precision
- Correct mathematical relationships
- All visible calculations correct
- Appropriate units for grade level

**Cultural Accuracy**:
- Accurate Mesopotamian cultural representation
- Faithful to museum sources
- Consistent with scholarly sources
- Archaeological evidence-based
- Appropriate to historical period

### File Quality Standards
- File size within specified limits
- Complete and accurate metadata
- Perfect filename grammar compliance
- Correct folder placement
- Proper version control

---

## 📋 SECTION 11: WORKFLOW & IMPLEMENTATION

### Asset Creation Process

#### Phase 1: Planning and Specification
1. Define lesson objectives and content requirements
2. Create detailed asset specifications
3. Assign RefID ranges for the lesson
4. Establish production timeline
5. Allocate team members and tools

#### Phase 2: Content Creation
1. Gather historical and cultural references
2. Create initial concepts and sketches
3. Produce assets according to specifications
4. Apply technical specifications and formatting
5. Conduct initial quality check

#### Phase 3: Review and Refinement
1. Technical review (automated and manual)
2. Content review (educational and cultural accuracy)
3. Design review (visual design and brand compliance)
4. Address review feedback
5. Re-review cycles as needed

#### Phase 4: Approval and Release
1. Final quality assurance review
2. Obtain stakeholder approvals
3. Complete CSV registration and metadata
4. Organize files in canonical structure
5. Prepare assets for distribution

### Version Control Process
**Version Numbering**:
- Major changes: Increment version (v01 → v02)
- Content changes: Always require version increment
- Metadata-only changes: May not require increment

**Change Documentation**:
- Document all changes with rationale
- Record all approvals and sign-offs
- Maintain complete version history
- Archive superseded versions

---

## 📊 SECTION 12: TRACKING & VALIDATION

### CSV Tracking Files Required
1. **lessons.csv** - Master lesson registry
2. **sections.csv** - Pedagogical sections
3. **assets.csv** - Complete asset registry with metadata
4. **overlays.csv** - Overlay type specifications
5. **specifications.csv** - Technical specifications

### Automated Validation Rules
**Filename Grammar Validation**:
```regex
^meso_(G[345]_[1-9][0-9]?[A-Z])-S([0-9]{2})-(IMG|OVL|VID|AUD|DOC|UI|TEX)_([a-z0-9-]{3,50})-([A-Z0-9_-]{3,15})-(R[0-9]{3})_v([0-9]{2})\.(png|jpg|jpeg|svg|mp4|mp3|wav|pdf)$
```

**Data Validation**:
- All files referenced in CSV must exist
- File sizes must match specifications
- Image dimensions must match specifications
- All foreign key relationships valid
- Required fields populated
- No duplicate RefIDs within lessons

---

## 🎯 SECTION 13: IMPLEMENTATION ROADMAP

### Immediate Actions
1. ✅ Create organized folder structure
2. ✅ Move files to new structure
3. ⏳ Update all Grade 1 references to Grade 3-5
4. ⏳ Create unified SSOT document (this document)
5. ⏳ Establish CSV tracking system
6. ⏳ Set up automated validation
7. ⏳ Configure Canva templates

### Short-term Goals (1-2 weeks)
- Complete Grade 3 Lesson 1A and 1B
- Establish image download pipeline
- Create first Canva templates
- Set up quality assurance process
- Train team on SSOT standards

### Medium-term Goals (1-3 months)
- Complete all Grade 3 lessons
- Begin Grade 4 curriculum
- Refine workflows based on feedback
- Expand Canva template library
- Establish automated testing

### Long-term Goals (3-6 months)
- Complete all Grades 3, 4, and 5
- Full Canva integration
- Comprehensive asset library
- Complete documentation
- Public release preparation

---

## 📖 APPENDICES

### Appendix A: Lesson Key Quick Reference
```
G3_1A - Sun & Circle of Sharing (Shamash)
G3_1B - Moon & Crescent (Sin)
G3_2A - Eight-Point Star (Ishtar)
G3_2B - Lightning Zigzag (Adad)
[Additional lessons...]

G4_1A - Square of Justice (Marduk)
[Additional lessons...]

G5_1A - Hexagon Journey (Gilgamesh)
[Additional lessons...]
```

### Appendix B: Common Error Messages
| Error Code | Message | Solution |
|------------|---------|----------|
| SSOT-001 | Invalid grade number | Must be 3, 4, or 5 |
| SSOT-002 | Filename grammar violation | Check format against SECTION 3 |
| SSOT-003 | Missing alt text | Add alt text 80-250 characters |
| SSOT-004 | Contrast ratio failure | Adjust colors for WCAG AA |
| SSOT-005 | File size exceeds limit | Optimize compression |

### Appendix C: Museum API Resources
**British Museum**:
- Collection API: https://www.britishmuseum.org/collection
- IIIF endpoint: https://media.britishmuseum.org/

**Met Museum**:
- Open Access API: https://metmuseum.github.io/
- Direct images available

**Penn Museum**:
- Collections: https://www.penn.museum/collections/

### Appendix D: External Dependencies
**Python Packages** (requirements.txt):
```
Pillow>=10.0.0
requests>=2.31.0
sqlite3 (built-in)
```

**Fonts Required**:
- Montserrat (Google Fonts)
- Roboto (Google Fonts)

**Software Tools**:
- Python 3.8+
- Image editing software (Photoshop, GIMP, etc.)
- Vector editor (Illustrator, Inkscape, etc.)
- Canva Pro account

---

## 📜 DOCUMENT CONTROL

**Document Version**: 1.0  
**Last Updated**: 2025-01-05  
**Next Review Date**: 2025-02-05  
**Document Owner**: MESO Program Management  
**Approval Authority**: Curriculum Director  
**Distribution**: All MESO Program Team Members  

**Change History**:
- v1.0 (2025-01-05): Initial comprehensive SSOT document consolidating all specifications

**Related Documents**:
- MESO Program Curriculum Standards
- Accessibility Compliance Guidelines
- Cultural Sensitivity Guidelines
- Quality Assurance Procedures

---

**END OF SSOT DOCUMENT**

This Single Source of Truth is the authoritative specification for all MESO Program asset management. Any questions, clarifications, or proposed changes must be directed through established change management procedures.
