# 01 Architecture Bridge Glossary

File: 01_Architecture_Bridge_Glossary.md

Purpose: Shared language for “equal parts form + function” in material/architectural objects. Tags are namespaced to plug into your existing system.

Core tags

- #arch/form-function — Use this on any object explicitly designed with aesthetic and utilitarian parity.
- #arch/constraint/structural — Load, span, compression/tension constraints that shape the design grammar.
- #arch/grammar/module — Units, bays, tiles, bricks, rosettes; repeatable parts.
- #arch/grammar/proportion — Ratios, grids, harmonic modules guiding layout.
- #arch/technique/joinery — Means of assembly: mortise/tenon, dovetail, bitumen bonding, clamp cramps, dowels.
- #arch/technique/brickwork — Bond patterns: stretcher, header, herringbone, diapering.
- #arch/technique/vault — Corbel, true arch, barrel vault, dome precursors.
- #arch/flow/procession — Planned human movement through space (routes, thresholds).
- #arch/wayfinding/iconic — Visual cues embedded for navigation/state signaling.
- #arch/surface/cosmogram — Cosmological diagrams embedded in facade/paving.
- #arch/material/behavior — Thermal mass, porosity, weathering, glazing.
- #arch/standard/measure — Modules, rod/cord units, brick size standards.
- #arch/institution/branding — Civic/state identity encoded in architecture.

Connections to MAGIC

- #magic/m: math/structure (proportion, module, symmetry, statics)
- #magic/a: aesthetics (ornament grammar, motif logic)
- #magic/g: geometric element (the controlling shape/motif)
- #magic/i: ideology/myth (cosmogram, axis mundi, patron deities)
- #magic/c: comptroller (standards, labor organization, patronage)

Notes

- Use #arch/form-function only when BOTH aesthetic and utilitarian constraints are evident and mutually shaping design choices.
- Mirror this status in YAML: parity_index and function_map (see templates).

# 02 Form + Function Criteria Rubric

File: 02_Form_Function_Rubric.md

Goal: A consistent way to declare “equal parts form + function.”

Scoring fields (0–2 each; total out of 10)

1. Functional necessity (FN): Does the object solve a clear physical/organizational problem? (0 none, 1 partial, 2 strong)
2. Aesthetic intentionality (AI): Is there deliberate visual grammar beyond bare utility? (0 none, 1 some, 2 strong)
3. Coupling strength (CS): Do function constraints drive aesthetic grammar (or vice versa)? (0 weak, 1 moderate, 2 strong)
4. Standardization impact (SI): Are modules/proportions standardized for reproduction/governance? (0 none, 1 local, 2 civic-state)
5. Embodied affordances (EA): Does human movement/gesture inform the geometry? (0 incidental, 1 occasional, 2 integral)

Parity index

- Compute parity_index = (AI + FN + CS)/6. Values:
    - 0.00–0.33: function-led (utilitarian)
    - 0.34–0.66: mixed
    - 0.67–1.00: parity or art-led with functional lock-in

Declaration rule

- Tag #arch/form-function when:
    - FN ≥ 1 AND AI ≥ 1 AND CS ≥ 1, and parity_index ≥ 0.50, OR
    - Clear historical scholarship evidences mutual shaping (cite in sources).

Evidence checklist

- Cite at least one artifact photo/plan.
- Note a module or proportion that affects both structure and pattern.
- Document at least one embodied affordance (procession, threshold posture, grip).

# 03 YAML Templates

File: 03_YAML_Templates_Architecture_Bridge.md

## — ArchitectureObject (material culture with explicit form+function)

## type: material subtype: architecture-object id: arch-unique title: civ: era: [] site: [] g_element: [] # e.g., ["arch","rosette","grid"] materials: [] # e.g., ["glazed-brick","mudbrick","stone"] dimensions: module: "" # e.g., "brick: 33×33×8 cm" ratio: "" # e.g., "1:2:√3" structural: load_path: [] # ["compression","corbel","true-arch"] span: "" # clear span if applicable constraints: [] # ["thermal","erosion","supply"] grammar: modules: [] # ["tile-rosette","brick-course"] proportion_rules: [] # ["6-petal rotational symmetry","3:2 facade bays"] surface_motifs: [] # ["rosette","lion-frieze"] function_map: primary: [] # ["procession-routing","flood-control","insulation"] secondary: [] # ["state-branding","wayfinding","acoustic"] embodied_affordances: [] # ["locomotion/procession","threshold-pause","orientation by color"] semiotics: signs: [] connotations: [] cosmogram: [] standards: measure: [] # rods, cords, brick standard labor: [] # guilds, corvée, workshops parity_rubric: FN: 0 AI: 0 CS: 0 SI: 0 EA: 0 parity_index: 0.0 sources: [] tags: [#material,#arch/form-function]

## — Lesson Bridge (Form+Function)

## type: lesson id: lesson-{{civ}}-{{element}}-bridge-g{{grade}} title: {{civ | title}} – {{element | title}} – Architecture Bridge day: {{day}} # A or B depending on where you teach it grade: [{{grade}}] civ: {{civ}} era: [{{era}}] g_element: [{{element}}] semiotics_focus: [] ritual_focus: [] everyday_focus: [] embodied_practice: [] magic: m: 0.0 a: 0.0 g: 1.0 i: 0.0 c: 0.0 bridge_focus: question: "How does form lock with function here?" criteria: ["module","proportion","load-path","movement"] artifact_refs: [] assessments: technique: [] math_reasoning: [] reflection: [] draws_from: [] tags: [#lesson,#arch/form-function,#grade/{{grade}}]

# 04 Dataview Dashboards

File: 04_Dashboards_Architecture_Bridge.md

— Finder: Architecture objects with strong parity

`TABLE WITHOUT ID   file.link as Item,   civ as Civ,   era as Era,   g_element as Element,   grammar.modules as Modules,   function_map.primary as Functions,   parity_rubric.parity_index as Parity FROM "" WHERE type = "material" AND subtype = "architecture-object"   AND contains(file.tags, "#arch/form-function")   AND parity_rubric.parity_index >= 0.5 SORT Parity desc`

— By geometric element across civs

`TABLE WITHOUT ID   file.link as Object,   civ as Civ,   era as Era,   grammar.proportion_rules as Proportion,   structural.load_path as Load,   function_map.primary as Function FROM "" WHERE type = "material" AND subtype = "architecture-object"   AND contains(g_element, input("element", "arch")) SORT Civ asc`

— Lesson Bridge seeds (pulls objects for current lesson’s element/civ/era)

`TABLE WITHOUT ID   file.link as Objects,   grammar.modules as Modules,   function_map.primary as Functions FROM "" WHERE type = "material"   AND subtype = "architecture-object"   AND any(g_element, (g) => contains(this.g_element, g))   AND contains(civ, this.civ)   AND any(era, (e) => contains(this.era, e))`

— QA: Missing parity rubrics

`TABLE file.link, parity_rubric WHERE type = "material" AND subtype = "architecture-object"   AND (parity_rubric.FN + parity_rubric.AI + parity_rubric.CS + parity_rubric.SI + parity_rubric.EA) = 0`

— QA: Missing module or function mapping

`TABLE file.link, grammar.modules, function_map.primary WHERE type = "material" AND subtype = "architecture-object"   AND (length(grammar.modules) = 0 OR length(function_map.primary) = 0)`

# 05 Example Entries

File: 05_Examples_Architecture_Bridge.md

## — Example 1: Ishtar Gate Rosette Facade (Mesopotamia)

## type: material subtype: architecture-object id: arch-meso-ishtar-rosette-facade title: Ishtar Gate — Rosette Tile Facade civ: mesopotamia era: ["neo-babylonian"] site: ["Babylon"] g_element: ["circle","rosette","grid"] materials: ["glazed-brick","bitumen"] dimensions: module: "brick ~ 33×33×8 cm (varies by source)" ratio: "facade bays approx. 1:2" structural: load_path: ["compression","archway (segmental)"] span: "processional gate passages" constraints: ["erosion","floodplain climate","mass production"] grammar: modules: ["tile-rosette","lion-frieze unit","brick-course"] proportion_rules: ["rosette spacing in equal grid", "order-6 rotational symmetry per rosette"] surface_motifs: ["rosette","lion","bull"] function_map: primary: ["procession-routing","gate marking","visibility at distance"] secondary: ["state-branding","urban-wayfinding"] embodied_affordances: ["locomotion/procession","threshold-pause","orientation by color"] semiotics: signs: ["rosette: symbol of divine favor"] connotations: ["prosperity","legitimacy"] cosmogram: ["axis-mundi implied by gate sequence"] standards: measure: ["cord grid for layout","brick size standard"] labor: ["state workshops","tile glazing specialists"] parity_rubric: FN: 2 AI: 2 CS: 2 SI: 2 EA: 2 parity_index: 1.0 sources: ["src-pergamon-museum","src-robertkoldewey-babylon","src-porada-seals"] tags: [#material,#arch/form-function,#arch/grammar/module,#arch/standard/measure,#arch/flow/procession,#arch/institution/branding,#magic/a,#magic/c]

## — Example 2: Mudbrick Buttressed Wall (Uruk-period)

## type: material subtype: architecture-object id: arch-meso-uruk-buttress-wall title: Uruk-Period Buttressed Mudbrick Wall civ: mesopotamia era: ["uruk"] site: ["Uruk"] g_element: ["pilaster","recess","vertical-rhythm","grid"] materials: ["mudbrick","plaster"] dimensions: module: "brick ~ 30×30×7 cm (approx.)" ratio: "buttress:recess rhythm ~ 1:1 to 2:1" structural: load_path: ["compression","buttress thickening"] span: "long facade runs" constraints: ["material fragility","rain erosion"] grammar: modules: ["buttress unit","recess unit"] proportion_rules: ["regular bay spacing","base-to-height taper"] surface_motifs: ["shadow banding"] function_map: primary: ["wall stiffening","rain-shedding via recess rhythm"] secondary: ["monumental rhythm","processional guidance"] embodied_affordances: ["locomotion/procession along facade","wayfinding via rhythm"] semiotics: signs: ["ordered facade implies civic order"] connotations: ["stability","authority"] cosmogram: [] standards: measure: ["brick module course heights"] labor: ["corvée labor crews"] parity_rubric: FN: 2 AI: 1 CS: 2 SI: 1 EA: 1 parity_index: 0.67 sources: ["src-uruk-excavation-reports","src-holliday-ancient-mesopotamian-architecture"] tags: [#material,#arch/form-function,#arch/technique/brickwork,#arch/grammar/module,#magic/m,#magic/a]

## — Example 3: Corbelled Niche Altar (Small Shrine)

## type: material subtype: architecture-object id: arch-meso-corbel-niche-altar title: Corbelled Niche Altar civ: mesopotamia era: ["early-dynastic"] site: ["various"] g_element: ["niche","step","triangle/corbel"] materials: ["mudbrick","wood lintel"] dimensions: module: "half-brick corbel increments" ratio: "step retreat ~ 1/4 brick per course" structural: load_path: ["pseudo-arch via corbel"] span: "narrow opening" constraints: ["limited long timber"] grammar: modules: ["stepped corbel unit"] proportion_rules: ["equal retreat per course","odd-number course emphasis"] surface_motifs: ["painted border"] function_map: primary: ["housing cult statue","protecting recess opening"] secondary: ["visual focus","acoustic amplification (local)"] embodied_affordances: ["posture/offer posture alignment","visual-centering"] semiotics: signs: ["threshold to sacred micro-space"] connotations: ["approach → respect"] cosmogram: ["micro-axis within wall plane"] standards: measure: ["brick halves/quarters"] labor: ["mason + painter pairing"] parity_rubric: FN: 2 AI: 2 CS: 2 SI: 1 EA: 2 parity_index: 0.83 sources: ["src-early-dynastic-altars","src-ritual-architecture-notes"] tags: [#material,#arch/form-function,#arch/technique/vault,#arch/grammar/proportion,#ritual/space/shrine,#magic/i]

# 06 Quick-Start Checklist

File: 06_Quick_Start_Architecture_Bridge.md

- Add the new #arch/* tags to your Tag Glossary.
- Use the ArchitectureObject YAML for gates, walls, altars, thresholds, pavements, roofs—anything where pattern and load/path co-determine design.
- Score parity using the rubric; set parity_index; tag #arch/form-function when criteria met.
- For lessons, create a “Lesson Bridge” note that:
    - Lists 1–2 architecture-objects for the same geometric element as the unit.
    - Identifies module, proportion, load path, and a human-movement affordance.
    - Adds one Day A technique and one Day B system link.
- Use the dashboards to pull candidates and to QA missing modules/functions.
- Reference MAGIC explicitly: how math/proportion enables the aesthetic, and how standards/patronage lock it in civically.

Teaching beat (plug into Day A/B)

- Day A: Touch → see → draw the module. Students reconstruct a small facade rhythm with paper bricks or tiles.
- Day B: Show how the module standard creates repeatable governance signals (wayfinding, brand, processional order). Ask “But for which constraint would this module be different?”

SEL tie-in

- “Find your structure.” Students design a personal “module” (tiny pattern + habit) that supports a function (calming before work). Embodied: 3-breath threshold before starting a task.