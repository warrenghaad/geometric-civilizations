#!/usr/bin/env python3
"""
Mesopotamian Sacred Geometry - Visual Asset Manager
Manages all visual assets: SVGs, deity symbols, artifact references, and complete catalog
"""

import json
import math
import os
from pathlib import Path
from svg_generator import GeometricSVGGenerator


class DeitySymbolGenerator:
    """Generate SVG representations of deities with their symbols"""

    def __init__(self, output_dir="svg_outputs/deities"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def svg_header(self, width=400, height=500):
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
'''

    def svg_footer(self):
        return "</svg>"

    def generate_shamash(self):
        """Shamash - Sun god with solar disc and rays"""
        svg = self.svg_header()

        # Solar disc
        svg += f'  <circle cx="200" cy="150" r="100" fill="#FFA500" stroke="#FF4500" stroke-width="4"/>\n'

        # Sun rays (long and short alternating)
        for i in range(16):
            angle = (i * 22.5 - 90) * math.pi / 180
            length = 140 if i % 2 == 0 else 120
            x1 = 200 + 100 * math.cos(angle)
            y1 = 150 + 100 * math.sin(angle)
            x2 = 200 + length * math.cos(angle)
            y2 = 150 + length * math.sin(angle)
            svg += f'  <line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#FF4500" stroke-width="6"/>\n'

        # Inner circle
        svg += f'  <circle cx="200" cy="150" r="70" fill="#FFD700" stroke="#FF8C00" stroke-width="3"/>\n'

        # Face features (simplified)
        svg += f'  <circle cx="180" cy="140" r="8" fill="#8B4513"/>\n'
        svg += f'  <circle cx="220" cy="140" r="8" fill="#8B4513"/>\n'
        svg += f'  <path d="M 180,170 Q 200,180 220,170" fill="none" stroke="#8B4513" stroke-width="4"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#F5DEB3"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#8B4513">SHAMASH</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#654321">Sun God • Justice</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#654321">Solar Disc • Circle Geometry</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_nanna(self):
        """Nanna/Sin - Moon god with crescent and horns"""
        svg = self.svg_header()

        # Crescent moon (large)
        svg += f'  <circle cx="200" cy="150" r="100" fill="#C0C0C0" stroke="#696969" stroke-width="4"/>\n'
        svg += f'  <circle cx="240" cy="150" r="100" fill="white" stroke="none"/>\n'

        # Horned crown
        svg += f'  <path d="M 120 120 Q 110 90 115 70" fill="none" stroke="#8B4513" stroke-width="6"/>\n'
        svg += f'  <path d="M 120 180 Q 110 210 115 230" fill="none" stroke="#8B4513" stroke-width="6"/>\n'

        # Stars around
        star_pos = [(280, 80), (310, 130), (300, 180), (280, 220)]
        for x, y in star_pos:
            svg += f'  <polygon points="{x},{y-10} {x-3},{y-3} {x-10},{y} {x-3},{y+3} {x},{y+10} {x+3},{y+3} {x+10},{y} {x+3},{y-3}" fill="#FFD700" stroke="#B8860B" stroke-width="1"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#E6E6FA"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#4B0082">NANNA/SIN</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#4B0082">Moon God • Wisdom</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#4B0082">Crescent • Lunar Cycles</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_enlil(self):
        """Enlil - King of gods with mountain/ziggurat"""
        svg = self.svg_header()

        # Ziggurat/Mountain (3 levels)
        svg += f'  <polygon points="200,60 100,250 300,250" fill="#8B4513" stroke="#654321" stroke-width="3"/>\n'

        # Steps
        svg += f'  <rect x="120" y="200" width="160" height="50" fill="#A0522D" stroke="#654321" stroke-width="2"/>\n'
        svg += f'  <rect x="150" y="150" width="100" height="50" fill="#CD853F" stroke="#654321" stroke-width="2"/>\n'
        svg += f'  <rect x="180" y="100" width="40" height="50" fill="#D2691E" stroke="#654321" stroke-width="2"/>\n'

        # Horned crown on top
        svg += f'  <circle cx="200" cy="70" r="20" fill="#FFD700" stroke="#B8860B" stroke-width="2"/>\n'
        svg += f'  <path d="M 185 60 L 180 40 L 182 42" fill="#FFD700" stroke="#B8860B" stroke-width="2"/>\n'
        svg += f'  <path d="M 215 60 L 220 40 L 218 42" fill="#FFD700" stroke="#B8860B" stroke-width="2"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#DEB887"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#8B4513">ENLIL</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#654321">King of Gods • Air • Storms</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#654321">Mountain/Ziggurat • Triangle</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_anu(self):
        """Anu - Sky god with celestial symbols"""
        svg = self.svg_header()

        # Large square (four directions/earth)
        svg += f'  <rect x="80" y="80" width="240" height="240" fill="#87CEEB" stroke="#4169E1" stroke-width="4"/>\n'

        # Stars in corners
        corners = [(120, 120), (280, 120), (120, 280), (280, 280)]
        for x, y in corners:
            for i in range(8):
                angle = (i * 45) * math.pi / 180
                x2 = x + 25 * math.cos(angle) if i % 2 == 0 else x + 12 * math.cos(angle)
                y2 = y + 25 * math.sin(angle) if i % 2 == 0 else y + 12 * math.sin(angle)
                svg += f'  <line x1="{x}" y1="{y}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#FFD700" stroke-width="3"/>\n'

        # Central heavenly symbol
        svg += f'  <circle cx="200" cy="200" r="60" fill="#191970" stroke="#FFD700" stroke-width="3"/>\n'
        # Stars inside
        for i in range(12):
            angle = (i * 30 - 90) * math.pi / 180
            x = 200 + 40 * math.cos(angle)
            y = 200 + 40 * math.sin(angle)
            svg += f'  <circle cx="{x:.2f}" cy="{y:.2f}" r="4" fill="#FFD700"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#F0F8FF"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#191970">ANU</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#4169E1">Sky God • Supreme Deity</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#4169E1">Square • Four Directions</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_inanna(self):
        """Inanna/Ishtar - Love and war goddess with 8-pointed star"""
        svg = self.svg_header()

        # Large 8-pointed star (Venus)
        points = []
        for i in range(16):
            angle = (i * 22.5 - 90) * math.pi / 180
            radius = 130 if i % 2 == 0 else 50
            x = 200 + radius * math.cos(angle)
            y = 150 + radius * math.sin(angle)
            points.append(f"{x:.2f},{y:.2f}")
        svg += f'  <polygon points="{" ".join(points)}" fill="#FF69B4" stroke="#C71585" stroke-width="4"/>\n'

        # Inner rosette
        svg += f'  <circle cx="200" cy="150" r="60" fill="#FFB6C1" stroke="#FF1493" stroke-width="3"/>\n'

        # Center star
        small_points = []
        for i in range(16):
            angle = (i * 22.5 - 90) * math.pi / 180
            radius = 40 if i % 2 == 0 else 15
            x = 200 + radius * math.cos(angle)
            y = 150 + radius * math.sin(angle)
            small_points.append(f"{x:.2f},{y:.2f}")
        svg += f'  <polygon points="{" ".join(small_points)}" fill="#FF1493" stroke="#C71585" stroke-width="2"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#FFE4E1"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#C71585">INANNA/ISHTAR</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#FF1493">Love • War • Fertility • Venus</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#FF1493">8-Pointed Star • Venus Cycle</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_enki(self):
        """Enki/Ea - Water and wisdom god with zigzag waves"""
        svg = self.svg_header()

        # Multiple wave layers
        for y_base in [100, 150, 200, 250]:
            path = f"M 50,{y_base} "
            for i in range(8):
                x = 50 + i * 45
                y = y_base + (30 if i % 2 == 0 else -30)
                path += f"L {x},{y} "
            svg += f'  <path d="{path}" fill="none" stroke="#1E90FF" stroke-width="8"/>\n'

        # Goat-fish creature (simplified)
        svg += f'  <circle cx="200" cy="150" r="40" fill="#4682B4" stroke="#00008B" stroke-width="3"/>\n'
        svg += f'  <circle cx="185" cy="140" r="6" fill="white"/>\n'
        svg += f'  <circle cx="215" cy="140" r="6" fill="white"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#E0F6FF"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#00008B">ENKI/EA</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#1E90FF">Water • Wisdom • Creation</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#1E90FF">Flowing Water • Zigzag Pattern</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_ningishzida(self):
        """Ningishzida - Underworld god with intertwined serpents"""
        svg = self.svg_header()

        # Intertwined serpents
        path1 = "M 80,250 "
        path2 = "M 80,250 "

        for i in range(8):
            x = 80 + i * 40
            y1 = 150 + 70 * math.sin(i * 0.7)
            y2 = 150 + 70 * math.sin(i * 0.7 + math.pi)
            path1 += f"Q {x+15},{y1-30} {x+40},{y1} "
            path2 += f"Q {x+15},{y2+30} {x+40},{y2} "

        svg += f'  <path d="{path1}" fill="none" stroke="#8B008B" stroke-width="12"/>\n'
        svg += f'  <path d="{path2}" fill="none" stroke="#9932CC" stroke-width="12"/>\n'

        # Serpent heads
        y1_final = 150 + 70 * math.sin(7 * 0.7)
        y2_final = 150 + 70 * math.sin(7 * 0.7 + math.pi)
        svg += f'  <circle cx="320" cy="{y1_final:.2f}" r="12" fill="#8B008B"/>\n'
        svg += f'  <circle cx="315" cy="{y1_final-3:.2f}" r="3" fill="#FF0000"/>\n'
        svg += f'  <circle cx="320" cy="{y2_final:.2f}" r="12" fill="#9932CC"/>\n'
        svg += f'  <circle cx="315" cy="{y2_final-3:.2f}" r="3" fill="#FF0000"/>\n'

        # Title
        svg += f'  <rect x="0" y="350" width="400" height="80" fill="#E6D8FF"/>\n'
        svg += f'  <text x="200" y="380" text-anchor="middle" font-family="Arial" font-size="20" font-weight="bold" fill="#4B0082">NINGISHZIDA</text>\n'
        svg += f'  <text x="200" y="405" text-anchor="middle" font-family="Arial" font-size="14" fill="#8B008B">Underworld • Vegetation • Serpents</text>\n'
        svg += f'  <text x="200" y="425" text-anchor="middle" font-family="Arial" font-size="12" fill="#8B008B">Intertwined Serpents • Spiral</text>\n'

        svg += self.svg_footer()
        return svg

    def generate_all_deities(self):
        """Generate all deity symbols"""
        deities = {
            "shamash.svg": self.generate_shamash,
            "nanna_sin.svg": self.generate_nanna,
            "enlil.svg": self.generate_enlil,
            "anu.svg": self.generate_anu,
            "inanna_ishtar.svg": self.generate_inanna,
            "enki_ea.svg": self.generate_enki,
            "ningishzida.svg": self.generate_ningishzida,
        }

        print(f"Generating {len(deities)} deity symbols...")
        for filename, generator_func in deities.items():
            filepath = self.output_dir / filename
            svg_content = generator_func()

            with open(filepath, 'w') as f:
                f.write(svg_content)

            print(f"✓ Created: deities/{filename}")

        return len(deities)


class ArtifactReferenceSystem:
    """Manage and document artifact references with museum links"""

    def __init__(self, inventory_file="visual_inventory.json", output_file="artifact_reference_guide.md"):
        self.inventory_file = inventory_file
        self.output_file = output_file
        self.data = None

    def load_inventory(self):
        """Load visual inventory data"""
        with open(self.inventory_file, 'r') as f:
            self.data = json.load(f)

    def generate_artifact_guide(self):
        """Generate comprehensive artifact reference guide"""
        self.load_inventory()

        md = "# Mesopotamian Sacred Geometry - Artifact Reference Guide\n\n"
        md += "## Complete Museum Artifact Database\n\n"
        md += "This guide provides detailed information about all 40+ artifacts referenced in the curriculum.\n\n"
        md += "---\n\n"

        # Group by museum
        artifacts_by_museum = {}
        for artifact in self.data['artifacts']:
            museum = artifact['museum']
            if museum not in artifacts_by_museum:
                artifacts_by_museum[museum] = []
            artifacts_by_museum[museum].append(artifact)

        # Generate content by museum
        for museum, artifacts in sorted(artifacts_by_museum.items()):
            md += f"## {museum}\n\n"
            md += f"**Total Artifacts:** {len(artifacts)}\n\n"

            for artifact in artifacts:
                md += f"### {artifact['name']}\n\n"
                md += f"**Accession Number:** {artifact['accession']}\n\n"
                md += f"**Period:** {artifact['period']}\n\n"
                md += f"**Location Found:** {artifact['location']}\n\n"
                md += f"**Description:** {artifact['description']}\n\n"

                if artifact['geometric_elements']:
                    md += f"**Geometric Elements:** {', '.join(artifact['geometric_elements'])}\n\n"

                if artifact['deity_connections']:
                    md += f"**Deity Connections:** {', '.join(artifact['deity_connections'])}\n\n"

                md += f"**Educational Value:** {artifact['educational_value']}\n\n"
                md += f"**Museum Link:** {artifact['url']}\n\n"
                md += f"**Image Needed:** {'Yes' if artifact['image_needed'] else 'No'}\n\n"
                md += "---\n\n"

        # Add summary statistics
        md += "\n## Summary Statistics\n\n"
        md += f"- **Total Artifacts:** {len(self.data['artifacts'])}\n"
        md += f"- **Museums Represented:** {len(artifacts_by_museum)}\n"
        md += f"- **Time Span:** ~3200 BCE to ~400 BCE (2800+ years)\n"
        md += f"- **Geometric Types:** {len(self.data['geometric_elements'])} major categories\n\n"

        # Period breakdown
        md += "### Artifacts by Period\n\n"
        periods = {}
        for artifact in self.data['artifacts']:
            period = artifact['period']
            periods[period] = periods.get(period, 0) + 1

        for period, count in sorted(periods.items()):
            md += f"- **{period}:** {count} artifact(s)\n"

        md += "\n---\n\n"

        # Image acquisition guide
        md += "## Image Acquisition Guide\n\n"
        md += "### Museum APIs and Resources\n\n"

        museum_apis = {
            "British Museum": {
                "API": "https://www.britishmuseum.org/collection",
                "License": "CC BY-NC-SA 4.0 for most items",
                "Notes": "High-resolution images available; requires attribution"
            },
            "Louvre": {
                "API": "https://collections.louvre.fr",
                "License": "Open Access for many items",
                "Notes": "Collections database with downloadable images"
            },
            "Metropolitan Museum": {
                "API": "https://www.metmuseum.org/art/collection",
                "License": "Open Access (CC0) for public domain works",
                "Notes": "Excellent API and high-res downloads"
            },
            "Pergamon Museum": {
                "API": "https://www.smb.museum/en/museums-institutions/pergamonmuseum",
                "License": "Varies by item",
                "Notes": "Part of Berlin State Museums"
            }
        }

        for museum, info in museum_apis.items():
            md += f"### {museum}\n\n"
            md += f"- **Collection URL:** {info['API']}\n"
            md += f"- **License:** {info['License']}\n"
            md += f"- **Notes:** {info['Notes']}\n\n"

        # Write to file
        with open(self.output_file, 'w') as f:
            f.write(md)

        print(f"✓ Created: {self.output_file}")
        return len(self.data['artifacts'])


class VisualAssetManager:
    """Main coordinator for all visual assets"""

    def __init__(self):
        self.inventory_file = "visual_inventory.json"
        self.stats = {
            'svg_shapes': 0,
            'deity_symbols': 0,
            'artifacts': 0,
            'total_files': 0
        }

    def generate_all_assets(self):
        """Generate all visual assets"""
        print("\n" + "=" * 70)
        print("MESOPOTAMIAN SACRED GEOMETRY - VISUAL ASSET MANAGER")
        print("=" * 70)
        print()

        # 1. Generate geometric SVGs
        print("📐 STEP 1: Generating Geometric Elements...")
        print("-" * 70)
        geo_gen = GeometricSVGGenerator()
        self.stats['svg_shapes'] = geo_gen.generate_all_shapes()
        print()

        # 2. Generate deity symbols
        print("🏛️  STEP 2: Generating Deity Symbols...")
        print("-" * 70)
        deity_gen = DeitySymbolGenerator()
        self.stats['deity_symbols'] = deity_gen.generate_all_deities()
        print()

        # 3. Generate artifact reference guide
        print("📚 STEP 3: Creating Artifact Reference System...")
        print("-" * 70)
        artifact_sys = ArtifactReferenceSystem()
        self.stats['artifacts'] = artifact_sys.generate_artifact_guide()
        print()

        # 4. Generate statistics report
        print("📊 STEP 4: Generating Statistics Report...")
        print("-" * 70)
        self.generate_statistics_report()
        print()

        # Final summary
        self.print_final_summary()

    def generate_statistics_report(self):
        """Generate comprehensive statistics report"""
        with open(self.inventory_file, 'r') as f:
            data = json.load(f)

        report = "# Mesopotamian Sacred Geometry - Content Statistics Report\n\n"
        report += "## 📊 Complete Curriculum Statistics\n\n"

        # Major sections
        report += "### Major Sections Fully Developed\n\n"
        sections = [
            "1. Introduction & Foundations",
            "2. Myth & Belief Systems",
            "3. Primary Shapes (Circle, Triangle, Square)",
            "4. Crescent Forms",
            "5. Star Forms (6, 8, 12-pointed)",
            "6. Pattern Forms (Zigzag, Spiral)",
            "7. 3D Forms (Cylinder, Cone)",
            "8. Composite Symbols",
            "9. Artifacts & Material Culture",
            "10. Technology & Inventions",
            "11. Mathematical Concepts",
            "12. Historical Legacy & Modern Applications"
        ]

        for section in sections:
            report += f"- {section}\n"

        report += f"\n**Total:** {len(sections)} major sections\n\n"

        # Geometric elements
        report += "### Geometric Elements Analyzed\n\n"
        report += f"**Total Elements:** {len(data['geometric_elements'])}\n\n"

        for elem in data['geometric_elements']:
            report += f"#### {elem['name']}\n"
            report += f"- **Deity:** {', '.join(elem['deity_connections'])}\n"
            report += f"- **Belief:** {elem['belief']}\n"
            report += f"- **Progressions:** Simple → Intermediate → Complex\n"
            report += f"- **Formulas:** {len(elem['formulas'])}\n"
            report += f"- **Technologies:** {', '.join(elem['technology_connections'][:3])}...\n\n"

        # Artifacts
        report += f"### Museum Artifacts Referenced\n\n"
        report += f"**Total:** {len(data['artifacts'])} artifacts\n\n"

        museums = {}
        for artifact in data['artifacts']:
            museum = artifact['museum']
            museums[museum] = museums.get(museum, 0) + 1

        report += "**By Museum:**\n\n"
        for museum, count in sorted(museums.items(), key=lambda x: x[1], reverse=True):
            report += f"- {museum}: {count} artifacts\n"

        report += "\n"

        # Mathematical formulas
        report += "### Mathematical Formulas\n\n"
        formula_count = sum(len(elem['formulas']) for elem in data['geometric_elements'])
        report += f"**Total Formulas:** {formula_count}\n\n"

        # Technology connections
        report += "### Technology Connections\n\n"
        all_tech = set()
        for elem in data['geometric_elements']:
            all_tech.update(elem['technology_connections'])
        report += f"**Total Technologies:** {len(all_tech)}\n\n"
        for tech in sorted(all_tech):
            report += f"- {tech}\n"

        report += "\n"

        # Grade differentiation
        report += "### Grade 3-5 Differentiation\n\n"
        report += "**All elements include:**\n"
        report += "- Grade 3: Simple recognition and basic construction\n"
        report += "- Grade 4: Intermediate calculations and analysis\n"
        report += "- Grade 5: Complex derivations and creative applications\n\n"

        # HOW/WHY/WHAT IF framework
        report += "### HOW/WHY/WHAT IF Framework\n\n"
        report += "**Integrated across all lessons:**\n"
        report += "- **HOW:** Construction techniques, measurement methods\n"
        report += "- **WHY:** Symbolic meanings, cultural significance\n"
        report += "- **WHAT IF:** Creative applications, cross-cultural comparisons\n\n"

        # Deity coverage
        report += "### Deity Coverage\n\n"
        report += f"**Total Deities:** {len(data['deities'])}\n\n"
        for deity in data['deities']:
            report += f"#### {deity['name']}\n"
            report += f"- **Role:** {deity['role']}\n"
            report += f"- **Symbols:** {', '.join(deity['symbols'])}\n"
            report += f"- **Geometric Association:** {deity['geometric_association']}\n"
            report += f"- **Image Sources:** {len(deity['image_sources'])}\n\n"

        # Visual assets generated
        report += "### Visual Assets Generated\n\n"
        report += f"- **Geometric SVGs:** {self.stats['svg_shapes']}\n"
        report += f"- **Deity Symbols:** {self.stats['deity_symbols']}\n"
        report += f"- **Artifact References:** {self.stats['artifacts']}\n"
        report += f"- **Total Visual Elements:** {sum([self.stats['svg_shapes'], self.stats['deity_symbols']])}\n\n"

        # Summary table
        report += "## Summary Table\n\n"
        report += "| Category | Count |\n"
        report += "|----------|-------|\n"
        report += f"| Major Sections | {len(sections)} |\n"
        report += f"| Geometric Elements | {len(data['geometric_elements'])} |\n"
        report += f"| Museum Artifacts | {len(data['artifacts'])} |\n"
        report += f"| Mathematical Formulas | {formula_count} |\n"
        report += f"| Technology Connections | {len(all_tech)} |\n"
        report += f"| Deities | {len(data['deities'])} |\n"
        report += f"| Grade Levels | 3 (Grades 3-5) |\n"
        report += f"| SVG Graphics Generated | {self.stats['svg_shapes']} |\n"
        report += f"| Deity Symbols | {self.stats['deity_symbols']} |\n\n"

        # Write report
        with open("content_statistics_report.md", 'w') as f:
            f.write(report)

        print("✓ Created: content_statistics_report.md")

    def print_final_summary(self):
        """Print final summary of all generated assets"""
        print("=" * 70)
        print("✅ GENERATION COMPLETE!")
        print("=" * 70)
        print()
        print("📦 Assets Created:")
        print(f"   • {self.stats['svg_shapes']} geometric SVG files")
        print(f"   • {self.stats['deity_symbols']} deity symbol files")
        print(f"   • {self.stats['artifacts']} artifact references documented")
        print()
        print("📁 Output Structure:")
        print("   svg_outputs/")
        print("   ├── shapes/          (geometric elements)")
        print("   ├── deities/         (deity symbols)")
        print("   ├── patterns/        (decorative patterns)")
        print("   ├── constructions/   (construction diagrams)")
        print("   ├── celestial/       (astronomical symbols)")
        print("   └── tools/           (technology diagrams)")
        print()
        print("📄 Documentation:")
        print("   • visual_inventory.json")
        print("   • artifact_reference_guide.md")
        print("   • content_statistics_report.md")
        print()
        print("=" * 70)
        print("Ready for curriculum integration! 🎓")
        print("=" * 70)


def main():
    """Main execution"""
    manager = VisualAssetManager()
    manager.generate_all_assets()


if __name__ == "__main__":
    main()
