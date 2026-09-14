# 🤖 MULTI-AGENT PRESENTATION SYSTEM - IMPLEMENTATION GUIDE

**Purpose:** This system breaks down presentation creation into specialized agents that work in parallel, avoiding the single-Claude-does-everything bottleneck that's been failing.

**Date:** 2025-10-31
**Status:** Ready for Implementation

---

## 🎯 WHY THIS APPROACH WORKS

### The Problem (What's Been Failing)
- Single Claude instance trying to do research + writing + visuals + assembly + QA
- Context window overload
- Loses track of requirements
- Inconsistent quality across sections
- Can't parallelize work

### The Solution (This System)
- **Specialization:** Each agent has ONE job
- **Parallel Execution:** Multiple agents work simultaneously
- **Clear Hand-offs:** Structured data artifacts between agents
- **Quality Gates:** Dedicated QA before delivery
- **Scalability:** Add more sub-agents as needed

---

## 📋 SYSTEM ARCHITECTURE

### 1 Master Orchestrator
- Coordinates all agents
- Manages dependencies
- Tracks progress
- Handles failures/retries

### 6 Main Agents
1. **Source & Research** - Find and validate content
2. **Content Writing** - Create text
3. **Visual Assets** - Acquire/create images and diagrams
4. **Slide Assembly** - Build the presentation
5. **QA & Review** - Quality assurance
6. **Export & Delivery** - Package and deliver

### 23 Sub-Agents
Each main agent has 3-5 sub-agents handling specific tasks

### 10 Data Artifacts
Structured data that flows between agents (JSON files, image folders, slide decks)

---

## 🚀 HOW TO EXECUTE THIS SYSTEM

### Phase 1: Setup (Do Once)

**1.1 Create Project Structure**
```bash
mkdir presentation-project
cd presentation-project

# Create directories for data artifacts
mkdir -p artifacts/{sources,notes,citations,outlines,drafts,images,charts,slides,qa,release}

# Create agent workspace
mkdir -p agents/{orchestrator,research,writing,visuals,assembly,qa,delivery}
```

**1.2 Create Master Requirements File**
```json
// requirements.json
{
  "presentation_title": "Your Presentation Title",
  "target_audience": "High school students / Academics / General public",
  "slide_count": 48,
  "duration_minutes": 60,
  "topic": "Specific topic description",
  "learning_objectives": [
    "Objective 1",
    "Objective 2"
  ],
  "visual_style": "Modern / Classic / Minimalist",
  "required_sections": [
    "Introduction",
    "Main Content (specify subsections)",
    "Activities",
    "Conclusion"
  ]
}
```

**1.3 Set Up Agent Templates**
See "AGENT PROMPTS" section below for each agent's specific prompt template.

---

### Phase 2: Execution (Per Presentation)

**STEP 1: Launch Orchestrator**

The orchestrator reads `requirements.json` and creates a project plan:

```json
// project_plan.json (created by orchestrator)
{
  "project_id": "pres_20251031_001",
  "status": "in_progress",
  "agents": {
    "research": {
      "status": "running",
      "started_at": "2025-10-31T10:00:00Z",
      "assigned_tasks": ["SCOPE", "COLLECT", "CITE"]
    },
    "writing": {
      "status": "pending",
      "depends_on": ["research"],
      "assigned_tasks": ["OUTLINE", "DRAFT", "STYLE", "FACT"]
    },
    "visuals": {
      "status": "running",
      "started_at": "2025-10-31T10:00:00Z",
      "assigned_tasks": ["FINDIMG", "RIGHTS", "DLIMG", "CHART"]
    },
    "assembly": {
      "status": "pending",
      "depends_on": ["writing", "visuals"]
    },
    "qa": {
      "status": "pending",
      "depends_on": ["assembly"]
    },
    "delivery": {
      "status": "pending",
      "depends_on": ["qa"]
    }
  }
}
```

**STEP 2: Launch Parallel Agents**

The orchestrator launches agents that don't depend on each other:

**PARALLEL GROUP 1:**
- ✅ Research Agent (starts immediately)
- ✅ Visuals Agent (starts immediately)

These run in parallel because they don't depend on each other.

**STEP 3: Monitor Agent Progress**

Each agent creates status files:

```json
// artifacts/sources/status.json
{
  "agent": "research/collect",
  "status": "completed",
  "output": "artifacts/sources/curated_sources.json",
  "artifacts_created": 144,
  "completion_time": "2025-10-31T10:15:00Z"
}
```

**STEP 4: Sequential Agent Launch**

Once dependencies are met:

- Research completes → Launch Writing Agent
- Writing + Visuals complete → Launch Assembly Agent
- Assembly completes → Launch QA Agent
- QA completes → Launch Delivery Agent

---

## 📦 DATA ARTIFACTS SPEC

### 1. Curated Sources (`sources/curated_sources.json`)

```json
{
  "sources": [
    {
      "id": "source_001",
      "type": "museum_artifact",
      "title": "Artifact Name",
      "museum": "Metropolitan Museum of Art",
      "url": "https://...",
      "image_url": "https://...",
      "date": "2000 BCE",
      "culture": "Mesopotamian",
      "license": "CC0 / Open Access",
      "relevance_score": 0.95,
      "notes": "Why this artifact is relevant",
      "lesson_numbers": [1, 5, 12]
    }
  ],
  "total_sources": 144,
  "collected_at": "2025-10-31T10:15:00Z"
}
```

### 2. Research Notes (`notes/research_notes.json`)

```json
{
  "topics": [
    {
      "topic": "Mesopotamian Geometry",
      "key_points": [
        "Point 1",
        "Point 2"
      ],
      "sources": ["source_001", "source_003"],
      "lesson_relevance": [1, 2, 3]
    }
  ]
}
```

### 3. Citations (`citations/bibliography.json`)

```json
{
  "citations": [
    {
      "id": "cite_001",
      "source_id": "source_001",
      "citation_style": "APA",
      "text": "Museum Name. (2024). Artifact Title. Retrieved from https://...",
      "bibtex": "@misc{...}"
    }
  ]
}
```

### 4. Outline (`outlines/presentation_outline.json`)

```json
{
  "slides": [
    {
      "slide_number": 1,
      "title": "Slide Title",
      "section": "Introduction",
      "content_type": "title_slide",
      "estimated_duration_seconds": 30,
      "key_points": ["Point 1", "Point 2"],
      "required_images": 0,
      "required_diagrams": 0
    },
    {
      "slide_number": 2,
      "title": "Historical Context",
      "section": "Background",
      "content_type": "content_slide",
      "estimated_duration_seconds": 90,
      "key_points": [
        "Mesopotamia 3500 BCE",
        "Early mathematics"
      ],
      "required_images": 2,
      "required_diagrams": 1,
      "source_ids": ["source_001", "source_002"]
    }
  ],
  "total_slides": 48,
  "estimated_total_duration_seconds": 3600
}
```

### 5. Draft Sections (`drafts/slide_drafts.json`)

```json
{
  "slides": [
    {
      "slide_number": 1,
      "title": "The Birth of Geometry in Ancient Mesopotamia",
      "subtitle": "From Practical Measurement to Mathematical Thinking",
      "body_text": "In the fertile crescent between the Tigris and Euphrates rivers...",
      "bullet_points": [],
      "speaker_notes": "This slide sets the scene. Emphasize the transition from practical to theoretical.",
      "word_count": 45,
      "reading_level": "grade_9"
    }
  ]
}
```

### 6. Image Candidates (`images/image_candidates.json`)

```json
{
  "images": [
    {
      "id": "img_001",
      "source_id": "source_001",
      "url": "https://...",
      "title": "Clay Tablet with Geometric Patterns",
      "museum": "Met Museum",
      "license": "CC0",
      "resolution": "3000x2400",
      "file_size_mb": 2.1,
      "intended_slides": [2, 15],
      "download_priority": "high"
    }
  ]
}
```

### 7. Optimized Assets (`assets/`)

Folder structure:
```
assets/
  ├── images/
  │   ├── img_001_optimized.jpg (1920x1080, <500KB)
  │   ├── img_001_thumbnail.jpg (320x240, <50KB)
  │   └── ...
  ├── charts/
  │   ├── diagram_001.svg
  │   ├── diagram_002.svg
  │   └── ...
  └── manifest.json
```

```json
// assets/manifest.json
{
  "images": [
    {
      "id": "img_001",
      "original_url": "https://...",
      "local_path": "assets/images/img_001_optimized.jpg",
      "thumbnail_path": "assets/images/img_001_thumbnail.jpg",
      "dimensions": {"width": 1920, "height": 1080},
      "file_size_bytes": 487321,
      "format": "JPEG",
      "alt_text": "Clay tablet showing geometric calculation from 2000 BCE"
    }
  ],
  "charts": [
    {
      "id": "diagram_001",
      "type": "geometric_overlay",
      "local_path": "assets/charts/diagram_001.svg",
      "description": "Circle and square overlay on artifact",
      "slide_number": 5
    }
  ]
}
```

### 8. Slide Deck (`slides/presentation.pptx`)

PowerPoint/Keynote file with:
- All slides assembled
- Images embedded
- Charts positioned
- Formatting applied
- NOT YET QA'd

### 9. QA Report (`qa/qa_report.json`)

```json
{
  "overall_status": "pass_with_warnings",
  "checks": [
    {
      "check_type": "completeness",
      "status": "pass",
      "details": "All 48 slides present"
    },
    {
      "check_type": "images",
      "status": "warning",
      "details": "Slide 23: Image resolution below recommended 1920x1080",
      "affected_slides": [23]
    },
    {
      "check_type": "accessibility",
      "status": "fail",
      "details": "15 images missing alt text",
      "affected_slides": [5, 8, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
    },
    {
      "check_type": "timing",
      "status": "pass",
      "details": "Total presentation time: 58 minutes (within target 60 minutes)"
    }
  ],
  "required_fixes": [
    {
      "priority": "high",
      "issue": "Missing alt text",
      "assigned_to": "assembly/a11y",
      "slides": [5, 8, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
    }
  ]
}
```

### 10. Release Package (`release/`)

```
release/
  ├── presentation_v1.0.pptx
  ├── presentation_v1.0.pdf
  ├── presentation_v1.0.key (if Keynote requested)
  ├── speaker_notes.pdf
  ├── bibliography.pdf
  ├── image_credits.pdf
  └── README.md
```

---

## 🤖 AGENT PROMPTS

### ORCHESTRATOR PROMPT

```
You are the Project Orchestrator for a multi-agent presentation creation system.

Your responsibilities:
1. Read requirements.json
2. Create project_plan.json with agent dependencies
3. Launch agents in correct order (parallel when possible)
4. Monitor agent status files
5. Handle failures and retry logic
6. Track overall progress
7. Report status to user

CRITICAL RULES:
- Never launch an agent before its dependencies are met
- Always check status.json files before proceeding
- If an agent fails, retry up to 3 times before escalating
- Keep project_plan.json updated in real-time

Current project requirements:
{PASTE requirements.json HERE}

Execute the project plan and coordinate all agents.
```

### RESEARCH AGENT: TOPIC SCOPER

```
You are the Topic Scoper sub-agent.

Your job:
1. Read requirements.json
2. Identify key topics and themes
3. Define scope boundaries (what to include/exclude)
4. Create research_notes.json with topic breakdown

Input: requirements.json
Output: artifacts/notes/research_notes.json

Requirements:
{PASTE requirements.json HERE}

Create comprehensive research notes with all key topics identified.
```

### RESEARCH AGENT: SOURCE COLLECTOR

```
You are the Source Collector sub-agent.

Your job:
1. Read research_notes.json to understand topics
2. Query museum APIs (Met, Louvre, British Museum, etc.)
3. Find 3-5 relevant artifacts per lesson (144+ total for 48 lessons)
4. Document metadata for each source
5. Create curated_sources.json

Museum APIs to use:
- Metropolitan Museum: https://metmuseum.github.io/
- Smithsonian: https://api.si.edu/openaccess/api/v1.0/search
- British Museum: (search their collection)

Input: research_notes.json
Output: artifacts/sources/curated_sources.json

Find ALL artifacts needed for this presentation.
```

### RESEARCH AGENT: CITATION & COMPLIANCE

```
You are the Citation & Compliance sub-agent.

Your job:
1. Read curated_sources.json
2. Verify licenses (prefer CC0, Open Access)
3. Create proper citations (APA format)
4. Generate BibTeX entries
5. Create bibliography.json

Input: curated_sources.json
Output: artifacts/citations/bibliography.json

Ensure legal compliance for all sources.
```

### WRITING AGENT: OUTLINE BUILDER

```
You are the Outline Builder sub-agent.

Your job:
1. Read requirements.json and research_notes.json
2. Create logical slide structure
3. Assign content to each slide
4. Estimate timing per slide
5. Create presentation_outline.json

Structure requirements:
- Total slides: {from requirements.json}
- Sections: {from requirements.json}
- Each slide needs: title, key points, image count, duration

Input: requirements.json, research_notes.json
Output: artifacts/outlines/presentation_outline.json

Create the complete outline for all slides.
```

### WRITING AGENT: SECTION DRAFTING

```
You are the Section Drafting sub-agent.

Your job:
1. Read presentation_outline.json
2. Write text for EACH slide
3. Create speaker notes
4. Keep appropriate word count per slide
5. Create slide_drafts.json

Writing guidelines:
- Target audience: {from requirements.json}
- Tone: Educational, engaging
- Word count: 50-100 words per slide for content slides
- Include speaker notes with additional context

Input: presentation_outline.json, curated_sources.json
Output: artifacts/drafts/slide_drafts.json

Write ALL slide content.
```

### WRITING AGENT: STYLE & TONE

```
You are the Style & Tone sub-agent.

Your job:
1. Read slide_drafts.json
2. Ensure consistent voice throughout
3. Adjust for target audience
4. Refine language for clarity
5. Update slide_drafts.json

Style requirements:
- Target audience: {from requirements.json}
- Avoid jargon (or define it)
- Active voice preferred
- Engaging, not dry

Input: slide_drafts.json (raw)
Output: slide_drafts.json (refined)

Polish all text for consistency and quality.
```

### WRITING AGENT: FACT-CHECK & ACCURACY

```
You are the Fact-check & Accuracy sub-agent.

Your job:
1. Read slide_drafts.json
2. Verify all factual claims against curated_sources.json
3. Cross-reference dates, names, locations
4. Flag any unsupported claims
5. Create fact_check_report.json

Verification process:
- Every claim must have a source
- Dates must be accurate
- Names/spellings must be correct
- No speculation presented as fact

Input: slide_drafts.json, curated_sources.json
Output: artifacts/qa/fact_check_report.json

Verify accuracy of ALL content.
```

### VISUAL AGENT: IMAGE DISCOVERY

```
You are the Image Discovery sub-agent.

Your job:
1. Read curated_sources.json
2. Find high-resolution image URLs for each artifact
3. Verify image quality (minimum 1920x1080 recommended)
4. Create image_candidates.json

Image requirements:
- High resolution (3000px+ width preferred)
- Museum quality photographs
- Clear, well-lit
- Directly from museum websites

Input: curated_sources.json
Output: artifacts/images/image_candidates.json

Find ALL images needed for the presentation.
```

### VISUAL AGENT: LICENSING & RIGHTS

```
You are the Licensing & Rights sub-agent.

Your job:
1. Read image_candidates.json
2. Verify license for EACH image
3. Flag any restricted images
4. Prefer CC0 and Open Access
5. Update image_candidates.json with license info

License verification:
- Check museum's terms of use
- Prefer public domain
- Document any restrictions
- Flag images that need permission

Input: image_candidates.json
Output: image_candidates.json (with license data)

Verify legal use of ALL images.
```

### VISUAL AGENT: IMAGE DOWNLOAD & OPTIMIZATION

```
You are the Image Download & Optimization sub-agent.

Your job:
1. Read image_candidates.json
2. Download ALL images
3. Optimize for presentation (1920x1080, <500KB)
4. Create thumbnails (320x240, <50KB)
5. Save to assets/images/
6. Create manifest.json

Optimization specs:
- Main image: 1920x1080 JPEG, quality 85%
- Thumbnail: 320x240 JPEG, quality 75%
- Progressive JPEG encoding
- Strip metadata to reduce file size

Input: image_candidates.json
Output: assets/images/ (all files), assets/manifest.json

Download and optimize ALL images.
```

### VISUAL AGENT: DIAGRAM/CHART GENERATOR

```
You are the Diagram/Chart Generator sub-agent.

Your job:
1. Read presentation_outline.json to identify needed diagrams
2. Create geometric overlays on artifact images
3. Create concept diagrams
4. Save as SVG files to assets/charts/
5. Update manifest.json

Diagram types needed:
- Geometric overlays (circles, squares, lines on artifacts)
- Concept diagrams (explaining mathematical concepts)
- Flow charts (if needed)
- All in SVG format for scalability

Input: presentation_outline.json, slide_drafts.json
Output: assets/charts/ (SVG files), assets/manifest.json

Create ALL diagrams needed.
```

### ASSEMBLY AGENT: LAYOUT & TEMPLATE

```
You are the Layout & Template sub-agent.

Your job:
1. Read requirements.json for visual style
2. Create PowerPoint template
3. Define master slides
4. Set up color scheme, fonts, branding
5. Save template.pptx

Design requirements:
- Style: {from requirements.json}
- Consistent header/footer
- Title slide, content slide, section slide templates
- Accessibility-compliant colors (WCAG AA)

Input: requirements.json
Output: artifacts/slides/template.pptx

Create the presentation template.
```

### ASSEMBLY AGENT: SLIDE CONTENT INTEGRATOR

```
You are the Slide Content Integrator sub-agent.

Your job:
1. Read template.pptx
2. Read slide_drafts.json
3. Read assets/manifest.json
4. Insert text into each slide
5. Insert images and charts
6. Position elements properly
7. Save presentation.pptx

Integration requirements:
- Use template layouts
- Position images according to layout guides
- Add speaker notes from drafts
- Ensure text is readable (font size 24pt minimum)

Input: template.pptx, slide_drafts.json, assets/manifest.json
Output: artifacts/slides/presentation.pptx

Assemble the complete presentation.
```

### ASSEMBLY AGENT: CONSISTENCY & FORMATTING

```
You are the Consistency & Formatting sub-agent.

Your job:
1. Read presentation.pptx
2. Check formatting consistency across all slides
3. Verify fonts, colors, spacing
4. Align elements
5. Fix any formatting issues
6. Save updated presentation.pptx

Consistency checks:
- All titles same font/size
- Consistent bullet point formatting
- Image alignment
- Color scheme adherence

Input: presentation.pptx
Output: presentation.pptx (formatted)

Ensure visual consistency throughout.
```

### ASSEMBLY AGENT: ACCESSIBILITY & ALT-TEXT

```
You are the Accessibility & Alt-Text sub-agent.

Your job:
1. Read presentation.pptx
2. Add alt text to ALL images
3. Verify color contrast (WCAG AA minimum)
4. Check reading order
5. Add slide titles for screen readers
6. Save accessible presentation.pptx

Accessibility requirements:
- Every image needs descriptive alt text
- Color contrast ratio 4.5:1 minimum
- Proper reading order for screen readers
- No color-only information

Input: presentation.pptx, assets/manifest.json
Output: presentation.pptx (accessible)

Make the presentation fully accessible.
```

### QA AGENT: COMPLETENESS CHECKLIST

```
You are the Completeness Checklist sub-agent.

Your job:
1. Read requirements.json
2. Read presentation.pptx
3. Verify all requirements are met
4. Check slide count
5. Verify all sections present
6. Create qa_report.json

Checklist:
- Slide count matches requirements
- All required sections present
- All images loaded correctly
- No placeholder text remaining
- Speaker notes present

Input: requirements.json, presentation.pptx
Output: artifacts/qa/qa_report.json

Verify completeness.
```

### QA AGENT: ANTI-PLAGIARISM & ATTRIBUTION

```
You are the Anti-plagiarism & Attribution sub-agent.

Your job:
1. Read slide_drafts.json
2. Verify all text is original or properly quoted
3. Check all sources are cited
4. Verify bibliography completeness
5. Update qa_report.json

Attribution checks:
- No uncited direct quotes
- All paraphrasing is original
- Bibliography includes all sources used
- Proper citation format

Input: slide_drafts.json, bibliography.json
Output: qa_report.json

Verify proper attribution.
```

### QA AGENT: COPYEDIT & PROOF

```
You are the Copyedit & Proof sub-agent.

Your job:
1. Read presentation.pptx
2. Check ALL text for errors
3. Fix spelling, grammar, punctuation
4. Verify consistency (e.g., "1st" vs "first")
5. Update qa_report.json

Proofing checklist:
- Spell check ALL slides
- Grammar check
- Punctuation
- Capitalization consistency
- Number formatting

Input: presentation.pptx
Output: qa_report.json, presentation.pptx (corrected)

Proof all content.
```

### QA AGENT: LIVE RUN-THROUGH & TIMING

```
You are the Live Run-through & Timing sub-agent.

Your job:
1. "Present" the slides mentally
2. Estimate time per slide
3. Verify total duration meets requirements
4. Check transitions and flow
5. Update qa_report.json

Timing requirements:
- Target duration: {from requirements.json}
- Each slide has realistic timing
- No jarring transitions
- Logical flow

Input: presentation.pptx, requirements.json
Output: qa_report.json

Verify timing and flow.
```

### DELIVERY AGENT: EXPORT PROFILES

```
You are the Export Profiles sub-agent.

Your job:
1. Read presentation.pptx (final QA'd version)
2. Export to multiple formats:
   - PPTX (PowerPoint)
   - PDF (for distribution)
   - KEY (Keynote, if requested)
3. Verify exports are correct
4. Save to release/

Export specifications:
- PDF: High quality, embedded fonts
- PPTX: Compatible with PowerPoint 2016+
- Keynote: If Apple platform needed

Input: presentation.pptx
Output: release/ (all format files)

Export to all required formats.
```

### DELIVERY AGENT: PACKAGING & VERSIONING

```
You are the Packaging & Versioning sub-agent.

Your job:
1. Collect all deliverables
2. Create version number (semantic versioning)
3. Generate speaker_notes.pdf
4. Generate bibliography.pdf
5. Generate image_credits.pdf
6. Create README.md for package
7. Zip entire release package

Package contents:
- presentation_v{version}.pptx
- presentation_v{version}.pdf
- speaker_notes.pdf
- bibliography.pdf
- image_credits.pdf
- README.md

Input: All artifacts
Output: release/presentation_package_v{version}.zip

Create complete release package.
```

### DELIVERY AGENT: STAKEHOLDER HANDOFF

```
You are the Stakeholder Handoff sub-agent.

Your job:
1. Create delivery documentation
2. Write usage guide
3. Document known issues (if any)
4. Create handoff email template
5. Generate final report

Handoff documentation:
- How to use the presentation
- System requirements
- Troubleshooting tips
- Contact information
- Attribution requirements

Input: All artifacts, qa_report.json
Output: release/HANDOFF_GUIDE.md

Create stakeholder documentation.
```

---

## 🔄 EXECUTION WORKFLOW

### Detailed Step-by-Step

**1. PROJECT INITIALIZATION**

```bash
# User creates requirements.json
# Orchestrator reads it
# Orchestrator creates project_plan.json
```

**2. PARALLEL EXECUTION: RESEARCH + VISUALS**

Both agents start simultaneously:

**Research Track:**
- Topic Scoper → research_notes.json
- Source Collector → curated_sources.json (uses notes)
- Citation Agent → bibliography.json (uses sources)

**Visual Track (can start immediately):**
- Image Discovery → image_candidates.json (uses curated_sources when ready)
- Licensing Agent → validates licenses
- Download Agent → downloads all images
- Chart Generator → creates diagrams

**3. SEQUENTIAL: WRITING (waits for research)**

Once research completes:
- Outline Builder → presentation_outline.json
- Section Drafter → slide_drafts.json
- Style Agent → refines drafts
- Fact Checker → verifies accuracy

**4. SEQUENTIAL: ASSEMBLY (waits for writing + visuals)**

Once both writing AND visuals complete:
- Layout Agent → template.pptx
- Integrator → presentation.pptx (text + images)
- Consistency Agent → formats everything
- Accessibility Agent → adds alt text

**5. SEQUENTIAL: QA (waits for assembly)**

Once assembly completes:
- Completeness → checks all requirements met
- Attribution → verifies citations
- Copyedit → fixes errors
- Timing → verifies duration

**6. SEQUENTIAL: DELIVERY (waits for QA)**

Once QA passes:
- Export → creates PPTX, PDF, Keynote
- Packaging → creates release package
- Handoff → creates documentation

**7. DONE**

Orchestrator marks project complete and delivers release package.

---

## 💡 IMPLEMENTATION TIPS

### For the Orchestrator

**Use Task API to launch agents:**
```python
# Example (pseudocode)
task1 = launch_agent("research/scope", input="requirements.json")
task2 = launch_agent("research/collect", depends_on=[task1])
task3 = launch_agent("visuals/find", input="requirements.json")

# Wait for completion
wait_all([task2, task3])

# Then launch writing
task4 = launch_agent("writing/outline", depends_on=[task2])
```

### For Sub-Agents

**Always write status files:**
```json
{
  "agent": "research/collect",
  "status": "completed" | "in_progress" | "failed",
  "started_at": "timestamp",
  "completed_at": "timestamp",
  "output_artifact": "path/to/output.json",
  "error": "error message if failed"
}
```

### Error Handling

**If an agent fails:**
1. Orchestrator checks status
2. Reads error message
3. Retries up to 3 times
4. If still failing, escalates to user
5. Logs failure for debugging

### Monitoring Progress

**Create a dashboard:**
```
Project: Mesopotamia Lessons (48 slides)
Status: In Progress

✅ Research (completed in 12 minutes)
  ✅ Topic Scoping
  ✅ Source Collection (144 artifacts found)
  ✅ Citations Generated

🔄 Writing (in progress, 45% complete)
  ✅ Outline Created
  ✅ Drafts: 22/48 slides
  ⏳ Style Refinement
  ⏳ Fact Checking

🔄 Visuals (in progress, 68% complete)
  ✅ Images Found (144 candidates)
  ✅ Licenses Verified
  ✅ Downloads: 98/144
  ⏳ Chart Generation

⏸️ Assembly (waiting for Writing + Visuals)
⏸️ QA (waiting for Assembly)
⏸️ Delivery (waiting for QA)

Estimated completion: 18 minutes
```

---

## 🎯 SUCCESS METRICS

**How to know it's working:**

1. **Parallelization:** Research and Visuals run simultaneously (saves 50% time)
2. **No Context Loss:** Each agent focuses on one task (higher quality)
3. **Clear Hand-offs:** Structured JSON artifacts (no ambiguity)
4. **Quality Gates:** QA catches issues before delivery
5. **Reproducibility:** Same inputs → same outputs

**Target Timeline:**
- Research: 10-15 minutes
- Writing: 20-30 minutes (parallel with visuals)
- Visuals: 25-35 minutes (download time varies)
- Assembly: 10-15 minutes
- QA: 5-10 minutes
- Delivery: 2-5 minutes

**Total: 60-90 minutes for 48 slides** (vs. 3+ weeks of failed attempts)

---

## 📋 NEXT STEPS

1. **Review this document**
2. **Create requirements.json for your first presentation**
3. **Set up project directory structure**
4. **Launch orchestrator with agent prompts**
5. **Monitor progress**
6. **Iterate and improve**

---

**Questions or issues?** Document them and adjust agent prompts as needed.

**This system is designed to succeed where single-agent approaches fail.**
