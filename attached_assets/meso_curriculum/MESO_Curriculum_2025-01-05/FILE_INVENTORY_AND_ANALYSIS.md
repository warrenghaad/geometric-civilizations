# MESO Curriculum File Inventory & Analysis
**Date**: 2025-01-05
**Purpose**: Complete inventory of all curriculum files with categorization and status

---

## 📋 EXECUTIVE SUMMARY

### Current State
- **Total Files Identified**: 40+ across multiple locations
- **Primary Locations**: 
  - `/Downloads/Lessonsslides/files/` (active development)
  - `/FINAL_DELIVERY_MESOPOTAMIAN_CURRICULUM/` (structured delivery)
  - Various scattered locations in `/Documents/Research/`

### Key Issues
1. Files scattered across multiple directories
2. Mix of Grade 1 and Grade 3 content (need to consolidate to Grade 3-5 only)
3. Multiple Python scripts with overlapping functionality
4. No clear Single Source of Truth (SSOT)

---

## 📁 FILE CATEGORIES & INVENTORY

### Category 1: SSOT & Core Documentation
**Purpose**: Define standards, naming conventions, database schemas

| File | Location | Status | Content Summary |
|------|----------|--------|-----------------|
| `SSOT_DATABASE_GUIDE.md` | Downloads/Lessonsslides/files | ✅ Current | Database structure documentation |
| `README_MASTER.md` | Downloads/Lessonsslides/files | ✅ Current | Master README with overview |
| `SUMMARY.md` | Downloads/Lessonsslides/files | ✅ Current | Project summary and structure |
| `CORRECTED_SUMMARY.md` | Downloads/Lessonsslides/files | ✅ Current | Corrected version of summary |
| `ARCHITECTURE.md` | FINAL_DELIVERY/03_Documentation | ✅ Current | System architecture |
| `MASTER_CURRICULUM_TABLE.md` | FINAL_DELIVERY/03_Documentation | ⚠️ Needs Review | Full curriculum mapping |

**Action Required**: 
- Consolidate into single SSOT document
- Remove "Grade 1" references, update to "Grade 3-5"
- Version control all changes

---

### Category 2: Python Scripts - Database Management
**Purpose**: Create and manage curriculum databases

| File | Location | Primary Function | Status | Keep/Archive |
|------|----------|-----------------|--------|--------------|
| `SSOT_DATABASE_SYSTEM.py` | Downloads/Lessonsslides/files | Creates complete SSOT database with all tables | ✅ **KEEP** | Keep - Most comprehensive |
| `curriculum_database.py` | Downloads/Lessonsslides/files | Basic curriculum database creation | 🔄 Archive | Archive - superseded by SSOT_DATABASE_SYSTEM |
| `curriculum_manager.py` | Research/Setup files/945p-1145p | Older curriculum management | 🔄 Archive | Archive - outdated |

**Recommendation**: Keep only `SSOT_DATABASE_SYSTEM.py`, archive others with version notes

---

### Category 3: Python Scripts - Image Download & Processing
**Purpose**: Download museum images and create geometric overlays

| File | Location | Primary Function | Status | Issues | Keep/Archive |
|------|----------|-----------------|--------|--------|--------------|
| `download_and_overlay_images.py` | Downloads/Lessonsslides/files | **Complete solution**: Downloads from museums + creates overlays | ✅ **KEEP** | Museum URLs may fail | Keep - most complete |
| `download_meso_images.py` | Downloads/Lessonsslides/files | Downloads + creates placeholders | ✅ **KEEP** | Uses Unsplash (better reliability) | Keep - good backup method |

**Key Differences**:
- `download_and_overlay_images.py`: Museum-focused, complex overlays (concentric circles, radial rays, etc.)
- `download_meso_images.py`: More flexible, creates placeholders when downloads fail, simpler overlays

**Debugging Issues Found**:
1. **Museum API Issues**: Many museum URLs are collection pages, not direct image links
2. **Output Restrictions**: Both scripts handle failures gracefully with placeholders
3. **Working Features**: 
   - Placeholder generation ✅
   - Overlay creation ✅  
   - Verification logging ✅
   - File organization ✅

**Recommendation**: 
- Keep both scripts
- Create hybrid version that tries museum URLs first, falls back to Unsplash/placeholders
- Document working museum APIs separately

---

### Category 4: Lesson Content Files
**Purpose**: Complete lesson specifications

| File | Location | Grade | Status | Content Quality |
|------|----------|-------|--------|-----------------|
| `Grade3_Lesson1A_Shamash_Circle.md` | Downloads/Lessonsslides/files | 3 | ✅ Complete | 62KB - Comprehensive spec |
| `Grade3_Lesson1B_SunCircle.md` | Downloads/Lessonsslides/files | 3 | ✅ Complete | 19KB - Full lesson |

**Action Required**:
- These are Grade 3 (correct)
- Move to structured folder: `Grade_3/G3_1A_SunCircleSharing/`
- Verify all content follows SSOT naming

---

### Category 5: Database Files
**Purpose**: Store structured curriculum data

| File | Location | Size | Purpose | Status |
|------|----------|------|---------|--------|
| `meso_ssot_complete.db` | Downloads/Lessonsslides/files | 140KB | **Complete SSOT database** | ✅ **Primary** |
| `meso_curriculum.db` | Downloads/Lessonsslides/files | 88KB | Basic curriculum data | 🔄 Archive |
| `curriculum_file_catalog.db` | Research/Setup files | Unknown | Legacy file tracking | 🔄 Archive |
| `curriculum_index.db` | archive/old_curriculum_root_scripts | Unknown | Old indexing system | 🔄 Archive |

**Recommendation**: Use `meso_ssot_complete.db` as primary, archive others

---

### Category 6: Canva Integration & Templates
**Purpose**: Define Canva templates and workflows

| File | Location | Status | Content |
|------|----------|--------|---------|
| `CANVA_TEMPLATES.md` | Downloads/Lessonsslides/files | ✅ Current | Template specifications for myth & presentation slides |

**Content Summary**:
- Defines 2 main templates: Myth Illustration, Lesson Presentation
- Specifies color palette, typography, layout grids
- Integration workflows
- **Action**: This is critical - keep and expand

---

### Category 7: Generated Images & Assets
**Purpose**: Downloaded images and overlays

| Location | File Count | Type | Status |
|----------|------------|------|--------|
| `meso_images/G3-1B/` | 32 files | Photos, illustrations, overlays | ✅ Successfully generated |
| `lesson_images/` | 12 files | Artifact placeholders, overlays | ✅ Successfully generated |
| `lesson_images/overlays/` | 7 files | Geometric overlays | ✅ Successfully generated |

**Analysis**:
- ✅ Images successfully downloaded from Unsplash
- ✅ Placeholders created for unavailable images
- ✅ Overlays (circles, halves, fourths, radius, diameter) created successfully
- ✅ Verification logs confirm all operations

---

### Category 8: Manifest & Tracking Files
**Purpose**: Track asset requirements and status

| File | Location | Status |
|------|----------|--------|
| `G3_1B_manifest.json` | Downloads/Lessonsslides/files | ✅ Current |
| `G3_1B_complete_manifest.json` | Downloads/Lessonsslides/files | ✅ Current |
| `verification_log.json` | Multiple locations | ✅ Current |

---

### Category 9: Reference & Documentation
**Purpose**: Quick start guides and completion reports

| File | Purpose | Status |
|------|---------|--------|
| `QUICKSTART.md` | Quick setup instructions | ✅ Current |
| `COMPLETION_REPORT.md` | Status report | ✅ Current |
| `README_IMAGE_DOWNLOADER.md` | Image download documentation | ✅ Current |
| `requirements.txt` | Python dependencies | ✅ Current |

---

## 🔧 SCRIPT DEBUGGING RESULTS

### Image Download Scripts - Issue Analysis

#### Script 1: `download_and_overlay_images.py`
**Status**: ⚠️ Partially Working

**Working Features**:
✅ Placeholder generation  
✅ Geometric overlay creation (center dot, radius, diameter, halves, fourths, concentric circles, radial rays)  
✅ Image verification with checksums  
✅ Comprehensive logging  
✅ Multiple overlay types with mathematical accuracy  

**Failing Features**:
❌ British Museum direct image URLs (return HTML pages, not images)  
❌ Penn Museum URLs (collection pages)  
❌ Oriental Institute URLs (non-existent image paths)  
❌ Yale Babylonian Collection URLs (collection search pages)  

**Root Causes**:
1. Museum URLs point to collection pages, not direct image files
2. Museum APIs require authentication or specific IIIF endpoints
3. Direct media URLs are not publicly documented

**Solutions Implemented**:
✅ Placeholder generation when downloads fail  
✅ Verification checks before accepting downloads  
✅ Multiple URL fallbacks  
✅ Graceful error handling  

#### Script 2: `download_meso_images.py`
**Status**: ✅ Working Well

**Working Features**:
✅ Unsplash downloads (more reliable)  
✅ Placeholder creation  
✅ Basic geometric overlays  
✅ Verification logging  
✅ Proper error handling  

**Successful Downloads**:
- Sun images from Unsplash ✅
- Wheel images from Unsplash ✅
- Drum images from Unsplash/Pexels ✅
- Met Museum artifact (1.7MB successful download) ✅

**Key Difference**: Uses Unsplash API which is more reliable for educational projects

---

## 📊 CONSOLIDATION RECOMMENDATIONS

### Files to KEEP (Move to organized structure)

#### Core SSOT (01_SSOT_Documents/)
- `SSOT_DATABASE_GUIDE.md` → Consolidate into master SSOT
- `ARCHITECTURE.md`
- `MASTER_CURRICULUM_TABLE.md`
- **NEW**: Create unified `MESO_SSOT_2025-01-05.md`

#### Python Scripts (02_Python_Scripts/)
- `SSOT_DATABASE_SYSTEM.py` ✅ Keep
- `download_meso_images.py` ✅ Keep (more reliable)
- `download_and_overlay_images.py` ✅ Keep (better overlays)
- **NEW**: Create `hybrid_image_downloader.py` combining both

#### Image Assets (03_Image_Download/)
- Move all `/meso_images/` contents
- Move all `/lesson_images/` contents
- Keep verification logs

#### Canva (04_Canva_Templates/)
- `CANVA_TEMPLATES.md`
- Add export specifications

#### Databases (05_Database_Files/)
- `meso_ssot_complete.db` (primary)
- Archive others with version notes

#### Lesson Content (06_Lesson_Content/)
- `Grade3_Lesson1A_Shamash_Circle.md`
- `Grade3_Lesson1B_SunCircle.md`

### Files to ARCHIVE (07_Archive/)
- `curriculum_database.py` (superseded)
- `curriculum_manager.py` (old version)
- `meso_curriculum.db` (basic version)
- Old curriculum files from `/archive/old_curriculum_root_scripts/`

---

## 🎯 IMMEDIATE ACTION ITEMS

### 1. Create Unified SSOT Document
**What**: Single comprehensive SSOT that defines:
- Naming conventions for ALL files
- Directory structure (canonical)
- Database schemas
- Asset specifications
- Quality standards
- Accessibility requirements

**How**:
- Merge `SSOT_DATABASE_GUIDE.md` + `ARCHITECTURE.md` + grade corrections
- Remove ALL Grade 1 references
- Add Grade 3, 4, 5 specifications
- Include image specifications table
- Add Canva integration specs

### 2. Fix Grade References
**Find and replace across all files**:
- "Grade 1" → "Grade 3"
- "G1_" → "G3_"
- Update all examples to Grade 3-5 range

### 3. Create Hybrid Image Downloader
**Combine best of both scripts**:
```python
# Pseudo-code structure
1. Try Unsplash/Pexels URLs first (more reliable)
2. Fall back to museum APIs
3. If all fail, create informative placeholder
4. Create all geometric overlays
5. Generate complete verification log
```

### 4. Database Schema Checklist
Create table showing which files have complete specs for:

| Component | SSOT | Database | Python Script | Markdown Docs | Canva Template |
|-----------|------|----------|---------------|---------------|----------------|
| Lessons | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| Assets | ✅ | ✅ | ✅ | ✅ | ❌ |
| Overlays | ✅ | ✅ | ✅ | ⚠️ | ❌ |
| Standards | ✅ | ✅ | ❌ | ✅ | ❌ |
| Specifications | ⚠️ | ❌ | ❌ | ⚠️ | ✅ |

Legend: ✅ Complete | ⚠️ Partial | ❌ Missing

---

## 📝 SSOT SUMMARY (What You Want)

Based on analysis of all files, here's what your SSOT should contain:

### Section 1: Program Identity
- Program name: MESO (Mesopotamian Educational Standards Optimization)
- Grades: 3, 4, 5 (ONLY - no Grade 1 or 2)
- Content domain: Ancient Mesopotamian civilization + geometry + SEL

### Section 2: Directory Structure (Canonical)
```
/MESO_Program/
├── Grade_3/
│   └── G3_1A_SunCircleSharing/
│       ├── 01_eTextbook/
│       ├── 02_Slides/
│       ├── 03_TeacherScript/
│       ├── 04_Worksheet/
│       ├── 05_Templates/
│       ├── 06_Rubrics/
│       ├── 07_Attribution/
│       └── Assets/
│           ├── Images/
│           ├── Overlays/
│           ├── Audio/
│           └── Video/
```

### Section 3: Filename Grammar
```
meso_{LessonKey}-S{SlideNum}-{Role}_{Descriptor}-{Spec}-{RefID}_v{Ver}.{ext}

Example:
meso_G3_1A-S03-IMG_myth-sun-over-river-HD2X-R001_v01.png
```

### Section 4: Database Schema
**Tables**: lessons, sections, assets, overlays, specifications, standards_alignment

### Section 5: Asset Specifications
| Code | Dimensions | Format | Use Case |
|------|------------|--------|----------|
| HD1X | 1920×1080 | PNG/JPG | Standard slides |
| HD2X | 3840×2160 | PNG | Full-bleed illustrations |
| SVGA | Vector | SVG | Scalable overlays |
| PRINT-LTR | 2550×3300 @ 300dpi | PDF | Worksheets |

### Section 6: Overlay Taxonomy
- CENTER_DOT: Center point indicator
- LINE_DIAMETER: Diameter line
- LINE_RADIUS: Radius line  
- HIGH_HALVES: Halves highlighting
- HIGH_FOURTHS: Fourths highlighting
- MOTION_ORBIT: Orbital path

### Section 7: Quality Standards
- Alt text: 80-250 characters
- Line weight: ≥3px at HD1X
- Contrast: WCAG AA minimum
- Color palette: Sky Gold, River Blue, Clay, Stone

### Section 8: Canva Integration
- Template IDs
- Brand kit specifications
- Export settings
- Workflow automation

---

## 🚀 NEXT STEPS

1. ✅ Create organized folder structure (DONE)
2. ⏳ Move files to `/Documents/Research/MESO_Curriculum_2025-01-05/`
3. ⏳ Create unified SSOT document
4. ⏳ Fix all Grade 1 → Grade 3 references
5. ⏳ Create hybrid image downloader
6. ⏳ Generate specification checklist table
7. ⏳ Export to Canva with proper naming

---

## 📋 FILE MANIFEST FOR MOVING

### Priority 1: Move Immediately
```bash
# SSOT Documents
Downloads/Lessonsslides/files/SSOT_DATABASE_GUIDE.md
Downloads/Lessonsslides/files/README_MASTER.md
FINAL_DELIVERY/03_Documentation/ARCHITECTURE.md
FINAL_DELIVERY/03_Documentation/MASTER_CURRICULUM_TABLE.md

# Python Scripts (keep both image downloaders)
Downloads/Lessonsslides/files/SSOT_DATABASE_SYSTEM.py
Downloads/Lessonsslides/files/download_meso_images.py
Downloads/Lessonsslides/files/download_and_overlay_images.py

# Database
Downloads/Lessonsslides/files/meso_ssot_complete.db

# Lesson Content
Downloads/Lessonsslides/files/Grade3_Lesson1A_Shamash_Circle.md
Downloads/Lessonsslides/files/Grade3_Lesson1B_SunCircle.md

# Canva
Downloads/Lessonsslides/files/CANVA_TEMPLATES.md

# Images (entire folders)
Downloads/Lessonsslides/files/meso_images/
Downloads/Lessonsslides/files/lesson_images/
```

### Priority 2: Archive
- Old curriculum files
- Superseded database files
- Legacy Python scripts

---

**END OF INVENTORY**
