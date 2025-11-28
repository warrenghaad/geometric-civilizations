{
  "metadata": {
    "title": "Dimensionality Atlas",
    "version": "1.0",
    "description": "Comprehensive schema of geometric dimensional permutations, materials, artifacts, architectures, math principles, cognition links, aesthetics, and deity symbol catalogs.",
    "invariantDrivers": ["m: math/structure", "a: geometrical art + material objects", "i: ideology/mythology/meaning", "p: power/institutional scaffold"]
  },
  "dimensions": [
    {
      "id": "D1",
      "name": "1D primitives",
      "primitives": ["dot", "segment", "ray", "line", "curve (parametric)", "polyline"],
      "math": ["set theory (points)", "metric spaces (distance)", "parametric functions", "combinatorics of segments", "graph theory (paths)", "measure (length)"],
      "materials": ["incised marks on clay", "ink on papyrus", "carved lines on stone", "warp or weft thread in textiles"],
      "examples": [
        "Prehistoric tally notches (bone, antler)",
        "Sumerian reed stylus impressions (clay tablets)",
        "Egyptian rulings for column alignment",
        "Textile warp threads (linear arrays)"
      ],
      "cognition": {
        "numeration": ["tally marks → cardinality recognition → base systems"],
        "writing": ["proto-writing line strokes → cuneiform wedges → linear scripts"],
        "visualization": ["line as boundary and measure"]
      }
    },
    {
      "id": "D1_2D",
      "name": "1D marks on 2D surfaces",
      "surfaces": ["tablets", "papyrus", "parchment", "paper", "walls", "pottery surfaces"],
      "operations": ["hatching", "contour drawing", "rulings", "grids", "calligraphic strokes"],
      "math": ["coordinate grids", "ratio and proportion on layout", "projective hints via contours"],
      "art": ["calligraphy styles (Chinese, Arabic, Blackletter)", "contour art", "hatching for shading"],
      "materials": ["ink, pigments, reeds, brushes, stylus"],
      "examples": [
        "Greek geometric pottery with ruled bands",
        "Islamic calligraphy (kufic/naskh) rulings",
        "Renaissance drawing with perspective guidelines"
      ]
    },
    {
      "id": "D1_3D",
      "name": "1D marks on 3D surfaces",
      "surfaces3D": ["vessels", "sculptures", "architecture (columns, domes)", "tools"],
      "operations": ["incised lines", "carved flutes", "engraved contours", "grooves for assembly"],
      "math": ["geodesics on surfaces", "curvature", "unwrap mapping (developable surfaces)"],
      "art": ["fluted columns (vertical 1D rhythm)", "engraved bands on metalwork"],
      "materials": ["stone, wood, metal, ceramic"],
      "examples": [
        "Doric column fluting (Greece)",
        "Maya carved linework on stelae",
        "Engraved banding on Islamic metal bowls"
      ]
    },
    {
      "id": "D1_make2D",
      "name": "1D assembling 2D objects on 2D",
      "construction": ["line meshes → nets", "grids → panels", "weaves → cloth"],
      "math": ["graph to planar embedding", "lattices", "tiling via line intersections"],
      "art": ["line-based ornaments", "grid-based page design"],
      "materials": ["threads, reeds, papyrus strips, wooden laths"],
      "examples": [
        "Loom weaving: warp/weft produce 2D textile",
        "Egyptian grid canon for figure drawing",
        "Architectural drafting grids"
      ]
    },
    {
      "id": "D2_patterns",
      "name": "2D primitives and patterns",
      "primitives": ["polygon", "circle", "ellipse", "spiral", "curve families (Bezier, sine)", "star polygons"],
      "math": ["Euclidean geometry", "symmetry groups", "tessellations (regular, semi-regular, Penrose)", "frieze/rosette/Wallpaper groups", "calculus for curves"],
      "art": ["ornament systems", "iconography", "biomorphic forms"],
      "materials": ["tile, textile, paper, paint, ceramic glaze"],
      "examples": [
        "Islamic geometric tessellation (girih)",
        "Greek meander",
        "Roman mosaic floors",
        "Chinese cloud scrolls"
      ]
    },
    {
      "id": "D2_on_2D",
      "name": "2D on 2D structures",
      "structures": ["tiles, panels, manuscripts, flags, carpets"],
      "math": ["tiling theory", "color symmetry", "combinatorics of motif layout"],
      "art": ["ornament, heraldry, manuscript illumination"],
      "materials": ["ceramic tile, textiles (flatweave), parchment/paper, paint"],
      "examples": [
        "Persian carpets (biomorphic arabesque)",
        "Roman mosaic pavements",
        "Illuminated manuscripts (Celtic knotwork)"
      ]
    },
    {
      "id": "D2_on_3D",
      "name": "2D patterns on 3D objects",
      "surfaces3D": ["vessels, domes, vaults, sculpture skin, tools, armor"],
      "math": ["surface parameterization", "projection (stereographic, cylindrical)", "developable vs non-developable wrapping"],
      "art": ["arabesque on domes", "scales on armor", "banding and cartouches"],
      "materials": ["glazed ceramics, metal emboss, stone relief, lacquer"],
      "examples": [
        "Muqarnas with 2D pattern logic extended to 3D",
        "Chinese cloisonné on vessels",
        "Greek black-figure on amphorae"
      ]
    },
    {
      "id": "D3_objects",
      "name": "3D objects: megaliths, figurines, tokens, sculptures",
      "primitives3D": ["polyhedra", "solids of revolution", "surfaces (ruled, minimal)", "complex meshes"],
      "math": ["solid geometry", "statics", "optimization (minimal surfaces)", "topology (handles, genus)"],
      "art": ["sculpture, ritual objects, tokens", "iconic form language"],
      "materials": ["stone, wood, metal, clay, bone"],
      "examples": [
        "Megalithic dolmens (post-lintel)",
        "Indus tokens with carved symbols",
        "Egyptian statuary canons",
        "Greek kouroi (proportion)"
      ]
    },
    {
      "id": "D3_arch_elements",
      "name": "3D architectural elements",
      "elements": ["post-and-lintel", "arch", "vault", "dome", "truss", "buttress", "cantilever", "muqarnas", "pendentive", "ribbing", "column orders", "stereotomy"],
      "math": ["catenary curves", "thrust lines", "vector decomposition", "triangulation", "stability optimization"],
      "art": ["Gothic verticality", "Islamic muqarnas honeycomb", "Renaissance harmonic proportion"],
      "materials": ["stone, brick, timber, iron, concrete"],
      "examples": [
        "Roman arch & vault",
        "Gothic ribbed vault + flying buttress",
        "Pantheon dome (coffers lighten mass)"
      ]
    },
    {
      "id": "D3_versions_of_D2",
      "name": "3D versions of 2D patterns in architecture",
      "techniques": ["muqarnas (3D tessellation)", "coffering (3D relief grid)", "tracery (3D carved 2D pattern)", "screen/jali (2D motifs extruded)"],
      "math": ["extrusion, revolution, lofting", "dual graphs of tessellations", "symmetry lifting to 3D"],
      "art": ["Islamic geometric reliefs", "Gothic stone tracery", "Indo-Islamic jali screens"],
      "materials": ["stone, stucco, wood, metal"],
      "examples": [
        "Alhambra muqarnas cornices",
        "Gothic rose window tracery",
        "Mughal jali lattices"
      ]
    }
  ],
  "materials": [
    { "id": "MAT_stone", "name": "Stone", "properties": ["compressive strength"], "uses": ["structure", "carving"] },
    { "id": "MAT_brick", "name": "Brick", "properties": ["modular, compressive"], "uses": ["vaults, walls"] },
    { "id": "MAT_wood", "name": "Wood", "properties": ["tension/compression, joinery"], "uses": ["frames, trusses"] },
    { "id": "MAT_metal", "name": "Metal (bronze/iron/steel)", "properties": ["tension, casting, forging"], "uses": ["mechanisms, reinforcement"] },
    { "id": "MAT_clay", "name": "Clay/Ceramic", "properties": ["moldable, fired"], "uses": ["vessels, tiles"] },
    { "id": "MAT_textile", "name": "Textile", "properties": ["flexible, patternable"], "uses": ["carpets, garments"] },
    { "id": "MAT_glass", "name": "Glass", "properties": ["transparency, color"], "uses": ["windows, mosaic"] }
  ],
  "mechanisms": [
    { "id": "MECH_lever", "name": "Lever", "principle": "Moment/torque", "shapeLinks": ["segment", "beam (1D→3D)"] },
    { "id": "MECH_pulley", "name": "Pulley", "principle": "Redirect force", "shapeLinks": ["circle", "rope (1D)"] },
    { "id": "MECH_gear", "name": "Gear", "principle": "Rotational ratio", "shapeLinks": ["circle", "tooth profile"] },
    { "id": "MECH_screw", "name": "Screw", "principle": "Helical incline", "shapeLinks": ["spiral", "cylinder"] },
    { "id": "MECH_cam", "name": "Cam", "principle": "Profile-to-motion", "shapeLinks": ["curve"] },
    { "id": "MECH_escapement", "name": "Escapement", "principle": "Discrete energy release", "shapeLinks": ["tooth geometry", "pendulum (curve)"] }
  ],
  "machines": [
    { "id": "M_clock", "name": "Mechanical Clock", "composition": ["MECH_gear", "MECH_escapement"], "architecture": ["frame", "dial"], "periods": ["Medieval Europe"] },
    { "id": "M_press", "name": "Printing Press", "composition": ["MECH_screw", "MECH_lever"], "architecture": ["post-and-beam"], "periods": ["Renaissance"] },
    { "id": "M_loom", "name": "Loom (Jacquard)", "composition": ["MECH_cam"], "architecture": ["frame"], "periods": ["Industrial Age"] }
  ],
  "mathPrinciples": [
    { "id": "M_ratio", "name": "Ratio & Proportion", "domains": ["layout", "pressure", "harmonic design"], "effects": ["balance", "scale"] },
    { "id": "M_perspective", "name": "Linear Perspective", "domains": ["visualization", "architecture drawing"], "effects": ["illusion of depth"] },
    { "id": "M_tessellation", "name": "Tessellation & Symmetry", "domains": ["pattern", "ornament", "tiling"], "effects": ["repeatability, modularity"] },
    { "id": "M_topology", "name": "Topology", "domains": ["surfaces", "knots", "textiles"], "effects": ["continuity, genus"] },
    { "id": "M_catenary", "name": "Catenary & Arches", "domains": ["vaults, domes"], "effects": ["stability, thrust management"] },
    { "id": "M_section", "name": "Sections & Stereotomy", "domains": ["stone cutting, vault construction"], "effects": ["fit, load paths"] },
    { "id": "M_trig", "name": "Trigonometry", "domains": ["astronomy, surveying"], "effects": ["angle/length relations"] }
  ],
  "proofsAndSections": [
    { "id": "PS_euclid", "name": "Euclidean Proof Style", "structure": ["definition", "postulate", "proposition", "proof"] },
    { "id": "PS_stereotomy", "name": "Stereotomy Sections", "structure": ["voussoir geometry", "thrust modeling"] },
    { "id": "PS_projective", "name": "Projective Constructions", "structure": ["cross-ratio", "vanishing lines"] }
  ],
  "aestheticsByCivilization": [
    {
      "id": "AE_egypt",
      "name": "Egyptian Axial Symmetry",
      "motifs": ["lotus", "papyrus", "ankh", "solar disk"],
      "geometry": ["grids", "bilateral symmetry"],
      "materials": ["stone relief", "painted walls", "gold inlay"]
    },
    {
      "id": "AE_greece",
      "name": "Greek Classical Proportion",
      "motifs": ["meander", "palmette"],
      "geometry": ["golden ratio", "order canons"],
      "materials": ["marble, painted pottery"]
    },
    {
      "id": "AE_islamic",
      "name": "Islamic Geometric Tessellation",
      "motifs": ["girih tiles", "arabesque", "calligraphic bands"],
      "geometry": ["rosette groups, star polygons", "symmetry groups"],
      "materials": ["tile, stucco, wood, metal"]
    },
    {
      "id": "AE_persian_biomorphic",
      "name": "Persian Biomorphic Arabesque",
      "motifs": ["vine scrolls", "split-leaf palmettes"],
      "geometry": ["curvilinear repetition, modular panels"],
      "materials": ["textiles, tile, manuscript"]
    },
    {
      "id": "AE_gothic",
      "name": "Gothic Verticality",
      "motifs": ["tracery", "pointed arch", "rose windows"],
      "geometry": ["rib networks, radials"],
      "materials": ["stone, glass"]
    },
    {
      "id": "AE_renaissance",
      "name": "Renaissance Harmonic Order",
      "motifs": ["coffering", "classical orders"],
      "geometry": ["proportion canon, perspective"],
      "materials": ["stone, fresco"]
    },
    {
      "id": "AE_bauhaus",
      "name": "Bauhaus Functional Minimalism",
      "motifs": ["grid, primary forms"],
      "geometry": ["orthogonal clarity"],
      "materials": ["steel, glass, concrete"]
    }
  ],
  "textiles": [
    { "id": "TX_plain", "name": "Plain Weave", "geometry": "orthogonal grid", "civilizations": ["Egypt", "China", "Indus"], "patterns": ["checks, stripes"] },
    { "id": "TX_twill", "name": "Twill Weave", "geometry": "diagonal repeat", "civilizations": ["Europe", "China"], "patterns": ["herringbone"] },
    { "id": "TX_knot", "name": "Knot Pile (Carpet)", "geometry": "node lattice", "civilizations": ["Persia"], "patterns": ["arabesque fields, medallions"] }
  ],
  "tokensArtifacts": [
    { "id": "TA_indus_token", "name": "Indus Seal & Token", "geometry": "2D relief on 3D stamp", "math": ["symbol coding"], "material": "steatite" },
    { "id": "TA_mesopotamia_cylinder", "name": "Mesopotamian Cylinder Seal", "geometry": "2D band → 3D cylinder → rolled 2D", "math": ["surface unwrapping"], "material": "stone" }
  ],
  "cognitionLinks": [
    {
      "id": "CO_num_write_viz",
      "name": "Number ↔ Writing ↔ Visualization",
      "sequence": [
        "1D tallies → quantities",
        "symbol codification → writing",
        "grids/ratios → layout → diagrams",
        "perspective → mental models of 3D"
      ],
      "effectsOnInvention": [
        "standardization of measures",
        "algorithmic layout (type, textiles)",
        "precision design (stereotomy, machinery)"
      ]
    }
  ],
  "dimensionalInteractions": [
    { "id": "DI_1D_to_2D", "from": "D1", "to": "D2_patterns", "mechanism": "line accumulation → shape closure", "examples": ["polygon from segments", "spiral from curve"] },
    { "id": "DI_2D_to_3D_extrude", "from": "D2_patterns", "to": "D3_objects", "mechanism": "extrusion/rotation/loft", "examples": ["column from rectangle extrude", "bowl from circle revolution"] },
    { "id": "DI_wrap_2D_on_3D", "from": "D2_on_2D", "to": "D2_on_3D", "mechanism": "projection/wrapping", "examples": ["tile motif on dome via stereographic"] }
  ],
  "architecturalProblemSolvers": [
    { "id": "AP_arch", "name": "Arch", "problem": "span under compression", "math": ["M_catenary"], "materials": ["MAT_stone", "MAT_brick"] },
    { "id": "AP_buttress", "name": "Flying Buttress", "problem": "counter lateral thrust", "math": ["vector decomposition"], "materials": ["MAT_stone"] },
    { "id": "AP_truss", "name": "Truss", "problem": "span under tension/compression", "math": ["triangulation"], "materials": ["MAT_wood", "MAT_metal"] },
    { "id": "AP_dome", "name": "Dome", "problem": "cover large area in compression", "math": ["thrust lines"], "materials": ["MAT_concrete", "MAT_brick", "MAT_stone"] }
  ],
  "civilization2DOrnaments": [
    { "id": "OR_islamic", "name": "Islamic Tessellation", "groups": ["rosette", "star", "girih"], "math": ["M_tessellation"], "dimensionUse": ["D2_on_2D", "D2_on_3D", "D3_versions_of_D2"] },
    { "id": "OR_persian_biomorph", "name": "Persian Arabesque", "groups": ["vine scrolls"], "math": ["curvilinear symmetries"], "dimensionUse": ["D2_on_2D", "D2_on_3D"] },
    { "id": "OR_celtic", "name": "Celtic Knotwork", "groups": ["interlace"], "math": ["M_topology"], "dimensionUse": ["D2_on_2D", "D2_on_3D"] },
    { "id": "OR_greek", "name": "Greek Meander", "groups": ["key pattern"], "math": ["grid + turns"], "dimensionUse": ["D2_on_2D"] }
  ],
  "periods": [
    { "id": "PER_prehistory", "name": "Prehistory" },
    { "id": "PER_mesopotamia", "name": "Mesopotamia" },
    { "id": "PER_egypt", "name": "Egypt" },
    { "id": "PER_greece", "name": "Greece" },
    { "id": "PER_rome", "name": "Rome" },
    { "id": "PER_china", "name": "China" },
    { "id": "PER_indus", "name": "Indus" },
    { "id": "PER_mesoamerica", "name": "Mesoamerica" },
    { "id": "PER_medieval", "name": "Medieval Europe" },
    { "id": "PER_islamic", "name": "Islamic Patterns" },
    { "id": "PER_renaissance", "name": "Renaissance" },
    { "id": "PER_impression_feudal", "name": "Impressionism/Feudalism" },
    { "id": "PER_modern", "name": "Post/Modern Abstract Art" },
    { "id": "PER_biomimicry", "name": "Biomimicry" }
  ],
  "deitiesCatalog": [
    {
      "id": "DE_greek",
      "name": "Greek Pantheon",
      "deities": [
        { "name": "Zeus", "domain": "Sky/Thunder", "symbols": ["thunderbolt", "eagle", "oak"], "stories": ["Olympian rule", "Io"] },
        { "name": "Athena", "domain": "Wisdom/Craft", "symbols": ["owl", "olive", "aegis"], "stories": ["Parthenon patron", "Arachne weaving"] },
        { "name": "Apollo", "domain": "Sun/Music/Prophecy", "symbols": ["lyre", "laurel"], "stories": ["Delphi", "Marsyas"] },
        { "name": "Hermes", "domain": "Messenger/Trade", "symbols": ["caduceus", "winged sandals"], "stories": ["Invention of lyre", "Guide of souls"] },
        { "name": "Hephaestus", "domain": "Forge/Tech", "symbols": ["anvil", "hammer"], "stories": ["Automata in workshop"] },
        { "name": "Poseidon", "domain": "Sea", "symbols": ["trident", "horse"], "stories": ["Walls of Troy"] },
        { "name": "Minos", "domain": "King of Crete", "symbols": ["labyrinth", "bull"], "stories": ["Minotaur, Daedalus, Ariadne"] },
        { "name": "Dionysus", "domain": "Wine/Drama", "symbols": ["thyrsus", "vine"], "stories": ["Theater, masks"] }
      ]
    },
    {
      "id": "DE_egypt",
      "name": "Egyptian",
      "deities": [
        { "name": "Ra", "domain": "Sun", "symbols": ["solar disk"], "stories": ["Daily journey"] },
        { "name": "Osiris", "domain": "Afterlife", "symbols": ["crook & flail"], "stories": ["Dismemberment, resurrection"] },
        { "name": "Isis", "domain": "Magic/Motherhood", "symbols": ["throne", "knot"], "stories": ["Reviving Osiris"] },
        { "name": "Thoth", "domain": "Writing/Measure", "symbols": ["ibis", "stylus"], "stories": ["Invents writing"] },
        { "name": "Horus", "domain": "Kingship/Sky", "symbols": ["falcon", "udjat eye"], "stories": ["Eye of Horus"] }
      ]
    },
    {
      "id": "DE_mesopotamia",
      "name": "Mesopotamian",
      "deities": [
        { "name": "Enki/Ea", "domain": "Wisdom/Water", "symbols": ["streams"], "stories": ["Crafts & creation"] },
        { "name": "Inanna/Ishtar", "domain": "Love/War", "symbols": ["star", "lion"], "stories": ["Descent to underworld"] },
        { "name": "Marduk", "domain": "Power/Order", "symbols": ["dragon"], "stories": ["Tiamat slaying"] },
        { "name": "Nabu", "domain": "Writing", "symbols": ["tablet", "stylus"], "stories": ["Scribe of gods"] }
      ]
    },
    {
      "id": "DE_norse",
      "name": "Norse",
      "deities": [
        { "name": "Odin", "domain": "Wisdom/Runes", "symbols": ["runes", "ravens"], "stories": ["Hanging on Yggdrasil for knowledge"] },
        { "name": "Thor", "domain": "Thunder", "symbols": ["Mjolnir"], "stories": ["Giant-slaying"] },
        { "name": "Freyja", "domain": "Love/Seiðr", "symbols": ["falcon cloak"], "stories": ["Seidr magic"] }
      ]
    },
    {
      "id": "DE_hindu",
      "name": "Hindu",
      "deities": [
        { "name": "Vishnu", "domain": "Preserver", "symbols": ["chakra", "conch"], "stories": ["Avatars"] },
        { "name": "Shiva", "domain": "Transformer", "symbols": ["trident", "damaru"], "stories": ["Nataraja cosmic dance"] },
        { "name": "Lakshmi", "domain": "Fortune", "symbols": ["lotus"], "stories": ["Churning of ocean"] },
        { "name": "Ganesh", "domain": "Remover of Obstacles", "symbols": ["elephant head"], "stories": ["Broken tusk, writing patron"] }
      ]
    },
    {
      "id": "DE_china",
      "name": "Chinese",
      "deities": [
        { "name": "Fuxi/Nüwa", "domain": "Order/Creation", "symbols": ["compass & square"], "stories": ["Civilization founding"] },
        { "name": "Gong Gong", "domain": "Water Chaos", "symbols": ["flood"], "stories": ["Tilted heavens"] }
      ]
    },
    {
      "id": "DE_mesoamerica",
      "name": "Mesoamerican",
      "deities": [
        { "name": "Quetzalcoatl", "domain": "Feathered Serpent/Wisdom", "symbols": ["serpent", "feather"], "stories": ["Calendar & knowledge"] },
        { "name": "Tlaloc", "domain": "Rain", "symbols": ["goggled eyes"], "stories": ["Water and fertility"] }
      ]
    }
  ],
  "mythsAndSELStories": [
    {
      "id": "MY_minotaur",
      "title": "Minos & the Minotaur",
      "themes": ["maze navigation", "ingenuity", "compassion"],
      "geometryLinks": ["labyrinth (2D-on-2D → 2D-on-3D in palace)", "thread as 1D guide"],
      "SELPrompts": [
        "When have you felt stuck in a maze emotionally? What thread helps you?",
        "How can design thinking (maps, steps) turn chaos into a path?"
      ]
    },
    {
      "id": "MY_arachne",
      "title": "Arachne’s Weave",
      "themes": ["craft, humility, consequence"],
      "geometryLinks": ["weave grids (1D→2D)", "pattern storytelling"],
      "SELPrompts": [
        "What skill do you practice daily? How can you honor others without dimming yourself?",
        "Where does patience turn threads into fabric in your life?"
      ]
    }
  ],
  "linkages": {
    "dimensionToMechanism": [
      { "dimensionId": "D2_patterns", "mechanismId": "MECH_gear", "notes": "Circle → gear profile" },
      { "dimensionId": "D2_patterns", "mechanismId": "MECH_screw", "notes": "Spiral → helical thread" },
      { "dimensionId": "D1", "mechanismId": "MECH_lever", "notes": "Line/beam as lever arm" }
    ],
    "dimensionToArchitecture": [
      { "dimensionId": "D3_arch_elements", "element": "arch", "math": ["M_catenary"] },
      { "dimensionId": "D3_arch_elements", "element": "truss", "math": ["triangulation"] },
      { "dimensionId": "D3_versions_of_D2", "element": "muqarnas", "math": ["symmetry lifting"] }
    ],
    "aestheticToCivilization": [
      { "aestheticId": "AE_islamic", "periodId": "PER_islamic" },
      { "aestheticId": "AE_persian_biomorphic", "periodId": "PER_islamic" },
      { "aestheticId": "AE_gothic", "periodId": "PER_medieval" },
      { "aestheticId": "AE_renaissance", "periodId": "PER_renaissance" }
    ],
    "cognitionToInventions": [
      { "cognitionId": "CO_num_write_viz", "machineId": "M_press", "notes": "Layouts, type proportions, standardization" },
      { "cognitionId": "CO_num_write_viz", "machineId": "M_clock", "notes": "Time standardization" }
    ]
  }
}