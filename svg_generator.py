#!/usr/bin/env python3
"""
Mesopotamian Sacred Geometry - SVG Generator
Generates all geometric elements with simple → complex progressions
"""

import json
import math
import os
from pathlib import Path


class GeometricSVGGenerator:
    """Generate SVG files for all Mesopotamian geometric elements"""

    def __init__(self, output_dir="svg_outputs"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Create subdirectories
        (self.output_dir / "shapes").mkdir(exist_ok=True)
        (self.output_dir / "deities").mkdir(exist_ok=True)
        (self.output_dir / "patterns").mkdir(exist_ok=True)
        (self.output_dir / "constructions").mkdir(exist_ok=True)
        (self.output_dir / "celestial").mkdir(exist_ok=True)
        (self.output_dir / "tools").mkdir(exist_ok=True)

    def svg_header(self, width=400, height=400, viewbox=None):
        """Create SVG header"""
        if viewbox is None:
            viewbox = f"0 0 {width} {height}"
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="{viewbox}">
'''

    def svg_footer(self):
        """Create SVG footer"""
        return "</svg>"

    # ===== CIRCLES =====

    def generate_circle_simple(self):
        """Simple circle - Grade 3"""
        svg = self.svg_header()
        svg += f'  <circle cx="200" cy="200" r="150" fill="none" stroke="#2C5F8D" stroke-width="3"/>\n'
        svg += f'  <circle cx="200" cy="200" r="3" fill="#2C5F8D"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Basic Circle</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_circle_rosette_6(self):
        """6-petal rosette - Grade 4"""
        svg = self.svg_header()
        cx, cy, r = 200, 200, 60

        # Draw 6 petals
        for i in range(6):
            angle = (i * 60) * math.pi / 180
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            svg += f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="none" stroke="#8B4513" stroke-width="2"/>\n'

        # Center circle
        svg += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#8B4513" stroke-width="3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">6-Petal Rosette</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_circle_rosette_12(self):
        """12-fold rosette - Grade 5"""
        svg = self.svg_header()
        cx, cy, r = 200, 200, 50

        # Draw 12 petals
        for i in range(12):
            angle = (i * 30) * math.pi / 180
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            svg += f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="none" stroke="#DAA520" stroke-width="1.5"/>\n'

        # Center circle
        svg += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#DAA520" stroke-width="3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">12-Fold Rosette</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== TRIANGLES =====

    def generate_triangle_simple(self):
        """Simple equilateral triangle - Grade 3"""
        svg = self.svg_header()
        # Equilateral triangle
        height = 150 * math.sqrt(3) / 2
        points = f"200,80 {200-75},{80+height} {200+75},{80+height}"
        svg += f'  <polygon points="{points}" fill="none" stroke="#8B0000" stroke-width="3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Equilateral Triangle</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_triangle_ziggurat_3(self):
        """3-level ziggurat - Grade 4"""
        svg = self.svg_header()
        svg += f'  <!-- Base level -->\n'
        svg += f'  <rect x="100" y="260" width="200" height="40" fill="#CD853F" stroke="#8B4513" stroke-width="2"/>\n'
        svg += f'  <!-- Middle level -->\n'
        svg += f'  <rect x="130" y="220" width="140" height="40" fill="#D2691E" stroke="#8B4513" stroke-width="2"/>\n'
        svg += f'  <!-- Top level -->\n'
        svg += f'  <rect x="160" y="180" width="80" height="40" fill="#DEB887" stroke="#8B4513" stroke-width="2"/>\n'
        svg += f'  <!-- Temple top -->\n'
        svg += f'  <rect x="180" y="160" width="40" height="20" fill="#F4A460" stroke="#8B4513" stroke-width="2"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">3-Level Ziggurat</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_triangle_ziggurat_7(self):
        """7-level stepped ziggurat - Grade 5"""
        svg = self.svg_header(500, 500)
        levels = 7
        base_y = 420
        level_height = 35
        base_width = 280

        colors = ["#8B4513", "#A0522D", "#CD853F", "#D2691E", "#DEB887", "#F4A460", "#FFE4B5"]

        for i in range(levels):
            width = base_width - (i * 35)
            x = 250 - width / 2
            y = base_y - (i * level_height)
            svg += f'  <rect x="{x}" y="{y}" width="{width}" height="{level_height}" fill="{colors[i]}" stroke="#654321" stroke-width="1.5"/>\n'

        # Temple structure on top
        svg += f'  <rect x="230" y="175" width="40" height="20" fill="#FFD700" stroke="#654321" stroke-width="1.5"/>\n'
        svg += f'  <text x="250" y="480" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">7-Level Ziggurat</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== SQUARES/RECTANGLES =====

    def generate_square_simple(self):
        """Simple square - Grade 3"""
        svg = self.svg_header()
        svg += f'  <rect x="100" y="100" width="200" height="200" fill="none" stroke="#4169E1" stroke-width="3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Basic Square</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_square_grid(self):
        """Grid pattern - Grade 4"""
        svg = self.svg_header()
        # 4x4 grid
        for i in range(5):
            # Vertical lines
            x = 100 + i * 50
            svg += f'  <line x1="{x}" y1="100" x2="{x}" y2="300" stroke="#4169E1" stroke-width="2"/>\n'
            # Horizontal lines
            y = 100 + i * 50
            svg += f'  <line x1="100" y1="{y}" x2="300" y2="{y}" stroke="#4169E1" stroke-width="2"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Grid Pattern</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_square_city_plan(self):
        """Urban grid plan - Grade 5"""
        svg = self.svg_header(500, 500)
        # Complex city grid with different zones
        # Main streets
        for i in range(6):
            x = 50 + i * 80
            svg += f'  <line x1="{x}" y1="50" x2="{x}" y2="450" stroke="#696969" stroke-width="3"/>\n'
            y = 50 + i * 80
            svg += f'  <line x1="50" y1="{y}" x2="450" y2="{y}" stroke="#696969" stroke-width="3"/>\n'

        # Temple (central blue square)
        svg += f'  <rect x="170" y="170" width="160" height="160" fill="#4682B4" stroke="#000080" stroke-width="2"/>\n'
        svg += f'  <text x="250" y="255" text-anchor="middle" font-family="Arial" font-size="12" fill="white">Temple</text>\n'

        svg += f'  <text x="250" y="480" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Urban Grid Plan</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== CRESCENTS =====

    def generate_crescent_simple(self):
        """Simple crescent - Grade 3"""
        svg = self.svg_header()
        # Two circles to create crescent
        svg += f'  <defs>\n'
        svg += f'    <clipPath id="crescent">\n'
        svg += f'      <circle cx="200" cy="200" r="120"/>\n'
        svg += f'    </clipPath>\n'
        svg += f'  </defs>\n'
        svg += f'  <circle cx="200" cy="200" r="120" fill="#C0C0C0" stroke="#696969" stroke-width="2"/>\n'
        svg += f'  <circle cx="230" cy="200" r="120" fill="white" stroke="none"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Lunar Crescent</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_crescent_with_stars(self):
        """Crescent with stars - Grade 4"""
        svg = self.svg_header()
        # Crescent
        svg += f'  <circle cx="200" cy="200" r="100" fill="#FFD700" stroke="#DAA520" stroke-width="2"/>\n'
        svg += f'  <circle cx="225" cy="200" r="100" fill="white" stroke="none"/>\n'

        # Add stars
        star_positions = [(280, 150), (300, 200), (280, 250)]
        for x, y in star_positions:
            svg += self.create_simple_star(x, y, 15, "#FFD700")

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Crescent with Stars</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_crescent_complex(self):
        """Crescent with horns and celestial symbols - Grade 5"""
        svg = self.svg_header()
        # Crescent
        svg += f'  <circle cx="200" cy="200" r="100" fill="#FFD700" stroke="#B8860B" stroke-width="3"/>\n'
        svg += f'  <circle cx="230" cy="200" r="100" fill="white" stroke="none"/>\n'

        # Horns
        svg += f'  <path d="M 150 170 Q 140 150 145 130" fill="none" stroke="#8B4513" stroke-width="4"/>\n'
        svg += f'  <path d="M 150 230 Q 140 250 145 270" fill="none" stroke="#8B4513" stroke-width="4"/>\n'

        # Stars around
        star_positions = [(270, 120), (300, 160), (320, 200), (300, 240), (270, 280)]
        for x, y in star_positions:
            svg += self.create_simple_star(x, y, 12, "#FFD700")

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Divine Crescent</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== STARS =====

    def create_simple_star(self, cx, cy, r, color="#FFD700", points=5):
        """Helper function to create a simple star"""
        outer_r = r
        inner_r = r * 0.4
        star_points = []

        for i in range(points * 2):
            angle = (i * 180 / points - 90) * math.pi / 180
            radius = outer_r if i % 2 == 0 else inner_r
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            star_points.append(f"{x:.2f},{y:.2f}")

        return f'  <polygon points="{" ".join(star_points)}" fill="{color}" stroke="#B8860B" stroke-width="1"/>\n'

    def generate_star_8_simple(self):
        """Simple 8-point star - Grade 3"""
        svg = self.svg_header()
        svg += self.create_8_point_star(200, 200, 120, "#FF6347", simple=True)
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">8-Pointed Star</text>\n'
        svg += self.svg_footer()
        return svg

    def create_8_point_star(self, cx, cy, r, color, simple=False):
        """Create 8-point star (Ishtar)"""
        points = []
        num_points = 8

        for i in range(num_points * 2):
            angle = (i * 180 / num_points - 90) * math.pi / 180
            radius = r if i % 2 == 0 else r * 0.4
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            points.append(f"{x:.2f},{y:.2f}")

        return f'  <polygon points="{" ".join(points)}" fill="{color}" stroke="#8B0000" stroke-width="2"/>\n'

    def generate_star_8_rosette(self):
        """8-petal rosette - Grade 4"""
        svg = self.svg_header()
        cx, cy = 200, 200

        # 8 petals
        for i in range(8):
            angle = (i * 45) * math.pi / 180
            x = cx + 60 * math.cos(angle)
            y = cy + 60 * math.sin(angle)
            svg += f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="40" fill="none" stroke="#FF6347" stroke-width="2"/>\n'

        # Center
        svg += f'  <circle cx="{cx}" cy="{cy}" r="40" fill="#FFE4E1" stroke="#FF6347" stroke-width="3"/>\n'
        svg += self.create_8_point_star(200, 200, 30, "#FF6347")

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">8-Petal Rosette (Ishtar)</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_star_8_ornate(self):
        """Ornate Venus star - Grade 5"""
        svg = self.svg_header()
        # Multiple nested layers
        svg += self.create_8_point_star(200, 200, 140, "#FFE4E1")
        svg += self.create_8_point_star(200, 200, 100, "#FFB6C1")
        svg += self.create_8_point_star(200, 200, 60, "#FF69B4")
        svg += f'  <circle cx="200" cy="200" r="20" fill="#FF1493" stroke="#8B0000" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Venus Star (Inanna/Ishtar)</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_star_6_simple(self):
        """Simple 6-point star - Grade 3"""
        svg = self.svg_header()
        svg += self.create_6_point_star(200, 200, 120, "#32CD32")
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">6-Pointed Star</text>\n'
        svg += self.svg_footer()
        return svg

    def create_6_point_star(self, cx, cy, r, color):
        """Create 6-point star"""
        points = []
        for i in range(12):
            angle = (i * 30 - 90) * math.pi / 180
            radius = r if i % 2 == 0 else r * 0.5
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            points.append(f"{x:.2f},{y:.2f}")

        return f'  <polygon points="{" ".join(points)}" fill="{color}" stroke="#228B22" stroke-width="2"/>\n'

    def generate_star_6_rosette(self):
        """Hexagonal rosette - Grade 4"""
        svg = self.svg_header()
        cx, cy, r = 200, 200, 60

        for i in range(6):
            angle = (i * 60) * math.pi / 180
            x = cx + r * math.cos(angle)
            y = cy + r * math.sin(angle)
            svg += f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="50" fill="none" stroke="#32CD32" stroke-width="2"/>\n'

        svg += f'  <circle cx="{cx}" cy="{cy}" r="50" fill="#F0FFF0" stroke="#228B22" stroke-width="3"/>\n'
        svg += self.create_6_point_star(200, 200, 40, "#32CD32")

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Hexagonal Rosette</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_star_6_nested(self):
        """Nested hexagonal patterns - Grade 5"""
        svg = self.svg_header()
        # Multiple hexagons
        for r in [140, 100, 60]:
            points = []
            for i in range(6):
                angle = (i * 60 - 30) * math.pi / 180
                x = 200 + r * math.cos(angle)
                y = 200 + r * math.sin(angle)
                points.append(f"{x:.2f},{y:.2f}")
            svg += f'  <polygon points="{" ".join(points)}" fill="none" stroke="#32CD32" stroke-width="2"/>\n'

        svg += self.create_6_point_star(200, 200, 80, "#90EE90")
        svg += f'  <circle cx="200" cy="200" r="15" fill="#228B22"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Nested Hexagonal Patterns</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_star_12_simple(self):
        """12 equal rays - Grade 3"""
        svg = self.svg_header()
        cx, cy = 200, 200

        for i in range(12):
            angle = (i * 30) * math.pi / 180
            x1 = cx + 30 * math.cos(angle)
            y1 = cy + 30 * math.sin(angle)
            x2 = cx + 130 * math.cos(angle)
            y2 = cy + 130 * math.sin(angle)
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#9370DB" stroke-width="3"/>\n'

        svg += f'  <circle cx="200" cy="200" r="30" fill="#E6E6FA" stroke="#9370DB" stroke-width="2"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">12-Pointed Star</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_star_12_zodiac(self):
        """Zodiac wheel - Grade 4"""
        svg = self.svg_header()
        cx, cy = 200, 200

        # Outer circle
        svg += f'  <circle cx="200" cy="200" r="150" fill="none" stroke="#9370DB" stroke-width="3"/>\n'

        # 12 divisions
        for i in range(12):
            angle = (i * 30 - 90) * math.pi / 180
            x1 = cx + 100 * math.cos(angle)
            y1 = cy + 100 * math.sin(angle)
            x2 = cx + 150 * math.cos(angle)
            y2 = cy + 150 * math.sin(angle)
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#9370DB" stroke-width="2"/>\n'

        # Inner circle
        svg += f'  <circle cx="200" cy="200" r="100" fill="#F8F8FF" stroke="#9370DB" stroke-width="2"/>\n'

        # 12-point star
        points = []
        for i in range(24):
            angle = (i * 15 - 90) * math.pi / 180
            radius = 90 if i % 2 == 0 else 50
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            points.append(f"{x:.2f},{y:.2f}")
        svg += f'  <polygon points="{" ".join(points)}" fill="#E6E6FA" stroke="#9370DB" stroke-width="1"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Zodiac Wheel</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_star_12_full_zodiac(self):
        """Full zodiac with symbols - Grade 5"""
        svg = self.svg_header(500, 500)
        cx, cy = 250, 250

        # Outer decorative circle
        svg += f'  <circle cx="250" cy="250" r="220" fill="none" stroke="#9370DB" stroke-width="4"/>\n'
        svg += f'  <circle cx="250" cy="250" r="200" fill="none" stroke="#9370DB" stroke-width="2"/>\n'

        # 12 divisions with alternating colors
        zodiac_names = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"]
        for i in range(12):
            angle_start = (i * 30 - 90) * math.pi / 180
            angle_mid = ((i * 30 + 15) - 90) * math.pi / 180

            # Division lines
            x = cx + 200 * math.cos(angle_start)
            y = cy + 200 * math.sin(angle_start)
            svg += f'  <line x1="{cx}" y1="{cy}" x2="{x:.2f}" y2="{y:.2f}" stroke="#9370DB" stroke-width="2"/>\n'

            # Zodiac symbols
            text_x = cx + 170 * math.cos(angle_mid)
            text_y = cy + 170 * math.sin(angle_mid)
            svg += f'  <text x="{text_x:.2f}" y="{text_y:.2f}" text-anchor="middle" font-family="Arial" font-size="24" fill="#4B0082">{zodiac_names[i]}</text>\n'

        # Center star
        points = []
        for i in range(24):
            angle = (i * 15 - 90) * math.pi / 180
            radius = 100 if i % 2 == 0 else 50
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            points.append(f"{x:.2f},{y:.2f}")
        svg += f'  <polygon points="{" ".join(points)}" fill="#E6E6FA" stroke="#4B0082" stroke-width="2"/>\n'
        svg += f'  <circle cx="250" cy="250" r="30" fill="#9370DB"/>\n'

        svg += f'  <text x="250" y="480" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Full Zodiac Wheel</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== ZIGZAG PATTERNS =====

    def generate_zigzag_simple(self):
        """Simple zigzag - Grade 3"""
        svg = self.svg_header()
        points = []
        for i in range(11):
            x = 50 + i * 30
            y = 200 + (50 if i % 2 == 0 else -50)
            points.append(f"{x},{y}")

        svg += f'  <polyline points="{" ".join(points)}" fill="none" stroke="#1E90FF" stroke-width="4"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Zigzag (Water Pattern)</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_zigzag_double(self):
        """Double zigzag band - Grade 4"""
        svg = self.svg_header()

        # Upper zigzag
        points1 = []
        for i in range(11):
            x = 50 + i * 30
            y = 160 + (40 if i % 2 == 0 else -40)
            points1.append(f"{x},{y}")
        svg += f'  <polyline points="{" ".join(points1)}" fill="none" stroke="#1E90FF" stroke-width="3"/>\n'

        # Lower zigzag
        points2 = []
        for i in range(11):
            x = 50 + i * 30
            y = 240 + (40 if i % 2 == 0 else -40)
            points2.append(f"{x},{y}")
        svg += f'  <polyline points="{" ".join(points2)}" fill="none" stroke="#1E90FF" stroke-width="3"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Double Zigzag Band</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_zigzag_guilloche(self):
        """Intertwined guilloche pattern - Grade 5"""
        svg = self.svg_header(500, 300)

        # Create interweaving wave pattern
        path1 = "M 20,150 "
        path2 = "M 20,150 "

        for i in range(10):
            x = 20 + i * 50
            if i % 2 == 0:
                path1 += f"Q {x+25},100 {x+50},150 "
                path2 += f"Q {x+25},200 {x+50},150 "
            else:
                path1 += f"Q {x+25},200 {x+50},150 "
                path2 += f"Q {x+25},100 {x+50},150 "

        svg += f'  <path d="{path1}" fill="none" stroke="#1E90FF" stroke-width="8" opacity="0.7"/>\n'
        svg += f'  <path d="{path2}" fill="none" stroke="#00BFFF" stroke-width="8" opacity="0.7"/>\n'

        svg += f'  <text x="250" y="280" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Guilloche Pattern (Enki\'s Waters)</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== SPIRALS =====

    def generate_spiral_simple(self):
        """Simple spiral - Grade 3"""
        svg = self.svg_header()

        # Create spiral path
        path = "M 200,200 "
        angle = 0
        radius = 5

        for i in range(100):
            angle += 0.3
            radius += 1.2
            x = 200 + radius * math.cos(angle)
            y = 200 + radius * math.sin(angle)
            path += f"L {x:.2f},{y:.2f} "

        svg += f'  <path d="{path}" fill="none" stroke="#8B008B" stroke-width="3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Spiral</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_spiral_double(self):
        """Double spiral - Grade 4"""
        svg = self.svg_header()

        # First spiral
        path1 = "M 200,200 "
        angle = 0
        radius = 5
        for i in range(80):
            angle += 0.3
            radius += 1.0
            x = 200 + radius * math.cos(angle)
            y = 200 + radius * math.sin(angle)
            path1 += f"L {x:.2f},{y:.2f} "

        # Second spiral (mirrored)
        path2 = "M 200,200 "
        angle = math.pi
        radius = 5
        for i in range(80):
            angle += 0.3
            radius += 1.0
            x = 200 + radius * math.cos(angle)
            y = 200 + radius * math.sin(angle)
            path2 += f"L {x:.2f},{y:.2f} "

        svg += f'  <path d="{path1}" fill="none" stroke="#8B008B" stroke-width="3"/>\n'
        svg += f'  <path d="{path2}" fill="none" stroke="#9932CC" stroke-width="3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Double Spiral</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_spiral_serpents(self):
        """Intertwined serpents - Grade 5"""
        svg = self.svg_header()

        # Serpent 1
        path1 = "M 100,200 "
        for i in range(8):
            x = 100 + i * 35
            y = 200 + 60 * math.sin(i * 0.8)
            path1 += f"Q {x+10},{y-30} {x+35},{y} "

        # Serpent 2
        path2 = "M 100,200 "
        for i in range(8):
            x = 100 + i * 35
            y = 200 + 60 * math.sin(i * 0.8 + math.pi)
            path2 += f"Q {x+10},{y+30} {x+35},{y} "

        svg += f'  <path d="{path1}" fill="none" stroke="#8B008B" stroke-width="8"/>\n'
        svg += f'  <path d="{path2}" fill="none" stroke="#9932CC" stroke-width="8"/>\n'

        # Serpent heads
        svg += f'  <circle cx="300" cy="{200 + 60 * math.sin(7 * 0.8):.2f}" r="8" fill="#8B008B"/>\n'
        svg += f'  <circle cx="300" cy="{200 + 60 * math.sin(7 * 0.8 + math.pi):.2f}" r="8" fill="#9932CC"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Intertwined Serpents (Ningishzida)</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== 3D FORMS =====

    def generate_cylinder_simple(self):
        """Basic cylinder - Grade 3"""
        svg = self.svg_header()

        # Top ellipse
        svg += f'  <ellipse cx="200" cy="120" rx="80" ry="20" fill="#D3D3D3" stroke="#696969" stroke-width="2"/>\n'
        # Side rectangles
        svg += f'  <rect x="120" y="120" width="160" height="150" fill="#C0C0C0" stroke="none"/>\n'
        # Side edges
        svg += f'  <line x1="120" y1="120" x2="120" y2="270" stroke="#696969" stroke-width="2"/>\n'
        svg += f'  <line x1="280" y1="120" x2="280" y2="270" stroke="#696969" stroke-width="2"/>\n'
        # Bottom ellipse
        svg += f'  <ellipse cx="200" cy="270" rx="80" ry="20" fill="#A9A9A9" stroke="#696969" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Cylinder</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_cylinder_bands(self):
        """Cylinder with bands - Grade 4"""
        svg = self.svg_header()

        # Top ellipse
        svg += f'  <ellipse cx="200" cy="100" rx="80" ry="20" fill="#D2B48C" stroke="#8B4513" stroke-width="2"/>\n'
        # Sides
        svg += f'  <rect x="120" y="100" width="160" height="180" fill="#DEB887" stroke="none"/>\n'
        svg += f'  <line x1="120" y1="100" x2="120" y2="280" stroke="#8B4513" stroke-width="2"/>\n'
        svg += f'  <line x1="280" y1="100" x2="280" y2="280" stroke="#8B4513" stroke-width="2"/>\n'

        # Decorative bands
        for y in [140, 180, 220]:
            svg += f'  <line x1="120" y1="{y}" x2="280" y2="{y}" stroke="#8B4513" stroke-width="2"/>\n'
            svg += f'  <ellipse cx="200" cy="{y}" rx="80" ry="5" fill="none" stroke="#8B4513" stroke-width="1"/>\n'

        # Bottom
        svg += f'  <ellipse cx="200" cy="280" rx="80" ry="20" fill="#BC8F8F" stroke="#8B4513" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Cylinder with Bands</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_cylinder_seal(self):
        """Carved narrative seal - Grade 5"""
        svg = self.svg_header()

        # Cylinder body
        svg += f'  <ellipse cx="200" cy="90" rx="80" ry="15" fill="#CD853F" stroke="#654321" stroke-width="2"/>\n'
        svg += f'  <rect x="120" y="90" width="160" height="200" fill="#D2691E" stroke="none"/>\n'
        svg += f'  <line x1="120" y1="90" x2="120" y2="290" stroke="#654321" stroke-width="2"/>\n'
        svg += f'  <line x1="280" y1="90" x2="280" y2="290" stroke="#654321" stroke-width="2"/>\n'

        # Carved figures (simplified)
        # Figure 1
        svg += f'  <circle cx="160" cy="150" r="12" fill="#654321"/>\n'
        svg += f'  <rect x="154" y="162" width="12" height="25" fill="#654321"/>\n'
        # Figure 2
        svg += f'  <circle cx="200" cy="160" r="12" fill="#654321"/>\n'
        svg += f'  <rect x="194" y="172" width="12" height="25" fill="#654321"/>\n'
        # Figure 3
        svg += f'  <circle cx="240" cy="150" r="12" fill="#654321"/>\n'
        svg += f'  <rect x="234" y="162" width="12" height="25" fill="#654321"/>\n'

        # Decorative patterns
        for y in [120, 210]:
            svg += f'  <line x1="130" y1="{y}" x2="270" y2="{y}" stroke="#654321" stroke-width="2"/>\n'

        svg += f'  <ellipse cx="200" cy="290" rx="80" ry="15" fill="#8B4513" stroke="#654321" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Cylinder Seal (Carved)</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_cone_simple(self):
        """Simple cone - Grade 3"""
        svg = self.svg_header()

        # Cone
        svg += f'  <polygon points="200,80 120,280 280,280" fill="#FFE4B5" stroke="#D2691E" stroke-width="2"/>\n'
        # Base ellipse
        svg += f'  <ellipse cx="200" cy="280" rx="80" ry="20" fill="#DEB887" stroke="#D2691E" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Cone</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_cone_bands(self):
        """Cone with bands - Grade 4"""
        svg = self.svg_header()

        # Cone with bands
        svg += f'  <polygon points="200,60 100,300 300,300" fill="#F5DEB3" stroke="#8B4513" stroke-width="2"/>\n'

        # Horizontal bands
        for i, y in enumerate([140, 200, 260]):
            width = (y - 60) * 200 / 240  # Proportional width
            svg += f'  <line x1="{200-width:.2f}" y1="{y}" x2="{200+width:.2f}" y2="{y}" stroke="#8B4513" stroke-width="3"/>\n'

        # Base
        svg += f'  <ellipse cx="200" cy="300" rx="100" ry="20" fill="#DEB887" stroke="#8B4513" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Cone with Bands</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_cone_spire(self):
        """Conical spire with decorative bands - Grade 5"""
        svg = self.svg_header()

        # Cone
        svg += f'  <polygon points="200,50 110,320 290,320" fill="#FFD700" stroke="#8B4513" stroke-width="2"/>\n'

        # Decorative bands with patterns
        band_positions = [120, 170, 220, 270]
        for y in band_positions:
            width = (y - 50) * 180 / 270
            svg += f'  <line x1="{200-width:.2f}" y1="{y}" x2="{200+width:.2f}" y2="{y}" stroke="#8B4513" stroke-width="4"/>\n'
            # Dots on bands
            for dx in range(-int(width), int(width)+1, 20):
                svg += f'  <circle cx="{200+dx}" cy="{y}" r="3" fill="#FF6347"/>\n'

        # Base
        svg += f'  <ellipse cx="200" cy="320" rx="90" ry="18" fill="#DAA520" stroke="#8B4513" stroke-width="2"/>\n'

        # Top ornament
        svg += f'  <circle cx="200" cy="50" r="8" fill="#FF6347" stroke="#8B0000" stroke-width="1"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Decorative Conical Spire</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== COMPOSITE =====

    def generate_composite_simple(self):
        """Two shapes combined - Grade 3"""
        svg = self.svg_header()

        # Circle + Star
        svg += f'  <circle cx="200" cy="200" r="120" fill="#FFE4E1" stroke="#B8860B" stroke-width="3"/>\n'
        svg += self.create_8_point_star(200, 200, 80, "#FFD700")

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Composite: Circle + Star</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_composite_layered(self):
        """Three shapes layered - Grade 4"""
        svg = self.svg_header()

        # Square background
        svg += f'  <rect x="80" y="80" width="240" height="240" fill="#E6E6FA" stroke="#4B0082" stroke-width="3"/>\n'
        # Circle
        svg += f'  <circle cx="200" cy="200" r="100" fill="#FFE4E1" stroke="#B8860B" stroke-width="3"/>\n'
        # Star
        svg += self.create_8_point_star(200, 200, 60, "#FFD700")

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Composite: Square + Circle + Star</text>\n'
        svg += self.svg_footer()
        return svg

    def generate_composite_deity(self):
        """Multi-symbol deity badge - Grade 5"""
        svg = self.svg_header()

        # Outer square (order/earth)
        svg += f'  <rect x="60" y="60" width="280" height="280" fill="#F0E68C" stroke="#8B4513" stroke-width="4"/>\n'

        # Circle (eternity)
        svg += f'  <circle cx="200" cy="200" r="130" fill="#E6E6FA" stroke="#4B0082" stroke-width="3"/>\n'

        # Crescent (moon - Nanna)
        svg += f'  <circle cx="200" cy="200" r="80" fill="#FFD700" stroke="#B8860B" stroke-width="2"/>\n'
        svg += f'  <circle cx="220" cy="200" r="80" fill="#E6E6FA" stroke="none"/>\n'

        # 8-point star (Ishtar)
        svg += self.create_8_point_star(200, 200, 50, "#FF69B4")

        # Central sun disc (Shamash)
        svg += f'  <circle cx="200" cy="200" r="25" fill="#FFA500" stroke="#FF4500" stroke-width="2"/>\n'

        # Rays
        for i in range(8):
            angle = (i * 45) * math.pi / 180
            x1 = 200 + 15 * math.cos(angle)
            y1 = 200 + 15 * math.sin(angle)
            x2 = 200 + 35 * math.cos(angle)
            y2 = 200 + 35 * math.sin(angle)
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#FF4500" stroke-width="2"/>\n'

        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="14" fill="#333">Divine Composite Symbol</text>\n'
        svg += self.svg_footer()
        return svg

    # ===== MAIN GENERATION METHOD =====

    def generate_all_shapes(self):
        """Generate all SVG files"""
        shapes = {
            # Circles
            "shapes/circle_01_simple.svg": self.generate_circle_simple,
            "shapes/circle_02_rosette_6.svg": self.generate_circle_rosette_6,
            "shapes/circle_03_rosette_12.svg": self.generate_circle_rosette_12,

            # Triangles
            "shapes/triangle_01_simple.svg": self.generate_triangle_simple,
            "shapes/triangle_02_ziggurat_3.svg": self.generate_triangle_ziggurat_3,
            "shapes/triangle_03_ziggurat_7.svg": self.generate_triangle_ziggurat_7,

            # Squares
            "shapes/square_01_simple.svg": self.generate_square_simple,
            "shapes/square_02_grid.svg": self.generate_square_grid,
            "shapes/square_03_city_plan.svg": self.generate_square_city_plan,

            # Crescents
            "shapes/crescent_01_simple.svg": self.generate_crescent_simple,
            "shapes/crescent_02_stars.svg": self.generate_crescent_with_stars,
            "shapes/crescent_03_complex.svg": self.generate_crescent_complex,

            # 8-Point Stars
            "shapes/star_8_01_simple.svg": self.generate_star_8_simple,
            "shapes/star_8_02_rosette.svg": self.generate_star_8_rosette,
            "shapes/star_8_03_ornate.svg": self.generate_star_8_ornate,

            # 6-Point Stars
            "shapes/star_6_01_simple.svg": self.generate_star_6_simple,
            "shapes/star_6_02_rosette.svg": self.generate_star_6_rosette,
            "shapes/star_6_03_nested.svg": self.generate_star_6_nested,

            # 12-Point Stars
            "shapes/star_12_01_simple.svg": self.generate_star_12_simple,
            "shapes/star_12_02_zodiac.svg": self.generate_star_12_zodiac,
            "shapes/star_12_03_full.svg": self.generate_star_12_full_zodiac,

            # Zigzag
            "patterns/zigzag_01_simple.svg": self.generate_zigzag_simple,
            "patterns/zigzag_02_double.svg": self.generate_zigzag_double,
            "patterns/zigzag_03_guilloche.svg": self.generate_zigzag_guilloche,

            # Spirals
            "patterns/spiral_01_simple.svg": self.generate_spiral_simple,
            "patterns/spiral_02_double.svg": self.generate_spiral_double,
            "patterns/spiral_03_serpents.svg": self.generate_spiral_serpents,

            # Cylinders
            "shapes/cylinder_01_simple.svg": self.generate_cylinder_simple,
            "shapes/cylinder_02_bands.svg": self.generate_cylinder_bands,
            "shapes/cylinder_03_seal.svg": self.generate_cylinder_seal,

            # Cones
            "shapes/cone_01_simple.svg": self.generate_cone_simple,
            "shapes/cone_02_bands.svg": self.generate_cone_bands,
            "shapes/cone_03_spire.svg": self.generate_cone_spire,

            # Composite
            "shapes/composite_01_simple.svg": self.generate_composite_simple,
            "shapes/composite_02_layered.svg": self.generate_composite_layered,
            "shapes/composite_03_deity.svg": self.generate_composite_deity,
        }

        print(f"Generating {len(shapes)} SVG files...")
        for filename, generator_func in shapes.items():
            filepath = self.output_dir / filename
            svg_content = generator_func()

            with open(filepath, 'w') as f:
                f.write(svg_content)

            print(f"✓ Created: {filename}")

        print(f"\n✅ All {len(shapes)} SVG files generated successfully!")
        return len(shapes)


def main():
    """Main execution"""
    print("=" * 60)
    print("MESOPOTAMIAN SACRED GEOMETRY - SVG GENERATOR")
    print("=" * 60)
    print()

    generator = GeometricSVGGenerator()
    count = generator.generate_all_shapes()

    print()
    print("=" * 60)
    print(f"COMPLETE: {count} geometric elements created")
    print(f"Output directory: {generator.output_dir}")
    print("=" * 60)


if __name__ == "__main__":
    main()
