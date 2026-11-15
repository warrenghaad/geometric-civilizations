#!/usr/bin/env python3
"""
Visualization Mapper - Maps parsed content to visualization requirements with provider selection
Part of the Multi-Provider AI Image Generation System
"""

import json
from typing import Dict, List, Any
from pathlib import Path


class VisualizationMapper:
    """Maps content elements to specific visualizations with optimal provider selection."""

    def __init__(self, provider_settings_path: Path = None):
        """
        Initialize mapper with provider settings.

        Args:
            provider_settings_path: Path to provider_settings.yaml
        """
        self.provider_settings = self._load_provider_settings(provider_settings_path)

    def _load_provider_settings(self, path: Path = None) -> Dict[str, Any]:
        """Load provider settings from YAML file."""
        if path is None:
            path = Path(__file__).parent.parent / 'config' / 'provider_settings.yaml'

        if not path.exists():
            # Return default settings
            return {
                "provider_selection": {
                    "photorealistic_scenes": {"provider": "openai"},
                    "educational_diagrams": {"provider": "gemini"},
                    "character_art": {"provider": "openai"},
                    "technical_illustrations": {"provider": "gemini"},
                    "sacred_geometry": {"provider": "gemini"},
                    "cultural_backgrounds": {"provider": "openai"}
                }
            }

        # Load YAML settings
        import yaml
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def map_element_to_visualizations(self, element: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Map a single element to its required visualizations.

        Args:
            element: Parsed element data

        Returns:
            List of visualization specifications
        """
        visualizations = []
        element_name = element["name"].lower().replace(' ', '_')

        # 1. Basic diagram (SVG - simple geometry)
        visualizations.append({
            "id": f"{element_name}_basic",
            "type": "basic_diagram",
            "element": element_name,
            "format": "svg",
            "provider": "programmatic",  # Generated via code, not AI
            "reason": "Simple geometric shape, scalable vector",
            "priority": 1,
            "estimated_cost": 0.0
        })

        # 2. Physics diagram (if physics content exists)
        if element.get("physics"):
            visualizations.append({
                "id": f"{element_name}_physics",
                "type": "physics_diagram",
                "element": element_name,
                "format": "png",
                "provider": "gemini",
                "reason": "Technical illustration with force vectors",
                "grade_levels": ["6-8"],
                "content": element["physics"],
                "priority": 2,
                "estimated_cost": 0.02
            })

        # 3. Cultural examples (artifact composites)
        for civ in element.get("civilizations", []):
            visualizations.append({
                "id": f"{element_name}_{civ.lower()}_artifact",
                "type": "cultural_artifact",
                "element": element_name,
                "civilization": civ,
                "format": "png",
                "provider": "openai",  # Photorealistic scene
                "reason": "Photorealistic cultural artifact rendering",
                "priority": 3,
                "estimated_cost": 0.04,
                "workflow": [
                    {"step": 1, "provider": "openai", "action": "generate artifact scene"},
                    {"step": 2, "provider": "vision", "action": "analyze geometry"},
                    {"step": 3, "provider": "gemini", "action": "generate overlay"},
                    {"step": 4, "provider": "cloud_vision", "action": "composite and optimize"}
                ]
            })

        # 4. Interactive demos (if applications exist)
        if element.get("applications"):
            for app in element["applications"][:2]:  # Limit to 2 demos
                app_clean = app.lower().replace(' ', '_').replace(',', '')
                visualizations.append({
                    "id": f"{element_name}_{app_clean}_demo",
                    "type": "interactive_demo",
                    "element": element_name,
                    "application": app,
                    "format": "html",
                    "provider": "programmatic",  # Canvas/JavaScript
                    "reason": "Interactive educational demonstration",
                    "grade_levels": ["K-1", "2-3"],
                    "priority": 4,
                    "estimated_cost": 0.0
                })

        # 5. Grade-specific versions
        for grade, activity in element.get("grade_levels", {}).items():
            visualizations.append({
                "id": f"{element_name}_grade_{grade.replace('-', '_')}",
                "type": "grade_adapted",
                "element": element_name,
                "grade_level": grade,
                "format": "png",
                "provider": "gemini",
                "reason": f"Grade-adapted educational diagram for {grade}",
                "content": activity,
                "priority": 5,
                "estimated_cost": 0.02
            })

        return visualizations

    def map_all_elements(self, parsed_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map all parsed elements to visualizations.

        Args:
            parsed_data: Output from ContentParser

        Returns:
            Complete visualization specification
        """
        all_visualizations = []

        for element in parsed_data.get("shapes", []):
            vizs = self.map_element_to_visualizations(element)
            all_visualizations.extend(vizs)

        # Calculate totals
        total_cost = sum(v.get("estimated_cost", 0) for v in all_visualizations)
        provider_breakdown = self._calculate_provider_breakdown(all_visualizations)

        return {
            "visualizations": all_visualizations,
            "summary": {
                "total_visualizations": len(all_visualizations),
                "estimated_cost": total_cost,
                "provider_breakdown": provider_breakdown,
                "format_breakdown": self._calculate_format_breakdown(all_visualizations)
            },
            "metadata": {
                "source": parsed_data.get("metadata", {}).get("source"),
                "total_elements": len(parsed_data.get("shapes", []))
            }
        }

    def _calculate_provider_breakdown(self, visualizations: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate breakdown by provider."""
        breakdown = {}

        for viz in visualizations:
            provider = viz.get("provider", "unknown")
            if provider not in breakdown:
                breakdown[provider] = {
                    "count": 0,
                    "estimated_cost": 0.0
                }
            breakdown[provider]["count"] += 1
            breakdown[provider]["estimated_cost"] += viz.get("estimated_cost", 0)

        return breakdown

    def _calculate_format_breakdown(self, visualizations: List[Dict[str, Any]]) -> Dict[str, int]:
        """Calculate breakdown by format."""
        breakdown = {}

        for viz in visualizations:
            fmt = viz.get("format", "unknown")
            breakdown[fmt] = breakdown.get(fmt, 0) + 1

        return breakdown

    def export_json(self, data: Dict[str, Any], output_path: Path):
        """Export visualization map to JSON."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


def main():
    """Command-line interface for visualization mapper."""
    import argparse

    parser = argparse.ArgumentParser(description='Map content to visualizations')
    parser.add_argument('input', type=Path, help='Input JSON file from content_parser')
    parser.add_argument('--output', type=Path, help='Output JSON file')
    parser.add_argument('--dry-run', action='store_true', help='Show cost estimate only')

    args = parser.parse_args()

    # Load parsed content
    with open(args.input, 'r') as f:
        parsed_data = json.load(f)

    # Map to visualizations
    mapper = VisualizationMapper()
    viz_data = mapper.map_all_elements(parsed_data)

    # Show summary
    summary = viz_data["summary"]
    print(f"\n=== Visualization Mapping Summary ===")
    print(f"Total Visualizations: {summary['total_visualizations']}")
    print(f"Estimated Total Cost: ${summary['estimated_cost']:.2f}")

    print(f"\nProvider Breakdown:")
    for provider, stats in summary["provider_breakdown"].items():
        print(f"  {provider}: {stats['count']} images × ${stats['estimated_cost']:.2f}")

    print(f"\nFormat Breakdown:")
    for fmt, count in summary["format_breakdown"].items():
        print(f"  {fmt}: {count} files")

    if args.dry_run:
        print("\n[DRY RUN MODE - No images will be generated]")
        return

    # Export
    if args.output:
        mapper.export_json(viz_data, args.output)
        print(f"\nExported to: {args.output}")
    else:
        print("\n" + json.dumps(viz_data, indent=2))


if __name__ == '__main__':
    main()
