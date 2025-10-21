"""
Add the Standards Calendar Layer - 108 Mythic Pattern Geometry Objectives
This creates the time-based curriculum timeline that forms Layer 1 of the 2D foundation
"""

import json
import os

def add_calendar_standards_layer():
    """Add the 108 learning objectives as calendar/timeline nodes"""
    
    # Load existing graph data
    with open('data/graph_data.json', 'r') as f:
        graph_data = json.load(f)
    
    # Define the 108 objectives organized by grade
    objectives = {
        'Kindergarten': [
            ('K.O1', 'Spot repeating shape patterns in story cloth', 'RL.K.7 | MP7 | Art Pattern'),
            ('K.O2', 'Retell simple myth with beginning, middle, end', 'RL.K.2 | SL.K.4'),
            ('K.O3', 'Name circle, triangle, square in objects', 'K.G.A.2 | L.K.5'),
            ('K.O4', 'Draw shape pattern to show hero\'s path', 'RL.K.3 | K.G.A.1'),
            ('K.O5', 'Clap syllable rhythms from myth name list', 'RF.K.2 | Music Rhythm'),
            ('K.O6', 'Sort story tokens by shape or color rule', 'K.MD.B.3 | L.K.1'),
            ('K.O7', 'Listen and name feeling a character has', 'RL.K.4 | SEL Awareness'),
            ('K.O8', 'Build shape hero using 2 shapes together', 'K.G.B.6 | Creativity'),
            ('K.O9', 'Notice symmetry in mask picture', 'K.G.A | Art Symmetry'),
            ('K.O10', 'Use "because" to tell why hero changes', 'RL.K.3 | SL.K.6'),
            ('K.O11', 'Stay calm with breathing bubble exercise', 'SEL Regulation'),
            ('K.O12', 'Choose story and say one pattern in it', 'RL.K.10 | Choice Motivation'),
        ],
        'Grade 1': [
            ('1.O1', 'Extend pattern seen in myth border', '1.OA | RL.1.7'),
            ('1.O2', 'Tell how two trickster tales are alike/different', 'RL.1.9'),
            ('1.O3', 'Build composite shape from 2-3 shapes', '1.G.A.2'),
            ('1.O4', 'Label character\'s problem and solution', 'RL.1.2'),
            ('1.O5', 'Write 3-sentence mini-myth with pattern words', 'W.1.3'),
            ('1.O6', 'Identify symmetry by folding paper art', '1.G | Art Fold Symmetry'),
            ('1.O7', 'Describe setting using at least 2 senses', 'RL.1.7 | L.1.1'),
            ('1.O8', 'Use calm counting when feeling stuck', 'SEL Strategy'),
            ('1.O9', 'Classify shapes by sides or corners', '1.G.A.1'),
            ('1.O10', 'Present drawing and speak clearly', 'SL.1.4'),
            ('1.O11', 'Choose respectful word to describe culture', 'L.1.5 | SEL Respect'),
            ('1.O12', 'Find repeating sound pattern (alliteration)', 'RL.1.4'),
        ],
        'Grade 2': [
            ('2.O1', 'Map events in order with shape timeline', 'RL.2.5'),
            ('2.O2', 'Partition rectangle into equal squares', '2.G.A.2'),
            ('2.O3', 'Compare myth openings from 2 cultures', 'RL.2.9'),
            ('2.O4', 'Write topic sentence about hero\'s choice', 'W.2.2'),
            ('2.O5', 'Explain why pattern rule works (AAB vs ABB)', 'MP3 | RL.2.1'),
            ('2.O6', 'Find lines of symmetry in simple figures', '2.G | Visual Arts'),
            ('2.O7', 'Use calm script when frustrated', 'SEL Regulation'),
            ('2.O8', 'Ask clarifying presentation question', 'SL.2.3'),
            ('2.O9', 'Measure using informal units for myth artifact', '2.MD.A'),
            ('2.O10', 'Revise sentence to add vivid verb', 'W.2.5 | L.2.1'),
            ('2.O11', 'Create mirrored pattern border for retelling', 'Art | 2.G'),
            ('2.O12', 'Paraphrase helper character\'s role', 'RL.2.7'),
        ],
        'Grade 3': [
            ('3.O1', 'Classify quadrilaterals by shared attributes', '3.G.A | MP7'),
            ('3.O2', 'Extract moral/theme from myth with 2 details', 'RL.3.2'),
            ('3.O3', 'Describe transformation (flip/slide/turn)', '3.G | W.3.2'),
            ('3.O4', 'Compare two myth heroes\' responses to conflict', 'RL.3.3'),
            ('3.O5', 'Write myth remix adding geometry clue', 'W.3.3 | 3.G.A'),
            ('3.O6', 'Plan breathing + stretch routine before presenting', 'SEL'),
            ('3.O7', 'Explain pattern using numbers (3,6,9)', '3.OA.D'),
            ('3.O8', 'Cite text sentences when answering', 'RL.3.1'),
            ('3.O9', 'Create tessellation-based shield motif', 'Art | 3.G'),
            ('3.O10', 'Distinguish literal vs nonliteral language', 'L.3.5'),
            ('3.O11', 'Respectfully identify cultural origin of motif', 'RL.3.9'),
            ('3.O12', 'Summarize chapter in 3 bullet points', 'RL.3.2'),
        ],
        'Grade 4': [
            ('4.O1', 'Measure and classify angles in artifact design', '4.G.A.1'),
            ('4.O2', 'Analyze myth structure (exposition → resolution)', 'RL.4.5'),
            ('4.O3', 'Write compare/contrast of two flood myths', 'RL.4.9 | W.4.2'),
            ('4.O4', 'Decompose composite area in temple floor plan', '4.MD.A | MP4'),
            ('4.O5', 'Support inference with two textual details', 'RL.4.1'),
            ('4.O6', 'Construct symmetry-based logo with rotation', '4.G | Art'),
            ('4.O7', 'Use mindful labeling (emotion + need) in groups', 'SEL'),
            ('4.O8', 'Paraphrase primary vs secondary source', 'RI.4.6'),
            ('4.O9', 'Revise for sentence variety (combine/expand)', 'W.4.5'),
            ('4.O10', 'Justify classification choice in hierarchy chart', '4.G.A | MP3'),
            ('4.O11', 'Present storyboard with geometry annotations', 'SL.4.4'),
            ('4.O12', 'Evaluate respectful cultural representation', 'RL.4.9 | SEL'),
        ],
        'Grade 5': [
            ('5.O1', 'Compute area of irregular shapes via decomposition', '5.MD.C'),
            ('5.O2', 'Analyze narrator point of view difference', 'RL.5.6'),
            ('5.O3', 'Construct tessellated border explaining angle sums', '5.G | MP7'),
            ('5.O4', 'Write explanatory piece linking myth to phenomenon', 'W.5.2'),
            ('5.O5', 'Summarize multi-chapter myth concisely', 'RL.5.2'),
            ('5.O6', 'Evaluate credibility of informational passages', 'RI.5.8'),
            ('5.O7', 'Model coordinate plane points to map journey', '5.G.A'),
            ('5.O8', 'Use mindfulness journaling to reflect on focus', 'SEL'),
            ('5.O9', 'Identify figurative language (simile, personification)', 'L.5.5'),
            ('5.O10', 'Assemble research mini-bibliography (3 sources)', 'W.5.8'),
            ('5.O11', 'Argue thematic interpretation with textual evidence', 'W.5.1 | SL.5.4'),
            ('5.O12', 'Critique cultural remix for accuracy/stereotypes', 'RI.5.6 | SEL'),
        ],
        'Grade 6': [
            ('6.O1', 'Use ratio reasoning to scale pattern border', '6.RP.A'),
            ('6.O2', 'Analyze how myth theme develops across scenes', 'RL.6.2'),
            ('6.O3', 'Write concise objective summary (no opinion)', 'RL.6.2'),
            ('6.O4', 'Describe transformation using coordinate notation', '6.G.A'),
            ('6.O5', 'Compare primary vs secondary myth commentary', 'RH.6-8.1'),
            ('6.O6', 'Build ethical remix retaining core motif', 'W.6.3 | SEL'),
            ('6.O7', 'Explain proportional change in symbol scaling', '6.RP.A | MP3'),
            ('6.O8', 'Annotate figurative & connotative meanings', 'RL.6.4'),
            ('6.O9', 'Plan 3-minute explanatory talk with visuals', 'SL.6.4'),
            ('6.O10', 'Use mindfulness (breath + reframe) before revision', 'SEL'),
            ('6.O11', 'Identify bias or omission in retelling source', 'RI.6.6'),
            ('6.O12', 'Justify transformation sequence for congruence', '6.G | MP6'),
        ],
        'Grade 7': [
            ('7.O1', 'Apply similarity & scale factor to redesign motif', '7.G.A'),
            ('7.O2', 'Trace thematic evolution to craft synthesis claim', 'RL.7.2'),
            ('7.O3', 'Analyze how perspective shapes reliability', 'RL.7.6'),
            ('7.O4', 'Integrate quantitative data into explanatory writing', 'W.7.2 | MP4'),
            ('7.O5', 'Construct argument evaluating adaptation authenticity', 'W.7.1'),
            ('7.O6', 'Model geometric construction of decorative pattern', '7.G | MP5'),
            ('7.O7', 'Explain proportional reasoning in map scale', '7.RP.A'),
            ('7.O8', 'Evaluate word choice\'s tone effect', 'RL.7.4'),
            ('7.O9', 'Facilitate collaborative dialogue with stems', 'SL.7.1'),
            ('7.O10', 'Use layered mindfulness (breath + somatic + focus)', 'SEL'),
            ('7.O11', 'Categorize motif diffusion using research logs', 'RI.7.1'),
            ('7.O12', 'Justify similarity claim with ratio evidence', '7.G | MP3'),
        ],
        'Grade 8': [
            ('8.O1', 'Prove angle relationships in transformations', '8.G.A | MP3'),
            ('8.O2', 'Analyze how contrasting myths shape themes', 'RL.8.9'),
            ('8.O3', 'Craft argument integrating symbolic geometry model', 'W.8.1'),
            ('8.O4', 'Evaluate sources for credibility, bias, corroboration', 'RI.8.8'),
            ('8.O5', 'Model dilation on coordinate plane with scale reasoning', '8.G.A'),
            ('8.O6', 'Adapt myth to explain contemporary issue', 'W.8.2 | SEL'),
            ('8.O7', 'Create layered symbolic system mapping arc to geometry', '8.G | RL.8.5'),
            ('8.O8', 'Analyze figurative density & tone shifts', 'RL.8.4'),
            ('8.O9', 'Guide peer feedback using criteria', 'SL.8.1'),
            ('8.O10', 'Use metacognitive journaling tracking strategies', 'SEL'),
            ('8.O11', 'Produce multimodal presentation synthesis', 'SL.8.5'),
            ('8.O12', 'Construct proof-style justification for pattern', '8.EE | MP3'),
        ],
    }
    
    # Add each objective as a Table node (representing curriculum lessons/activities)
    for grade, objectives_list in objectives.items():
        for obj_id, description, standards in objectives_list:
            node_name = f"{obj_id}: {description[:40]}..." if len(description) > 40 else f"{obj_id}: {description}"
            
            graph_data['nodes'][node_name] = {
                'type': 'Table',
                'description': f"Grade: {grade}\n\nStudent Objective: I can {description}\n\nStandards Alignment: {standards}\n\nThis objective is part of the Mythic Pattern Geometry integrated curriculum.",
                'images': []
            }
            
            # Connect to Common Core Standards schema
            graph_data['edges'].append([node_name, 'Common Core Standards', 'aligned-to'])
            
            # Connect to the 9x6 Template
            graph_data['edges'].append([node_name, '9x6 Curriculum Template', 'implements'])
    
    # Save updated graph data
    with open('data/graph_data.json', 'w') as f:
        json.dump(graph_data, f, indent=2)
    
    print("✅ Calendar/Standards Layer added successfully!")
    print(f"\nAdded 108 learning objective nodes (Table type):")
    print(f"  - Kindergarten: 12 objectives")
    print(f"  - Grades 1-8: 12 objectives each")
    print(f"\nEach objective:")
    print(f"  ✓ Connected to Common Core Standards")
    print(f"  ✓ Connected to 9×6 Curriculum Template")
    print(f"  ✓ Shows grade level, student-facing objective, and standards alignment")
    print(f"\n🎯 Layer 1 (Standards Calendar) is now in place!")
    print(f"💡 Next: Connect these to Cognitive Domains to create Layer 2 interaction")

if __name__ == "__main__":
    add_calendar_standards_layer()
