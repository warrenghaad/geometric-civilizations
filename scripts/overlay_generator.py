#!/usr/bin/env python3
"""
Artifact Overlay Generator - Geometric Civilizations
Creates SVG geometric overlays for artifact images
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass


@dataclass
class OverlayElement:
    """Single geometric element in an overlay"""
    shape: str
    coordinates: Dict[str, Any]
    label: str = ""
    style: Dict[str, str] = None


class OverlayGenerator:
    def __init__(self, design_system_path: str):
        with open(design_system_path, 'r') as f:
            self.design_system = json.load(f)

        self.overlay_styles = self.design_system['overlayStyles']
        self.default_width = 1920
        self.default_height = 1080

    def create_svg_wrapper(self, width: int = None, height: int = None) -> str:
        """Create SVG wrapper with viewBox"""
        w = width or self.default_width
        h = height or self.default_height

        return f'''<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {w} {h}"
     width="{w}"
     height="{h}"
     style="position: absolute; top: 0; left: 0; pointer-events: none;">
'''

    def convert_percent_to_pixels(self, value: str, dimension: int) -> float:
        """Convert percentage string to pixel value"""
        if isinstance(value, str) and '%' in value:
            percent = float(value.replace('%', ''))
            return (percent / 100.0) * dimension
        return float(value)

    def create_circle(self, element: Dict, width: int, height: int) -> str:
        """Create SVG circle element"""
        coords = element['coordinates']
        cx = self.convert_percent_to_pixels(coords.get('cx', '50%'), width)
        cy = self.convert_percent_to_pixels(coords.get('cy', '50%'), height)
        r = self.convert_percent_to_pixels(coords.get('r', '10%'), min(width, height))

        style = element.get('style', {})
        default_style = self.overlay_styles['geometric']['circles']

        stroke = style.get('stroke', default_style['stroke'])
        stroke_width = style.get('strokeWidth', default_style['strokeWidth'])
        fill = style.get('fill', default_style['fill'])
        opacity = style.get('opacity', default_style['opacity'])

        svg = f'''  <circle cx="{cx}" cy="{cy}" r="{r}"
          stroke="{stroke}"
          stroke-width="{stroke_width}"
          fill="{fill}"
          opacity="{opacity}"/>
'''

        # Add label if present
        if element.get('label'):
            label_x = cx + r + 10
            label_y = cy
            svg += self.create_label(element['label'], label_x, label_y)

        return svg

    def create_line(self, element: Dict, width: int, height: int) -> str:
        """Create SVG line element"""
        coords = element['coordinates']
        x1 = self.convert_percent_to_pixels(coords.get('x1', '0%'), width)
        y1 = self.convert_percent_to_pixels(coords.get('y1', '0%'), height)
        x2 = self.convert_percent_to_pixels(coords.get('x2', '100%'), width)
        y2 = self.convert_percent_to_pixels(coords.get('y2', '100%'), height)

        style = element.get('style', {})
        default_style = self.overlay_styles['geometric']['lines']

        stroke = style.get('stroke', default_style['stroke'])
        stroke_width = style.get('strokeWidth', default_style['strokeWidth'])
        opacity = style.get('opacity', default_style['opacity'])

        svg = f'''  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
          stroke="{stroke}"
          stroke-width="{stroke_width}"
          opacity="{opacity}"/>
'''

        # Add label if present
        if element.get('label'):
            label_x = (x1 + x2) / 2
            label_y = (y1 + y2) / 2
            svg += self.create_label(element['label'], label_x, label_y)

        return svg

    def create_rectangle(self, element: Dict, width: int, height: int) -> str:
        """Create SVG rectangle element"""
        coords = element['coordinates']
        x = self.convert_percent_to_pixels(coords.get('x', '10%'), width)
        y = self.convert_percent_to_pixels(coords.get('y', '10%'), height)
        w = self.convert_percent_to_pixels(coords.get('width', '80%'), width)
        h = self.convert_percent_to_pixels(coords.get('height', '80%'), height)

        style = element.get('style', {})
        default_style = self.overlay_styles['geometric']['squares']

        stroke = style.get('stroke', default_style['stroke'])
        stroke_width = style.get('strokeWidth', default_style['strokeWidth'])
        fill = style.get('fill', default_style['fill'])
        opacity = style.get('opacity', default_style['opacity'])

        svg = f'''  <rect x="{x}" y="{y}" width="{w}" height="{h}"
          stroke="{stroke}"
          stroke-width="{stroke_width}"
          fill="{fill}"
          opacity="{opacity}"/>
'''

        if element.get('label'):
            label_x = x + w / 2
            label_y = y - 10
            svg += self.create_label(element['label'], label_x, label_y)

        return svg

    def create_polygon(self, element: Dict, width: int, height: int) -> str:
        """Create SVG polygon element"""
        coords = element['coordinates']
        points = coords.get('points', [])

        # Convert points
        point_strs = []
        for point in points:
            x = self.convert_percent_to_pixels(point[0], width)
            y = self.convert_percent_to_pixels(point[1], height)
            point_strs.append(f"{x},{y}")

        points_attr = " ".join(point_strs)

        style = element.get('style', {})
        default_style = self.overlay_styles['geometric']['polygons']

        stroke = style.get('stroke', default_style['stroke'])
        stroke_width = style.get('strokeWidth', default_style['strokeWidth'])
        fill = style.get('fill', default_style['fill'])
        opacity = style.get('opacity', default_style['opacity'])

        svg = f'''  <polygon points="{points_attr}"
          stroke="{stroke}"
          stroke-width="{stroke_width}"
          fill="{fill}"
          opacity="{opacity}"/>
'''

        return svg

    def create_arrow(self, element: Dict, width: int, height: int) -> str:
        """Create SVG arrow (line with marker)"""
        coords = element['coordinates']
        x1 = self.convert_percent_to_pixels(coords.get('x1', '0%'), width)
        y1 = self.convert_percent_to_pixels(coords.get('y1', '0%'), height)
        x2 = self.convert_percent_to_pixels(coords.get('x2', '100%'), width)
        y2 = self.convert_percent_to_pixels(coords.get('y2', '100%'), height)

        style = element.get('style', {})
        default_style = self.overlay_styles['annotations']['arrows']

        stroke = style.get('stroke', default_style['stroke'])
        stroke_width = style.get('strokeWidth', default_style['strokeWidth'])
        opacity = style.get('opacity', default_style['opacity'])

        # Define arrowhead marker
        marker_id = f"arrowhead-{hash(str(element))}"

        svg = f'''  <defs>
    <marker id="{marker_id}" markerWidth="10" markerHeight="10"
            refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="{stroke}" />
    </marker>
  </defs>
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"
        stroke="{stroke}"
        stroke-width="{stroke_width}"
        opacity="{opacity}"
        marker-end="url(#{marker_id})"/>
'''

        if element.get('label'):
            label_x = (x1 + x2) / 2
            label_y = (y1 + y2) / 2 - 10
            svg += self.create_label(element['label'], label_x, label_y)

        return svg

    def create_label(self, text: str, x: float, y: float) -> str:
        """Create SVG text label with background"""
        label_style = self.overlay_styles['annotations']['labels']

        font_family = label_style['fontFamily']
        font_size = label_style['fontSize']
        font_weight = label_style['fontWeight']
        fill = label_style['fill']
        stroke = label_style['stroke']
        stroke_width = label_style['strokeWidth']

        # Estimate text width (rough approximation)
        text_width = len(text) * 8 + 16

        return f'''  <g>
    <rect x="{x - text_width/2}" y="{y - 18}"
          width="{text_width}" height="28"
          fill="rgba(0,0,0,0.7)" rx="4"/>
    <text x="{x}" y="{y}"
          font-family="{font_family}"
          font-size="{font_size}"
          font-weight="{font_weight}"
          fill="{fill}"
          text-anchor="middle"
          dominant-baseline="middle">
      {text}
    </text>
  </g>
'''

    def generate_overlay_svg(self, overlay_data: Dict, width: int = None, height: int = None) -> str:
        """Generate complete SVG overlay from overlay data"""
        w = width or self.default_width
        h = height or self.default_height

        svg = self.create_svg_wrapper(w, h)

        elements = overlay_data.get('elements', [])
        for element in elements:
            shape = element['shape']

            if shape == 'circle':
                svg += self.create_circle(element, w, h)
            elif shape == 'line':
                svg += self.create_line(element, w, h)
            elif shape == 'rectangle':
                svg += self.create_rectangle(element, w, h)
            elif shape == 'polygon':
                svg += self.create_polygon(element, w, h)
            elif shape == 'arrow':
                svg += self.create_arrow(element, w, h)
            elif shape == 'label':
                coords = element['coordinates']
                x = self.convert_percent_to_pixels(coords.get('x', '50%'), w)
                y = self.convert_percent_to_pixels(coords.get('y', '50%'), h)
                svg += self.create_label(element.get('label', 'Label'), x, y)

        svg += '</svg>'
        return svg

    def generate_overlays_for_lesson(self, lesson_path: str, output_dir: str):
        """Generate all overlay SVGs for a lesson"""
        with open(lesson_path, 'r') as f:
            lesson = json.load(f)

        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        lesson_id = lesson['lessonId']

        for artifact in lesson.get('artifacts', []):
            artifact_id = artifact['artifactId']

            for overlay in artifact.get('overlays', []):
                overlay_id = overlay['overlayId']
                svg_content = self.generate_overlay_svg(overlay)

                filename = f"{lesson_id}-{artifact_id}-{overlay_id}.svg"
                filepath = output_path / filename

                with open(filepath, 'w') as f:
                    f.write(svg_content)

                print(f"✓ Generated overlay: {filename}")


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python overlay_generator.py <lesson_json_path>")
        sys.exit(1)

    lesson_path = sys.argv[1]
    root_dir = Path(__file__).parent.parent
    design_system_path = root_dir / "schemas" / "design_system.json"
    output_dir = root_dir / "assets" / "overlays"

    generator = OverlayGenerator(str(design_system_path))
    generator.generate_overlays_for_lesson(lesson_path, str(output_dir))


if __name__ == "__main__":
    main()
