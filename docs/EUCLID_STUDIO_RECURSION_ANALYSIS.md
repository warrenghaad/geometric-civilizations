# EUCLID_STUDIO: Architecture and Recursive Structures

A comprehensive analysis of the EUCLID_STUDIO system, its organizational logic, and the recursive patterns that emerge from its design.

---

## 1. System Overview

EUCLID_STUDIO is a working/production folder tree for Project Euclid — a system supporting:
- **Theory canon development** (GE Taxonomy, MAGIC variables, cognitive through-lines)
- **K-8 curriculum instantiation** (Geometric Civilizations, Mesopotamian pilot)
- **Claude skill/plugin ecosystem** (decompose-artifact, find-motif, permutative-matrix, etc.)
- **Visual production pipeline** (animation cells, Figma orchestration, video explainers)

The system is organized as a **faceted component graph**, not a hierarchy. This design choice is intentional and mirrors the GE Taxonomy's own structure: composable units that can be recombined, inspected, and transformed.

---

## 2. Primary Organizational Structure

### 2.1 The Seven Drawers

```
EUCLID_STUDIO/
├── 00_Reconciliation/     # Active theory/curriculum work (Obsidian vault)
├── 01_Skills/             # Claude skill definitions
├── 02_Plugins/            # Packaged skill bundles
├── 03_Prompts/            # Agent and system prompts
├── 04_Tools/              # Standalone scripts/utilities
├── 05_Instantiations_Builds/  # Generated outputs
├── 06_Animation_Studio_Cells/ # Motion/sequence design
├── 07_Examples/           # Worked examples for onboarding
└── Semyceliance/          # Research epistemology pipeline
```

### 2.2 The Reconciliation Vault (00_Reconciliation)

The active workspace contains a full Obsidian vault with git versioning:

```
00_Reconciliation/
├── 00_INBOX/              # Incoming material
├── 01_CANON/              # Established truth
├── 02_SCHEMA/             # Data structures
├── 03_CONCEPTS/           # Conceptual units
├── 04_FLOWS/              # Process definitions
├── 05_WORKSPACES/         # Active work contexts
├── 05_TEMPLATES/          # Reusable templates
├── 06_EVIDENCE/           # Supporting material
├── 07_DATASETS/           # Structured data
├── 08_TRANSLATIONS/       # Cross-format mappings
├── 09_WORKFLOW/           # Automation definitions
├── 10_AUTOMATION/         # Automated processes
├── 90_PATCHES/            # Fixes and corrections
├── 99_ARCHIVE/            # Historical material
├── .git/                  # Version control
└── .obsidian/             # Vault configuration
```

### 2.3 The Semyceliance Pipeline

A parallel research epistemology structure:

```
Semyceliance/
├── 00_canon/        # Established knowledge
├── 01_theory/       # Theoretical frameworks
├── 02_terrain/      # Domain mapping
├── 03_inference/    # Reasoning processes
├── 04_lenses/       # Analytical perspectives
├── 05_graph/        # Relationship structures
├── 06_figures/      # Visual representations
├── 07_sessions/     # Work sessions
├── 08_provisional/  # Tentative conclusions
└── 09_residue/      # Unresolved material
```

---

## 3. Recursive Structures

### 3.1 The GE Taxonomy Recursion

The foundational recursive structure is the GE (Geometric Element) composition model:

```
GEM = GEA + GEA
GEM = GEA + GEM
GEM = GEM + GEM
```

This is **structural recursion**: a molecular element (GEM) can contain atomic elements (GEA) or other molecular elements, to arbitrary depth.

**Example:**
```
gem.rosette
├── gem.petal-ring
│   ├── gea.sh.circle (center)
│   └── gem.petal (×8)
│       ├── gea.sh.arc
│       └── gea.sh.line
└── gem.border
    └── gea.sh.circle (outer)
```

**Recursion Risk:** Unbounded decomposition. A rosette decomposes into petals, which decompose into arcs and lines. But lines can be seen as infinite points, arcs as infinite lines... The recursion must be grounded at a "primitive" level.

**Grounding mechanism:** The system defines **Primitives** as generative operands that cannot be further decomposed in the GE frame:
```
Primitive + Motion Type + Duration + Vector = F(ge)
```

---

### 3.2 The Skill → Plugin → Build Recursion

Skills, plugins, and builds form a production cycle:

```
01_Skills/          →  Skill definitions (SKILL.md)
    ↓
02_Plugins/         →  Packaged skills (plugin bundles)
    ↓
03_Prompts/         →  Agent configurations using plugins
    ↓
05_Builds/          →  Generated outputs from agents
    ↓
07_Examples/        →  Curated outputs for onboarding
    ↓
01_Skills/          →  Improved skills based on examples
```

**Recursion Pattern:** Each production cycle potentially improves the skills that produce the next cycle.

**Recursion Risk:** **Drift amplification.** If a skill produces outputs that train the next skill version, errors compound. A subtle bias in `decompose-artifact` propagates through every artifact decomposition in the curriculum.

**Grounding mechanism:** 
- **01_CANON** in the Reconciliation vault serves as ground truth
- **07_Examples** are curated "what good looks like" exemplars
- Human review at the CANON ↔ BUILD interface

---

### 3.3 The Canon ↔ Instance Recursion

The Reconciliation vault creates a bidirectional flow:

```
CANON (established truth)
    ↓ instantiates
SCHEMA (structures)
    ↓ organizes
CONCEPTS (units)
    ↓ connect via
FLOWS (processes)
    ↓ generate
EVIDENCE (material)
    ↓ feeds
DATASETS (structured)
    ↓ may revise
CANON (updated truth)
```

**Recursion Pattern:** Evidence can update canon, which changes schemas, which reorganizes concepts, which modifies flows, which produces different evidence.

**Recursion Risk:** **Canon instability.** If evidence too readily revises canon, the system oscillates. If canon is too rigid, the system calcifies.

**Grounding mechanism:**
- **Versioning via Mesopotamian periods** (Halaf → Ubaid → Uruk → ...) - substantive breaks start new lineages, not incremental saves
- **Provisional vs. Canon distinction** - Semyceliance's `08_provisional` holds tentative material separate from `00_canon`
- **Residue capture** - Semyceliance's `09_residue` holds unresolved material rather than forcing premature canonization

---

### 3.4 The Animation Breathing Cycle

The Animation Studio uses a cyclical model:

```
invention → ornamentation → saturation → nostalgia → minimalism → invention
```

**Recursion Pattern:** Creative cycles return to origin, but transformed.

This maps to the **phenomenaffective line-contour taxonomy** (contour_affect_index.py):
- **Invention:** New form emerges
- **Ornamentation:** Form elaborates
- **Saturation:** Elaboration peaks
- **Nostalgia:** Retrospective simplification
- **Minimalism:** Essential reduction
- **Invention:** Reduced form enables new emergence

**Recursion Risk:** **Premature cycling.** Moving to "nostalgia" before saturation completes produces shallow work. Stuck in "ornamentation" produces baroque excess.

**Grounding mechanism:**
- Cell sequencing tracks position in cycle
- Each cell is dated (YYYY-MM-DD_description.ext)
- Motion/permutation design-space maps the phase space

---

### 3.5 The Semyceliance Epistemology Recursion

The research pipeline has an implicit recursion:

```
canon → theory → terrain → inference → lenses → graph → figures → sessions → provisional → residue
                                                                                    ↓
                                                                            [review]
                                                                                    ↓
                                                                              canon (updated)
```

But also:
- **Lenses** can be applied to the pipeline itself
- **Theory** about the pipeline modifies the pipeline
- **Graphs** of the pipeline are themselves pipeline products

**Recursion Pattern:** **Meta-recursion.** The system can model itself.

**Recursion Risk:** **Infinite regress.** Meta-theory about meta-theory about meta-theory... The system could spend infinite resources modeling itself rather than doing work.

**Grounding mechanism:**
- **Sessions** (07_sessions) are time-bounded work units
- **Figures** (06_figures) are fixed outputs that don't self-modify
- **Residue** (09_residue) captures what can't be resolved, preventing infinite pursuit

---

### 3.6 The Prism ↔ Canvas Recursion (ArtisanalCanvas)

The local ArtisanalCanvas app has its own recursive structure:

```
Prism (context selector)
    ↓ emits context to
Canvas (spatial surface)
    ↓ contains
Objects (cards, drawings, connections)
    ↓ may include
Meta-Build tools
    ↓ can modify
Prism configuration
```

**Recursion Pattern:** The studio can build the studio.

The Prism address model:
```
workspace × engine × functionality
```

Where workspaces include:
- meta-navigation (navigating the navigation)
- inspect-repair-debug (inspecting the inspection)

**Recursion Risk:** **Tool-use regress.** Using the meta-build tool to build the meta-build tool.

**Grounding mechanism:**
- **Dock viewers** are fixed interface units, not infinitely composable
- **Academy pages** are preserved product surfaces outside the recursive studio
- **Student/final-use experience** is explicitly separated from build/debug

---

### 3.7 The GEK ↔ GEpHR ↔ F(ge) Recursion

The lens system creates cross-referencing:

```
GEK (functional truth)     →  "Circle has center-radius relation"
    ↓ enables
F(ge) (functional output)  →  "Wheel rolls load"
    ↓ carries
GEpHR (meaning)            →  "Divine justice, cosmic order"
    ↓ motivates
GEK (new insight)          →  "Justice requires equal distribution"
```

**Recursion Pattern:** Meaning motivates function, function reveals truth, truth enables new meaning.

**Example:**
```
gek.rotation
    → fge.transport-load (wheel function)
    → gephr.cosmic-cycle (celestial meaning)
    → gek.periodicity (mathematical truth)
    → fge.calendar-computation (new function)
    → gephr.divine-order (refined meaning)
```

**Recursion Risk:** **Meaning overload.** Every function carries meaning, every meaning implies function, spiraling into increasingly abstract interpretations.

**Grounding mechanism:**
- **Carriers** (car.*) ground meaning in physical substrate
- **Skills** (skill.*) ground function in human capacity
- **Operators** (op.*) are discrete transformations, not continuous interpretation

---

## 4. Meta-Recursive Patterns

### 4.1 The System Models Itself

EUCLID_STUDIO contains:
- Skills that define skills (skill-creator)
- Prompts that generate prompts (Figma orchestration agent graph)
- Builds that produce build templates
- Reconciliation processes that reconcile reconciliation

This is **intentional design**, not accidental complexity. The system is meant to evolve its own structure.

### 4.2 The Versioning Recursion

Mesopotamian period versioning:
```
Halaf → Ubaid → Uruk → Jemdet Nasr → Early Dynastic → Akkadian → Ur III → Old Babylonian → Kassite → Neo-Assyrian → Neo-Babylonian → Achaemenid
```

But what versions the versioning? The answer: **the versioning system itself is dated**.

```
01_Skills/Halaf/2026-07-14_lineage-convention-example.md
```

The convention document is inside the first lineage, demonstrating the pattern it describes.

**Recursion Risk:** If the versioning convention changes, all previous versions become ambiguous.

**Grounding mechanism:** The convention is fixed at project creation and explicitly documented in the root README.

---

## 5. Recursion Management Strategies

### 5.1 Grounding Points

Every recursive structure has explicit grounding:

| Recursion | Grounding |
|-----------|-----------|
| GEM composition | Primitives (cannot decompose further) |
| Skill → Build | CANON (human-verified truth) |
| Canon ↔ Instance | Versioning lineages (substantive breaks) |
| Animation cycle | Dated cell sequences |
| Semyceliance | Sessions (time-bounded), Residue (unresolved capture) |
| Prism ↔ Canvas | Academy pages (fixed product surface) |
| GEK ↔ GEpHR ↔ F(ge) | Carriers, Skills (physical grounding) |

### 5.2 Separation Strategies

The system uses explicit separation to prevent recursion collapse:

1. **Component vs. Operator vs. Lens** - Different "drawers" for different types
2. **Canon vs. Provisional** - Established vs. tentative
3. **Skills vs. Plugins vs. Builds** - Definition vs. package vs. output
4. **Student experience vs. Build tools** - Final use vs. meta-work

### 5.3 Time-Binding

Recursions are bounded by time:
- Sessions have dates
- Files have YYYY-MM-DD prefixes
- Lineages have substantive break points
- Cycles have named phases

---

## 6. Potential Recursion Hazards

### 6.1 Unbounded Decomposition

**Risk:** Decomposing artifacts to atomic level, then decomposing atoms.

**Symptom:** A single cylinder seal generates thousands of GEA nodes.

**Mitigation:** Define "useful decomposition depth" per context. Curriculum may stop at GEM level; research may go to GEA.

### 6.2 Skill Drift

**Risk:** Skills improve based on their own outputs, amplifying biases.

**Symptom:** decompose-artifact produces increasingly stylized decompositions that match its own training.

**Mitigation:** External validation against CANON. Human review of Examples before they become training.

### 6.3 Meta-Meta-Meta...

**Risk:** Infinite levels of meta-work.

**Symptom:** Sessions about sessions about sessions. Skills for making skills for making skills.

**Mitigation:** The Residue folder. Unresolved meta-questions go to residue rather than spawning infinite meta-levels.

### 6.4 Canon Oscillation

**Risk:** Evidence revises canon, new canon produces different evidence, which revises canon again.

**Symptom:** Core definitions change every build cycle.

**Mitigation:** Versioning. Canon changes start new lineages, not overwrite existing ones. Both versions coexist until one is explicitly archived.

### 6.5 Breathing Cycle Stuck States

**Risk:** Animation cycle stuck in one phase.

**Symptom:** Everything is "invention" (chaotic novelty) or everything is "saturation" (baroque excess).

**Mitigation:** Explicit phase tracking in cell sequences. Named cycles with dated transitions.

---

## 7. Productive Recursions

Not all recursion is hazardous. The system leverages recursion productively:

### 7.1 Self-Improving Skills

Skills that improve their own definitions enable:
- Automatic documentation updates
- Pattern extraction from successful uses
- Error detection from failed uses

### 7.2 Compositional Richness

GEM recursion enables:
- Complex artifacts from simple primitives
- Shared vocabulary across civilizations
- Graduated complexity for curriculum levels

### 7.3 Knowledge Accumulation

Canon ↔ Instance recursion enables:
- Progressive refinement of theory
- Evidence-grounded truth claims
- Traceable lineage of ideas

### 7.4 Creative Cycles

Animation breathing enables:
- Natural creative rhythm
- Prevents both stagnation and chaos
- Connects to historical/cultural cycles

---

## 8. Implementation Recommendations

### 8.1 For New Skills

When creating skills in 01_Skills/:
1. Define explicit grounding (what can't be decomposed)
2. Specify recursion depth limits
3. Document exit conditions
4. Place in appropriate lineage folder

### 8.2 For New Builds

When generating builds in 05_Instantiations_Builds/:
1. Date all outputs
2. Link to source canon version
3. Flag provisional vs. verified status
4. Capture residue separately

### 8.3 For Canon Updates

When modifying canon in 00_Reconciliation/01_CANON/:
1. Start new lineage if substantive change
2. Document the evidence that motivated change
3. Preserve previous version in archive
4. Update dependent schemas/concepts

### 8.4 For Animation Work

When creating cells in 06_Animation_Studio_Cells/:
1. Name the breathing phase
2. Date each cell
3. Track position in cycle
4. Note transitions between phases

---

## 9. Conclusion

EUCLID_STUDIO is a **deliberately recursive system**. Its recursions are features, not bugs — they enable composition, self-improvement, and creative cycling.

The key to managing recursion is **explicit grounding**:
- Primitives ground composition
- Canon grounds truth
- Dates ground time
- Residue grounds the unresolvable

When recursion threatens to spiral:
1. Check for grounding point
2. Apply separation (different drawer)
3. Time-bind (new lineage/session)
4. Capture residue (don't force resolution)

The system is designed to evolve, but evolution requires both variation (recursion) and selection (grounding). Balance these, and the recursions become productive rather than pathological.

---

*Document created: 2026-09-24*
*Location: geometric-civilizations/docs/EUCLID_STUDIO_RECURSION_ANALYSIS.md*
*Related: GE_TAXONOMY_SPECIFICATION.md, ArtisanalCanvas/AGENTS.md*
