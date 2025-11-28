  {
    "version": "1.0",
    "about": {
      "title": "Geometric Dimensionality, Combinations, Manifestations, Math, and Myth Ontology",
      "authoring_model": "gpt-5",
      "notes": [
        "This dataset models dimensional permutations (1D, 2D, 3D) and their combinations across supports and materials.",
        "It links to cultural artifacts, architectural translations, and mathematical frameworks (proportion, perspective, sections).",
        "It includes a mythology index with symbols and geometric associations.",
        "Exhaustiveness is unattainable; this is an extensible scaffold with exemplary coverage."
      ]
    },
    "ontology": {
      "dimensions": [
        { "id": "dim-0d", "name": "0D", "description": "Point as location; dot; node" },
        { "id": "dim-1d", "name": "1D", "description": "Line/curve; path; stroke; thread" },
        { "id": "dim-2d", "name": "2D", "description": "Surface; area-bound shape; plane" },
        { "id": "dim-3d", "name": "3D", "description": "Solid/volume; mass; relief" },
        { "id": "dim-4d", "name": "4D", "description": "Time as param; motion/animation; sequencing (for perspective, kinematics)" }
      ],
      "geometric_elements": [
        { "id": "geo-point", "dimension": "0D", "name": "Point", "variants": ["dot", "node", "bead"] },
        { "id": "geo-line", "dimension": "1D", "name": "Line", "variants": ["segment", "stroke", "edge", "thread"] },
        { "id": "geo-curve", "dimension": "1D", "name": "Curve", "variants": ["arc", "spiral", "sine", "catenary"] },
        { "id": "geo-polygon", "dimension": "2D", "name": "Polygon", "variants": ["triangle", "square", "hexagon", "star"] },
        { "id": "geo-circle", "dimension": "2D", "name": "Circle", "variants": ["disk", "ring", "mandala"] },
        { "id": "geo-curvearea", "dimension": "2D", "name": "Curvilinear area", "variants": ["arabesque panel", "biomorphic tile"] },
        { "id": "geo-surface", "dimension": "2D", "name": "Surface", "variants": ["plane", "fabric", "wall", "ceramic slip"] },
        { "id": "geo-polyhedron", "dimension": "3D", "name": "Polyhedron", "variants": ["cube", "tetrahedron", "dodecahedron"] },
        { "id": "geo-sphere", "dimension": "3D", "name": "Sphere", "variants": ["globe", "bead", "dome cap"] },
        { "id": "geo-cylinder", "dimension": "3D", "name": "Cylinder", "variants": ["column", "spool", "pillar"] },
        { "id": "geo-cone", "dimension": "3D", "name": "Cone", "variants": ["spire", "funnel"] },
        { "id": "geo-archform", "dimension": "3D", "name": "Architectural Form", "variants": ["arch", "vault", "dome", "truss", "buttress"] },
        { "id": "geo-relief", "dimension": "3D", "name": "Relief", "variants": ["bas-relief", "high-relief", "intaglio"] }
      ],
      "operations": [
        { "id": "op-tiling", "name": "Tiling/Tessellation", "description": "Repeat units in plane with symmetry group" },
        { "id": "op-frieze", "name": "Frieze Repetition", "description": "1D repetition across a band" },
        { "id": "op-lattice", "name": "Lattice/Network", "description": "Grid or net structure" },
        { "id": "op-extrude", "name": "Extrusion", "description": "Lift 2D profile into 3D along perpendicular" },
        { "id": "op-revolve", "name": "Revolution", "description": "Rotate 2D profile around axis (lathe/dome)" },
        { "id": "op-project", "name": "Projection", "description": "Map 3D to 2D (orthographic, perspective, stereographic)" },
        { "id": "op-unwrap", "name": "Unwrapping/Net", "description": "Flatten 3D surface to 2D pattern (nets, developables)" },
        { "id": "op-emboss", "name": "Emboss/Relief", "description": "Raise/depress 2D pattern into 3D surface" },
        { "id": "op-weave", "name": "Weaving/Braiding", "description": "Interlacing 1D threads to make 2D/3D forms" },
        { "id": "op-symmetry", "name": "Symmetry Operation", "description": "Translation, reflection, rotation, glide" },
        { "id": "op-subdivide", "name": "Subdivision", "description": "Recursive division; fractals; geometric refinement" },
        { "id": "op-section", "name": "Section/Cut", "description": "Intersect 3D with 2D plane to study/prove" },
        { "id": "op-param", "name": "Parametric Deformation", "description": "Proportional scaling, perspective foreshortening, curvature" }
      ],
      "pattern_types": [
        { "id": "pat-frieze", "name": "Frieze", "groups": 7 },
        { "id": "pat-wallpaper", "name": "Wallpaper", "groups": 17 },
        { "id": "pat-rosace", "name": "Rosette/Radial", "groups": "cyclic/dihedral" },
        { "id": "pat-biomorphic", "name": "Biomorphic Arabesque", "groups": "varied curvilinear symmetries" },
        { "id": "pat-interlace", "name": "Interlace/Knot", "groups": "planar interweave" }
      ],
      "materials": [
        { "id": "mat-stone", "name": "Stone", "classes": ["limestone", "granite", "marble"] },
        { "id": "mat-clay", "name": "Clay/Ceramic" },
        { "id": "mat-wood", "name": "Wood" },
        { "id": "mat-metal", "name": "Metal", "classes": ["bronze", "iron", "brass", "steel", "gold"] },
        { "id": "mat-textile", "name": "Textile", "classes": ["wool", "cotton", "silk", "linen"] },
        { "id": "mat-glass", "name": "Glass" },
        { "id": "mat-papyrus", "name": "Papyrus/Paper/Parchment" }
      ],
      "techniques": [
        { "id": "tech-incision", "name": "Incision/Engraving" },
        { "id": "tech-carving", "name": "Carving" },
        { "id": "tech-casting", "name": "Casting" },
        { "id": "tech-weaving", "name": "Weaving" },
        { "id": "tech-embroidery", "name": "Embroidery" },
        { "id": "tech-mosaic", "name": "Mosaic" },
        { "id": "tech-tiling", "name": "Tiling" },
        { "id": "tech-painting", "name": "Painting/Pigments" },
        { "id": "tech-stainedglass", "name": "Stained Glass Leading" },
        { "id": "tech-masonry", "name": "Masonry/Joinery" },
        { "id": "tech-turning", "name": "Turning/Revolve (lathe)" }
      ],
      "architectural_elements": [
        { "id": "arch-arch", "name": "Arch" },
        { "id": "arch-vault", "name": "Vault (barrel, groin, ribbed)" },
        { "id": "arch-dome", "name": "Dome (hemispherical, onion, muqarnas transition)" },
        { "id": "arch-buttress", "name": "Buttress/Flying Buttress" },
        { "id": "arch-truss", "name": "Truss" },
        { "id": "arch-muqarnas", "name": "Muqarnas (3D stalactite from 2D cells)" },
        { "id": "arch-screen", "name": "Screen/Mashrabiya (perforated 2D to 3D facade)" },
        { "id": "arch-rose", "name": "Rose Window (radial 2D in 3D wall)" }
      ],
      "math_concepts": [
        { "id": "math-proportion", "name": "Proportion", "topics": ["ratio", "means", "module systems"] },
        { "id": "math-perspective", "name": "Perspective", "topics": ["vanishing points", "foreshortening", "projective"] },
        { "id": "math-symmetry", "name": "Symmetry Groups", "topics": ["frieze", "wallpaper", "dihedral"] },
        { "id": "math-geometry", "name": "Euclidean Geometry", "topics": ["congruence", "similarity", "constructions"] },
        { "id": "math-trig", "name": "Trigonometry", "topics": ["angles", "sine/cosine", "projections"] },
        { "id": "math-section", "name": "Sections/Proofs", "topics": ["cross-sections", "solids by slicing", "Cavalieri"] },
        { "id": "math-param", "name": "Parametric/Deformation", "topics": ["curvature", "transformations", "mapping distortions"] }
      ],
      "cultural_contexts": [
        { "id": "civ-egypt", "name": "Ancient Egypt" },
        { "id": "civ-greece", "name": "Classical Greece" },
        { "id": "civ-islam", "name": "Islamic Civilizations" },
        { "id": "civ-india", "name": "South Asia/India" },
        { "id": "civ-china", "name": "China" },
        { "id": "civ-meso", "name": "Mesoamerica" },
        { "id": "civ-medieval-eu", "name": "Medieval Europe" },
        { "id": "civ-renaissance", "name": "Renaissance Europe" },
        { "id": "civ-andes", "name": "Andean Civilizations" }
      ]
    },
    "combinatorics": {
      "dimension_mappings": [
        {
          "id": "map-1d-on-2d",
          "name": "1D on 2D",
          "description": "Lines/curves drawn on surfaces (painted, incised, woven).",
          "common_materials": ["mat-papyrus", "mat-textile", "mat-clay", "mat-stone"],
          "operations": ["op-frieze", "op-tiling", "op-symmetry", "op-weave"]
        },
        {
          "id": "map-1d-on-3d",
          "name": "1D on 3D",
          "description": "Linear marks on volumetric objects (incised pottery, carved columns).",
          "common_materials": ["mat-clay", "mat-stone", "mat-metal", "mat-wood"],
          "operations": ["op-emboss", "op-incision", "op-weave"]
        },
        {
          "id": "map-1d-builds-2d-on-2d",
          "name": "1D composing 2D on 2D",
          "description": "Threads forming planar textiles; strokes forming planar drawings.",
          "common_materials": ["mat-textile", "mat-papyrus"],
          "operations": ["op-weave", "op-lattice", "op-tiling"]
        },
        {
          "id": "map-2d-on-2d",
          "name": "2D on 2D",
          "description": "Tessellations, ornaments, mosaics on flat surfaces.",
          "common_materials": ["mat-stone", "mat-ceramic", "mat-papyrus", "mat-textile"],
          "operations": ["op-tiling", "op-symmetry", "op-subdivide"]
        },
        {
          "id": "map-2d-on-3d",
          "name": "2D on 3D",
          "description": "Patterns applied to curved solids (vessels, domes, bodies).",
          "common_materials": ["mat-clay", "mat-stone", "mat-metal", "mat-glass"],
          "operations": ["op-project", "op-unwrap", "op-emboss"]
        },
        {
          "id": "map-2d-to-3d",
          "name": "2D becomes 3D",
          "description": "Extrusion/revolution/embossing of plan into volume (columns, domes).",
          "operations": ["op-extrude", "op-revolve", "op-emboss"]
        },
        {
          "id": "map-3d-objects",
          "name": "3D Objects",
          "description": "Megaliths, figurines, tokens, sculpture, architecture.",
          "operations": ["op-section", "op-param"]
        },
        {
          "id": "map-3d-versions-of-2d",
          "name": "3D versions of 2D patterns",
          "description": "Muqarnas, mashrabiya, perforated stone screens, rib networks.",
          "operations": ["op-extrude", "op-emboss", "op-subdivide"]
        }
      ],
      "permutation_rules": [
        "Select base dimension of motif (0D/1D/2D).",
        "Select support dimension (2D surface or 3D body).",
        "Apply operations (tiling, symmetry, weave, projection, emboss, extrude, revolve).",
        "Select material + technique compatible with support curvature.",
        "Optional: transform by proportion/perspective/parametric deformation.",
        "Document cultural context, function, and math linkage."
      ]
    },
    "manifestations": [
      {
        "id": "man-egypt-grids",
        "title": "Egyptian Canon Grids",
        "dimension_mapping": "map-1d-on-2d",
        "elements": ["geo-line", "geo-rectangle"],
        "materials": ["mat-papyrus"],
        "techniques": ["tech-painting"],
        "culture": "civ-egypt",
        "pattern_type": "pat-lattice",
        "math_links": ["math-proportion", "math-geometry"],
        "description": "Gridded 1D lines establish 2D proportion for human figures; modules regulate composition and writing columns.",
        "number_writing_visualization": {
          "number": "Modular ratios define body parts.",
          "writing": "Hieroglyph columns aligned to grids.",
          "visualization": "Drafting proportion before painting."
        }
      },
      {
        "id": "man-greece-meander",
        "title": "Greek Meander Frieze",
        "dimension_mapping": "map-1d-on-2d",
        "elements": ["geo-line"],
        "materials": ["mat-stone", "mat-ceramic"],
        "techniques": ["tech-painting", "tech-carving"],
        "culture": "civ-greece",
        "pattern_type": "pat-frieze",
        "math_links": ["math-symmetry", "math-geometry"],
        "description": "1D line creates a repeating 2D band; dihedral symmetries manifest order."
      },
      {
        "id": "man-islam-tess",
        "title": "Islamic Tessellations",
        "dimension_mapping": "map-2d-on-2d",
        "elements": ["geo-polygon", "geo-curvearea", "geo-circle"],
        "materials": ["mat-ceramic", "mat-stone"],
        "techniques": ["tech-tiling", "tech-mosaic", "tech-incision"],
        "culture": "civ-islam",
        "pattern_type": "pat-wallpaper",
        "math_links": ["math-symmetry", "math-geometry", "math-subdivide"],
        "description": "17 wallpaper groups explored in complex star/rosette networks; biomorphic Persian arabesques integrate sacred proportion."
      },
      {
        "id": "man-renaissance-persp",
        "title": "Renaissance Perspective Drawings",
        "dimension_mapping": "map-2d-on-2d",
        "elements": ["geo-line", "geo-polygon", "geo-circle"],
        "materials": ["mat-papyrus"],
        "techniques": ["tech-painting"],
        "culture": "civ-renaissance",
        "pattern_type": "pat-lattice",
        "math_links": ["math-perspective", "math-proportion", "math-projective"],
        "description": "Projective geometry renders 3D scenes onto 2D planes with vanishing points; establishes visual proof via sections and gridding."
      },
      {
        "id": "man-islam-muqarnas",
        "title": "Muqarnas: 3D Version of 2D Cells",
        "dimension_mapping": "map-3d-versions-of-2d",
        "elements": ["geo-archform"],
        "materials": ["mat-stone", "mat-plaster", "mat-wood"],
        "techniques": ["tech-masonry", "tech-carving"],
        "culture": "civ-islam",
        "pattern_type": "pat-subdivide",
        "math_links": ["math-geometry", "math-proportion"],
        "description": "2D geometric cells are extruded and stepped to create 3D stalactite vaults, mediating square-to-dome transitions in architecture."
      },
      {
        "id": "man-medieval-rose",
        "title": "Gothic Rose Window",
        "dimension_mapping": "map-2d-on-3d",
        "elements": ["geo-circle", "geo-polygon"],
        "materials": ["mat-glass", "mat-stone"],
        "techniques": ["tech-stainedglass", "tech-masonry"],
        "culture": "civ-medieval-eu",
        "pattern_type": "pat-rosace",
        "math_links": ["math-symmetry", "math-proportion"],
        "description": "Radial geometry translated into stone tracery and glass; 2D plan inset into 3D wall and vault system."
      },
      {
        "id": "man-andes-khipu",
        "title": "Andean Khipu (Quipu)",
        "dimension_mapping": "map-1d-on-3d",
        "elements": ["geo-line", "geo-curve"],
        "materials": ["mat-textile"],
        "techniques": ["tech-weaving", "tech-embroidery"],
        "culture": "civ-andes",
        "pattern_type": "pat-frieze",
        "math_links": ["math-proportion", "math-geometry"],
        "description": "1D knotted cords encode numbers; a tangible interface between number and record-keeping (proto-writing and computation).",
        "number_writing_visualization": {
          "number": "Decimal positional values encoded in knots.",
          "writing": "Information encoding without script.",
          "visualization": "Materialized data structure with hierarchical cords."
        }
      },
      {
        "id": "man-meso-steps",
        "title": "Mesoamerican Stepped Pyramids",
        "dimension_mapping": "map-2d-to-3d",
        "elements": ["geo-polygon", "geo-archform"],
        "materials": ["mat-stone"],
        "techniques": ["tech-masonry"],
        "culture": "civ-meso",
        "pattern_type": "pat-subdivide",
        "math_links": ["math-geometry", "math-proportion", "math-astronomy"],
        "description": "2D stepped profiles extruded to 3D mass; alignments encode calendrical astronomy; sections used for design and ritual procession."
      },
      {
        "id": "man-greece-megaliths",
        "title": "Greek Megalithic Architecture: Post-and-Lintel",
        "dimension_mapping": "map-3d-objects",
        "elements": ["geo-archform"],
        "materials": ["mat-stone"],
        "techniques": ["tech-masonry"],
        "culture": "civ-greece",
        "math_links": ["math-geometry", "math-proportion"],
        "description": "3D solids composed from 2D elevations and sections; trig and proportion govern span/height ratios."
      },
      {
        "id": "man-persian-biomorphic",
        "title": "Persian Biomorphic Arabesque Textiles",
        "dimension_mapping": "map-1d-builds-2d-on-2d",
        "elements": ["geo-curve", "geo-curvearea"],
        "materials": ["mat-textile"],
        "techniques": ["tech-weaving", "tech-embroidery"],
        "culture": "civ-islam",
        "pattern_type": "pat-biomorphic",
        "math_links": ["math-symmetry", "math-proportion"],
        "description": "Curvilinear 1D threads build continuous 2D biomorphic patterns; tiled and mirrored to cover surfaces; later carved as 3D stucco."
      }
    ],
    "architecture_translations": [
      {
        "id": "archtrans-mashrabiya",
        "title": "Mashrabiya Screens",
        "from_2d_pattern": "pat-wallpaper",
        "to_3d_element": "arch-screen",
        "operations": ["op-extrude", "op-emboss"],
        "benefits": ["solar control", "privacy", "ventilation"],
        "math_links": ["math-proportion", "math-symmetry"]
      },
      {
        "id": "archtrans-muqarnas",
        "title": "Muqarnas Cells",
        "from_2d_pattern": "pat-rosace",
        "to_3d_element": "arch-muqarnas",
        "operations": ["op-subdivide", "op-extrude"],
        "benefits": ["transition geometry", "acoustic diffusion", "ornament-structure fusion"]
      },
      {
        "id": "archtrans-ribvault",
        "title": "Gothic Rib Vaults",
        "from_2d_pattern": "pat-lattice",
        "to_3d_element": "arch-vault",
        "operations": ["op-extrude", "op-revolve"],
        "benefits": ["load channelling", "thin walls", "large windows"],
        "math_links": ["math-geometry", "math-section"]
      }
    ],
    "math_links": {
      "proportion": {
        "id": "math-proportion",
        "effects": [
          "Sets modular grids for 2D and 3D (Egyptian canon, Vitruvian modules).",
          "Controls transformations between plan, elevation, and section.",
          "Regulates ornament scale when mapped to curved surfaces."
        ],
        "dimensional_impacts": [
          "1D→2D: line rhythms to area modules.",
          "2D→3D: plan proportion controls massing.",
          "2D on 3D: proportional compensation for curvature (equal-area distortion management)."
        ]
      },
      "perspective": {
        "id": "math-perspective",
        "effects": [
          "Projects 3D scenes onto 2D reliably (vanishing points, horizon).",
          "Enables verification via sections and foreshortening.",
          "Introduces time/observer as 4th parameter in visualization."
        ],
        "dimensional_impacts": [
          "3D→2D: projective mapping alters shape metrics but preserves incidence/collinearity.",
          "2D patterns on 3D: painted illusions of relief/space (trompe-l'oeil)."
        ]
      },
      "sections": {
        "id": "math-section",
        "effects": [
          "Analyze internal structure by slicing.",
          "Prove volume equivalences (Cavalieri).",
          "Derive profiles for vaults, domes, arches."
        ],
        "dimensional_impacts": [
          "3D→2D: sections reduce solids to analyzable curves.",
          "2D→3D: stacking sections reconstructs volumes (lofting)."
        ]
      },
      "parametrics": {
        "id": "math-param",
        "effects": [
          "Deforms patterns to fit curved surfaces (conformal vs. equal-area tradeoffs).",
          "Generates families of forms (arches with varying rise/span).",
          "Animates mechanisms and kinetic facades."
        ]
      }
    },
    "number_writing_visualization": {
      "nexus_examples": [
        {
          "id": "nexus-abacus",
          "title": "Counting Boards/Abacus",
          "dimension_mapping": "map-1d-on-3d",
          "description": "Beads (0D/3D) along rods (1D) on a frame (2D/3D) to compute numbers—embodied arithmetic."
        },
        {
          "id": "nexus-cuneiform",
          "title": "Cuneiform Tablets",
          "dimension_mapping": "map-1d-on-3d",
          "description": "Stylus makes 1D wedge impressions on 3D clay tablets; number and writing converge in bookkeeping and geometry."
        },
        {
          "id": "nexus-geometry-proofs",
          "title": "Geometric Proof Diagrams",
          "dimension_mapping": "map-1d-builds-2d-on-2d",
          "description": "Lines and arcs on papyrus/parchment instantiate abstract theorems; sections used for architectural design."
        }
      ]
    },
    "mythology": {
      "deities": [
        {
          "id": "my-egypt-thoth",
          "name": "Thoth",
          "culture": "civ-egypt",
          "domains": ["writing", "measurement", "knowledge"],
          "symbols": ["ibis", "stylus", "moon disk"],
          "geometric_associations": ["lunar cycles (circle)", "measurement rods (1D)"],
          "image_refs": [],
          "stories": ["Patron of scribes; mediator of cosmic order (Ma'at)."]
        },
        {
          "id": "my-greece-athena",
          "name": "Athena",
          "culture": "civ-greece",
          "domains": ["crafts", "wisdom", "war strategy"],
          "symbols": ["owl", "olive tree", "aegis"],
          "geometric_associations": ["weaving patterns (frieze/interlace)", "ordered city plans (grid)"],
          "image_refs": [],
          "stories": ["Patron of weaving and city-building; Parthenon proportions."]
        },
        {
          "id": "my-greece-dedalus",
          "name": "Daedalus",
          "culture": "civ-greece",
          "domains": ["craftsmanship", "architecture"],
          "symbols": ["labyrinth", "tools"],
          "geometric_associations": ["maze/labyrinth (tessellated paths)", "mechanical birds (projection and articulation)"],
          "image_refs": [],
          "stories": ["Builder of the Labyrinth; father of Icarus."]
        },
        {
          "id": "my-greece-minos-minotaur",
          "name": "Minos and the Minotaur",
          "culture": "civ-greece",
          "domains": ["kingship", "sacrifice", "trial"],
          "symbols": ["labyrinth", "bull"],
          "geometric_associations": ["labyrinthine 2D-to-3D spatial logic", "spiral meanders"],
          "image_refs": [],
          "stories": ["Minos commissions Daedalus to build the Labyrinth to contain the Minotaur; Theseus navigates using thread (1D) to resolve a 3D spatial puzzle."]
        },
        {
          "id": "my-mesopotamia-nabu",
          "name": "Nabu",
          "culture": "civ-meso",
          "domains": ["writing", "wisdom"],
          "symbols": ["stylus", "tablet"],
          "geometric_associations": ["cuneiform wedge geometry", "accounting grids"],
          "image_refs": [],
          "stories": ["Patron of scribes; linked to measurement and fate."]
        },
        {
          "id": "my-india-vishwakarma",
          "name": "Vishwakarma",
          "culture": "civ-india",
          "domains": ["architecture", "crafts", "engineering"],
          "symbols": ["tools", "measuring cord"],
          "geometric_associations": ["vastu grids", "mandala proportions"],
          "image_refs": [],
          "stories": ["Divine architect; codifies temple geometry."]
        },
        {
          "id": "my-china-luban",
          "name": "Lu Ban",
          "culture": "civ-china",
          "domains": ["carpentry", "construction"],
          "symbols": ["ink-line", "square", "compass"],
          "geometric_associations": ["inked snap-lines (1D)", "modular timber grids (2D/3D)"],
          "image_refs": [],
          "stories": ["Legendary carpenter; attributed with tools and joinery methods."]
        }
      ],
      "symbols_index": [
        { "symbol": "labyrinth", "linked_to": ["my-greece-dedalus", "my-greece-minos-minotaur"], "geometric": ["maze", "spiral", "grid"] },
        { "symbol": "knot", "linked_to": ["my-greece-athena"], "geometric": ["interlace", "braid (1D→2D)"] },
        { "symbol": "moon disk", "linked_to": ["my-egypt-thoth"], "geometric": ["circle", "cycle"] },
        { "symbol": "stylus/tablet", "linked_to": ["my-mesopotamia-nabu"], "geometric": ["1D on 3D", "grid"] }
      ]
    },
    "query_examples": [
      {
        "question": "Show 3D versions of 2D patterns in architecture.",
        "filter": { "dimension_mapping": "map-3d-versions-of-2d" },
        "returns": ["man-islam-muqarnas", "archtrans-mashrabiya", "archtrans-ribvault"]
      },
      {
        "question": "Find 1D making 2D on 2D surfaces (textiles, drawings).",
        "filter": { "dimension_mapping": "map-1d-builds-2d-on-2d" },
        "returns": ["man-persian-biomorphic", "nexus-geometry-proofs", "man-andes-khipu"]
      },
      {
        "question": "List deities tied to writing/measurement.",
        "filter": { "mythology.domains": ["writing", "measurement"] },
        "returns": ["my-egypt-thoth", "my-mesopotamia-nabu"]
      }
    ],
    "extensibility": {
      "how_to_add_permutation": [
        "Choose dimension mapping (e.g., 2D on 3D).",
        "Specify geometric elements and operations.",
        "Assign material, technique, culture, and math links.",
        "Describe number-writing-visualization nexus if applicable.",
        "Attach image_refs with source URLs when available."
      ],
      "image_ref_schema": { "source": "string", "url": "string", "license": "string", "notes": "string" }
    }
  }