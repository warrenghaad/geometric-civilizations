#!/usr/bin/env python3
"""
Curriculum Generator - Geometric Civilizations
Generates 54 complete lesson JSON files from curriculum master CSV
"""

import csv
import json
import os
from pathlib import Path
from typing import Dict, List, Any


class CurriculumGenerator:
    def __init__(self, csv_path: str, output_dir: str, design_system_path: str):
        self.csv_path = csv_path
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        with open(design_system_path, 'r') as f:
            self.design_system = json.load(f)

    def load_curriculum_data(self) -> List[Dict[str, str]]:
        """Load curriculum master CSV"""
        with open(self.csv_path, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def get_palette(self, grade: int) -> Dict[str, str]:
        """Get color palette for grade level"""
        grade_key = f"grade{grade}"
        return self.design_system['colorPalettes'].get(grade_key, {})

    def generate_sel(self, lesson_data: Dict[str, str]) -> Dict[str, Any]:
        """Generate SEL section with grade-appropriate prompt"""
        grade = int(lesson_data['Grade'])
        geometric_concept = lesson_data['GeometricConcept']

        # Grade-specific SEL prompts
        prompts = {
            3: f"Draw a shape that shows how you're feeling today. Can you find a {geometric_concept.split()[0].lower()} in your shape?",
            4: f"Create a geometric design that represents something you're proud of. How does {geometric_concept.split()[0]} help tell your story?",
            5: f"Design a symbol using {geometric_concept.split()[0]} to represent a challenge you've overcome. What does the geometry reveal?"
        }

        return {
            "prompt": prompts.get(grade, prompts[3]),
            "duration": 5,
            "materials": ["Paper", "Pencil", "Colored pencils"],
            "reflectionQuestions": [
                "How did your shape choice reflect your feelings?",
                "Did the geometry help you express something you couldn't put into words?"
            ]
        }

    def generate_hook(self, lesson_data: Dict[str, str]) -> Dict[str, Any]:
        """Generate hook section with character and narrative"""
        civilization = lesson_data['Civilization']
        math_concept = lesson_data['MathConcept']

        # Character generation based on civilization
        characters = {
            "Prehistoric": {"name": "Kira the Cave Keeper", "role": "Stone age counter"},
            "Egypt": {"name": "Ahmose the Scribe", "role": "Royal architect"},
            "Mesopotamia": {"name": "Enlil the Seal Maker", "role": "Master craftsperson"},
            "Greece": {"name": "Sophia the Geometer", "role": "Mathematical philosopher"},
            "Rome": {"name": "Marcus the Builder", "role": "Engineering master"},
            "Byzantine": {"name": "Theodora the Mosaic Artist", "role": "Cathedral designer"},
            "Gothic": {"name": "Pierre the Mason", "role": "Cathedral builder"},
            "Islamic": {"name": "Fatima the Tiler", "role": "Pattern master"},
            "China": {"name": "Li Wei the Craftsperson", "role": "Lattice designer"},
            "India": {"name": "Arjun the Mandala Maker", "role": "Sacred geometer"},
            "Aztec": {"name": "Xochitl the Calendar Keeper", "role": "Time tracker"},
            "Mesoamerican": {"name": "Itzamna the Astronomer", "role": "Sky watcher"},
            "Polynesia": {"name": "Koa the Navigator", "role": "Ocean voyager"},
            "Andean": {"name": "Qori the Weaver", "role": "Textile master"},
            "Celtic": {"name": "Brigid the Scribe", "role": "Spiral carver"},
            "West African": {"name": "Amara the Weaver", "role": "Kente master"},
            "Art Nouveau": {"name": "Alphonse the Designer", "role": "Organic architect"},
            "Renaissance": {"name": "Leonardo the Architect", "role": "Universal mind"},
            "Contemporary": {"name": "Zara the Parametric Designer", "role": "Digital architect"}
        }

        char_info = characters.get(civilization, characters["Prehistoric"])

        return {
            "character": {
                "name": char_info["name"],
                "role": char_info["role"],
                "imageUrl": f"assets/characters/{civilization.lower().replace(' ', '-')}-character.png",
                "biography": f"{char_info['name']} uses {lesson_data['GeometricConcept'].split()[0].lower()} to solve problems about {math_concept.lower()}."
            },
            "narrative": f"Follow {char_info['name']} as they discover how {lesson_data['GeometricConcept'].lower()} helps them understand {math_concept.lower()}. Their journey reveals the hidden mathematics in everyday patterns.",
            "duration": 5,
            "visualType": "illustration",
            "questionPrompt": f"How does {lesson_data['GeometricConcept'].split()[0].lower()} help us think about {math_concept.lower()}?"
        }

    def generate_artifacts(self, lesson_data: Dict[str, str]) -> List[Dict[str, Any]]:
        """Generate artifact entries with overlay specifications"""
        artifacts_str = lesson_data['Artifacts']
        artifact_names = [a.strip() for a in artifacts_str.split(',')]

        artifacts = []
        for idx, artifact_name in enumerate(artifact_names, 1):
            artifact = {
                "artifactId": f"artifact-{idx:02d}",
                "title": artifact_name,
                "civilization": lesson_data['Civilization'],
                "period": "TBD - Research needed",
                "imageUrl": f"assets/artifacts/{lesson_data['LessonId']}-artifact-{idx:02d}.jpg",
                "overlays": [
                    {
                        "overlayId": f"overlay-01",
                        "type": "circles",
                        "elements": [
                            {
                                "shape": "circle",
                                "coordinates": {"cx": "50%", "cy": "50%", "r": "25%"},
                                "label": "Primary geometric feature",
                                "style": {}
                            }
                        ],
                        "description": f"Overlay reveals {lesson_data['GeometricConcept'].split()[0].lower()} structure in {artifact_name}"
                    }
                ],
                "metadata": {
                    "source": "TBD",
                    "museum": "TBD",
                    "accessionNumber": "TBD",
                    "license": "CC0 1.0",
                    "url": f"https://example.com/artifact-{idx}"
                },
                "teachingNotes": f"Highlight the {lesson_data['GeometricConcept'].lower()} visible in this artifact."
            }
            artifacts.append(artifact)

        return artifacts

    def generate_lesson(self, lesson_data: Dict[str, str]) -> Dict[str, Any]:
        """Generate complete lesson JSON from CSV row"""
        lesson_id = lesson_data['LessonId']
        grade = int(lesson_data['Grade'])

        lesson = {
            "lessonId": lesson_id,
            "metadata": {
                "grade": grade,
                "weekNumber": int(lesson_data['Week']),
                "lessonNumber": int(lesson_id.split('-')[1]),
                "duration": 50,
                "mathConcept": lesson_data['MathConcept'],
                "geometricConcept": lesson_data['GeometricConcept'],
                "civilization": lesson_data['Civilization'],
                "standards": {
                    "ccss": [],  # To be filled
                    "ncas": []
                },
                "keywords": [
                    lesson_data['MathConcept'].lower(),
                    lesson_data['GeometricConcept'].lower(),
                    lesson_data['Civilization'].lower()
                ]
            },
            "sel": self.generate_sel(lesson_data),
            "hook": self.generate_hook(lesson_data),
            "myth": {
                "title": f"TBD: Myth for {lesson_data['Civilization']}",
                "civilization": lesson_data['Civilization'],
                "summary": "To be researched and written",
                "scenes": [],
                "sources": []
            },
            "artifacts": self.generate_artifacts(lesson_data),
            "mathActivity": {
                "title": f"{lesson_data['MathConcept']} with {lesson_data['GeometricConcept']}",
                "objective": f"Students will apply {lesson_data['MathConcept'].lower()} using {lesson_data['GeometricConcept'].lower()}.",
                "procedure": [
                    "Review prior knowledge",
                    "Introduce geometric model",
                    "Guided practice",
                    "Independent work",
                    "Share and discuss"
                ],
                "duration": 15,
                "materials": ["Paper", "Pencils", "Rulers", "Protractors"]
            },
            "artActivity": {
                "title": lesson_data['ArtisticThinking'],
                "technique": "To be specified",
                "procedure": [
                    "Examine cultural artifacts",
                    "Identify geometric patterns",
                    "Practice technique",
                    "Create original design",
                    "Reflect on process"
                ],
                "duration": 15,
                "materials": ["Art supplies TBD"]
            },
            "geometryActivity": {
                "title": lesson_data['GeometricConcept'],
                "concept": lesson_data['MathThinking'],
                "procedure": [
                    "Define key geometric concepts",
                    "Explore with hands-on tools",
                    "Make connections to artifacts",
                    "Apply to new contexts"
                ],
                "duration": 10,
                "materials": ["Geometric tools TBD"],
                "vocabulary": []
            },
            "bridge": {
                "title": f"Connecting {lesson_data['MathConcept']} to {lesson_data['GeometricConcept']}",
                "mathToArt": f"Math concept {lesson_data['MathConcept'].lower()} illuminates artistic thinking in {lesson_data['ArtisticThinking'].lower()}.",
                "artToGeometry": f"Artistic expression reveals geometric structure: {lesson_data['GeometricConcept'].lower()}.",
                "synthesis": f"{lesson_data['MathThinking']} and {lesson_data['ArtisticThinking'].lower()} are two views of the same cognitive tool.",
                "visualDiagram": f"assets/diagrams/{lesson_id}-bridge.svg"
            },
            "exit": {
                "prompt": f"How does {lesson_data['GeometricConcept'].split()[0].lower()} help you think about {lesson_data['MathConcept'].lower()}?",
                "format": "verbal",
                "expectedResponses": [
                    "Sample response 1",
                    "Sample response 2"
                ],
                "duration": 5
            },
            "assessments": {
                "formative": [
                    {"type": "observation", "criteria": "Student engagement with geometric concepts"}
                ],
                "summative": {
                    "type": "portfolio",
                    "rubricUrl": f"assets/rubrics/{lesson_id}-rubric.pdf"
                }
            },
            "extensions": {
                "homeConnections": [],
                "literatureLinks": [],
                "digitalTools": []
            },
            "teacherNotes": {
                "preparation": ["Review lesson materials", "Prepare artifacts", "Set up workstations"],
                "commonMisconceptions": [],
                "timingTips": [],
                "culturalNotes": f"Respectfully present {lesson_data['Civilization']} cultural context."
            }
        }

        return lesson

    def generate_all_lessons(self):
        """Generate all 54 lessons from CSV"""
        curriculum_data = self.load_curriculum_data()

        for lesson_data in curriculum_data:
            lesson = self.generate_lesson(lesson_data)
            lesson_id = lesson_data['LessonId']

            output_path = self.output_dir / f"{lesson_id}.json"
            with open(output_path, 'w') as f:
                json.dump(lesson, f, indent=2)

            print(f"✓ Generated {lesson_id}")

        print(f"\n✓ Successfully generated {len(curriculum_data)} lessons")
        print(f"✓ Output directory: {self.output_dir}")


def main():
    root_dir = Path(__file__).parent.parent
    csv_path = root_dir / "curriculum_master.csv"
    output_dir = root_dir / "lessons"
    design_system_path = root_dir / "schemas" / "design_system.json"

    generator = CurriculumGenerator(
        csv_path=str(csv_path),
        output_dir=str(output_dir),
        design_system_path=str(design_system_path)
    )

    generator.generate_all_lessons()


if __name__ == "__main__":
    main()
