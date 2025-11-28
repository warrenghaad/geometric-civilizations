# SDA Week Tagging System
File: 01_SDA_Week_Tagging_System.md

Purpose
Balance the week across Myth → Geometric Element → Metaphor (Day A), Architecture as Bridge (form+function), and Systems/Discovery (Day B), with tag parity to avoid material-culture bias.

----------------------------
1) Weekly Container
----------------------------
---
type: week
id: week-{{civ}}-{{element}}-g{{grade}}-w{{week_no}}
title: {{civ | title}} – {{element | title}} – Week {{week_no}}
civ: {{civ}}
era: [{{era}}]
grade: [{{grade}}]
g_element: [{{element}}]
myth:
  deity: ""
  metaphor: ""         # e.g., “many-as-one,” “turning toward the center”
balance:
  dayA_tags_target: 4
  bridge_tags_target: 2
  dayB_tags_target: 4
schedule:
  dayA_id: lesson-{{civ}}-{{element}}-dayA-g{{grade}}
  bridge_id: bridge-{{civ}}-{{element}}-g{{grade}}
  dayB_id: lesson-{{civ}}-{{element}}-dayB-g{{grade}}
draws_from: []          # myth-*, art-*, arch-*, concept-*, ontology image sets
tags: [#week]
---

----------------------------
2) Tag Bundles (pick 3–5 each day)
----------------------------
Day A (Embodied / Material / Meaning)
- #semiotics/symbol
- #semiotics/icon
- #semiotics/metaphor
- #semiotics/grammar/pattern
- #semiotics/cosmogram
- #embodied/gesture
- #embodied/rhythm
- #embodied/sensorimotor/rotation
- #embodied/proprioception/centering
- #artifact
- #material
- #ritual/space
- #everyday/tool
- Architecture (cap 1–2): #arch/form-function, #arch/grammar/module

Bridge (Architecture as form+function)
- #arch/form-function
- #arch/grammar/module
- #arch/standard/measure
- #arch/flow/procession
- #arch/technique/…
- #arch/institution/branding

Day B (Systems / Math / Institution)
- #magic/m
- #magic/c
- #math/ratio
- #math/symmetry/rotational
- #math/tiling/plane
- #math/graph
- #design/specification
- #design/constraint
- #standard/module
- #standard/measure
- #standard/protocol
- #institution/labor
- #institution/workshop
- #infrastructure/transport
- #market/exchange
- #discovery
- #innovation
- #invention

----------------------------
3) Day A Template
----------------------------
---
type: lesson
id: lesson-{{civ}}-{{element}}-dayA-g{{grade}}
title: {{civ | title}} – {{element | title}} – Day A
day: A
civ: {{civ}}
era: [{{era}}]
grade: [{{grade}}]
g_element: [{{element}}]
myth_ref:
  deity: ""
  metaphor: ""
sel:
  prompt: "What is the metaphor and how do I enact it?"
  skill: "Grounding; embodied attention"
semiotics_focus: []
embodied_practice: []
material_objects: []
architecture_bridge_refs: []
tags:
  - #lesson
  - #semiotics/metaphor
  - #semiotics/grammar/pattern
  - #embodied/gesture
  - #artifact
  - #arch/form-function
---

----------------------------
4) Architecture Bridge Note
----------------------------
---
type: bridge
id: bridge-{{civ}}-{{element}}-g{{grade}}
title: Architecture Bridge – {{civ | title}} – {{element | title}}
civ: {{civ}}
era: [{{era}}]
grade: [{{grade}}]
g_element: [{{element}}]
arch_objects: []               # ["arch-…","arch-…"]
module_or_ratio: ""
load_path: []
procession: []
form_function_note: ""
tags:
  - #bridge
  - #arch/form-function
  - #arch/grammar/module
  - #arch/standard/measure
  - #arch/flow/procession
---

----------------------------
5) Day B Template
----------------------------
---
type: lesson
id: lesson-{{civ}}-{{element}}-dayB-g{{grade}}
title: {{civ | title}} – {{element | title}} – Day B
day: B
civ: {{civ}}
era: [{{era}}]
grade: [{{grade}}]
g_element: [{{element}}]
review:
  myth_metaphor: ""
  institutionalization: []
systems_focus: []
pathway:
  chain:
    - "element → module"
    - "module → standard"
    - "standard → capability"
    - "capability → invention"
sel:
  prompt: "Why did this matter? What if it hadn’t existed?"
  skill: "Causal reasoning; future thinking"
tags:
  - #lesson
  - #magic/m
  - #magic/c
  - #math/ratio
  - #math/symmetry/rotational
  - #math/tiling/plane
  - #design/constraint
  - #standard/module
  - #standard/measure
  - #discovery
  - #innovation
  - #invention
---