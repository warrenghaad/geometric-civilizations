#!/usr/bin/env python3
"""
Content Parser - Parses structured content documents into visualization requirements
Part of the Multi-Provider AI Image Generation System
"""

import re
import json
from typing import Dict, List, Any
from pathlib import Path


class ContentParser:
    """Parses structured markdown content documents into structured data."""

    def __init__(self):
        self.grade_levels = ['K-1', '2-3', '4-5', '6-8']
        self.civilizations = ['Egypt', 'Mesopotamia', 'Greece', 'India', 'China', 'Islamic', 'Mesoamerica']

    def parse_markdown(self, content: str) -> Dict[str, Any]:
        """
        Parse markdown content into structured data.

        Args:
            content: Markdown content string

        Returns:
            Dictionary with parsed geometric elements
        """
        result = {
            "shapes": [],
            "patterns": [],
            "cultural_motifs": [],
            "metadata": {
                "source": "markdown",
                "total_elements": 0
            }
        }

        # Split into sections by ### headers
        sections = re.split(r'\n###\s+', content)

        for section in sections[1:]:  # Skip first empty section
            element = self._parse_element_section(section)
            if element:
                result["shapes"].append(element)

        result["metadata"]["total_elements"] = len(result["shapes"])
        return result

    def _parse_element_section(self, section: str) -> Dict[str, Any]:
        """Parse a single element section (e.g., Triangle, Circle)."""
        lines = section.strip().split('\n')
        if not lines:
            return None

        # First line is the element name
        name = lines[0].strip()

        element = {
            "name": name,
            "physics": "",
            "applications": [],
            "grade_levels": {},
            "civilizations": [],
            "math_standards": [],
            "visualizations": []
        }

        # Parse content
        current_field = None
        for line in lines[1:]:
            line = line.strip()

            # Physics/Engineering
            if line.startswith('**Physics/Engineering'):
                match = re.search(r'\*\*Physics/Engineering[^\*]*\*\*:\s*(.+)', line)
                if match:
                    element["physics"] = match.group(1)

            # Problem-Solving Application
            elif line.startswith('**Problem-Solving'):
                match = re.search(r'\*\*Problem-Solving[^\*]*\*\*:\s*(.+)', line)
                if match:
                    apps = match.group(1).split(',')
                    element["applications"] = [app.strip() for app in apps]

            # Grade levels
            elif line.startswith('**Grade K-1'):
                match = re.search(r'\*\*Grade K-1\*\*:\s*(.+)', line)
                if match:
                    element["grade_levels"]["K-1"] = match.group(1)

            elif line.startswith('**Grade 2-3'):
                match = re.search(r'\*\*Grade 2-3\*\*:\s*(.+)', line)
                if match:
                    element["grade_levels"]["2-3"] = match.group(1)

            elif line.startswith('**Grade 4-5'):
                match = re.search(r'\*\*Grade 4-5\*\*:\s*(.+)', line)
                if match:
                    element["grade_levels"]["4-5"] = match.group(1)

            elif line.startswith('**Grade 6-8'):
                match = re.search(r'\*\*Grade 6-8\*\*:\s*(.+)', line)
                if match:
                    element["grade_levels"]["6-8"] = match.group(1)
                    # Extract math standards
                    std_match = re.search(r'\((AZ[^\)]+)\)', match.group(1))
                    if std_match:
                        element["math_standards"].append(std_match.group(1))

            # Cultural examples
            elif line.startswith('**Cultural'):
                match = re.search(r'\*\*Cultural[^\*]*\*\*:\s*(.+)', line)
                if match:
                    civs = match.group(1).split(',')
                    for civ in civs:
                        # Extract civilization name from patterns like "Egypt (pyramids)"
                        civ_match = re.search(r'([A-Za-z]+)', civ)
                        if civ_match:
                            element["civilizations"].append(civ_match.group(1))

        return element

    def parse_file(self, filepath: Path) -> Dict[str, Any]:
        """Parse a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return self.parse_markdown(content)

    def export_json(self, data: Dict[str, Any], output_path: Path):
        """Export parsed data to JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def get_visualization_summary(self, data: Dict[str, Any]) -> Dict[str, int]:
        """Get summary of how many visualizations will be needed."""
        summary = {
            "total_elements": len(data["shapes"]),
            "basic_diagrams": len(data["shapes"]),
            "physics_diagrams": 0,
            "cultural_examples": 0,
            "interactive_demos": 0,
            "grade_versions": 0
        }

        for element in data["shapes"]:
            # Physics diagram if physics description exists
            if element["physics"]:
                summary["physics_diagrams"] += 1

            # Cultural examples (estimate 2 per civilization mentioned)
            summary["cultural_examples"] += len(element["civilizations"]) * 2

            # Interactive demos if applications exist
            if element["applications"]:
                summary["interactive_demos"] += 1

            # Grade-specific versions (4 grades per element)
            summary["grade_versions"] += len(element["grade_levels"]) * 2  # simplified + standard

        summary["estimated_total"] = (
            summary["basic_diagrams"] +
            summary["physics_diagrams"] +
            summary["cultural_examples"] +
            summary["interactive_demos"] +
            summary["grade_versions"]
        )

        return summary


def main():
    """Command-line interface for content parser."""
    import argparse

    parser = argparse.ArgumentParser(description='Parse structured content documents')
    parser.add_argument('input', type=Path, help='Input markdown file')
    parser.add_argument('--output', type=Path, help='Output JSON file')
    parser.add_argument('--summary', action='store_true', help='Show visualization summary')

    args = parser.parse_args()

    # Parse content
    content_parser = ContentParser()
    data = content_parser.parse_file(args.input)

    # Show summary
    if args.summary:
        summary = content_parser.get_visualization_summary(data)
        print(f"\n=== Visualization Summary ===")
        print(f"Total Elements: {summary['total_elements']}")
        print(f"Basic Diagrams: {summary['basic_diagrams']}")
        print(f"Physics Diagrams: {summary['physics_diagrams']}")
        print(f"Cultural Examples: {summary['cultural_examples']}")
        print(f"Interactive Demos: {summary['interactive_demos']}")
        print(f"Grade Versions: {summary['grade_versions']}")
        print(f"Estimated Total Images: {summary['estimated_total']}")

    # Export to JSON
    if args.output:
        content_parser.export_json(data, args.output)
        print(f"\nExported to: {args.output}")
    else:
        print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
