# GE Taxonomy Specification

A faceted graph node taxonomy for the Geometric Civilizations curriculum. This specification defines how to categorize, connect, and inspect nodes in artifact/invention knowledge graphs.

---

## Organizing Principle

**Do not build this as a tree. Build it as a component graph.**

Wrong (tree):
```
GE
└── GEA
    └── GEM
        └── GEpHR
```

Correct (component graph):
```
GEA/GEM components
+ Operators
+ Carriers
+ Skill actions
+ Meaning lenses
+ Function lenses
+ Output/function badges
+ Insight/Ingenuity process markers
= artifact or invention reading
```

Think: **palette → canvas → nested graph → inspector panel**

Terms become draggable tiles, not paragraphs.

---

## The Seven Drawers

### Drawer 1: GE Components

Composable spatial objects.

#### GE
The total spatial object universe.
- Visual treatment: **open canvas / universe frame**
- Use as largest namespace, not a frequently-dragged tile

#### Primitive
A generative operand.
- Visual treatment: **seed tile**
- What can act or be acted on through motion, duration, and vector

Construction grammar:
```
Primitive + Motion Type + Duration + Vector = F(ge)
```

#### GEA (Atomic Geometric Element)
- Visual treatment: **solid tile**

Subtypes:
```
GEA.I  = insignia
GEA.Sh = shape
```

Examples:
```
gea.i.sun-disk
gea.i.crescent-mark
gea.sh.point
gea.sh.line
gea.sh.angle
gea.sh.circle
gea.sh.triangle
gea.sh.square
```

#### GEM (Molecular/Composite)
Any composite element.
- Visual treatment: **compound tile / grouped tile**

Recursive composition:
```
GEM = GEA + GEA
GEM = GEA + GEM
GEM = GEM + GEM
```

Examples:
```
gem.crescent
gem.rosette
gem.8-point-star
gem.arch
gem.tessellation
gem.cylinder-seal-composition
```

---

### Drawer 2: Operators

Operators are **verbs**. They should never look like GEAs or GEMs.
- Visual treatment: **arrow tiles**

#### Transformation Operators
```
op.rotate
op.translate
op.reflect
op.scale
op.shear
op.extrude
op.revolve
op.tessellate
op.repeat
op.wrap
op.cut
op.carve
op.press
op.roll
```

#### Representation Operators
```
rep.3d-to-2d
rep.2d-to-3d
rep.1d-on-3d
rep.surface-projection
rep.relief
rep.incision
rep.stencil
rep.mosaic-assembly
```

Example chains:
```
gea.sh.line + op.rotate → gem.circle
gem.triangle + op.revolve → cone-like form
gem.cylinder + op.roll + rep.3d-to-2d → seal impression
```

Operators sit **between** nodes, not inside nodes.

---

### Drawer 3: Carriers

Where cognition lands.
- Visual treatment: **tray / substrate tile**

Examples:
```
car.wall
car.body
car.clay-tablet
car.pottery
car.cylinder-seal
car.textile
car.mosaic-floor
car.architecture
car.tool
car.institution
```

Carrier metadata:
```
carrier dimension
surface type
material resistance
tool requirements
visibility context
social access
repeatability
```

A circle on a wall, a circle on a pot, a circle as a wheel, and a circle rolled from a cylinder seal are **different construction events**.

---

### Drawer 4: Lenses

Ways of reading components (not components themselves).
- Visual treatment: **transparent overlay / colored lens**

#### GEK (Functional/Conceptual Truth)
```
gek.symmetry
gek.ratio
gek.rotation
gek.load-distribution
gek.projection
gek.circumference
gek.center-radius
```

Use GEK when asking: *What does this GE know or do mathematically/functionally?*

#### GEpHR (Perceptual-Historical Resonance)
Meaning, symbol, cultural resonance, visual rhetoric.
```
gephr.divine-justice
gephr.renewal
gephr.power
gephr.fertility
gephr.boundary
gephr.cosmos
gephr.kingship
```

Use GEpHR when asking: *What does this GE mean in this culture, on this carrier, in this form?*

#### GEU (Ubiquity Flag)
- Visual treatment: **badge, not tile**
- Annotates GEA/GEM; does not replace them

```
gem.rosette + geu.cross-cultural
gea.i.crescent + geu.cross-cultural
gem.spiral + geu.cross-cultural
```

---

### Drawer 5: Skills

Human production capacities.
- Visual treatment: **hand/tool icon tiles**

```
skill.trace
skill.measure
skill.align
skill.center
skill.mirror
skill.repeat
skill.rotate-by-hand
skill.keep-radius
skill.shade
skill.hatch
skill.carve
skill.press
skill.weave
skill.tile
skill.project
skill.balance
skill.sequence
```

A skill tile answers: *What must the maker be able to perform?*

Visual Skill is **production-side**.

---

### Drawer 6: Rhetoric / Effects

Visual Rhetoric is the **effect of composition on perception, meaning, and attention**.
- Visual treatment: **glow / effect badge / annotation ribbon**

```
vr.centering
vr.radiance
vr.symmetry-authority
vr.boundary-making
vr.containment
vr.motion-impression
vr.divine-scale
vr.order
vr.repetition
vr.threshold
vr.balance
```

A Visual Rhetoric tile answers: *What does the composition make the viewer see, feel, infer, or recognize?*

**Key distinction:**
```
Visual Skill = how it is made
Visual Rhetoric = what the made thing does visually
```

Example:
```
skill.keep-radius → produces clean circle
clean circle + gephr.justice → vr.radial-equality
```

---

### Drawer 7: Outputs / Functions

Where **F(ge)** belongs.
- Visual treatment: **output port / function badge**

```
fge.rotate-load
fge.redirect-force
fge.reduce-effort
fge.contain-volume
fge.project-image
fge.fastening
fge.span-opening
fge.mark-ownership
fge.repeat-symbol
```

**GEK vs F(ge):**
```
GEK = the principle/truth
F(ge) = the produced functionality
```

Example:
```
GEK: rotational symmetry
F(ge): wheel rolls load

GEK: inclined plane reduces force
F(ge): screw advances through material
```

Visual model:
```
GEA/GEM + operator + carrier + skill → F(ge)
```

---

## Process Markers

**Timeline/process markers** - not in same drawer as GEA/GEM.
- Visual treatment: **timeline dots, arrows, and lightning choices**

### Insight
A moment/state.
- Visual treatment: **point marker**

```
insight.circle-can-enclose
insight.circle-can-rotate
insight.surface-can-carry-symbol
insight.3d-carrier-can-produce-2d-image
```

### Ingenuity
The delta between insight states.
- Visual treatment: **arrow between points**

```
ingenuity.path-circle-to-field-circle
ingenuity.circle-to-wheel
ingenuity.cylinder-to-rolling-image
ingenuity.inclined-plane-to-screw
```

### Creativity
The choice/reconfiguration capacity.
- Visual treatment: **spark / wildcard connector**

Not a measurable component tile - the **choice event** where the graph is reconfigured.

```
creativity.choice:
"Use the cylinder not merely as an object, but as a rolling image carrier."
```

---

## Visual Library Structure

```
┌──────────────────────────────────────────────────────────────┐
│ COMPONENT PALETTE                                             │
├─────────────┬─────────────┬────────────┬─────────────────────┤
│ GE Units    │ Operators   │ Carriers   │ Lenses              │
│ Primitive   │ op.*        │ car.*      │ GEK / GEpHR / GEU   │
│ GEA.I       │ rep.*       │ mat.*      │                     │
│ GEA.Sh      │             │            │                     │
│ GEM         │             │            │                     │
├─────────────┴─────────────┴────────────┴─────────────────────┤
│ Skills        Visual Rhetoric        Outputs/F(ge)            │
│ skill.*       vr.*                   fge.* / F(ge).*          │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ COMPOSITION CANVAS                                            │
│ Drag components here. Build artifact/invention graph.         │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ INSPECTOR PANEL                                               │
│ Selected node metadata, sources, evidence, lesson section.    │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│ INSIGHT / INGENUITY TIMELINE                                  │
│ State points + delta arrows + evidence/proposed gaps.         │
└──────────────────────────────────────────────────────────────┘
```

---

## Node Types and Visual Shapes

| Type                    | Visual Shape                      | Example                             |
| ----------------------- | --------------------------------- | ----------------------------------- |
| GE / universe           | large frame                       | `ge.spatial-object`                 |
| Primitive               | seed dot                          | `primitive.point`                   |
| GEA.I                   | small diamond                     | `gea.i.sun-disk`                    |
| GEA.Sh                  | solid circle/square/triangle tile | `gea.sh.circle`                     |
| GEM                     | grouped molecule tile             | `gem.rosette`                       |
| Operator                | arrow                             | `op.rotate`                         |
| Representation operator | folded arrow                      | `rep.3d-to-2d`                      |
| Carrier                 | tray/plate                        | `car.cylinder-seal`                 |
| GEK                     | blue lens / formula lens          | `gek.rotation`                      |
| GEpHR                   | gold lens / myth lens             | `gephr.justice`                     |
| GEU                     | small globe badge                 | `geu.cross-cultural`                |
| Visual Skill            | hand/tool icon                    | `skill.carve`                       |
| Visual Rhetoric         | glow/effect badge                 | `vr.radiance`                       |
| F(ge)/FGE               | output port                       | `fge.repeatable-impression`         |
| Insight                 | point on timeline                 | `insight.surface-can-carry-symbol`  |
| Ingenuity               | arrow between points              | `ingenuity.3d-to-2d-image-transfer` |
| Creativity              | spark connector                   | `creativity.reframe-carrier`        |

---

## Edge Types

Standard connectors:
```
composes
contains
carries
is-carrier-for
transformed-by
represented-by
requires-skill
requires-tool
produces
signifies
exhibits
maps-to
outputs
annotated-by
ubiquitous-as
insight-state
ingenuity-delta
```

Example node with edges:
```
gea.sh.circle
  transformed-by → op.rotate
  exhibits → gek.rotational-symmetry
  signifies → gephr.divine-justice
  carried-by → car.cylinder-seal
  requires-skill → skill.keep-radius
  outputs → fge.rotation
```

---

## Example: Cylinder Seal

```
Artifact: Cylinder seal impression

car.stone-cylinder
  carries → gem.iconographic-band

gem.iconographic-band
  composed-of → gea.i.deity-symbol
  composed-of → gea.sh.line
  composed-of → gem.repeated-figure

car.stone-cylinder
  transformed-by → op.roll
  transformed-by → op.translate
  representation → rep.3d-to-2d

rep.3d-to-2d
  produces → fge.continuous-impression

skill.carve
  required-by → gem.iconographic-band

skill.sequence
  required-by → gem.narrative-band

gephr.authority
  lens-on → gem.iconographic-band

gek.rotation
  lens-on → op.roll

insight:
  3D carrier can produce 2D image

ingenuity:
  carved cylinder → rolling narrative surface
```

---

## Example: Screw

```
Artifact: Screw

gem.helix
  composed-of → gea.sh.circle
  composed-of → gea.sh.line
  composed-of → gea.sh.triangle / inclined-plane logic

gem.helix
  transformed-by → op.wrap
  transformed-by → op.rotate
  transformed-by → op.translate

gek.inclined-plane
  lens-on → gem.helix

gek.rotation-to-translation
  lens-on → op.rotate + op.translate

skill.thread-cutting
  required-by → gem.helix-on-cylinder

fge.fastening
  produced-by → gem.helix-on-cylinder

insight:
  inclined plane reduces effort

ingenuity:
  inclined plane wrapped around axis converts rotation into linear advance

creativity:
  reframe plane as spiral path
```

---

## Key Distinctions

### Visual Skill vs Visual Rhetoric

**Visual Skill** (production side): *Can the maker do it?*
```
draw straight line
maintain radius
center composition
mirror symmetry
shade volume
hatch surface
tile a plane
carve relief
roll cylinder seal
weave alternating pattern
```

**Visual Rhetoric** (reception/meaning side): *What does the form do to perception and meaning?*
```
centers attention
radiates authority
signals divine order
stabilizes composition
creates motion
creates enclosure
creates hierarchy
creates threshold
```

Connection:
```
skill.radial-repeat → enables → vr.radiance
skill.symmetry-control → enables → vr.authority / vr.balance / vr.order
```

### GEpHR vs Visual Rhetoric

**GEpHR** (cultural meaning):
```
circle = divine justice
crescent = renewal
star = divine presence
triangle = stability/power
```

**Visual Rhetoric** (perceptual effect):
```
circle radiates evenly
crescent suggests phase/change
star creates radial attention
triangle creates upward thrust/stability
```

Graph flow:
```
GEA/GEM property → visual rhetoric effect → GEpHR cultural meaning

gea.sh.circle → vr.radial-equality → gephr.justice
```

### GEK vs F(ge)

**GEK** (principle):
```
circle has center-radius relation
circle can rotate around center
inclined plane reduces force
arch redirects load
```

**F(ge)** (produced functionality):
```
wheel rolls load
pulley redirects force
screw fastens
arch spans opening
seal repeats authority mark
```

---

## Decomposition Modes

Four ways to view any artifact:

### Mode 1: Composition View
*What is it made of?*
```
artifact → GEMs → GEAs
```

### Mode 2: Construction View
*How was it made?*
```
carrier + tools + skills + operators + materials
```

### Mode 3: Meaning View
*What does it mean?*
```
GEA/GEM → Visual Rhetoric → GEpHR
```

### Mode 4: Function View
*What does it do?*
```
GEA/GEM → GEK → operator → F(ge)
```

---

## Layer Model

For any artifact or invention:

```
Layer 1: Component skeleton     → GEA/GEM
Layer 2: Carrier/material       → where it lives
Layer 3: Operator/action        → how it transforms
Layer 4: Skill/tool             → how it was made
Layer 5: GEK                    → what principle it reveals
Layer 6: GEpHR                  → what meaning it carries
Layer 7: F(ge)                  → what function it outputs
Layer 8: Insight/Ingenuity      → what changed over time
```

Each term gets its own job. No fighting for oxygen.

---

## Compact Taxonomy

```
GE
│
├── COMPOSABLE THINGS
│   ├── Primitive
│   ├── GEA
│   │   ├── GEA.I
│   │   └── GEA.Sh
│   └── GEM
│       └── recursive composite: GEA+GEA / GEA+GEM / GEM+GEM
│
├── VERBS
│   ├── op.*  transformation
│   └── rep.* representation / dimensional mapping
│
├── WHERE
│   └── carrier / material / institution
│
├── LENSES
│   ├── GEK     function/truth
│   ├── GEpHR   meaning/rhetoric/cultural resonance
│   └── GEU     cross-cultural flag
│
├── HUMAN CAPACITY
│   ├── Visual Skill
│   └── Tool Use
│
├── EFFECTS
│   ├── Visual Rhetoric
│   └── F(ge) / FGE
│
└── PROCESS
    ├── Insight
    ├── Ingenuity
    └── Creativity
```

---

## Naming Convention

Dot notation:
```
gea.i.*
gea.sh.*
gem.*
gek.*
gephr.*
geu.*
op.*
rep.*
car.*
mat.*
skill.*
tool.*
vr.*
fge.*
insight.*
ingenuity.*
creativity.*
```

---

## Component Card Schema

```yaml
id:
label:
type:
subtype:
dimensionality:
can_compose_with:
can_be_transformed_by:
can_be_carried_by:
typical_skills:
typical_visual_rhetoric:
typical_GEK:
typical_GEpHR:
typical_Fge:
GEU_flag:
examples:
source_links:
```

Example:
```yaml
id: gea.sh.circle
label: Circle
type: GEA
subtype: GEA.Sh
dimensionality: 1D boundary / 2D field depending construction
can_compose_with: [line, point, triangle, circle, arc]
can_be_transformed_by: [op.rotate, op.scale, op.repeat, op.project]
can_be_carried_by: [wall, pottery, seal, wheel, coin, architecture]
typical_skills: [keep-radius, find-center, trace-boundary, fill-field]
typical_visual_rhetoric: [radiance, equality, enclosure, completeness]
typical_GEK: [center-radius, circumference, rotation]
typical_GEpHR: [sun, justice, divine order]
typical_Fge: [rolling, enclosing, rotating, distributing]
GEU_flag: possible
```

---

## Graph JSON Export Format

```json
{
  "artifact": "cylinder_seal",
  "components": ["car.stone-cylinder", "gem.iconographic-band"],
  "operators": ["op.roll", "op.translate", "rep.3d-to-2d"],
  "skills": ["skill.carve", "skill.sequence"],
  "lenses": ["gek.rotation", "gephr.authority"],
  "outputs": ["fge.continuous-impression"],
  "process": {
    "insight": "3D carrier can produce 2D image",
    "ingenuity": "rolling carrier becomes narrative printing tool"
  }
}
```

---

## Summary

> **GEA and GEM are the manipulable spatial components. Operators transform them. Carriers receive them. Skills produce them. GEK reads what they do. GEpHR reads what they mean. GEU flags cross-cultural recurrence. Visual Rhetoric describes their perceptual effect. F(ge) names their functional output. Insight marks a state. Ingenuity marks the delta. Creativity marks the choice that reconfigures the graph.**
