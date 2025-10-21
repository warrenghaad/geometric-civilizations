"""
Setup script to create the foundational curriculum framework nodes
Run this once to populate the 3D visualization with the core structure
"""

import json
import os

def create_foundation_structure():
    """Create the core curriculum framework nodes"""
    
    # Initialize data structure
    graph_data = {
        'nodes': {},
        'edges': []
    }
    
    # 1. Create 9 Cognitive Domain Nodes (Type: Database)
    cognitive_domains = [
        ("Attention", "Selecting and maintaining focus on relevant information, shifting focus when needed, and dividing attention across tasks."),
        ("Memory", "Encoding, storing, and retrieving information; includes short-term/working memory, episodic memory (events), semantic memory (facts), and procedural memory (skills)."),
        ("Executive Functions", "Higher-order control processes such as planning, problem solving, cognitive flexibility, inhibition (self-control), reasoning, and decision-making."),
        ("Language", "Understanding and producing spoken and written language; includes vocabulary, grammar, syntax, pragmatics, and discourse."),
        ("Learning", "Acquiring new knowledge or skills through experience, practice, and feedback; includes associative learning and skill acquisition."),
        ("Visuospatial Processing", "Understanding spatial relationships, mental rotation, navigation, and constructional abilities."),
        ("Social Cognition", "Recognizing and interpreting others' emotions, intentions, and perspectives; theory of mind and empathy."),
        ("Emotional Processing", "Identifying, regulating, and integrating emotions; how emotion influences attention, memory, and decisions."),
        ("Metacognition", "Awareness and regulation of one's own thinking; self-monitoring, strategy selection, and reflection.")
    ]
    
    for name, description in cognitive_domains:
        graph_data['nodes'][name] = {
            'type': 'Database',
            'description': description,
            'images': []
        }
    
    # 2. Create 6 Content Area Nodes (Type: Course)
    content_areas = [
        ("Math/Geometry", "Mathematical thinking, geometric patterns, spatial reasoning, and formal proof structures."),
        ("Art/Architecture", "Visual design, cultural aesthetics, pattern creation, and architectural elements across civilizations."),
        ("Inventions/Innovation", "Problem-solving through design, technological evolution, and creative adaptation of ideas."),
        ("Myths/Culture", "Storytelling traditions, cultural identity, narrative structures, and symbolic meaning-making."),
        ("Power/Society", "Social structures, governance systems, community organization, and ethical decision-making."),
        ("SEL Skills", "Social-emotional learning: self-awareness, self-regulation, relationship skills, and responsible choices.")
    ]
    
    for name, description in content_areas:
        graph_data['nodes'][name] = {
            'type': 'Course',
            'description': description,
            'images': []
        }
    
    # 3. Create the 9×6 Template Schema Node
    graph_data['nodes']['9x6 Curriculum Template'] = {
        'type': 'Schema',
        'description': 'The core 9×6 matrix structure: 9 Cognitive Domains × 6 Content Areas = 54-cell framework that applies across all 982 lessons. Each lesson activates specific cognitive domains while addressing content areas.',
        'images': []
    }
    
    # 4. Create Tesseract Dimensional Progression Nodes (Type: Concept)
    tesseract_levels = [
        ("D0: Bits (Facts)", "Dimension 0/1: Individual facts and concepts (e.g., '5', 'circle', 'hero'). Foundation-level discrete information."),
        ("D1: Bytes (Operations)", "Dimension 1: Operations and transformations (e.g., 'multiply by 5', 'rotate shape', 'hero's journey'). Single-strand processes."),
        ("D2: Networks (Interactions)", "Dimension 2: Interactions across strands (e.g., '5 across arithmetic operations', 'patterns across cultures'). How elements combine and relate."),
        ("D3: Algebra (Emergent)", "Dimension 3: Emergent unknowns from network interactions (e.g., algebraic thinking, symbolic representation). The third dimension creates abstraction."),
        ("D4: Calculus (Meta)", "Dimension 4: Meta-level 'what if' thinking (e.g., Newton finding algebra incomplete, inventing calculus). Questioning and transcending existing frameworks.")
    ]
    
    for name, description in tesseract_levels:
        graph_data['nodes'][name] = {
            'type': 'Concept',
            'description': description,
            'images': []
        }
    
    # 5. Create 6 Vertical Thread Nodes (Type: Module)
    vertical_threads = [
        ("Pattern Recognition → Proof", "K-2: identify & describe patterns | 3-5: classify & transform | 6-8: generalize & justify with formal proof"),
        ("Myth Structure → Analytical Writing", "Oral retell → compare motifs → structural analysis → thematic synthesis and critical writing"),
        ("Symbol → Model", "Draw → label → encode → abstract into variable/formula representation"),
        ("Global Motifs & Equity", "Hear diverse stories → respect perspectives → connect across cultures → critique representation & bias"),
        ("Creative Remix → Innovation", "Combine shapes + myths → adapt culturally responsibly → prototype explanatory artifacts"),
        ("Mindful Metacognition", "Name feelings → regulate focus → select strategies → reflect & refine thinking processes")
    ]
    
    for name, description in vertical_threads:
        graph_data['nodes'][name] = {
            'type': 'Module',
            'description': description,
            'images': []
        }
    
    # 6. Create Common Core Standards Foundation Node
    graph_data['nodes']['Common Core Standards'] = {
        'type': 'Schema',
        'description': 'Foundation educational standards framework covering Math and ELA. The curriculum builds on and extends Common Core with spatial complexity, arts integration, and SEL layers.',
        'images': []
    }
    
    # Create initial relationships
    # Connect 9x6 Template to Cognitive Domains
    for name, _ in cognitive_domains:
        graph_data['edges'].append([name, '9x6 Curriculum Template', 'domain-of'])
    
    # Connect 9x6 Template to Content Areas
    for name, _ in content_areas:
        graph_data['edges'].append(['9x6 Curriculum Template', name, 'applies-to'])
    
    # Connect Tesseract levels in sequence
    tesseract_names = [name for name, _ in tesseract_levels]
    for i in range(len(tesseract_names) - 1):
        graph_data['edges'].append([tesseract_names[i], tesseract_names[i+1], 'progresses-to'])
    
    # Connect Vertical Threads to Content Areas (they span across all)
    for thread_name, _ in vertical_threads:
        for content_name, _ in content_areas:
            graph_data['edges'].append([thread_name, content_name, 'develops-across'])
    
    # Connect Common Core to the Template
    graph_data['edges'].append(['Common Core Standards', '9x6 Curriculum Template', 'foundational-for'])
    
    # Save to data file
    os.makedirs('data', exist_ok=True)
    
    with open('data/graph_data.json', 'w') as f:
        json.dump(graph_data, f, indent=2)
    
    print("✅ Foundation structure created successfully!")
    print(f"\nCreated {len(graph_data['nodes'])} nodes:")
    print(f"  - 9 Cognitive Domains (Database type)")
    print(f"  - 6 Content Areas (Course type)")
    print(f"  - 6 Vertical Threads (Module type)")
    print(f"  - 5 Tesseract Levels (Concept type)")
    print(f"  - 2 Schema nodes (Template + Standards)")
    print(f"\nCreated {len(graph_data['edges'])} relationships")
    print(f"\n🎯 Open the Streamlit app to visualize the framework!")

if __name__ == "__main__":
    create_foundation_structure()
