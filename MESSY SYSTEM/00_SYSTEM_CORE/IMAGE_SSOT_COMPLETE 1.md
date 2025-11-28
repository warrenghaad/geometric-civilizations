# 🖼️ IMAGE SSOT - SINGLE SOURCE OF TRUTH
**Complete Specification for All Images**  
**Version:** 1.0  
**Date:** 2025-11-05

---

## 📊 OVERVIEW

Every lesson requires approximately **100-120 images** organized into **4 categories**.

---

## 🎯 IMAGE CATEGORIES

### **1. Backgrounds (30-35 images)**
### **2. Characters (15-20 images)**
### **3. Diagrams (20-25 images)**
### **4. Artifacts (15-20 images)**
### **5. Miscellaneous (20-25 images)**

---

## 📐 IMAGE SPECIFICATIONS

### **Category 1: Backgrounds**
- **Purpose:** Slideshow backgrounds, scene setting
- **Count:** 30-35 per lesson
- **Size:** 1920x1080 (HD, 16:9)
- **Resolution:** Minimum 300 DPI
- **Format:** JPG (photos), PNG (illustrations)
- **Style:** Historically accurate, visually rich

**Required Backgrounds:**
- Landscape scenes (5-7)
- Sky/atmosphere (5-7)
- Architecture/buildings (5-7)
- Interior scenes (3-5)
- Textures/patterns (5-7)
- Abstract/symbolic (3-5)

---

### **Category 2: Characters**
- **Purpose:** Myth storytelling, human elements
- **Count:** 15-20 per lesson
- **Size:** 800x1000 (Portrait orientation)
- **Resolution:** Minimum 300 DPI
- **Format:** PNG with transparency
- **Style:** Culturally appropriate, expressive

**Required Characters:**
- Main deity/hero (5-7 poses)
- Supporting characters (3-5 each)
- Civilians/people (3-5)
- Animals (if applicable)

---

### **Category 3: Diagrams**
- **Purpose:** Geometry instruction, math problems
- **Count:** 20-25 per lesson
- **Size:** 1920x1080 or 1200x1200
- **Resolution:** 600 DPI (vector preferred)
- **Format:** PNG, SVG
- **Style:** Clean, educational, clearly labeled

**Required Diagrams:**
- Basic element (unlabeled)
- Labeled diagram (parts named)
- Properties diagram
- Formula visualization
- Math problem diagrams (12+)
- Decomposition overlays (10+)

---

### **Category 4: Artifacts**
- **Purpose:** Cultural connection, analysis
- **Count:** 15-20 per lesson
- **Size:** 1200x900 (4:3 ratio)
- **Resolution:** 600 DPI minimum
- **Format:** JPG (photos)
- **Source:** Museum collections, licensed

**Required Artifacts:**
- 3 primary artifacts (high res)
- Detail views of each (3)
- Context photos (3)
- Related artifacts (3-6)
- Comparison images (3)

---

### **Category 5: Miscellaneous**
- **Purpose:** Various lesson needs
- **Count:** 20-25 per lesson
- **Size:** Variable
- **Resolution:** 300+ DPI
- **Format:** PNG or JPG
- **Content:** Icons, buttons, borders, etc.

---

## 📋 IMAGE INVENTORY REQUIREMENTS

Every image MUST be cataloged:

```json
{
  "image_id": "G3_L01_BG_001",
  "category": "Background",
  "subcategory": "Landscape",
  "description": "Mesopotamian cityscape at dawn with Euphrates River",
  "size": "1920x1080",
  "resolution": "300 DPI",
  "format": "JPG",
  "color_mode": "RGB",
  "source": "Custom illustration / Stock photo / Museum",
  "license": "Licensed / Public domain / Custom",
  "location": "/07_IMAGES/backgrounds/G3_L01_BG_001.jpg",
  "used_in": ["Slide 1", "Slide 16"],
  "tags": ["mesopotamia", "cityscape", "river", "dawn"],
  "created_date": "2025-11-05",
  "created_by": "Artist name"
}
```

---

## 🎨 STYLE GUIDELINES

### **Backgrounds:**
- Rich, saturated colors for myth
- Neutral colors for instruction
- Historically accurate architecture
- Atmospheric lighting
- No modern elements

### **Characters:**
- Period-appropriate clothing
- Expressive faces/poses
- Clear against backgrounds
- Consistent style across lesson
- Cultural authenticity

### **Diagrams:**
- Clean lines
- Clear labels
- High contrast
- Color-coded when helpful
- Print-friendly

### **Artifacts:**
- Sharp focus
- Neutral background
- Accurate colors
- Multiple angles if needed
- Detail shots included

---

## 📏 TECHNICAL SPECIFICATIONS

### **File Naming Convention:**
```
G[grade]_L[lesson]_[CATEGORY]_[###].[ext]

Examples:
- G3_L01_BG_001.jpg (Background 1)
- G3_L01_CHAR_003.png (Character 3)
- G3_L01_DIAG_012.png (Diagram 12)
- G3_L01_ART_002.jpg (Artifact 2)
```

### **Color Specifications:**
- **Color mode:** RGB (screen), CMYK (print)
- **Profile:** sRGB IEC61966-2.1
- **Bit depth:** 24-bit minimum

### **File Size:**
- **Maximum:** 5MB per image
- **Recommended:** 1-3MB
- **Compression:** Quality 90+ for JPG

---

## ✅ VALIDATION CHECKLIST

Before images are approved:

- [ ] Correct count per category
- [ ] All sizes correct
- [ ] All resolutions 300+ DPI
- [ ] All properly named
- [ ] All cataloged in inventory
- [ ] All sourced/licensed properly
- [ ] All culturally appropriate
- [ ] All print-tested
- [ ] All display-tested

---

**SSOT Status:** ✅ COMPLETE  
**Last Updated:** 2025-11-05
