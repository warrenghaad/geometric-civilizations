#!/usr/bin/env python3
"""
Mesopotamian Sacred Geometry - HTML Gallery Generator
Creates interactive HTML gallery for all visual assets
"""

import json
from pathlib import Path


class HTMLGalleryGenerator:
    """Generate comprehensive HTML gallery viewer"""

    def __init__(self, inventory_file="visual_inventory.json", output_file="visual_gallery.html"):
        self.inventory_file = inventory_file
        self.output_file = output_file
        self.data = None

    def load_inventory(self):
        """Load visual inventory data"""
        with open(self.inventory_file, 'r') as f:
            self.data = json.load(f)

    def generate_html(self):
        """Generate complete HTML gallery"""
        self.load_inventory()

        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mesopotamian Sacred Geometry - Visual Gallery</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Georgia', serif;
            background: linear-gradient(135deg, #f5e6d3 0%, #e8d5c4 100%);
            color: #3e2723;
            line-height: 1.6;
        }

        header {
            background: linear-gradient(135deg, #8B4513 0%, #654321 100%);
            color: #f5e6d3;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        nav {
            background: #654321;
            padding: 1rem;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
        }

        nav a {
            color: #f5e6d3;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: background 0.3s;
            font-weight: bold;
        }

        nav a:hover {
            background: #8B4513;
        }

        .container {
            max-width: 1400px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .section {
            background: white;
            margin-bottom: 2rem;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .section h2 {
            color: #8B4513;
            border-bottom: 3px solid #DAA520;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }

        .section h3 {
            color: #654321;
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .gallery-item {
            background: #faf8f5;
            border: 2px solid #d4a574;
            border-radius: 8px;
            padding: 1.5rem;
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }

        .gallery-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(139, 69, 19, 0.3);
        }

        .gallery-item img {
            width: 100%;
            height: 250px;
            object-fit: contain;
            border-radius: 5px;
            background: white;
            padding: 1rem;
        }

        .gallery-item h4 {
            color: #8B4513;
            margin: 1rem 0 0.5rem 0;
            font-size: 1.2rem;
        }

        .gallery-item p {
            color: #5d4037;
            font-size: 0.9rem;
            margin: 0.3rem 0;
        }

        .badge {
            display: inline-block;
            background: #DAA520;
            color: white;
            padding: 0.2rem 0.6rem;
            border-radius: 12px;
            font-size: 0.8rem;
            margin: 0.2rem;
            font-weight: bold;
        }

        .badge.grade-3 { background: #4CAF50; }
        .badge.grade-4 { background: #FF9800; }
        .badge.grade-5 { background: #F44336; }
        .badge.deity { background: #9C27B0; }
        .badge.artifact { background: #2196F3; }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .stat-box {
            background: linear-gradient(135deg, #8B4513 0%, #A0522D 100%);
            color: white;
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .stat-box h3 {
            font-size: 2.5rem;
            margin: 0;
            color: #FFD700;
        }

        .stat-box p {
            margin-top: 0.5rem;
            opacity: 0.9;
        }

        .artifact-list {
            display: grid;
            gap: 1.5rem;
        }

        .artifact-card {
            background: #faf8f5;
            border-left: 4px solid #8B4513;
            padding: 1.5rem;
            border-radius: 5px;
            transition: background 0.3s;
        }

        .artifact-card:hover {
            background: #f5f0eb;
        }

        .artifact-card h4 {
            color: #8B4513;
            margin-bottom: 0.5rem;
        }

        .artifact-card .meta {
            color: #666;
            font-size: 0.9rem;
            margin: 0.3rem 0;
        }

        .artifact-card a {
            color: #2196F3;
            text-decoration: none;
            font-weight: bold;
        }

        .artifact-card a:hover {
            text-decoration: underline;
        }

        .deity-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .deity-card {
            background: linear-gradient(135deg, #fff8e1 0%, #ffe082 100%);
            border: 3px solid #DAA520;
            border-radius: 10px;
            padding: 1.5rem;
            text-align: center;
        }

        .deity-card img {
            width: 100%;
            max-width: 300px;
            height: auto;
            margin: 1rem auto;
            display: block;
        }

        .deity-card h3 {
            color: #8B4513;
            margin: 1rem 0;
        }

        .deity-card p {
            color: #5d4037;
            margin: 0.5rem 0;
        }

        footer {
            background: #654321;
            color: #f5e6d3;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }

        .filter-bar {
            background: #f5e6d3;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            align-items: center;
        }

        .filter-bar label {
            font-weight: bold;
            color: #654321;
        }

        .filter-bar select, .filter-bar input {
            padding: 0.5rem;
            border: 2px solid #8B4513;
            border-radius: 5px;
            background: white;
            color: #3e2723;
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.8);
            justify-content: center;
            align-items: center;
        }

        .modal-content {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            max-width: 800px;
            max-height: 90vh;
            overflow-y: auto;
            position: relative;
        }

        .modal-close {
            position: absolute;
            top: 1rem;
            right: 1rem;
            font-size: 2rem;
            cursor: pointer;
            color: #8B4513;
        }

        @media (max-width: 768px) {
            .gallery {
                grid-template-columns: 1fr;
            }

            header h1 {
                font-size: 1.8rem;
            }

            nav ul {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>

<header>
    <h1>🏛️ Mesopotamian Sacred Geometry</h1>
    <p>Complete Visual Gallery & Curriculum Resource</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">Grades 3-5 • 40+ Artifacts • 12 Geometric Elements • 7 Deities</p>
</header>

<nav>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#shapes">Geometric Shapes</a></li>
        <li><a href="#deities">Deities</a></li>
        <li><a href="#artifacts">Artifacts</a></li>
        <li><a href="#patterns">Patterns</a></li>
        <li><a href="#constructions">Constructions</a></li>
        <li><a href="#statistics">Statistics</a></li>
    </ul>
</nav>

<div class="container">
"""

        # Overview Section
        html += self.generate_overview_section()

        # Statistics Section
        html += self.generate_statistics_section()

        # Geometric Shapes Section
        html += self.generate_shapes_section()

        # Deities Section
        html += self.generate_deities_section()

        # Artifacts Section
        html += self.generate_artifacts_section()

        # Patterns Section
        html += self.generate_patterns_section()

        # Tools & Technology Section
        html += self.generate_tools_section()

        html += """
</div>

<footer>
    <p><strong>Mesopotamian Sacred Geometry Curriculum</strong></p>
    <p>Grades 3-5 Differentiated Learning • HOW/WHY/WHAT IF Framework</p>
    <p style="margin-top: 1rem; font-size: 0.9rem;">
        © 2024 • Educational Use • All museum links provided for reference
    </p>
</footer>

<script>
    // Smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Gallery item interactions
    document.querySelectorAll('.gallery-item').forEach(item => {
        item.addEventListener('click', function() {
            this.style.transform = 'scale(1.05)';
            setTimeout(() => {
                this.style.transform = '';
            }, 300);
        });
    });

    console.log('Mesopotamian Sacred Geometry Gallery Loaded ✓');
</script>

</body>
</html>
"""

        # Write HTML file
        with open(self.output_file, 'w') as f:
            f.write(html)

        print(f"✓ Created: {self.output_file}")

    def generate_overview_section(self):
        """Generate overview section"""
        return """
    <section id="overview" class="section">
        <h2>📚 Curriculum Overview</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 1.5rem;">
            This comprehensive visual gallery contains all geometric elements, deity symbols, artifacts,
            and educational resources for the <strong>Mesopotamian Sacred Geometry</strong> curriculum.
            Each element includes simple-to-complex progressions aligned with grades 3-5.
        </p>

        <div style="background: #fff8e1; padding: 1.5rem; border-radius: 8px; border-left: 4px solid #DAA520;">
            <h3 style="color: #8B4513; margin-top: 0;">🎯 Learning Framework</h3>
            <ul style="margin-left: 2rem; color: #5d4037;">
                <li><strong>HOW:</strong> Construction techniques, measurement methods, material analysis</li>
                <li><strong>WHY:</strong> Symbolic meanings, cultural significance, divine connections</li>
                <li><strong>WHAT IF:</strong> Creative applications, cross-cultural comparisons, innovations</li>
            </ul>
        </div>
    </section>
"""

    def generate_statistics_section(self):
        """Generate statistics section"""
        total_shapes = len(self.data['geometric_elements'])
        total_artifacts = len(self.data['artifacts'])
        total_deities = len(self.data['deities'])
        total_patterns = len(self.data.get('patterns_decorative', []))

        return f"""
    <section id="statistics" class="section">
        <h2>📊 Content Statistics</h2>

        <div class="stats-grid">
            <div class="stat-box">
                <h3>12</h3>
                <p>Major Sections</p>
            </div>
            <div class="stat-box">
                <h3>{total_shapes}</h3>
                <p>Geometric Elements</p>
            </div>
            <div class="stat-box">
                <h3>{total_artifacts}</h3>
                <p>Museum Artifacts</p>
            </div>
            <div class="stat-box">
                <h3>{total_deities}</h3>
                <p>Deities</p>
            </div>
            <div class="stat-box">
                <h3>40+</h3>
                <p>SVG Graphics</p>
            </div>
            <div class="stat-box">
                <h3>3</h3>
                <p>Grade Levels</p>
            </div>
        </div>

        <div style="margin-top: 2rem; background: #f5f0eb; padding: 1.5rem; border-radius: 8px;">
            <h3>✅ Complete Features</h3>
            <ul style="margin-left: 2rem; color: #5d4037; line-height: 2;">
                <li>✓ Simple → Complex progressions for all shapes</li>
                <li>✓ Mathematical formulas with visual demonstrations</li>
                <li>✓ Technology connections for each element</li>
                <li>✓ Grade 3-5 differentiation built in</li>
                <li>✓ HOW/WHY/WHAT IF framework integrated</li>
                <li>✓ Museum artifact citations with URLs</li>
                <li>✓ Deity connections and symbolism</li>
                <li>✓ Cross-cultural comparisons</li>
            </ul>
        </div>
    </section>
"""

    def generate_shapes_section(self):
        """Generate geometric shapes gallery"""
        html = """
    <section id="shapes" class="section">
        <h2>📐 Geometric Elements</h2>
        <p>All 12 geometric elements with simple → intermediate → complex progressions</p>

        <div class="gallery">
"""

        shape_categories = {
            "Primary Shapes": ["circle", "triangle", "square"],
            "Crescent Forms": ["crescent"],
            "Star Forms": ["star_8", "star_6", "star_12"],
            "Pattern Forms": ["zigzag", "spiral"],
            "3D Forms": ["cylinder", "cone"],
            "Composite": ["composite"]
        }

        for category, shape_ids in shape_categories.items():
            for elem in self.data['geometric_elements']:
                if elem['id'] in shape_ids:
                    deity_names = ', '.join(elem['deity_connections'])
                    progressions = len(elem['progressions'])

                    html += f"""
            <div class="gallery-item">
                <img src="svg_outputs/shapes/{elem['id']}_01_simple.svg" alt="{elem['name']}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'200\\' height=\\'200\\'%3E%3Crect width=\\'200\\' height=\\'200\\' fill=\\'%23f0f0f0\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dy=\\'.3em\\' fill=\\'%23999\\' font-family=\\'Arial\\' font-size=\\'14\\'%3E{elem['name']}%3C/text%3E%3C/svg%3E'">
                <h4>{elem['name']}</h4>
                <p><strong>Belief:</strong> {elem['belief']}</p>
                <p><strong>Deity:</strong> {deity_names}</p>
                <div style="margin-top: 0.5rem;">
                    <span class="badge">{progressions} Progressions</span>
                    <span class="badge deity">{len(elem['deity_connections'])} Deities</span>
                </div>
            </div>
"""

        html += """
        </div>
    </section>
"""
        return html

    def generate_deities_section(self):
        """Generate deities section"""
        html = """
    <section id="deities" class="section">
        <h2>🏛️ Mesopotamian Deities</h2>
        <p>Seven major deities with their geometric associations and symbols</p>

        <div class="deity-grid">
"""

        for deity in self.data['deities']:
            symbols = ', '.join(deity['symbols'])
            sources = len(deity['image_sources'])

            html += f"""
            <div class="deity-card">
                <img src="svg_outputs/deities/{deity['id']}.svg" alt="{deity['name']}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'300\\' height=\\'400\\'%3E%3Crect width=\\'300\\' height=\\'400\\' fill=\\'%23f5e6d3\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dy=\\'.3em\\' fill=\\'%238B4513\\' font-family=\\'Arial\\' font-size=\\'20\\'%3E{deity['name']}%3C/text%3E%3C/svg%3E'">
                <h3>{deity['name']}</h3>
                <p><strong>Role:</strong> {deity['role']}</p>
                <p><strong>Symbols:</strong> {symbols}</p>
                <p><strong>Geometry:</strong> {deity['geometric_association'].replace('_', '-').title()}</p>
                <div style="margin-top: 1rem;">
                    <span class="badge artifact">{sources} Image Sources</span>
                </div>
            </div>
"""

        html += """
        </div>
    </section>
"""
        return html

    def generate_artifacts_section(self):
        """Generate artifacts section"""
        html = """
    <section id="artifacts" class="section">
        <h2>🏺 Museum Artifacts</h2>
        <p>40+ artifacts from major museums with citations and educational context</p>

        <div class="filter-bar">
            <label for="museum-filter">Filter by Museum:</label>
            <select id="museum-filter" onchange="filterArtifacts()">
                <option value="all">All Museums</option>
"""

        # Get unique museums
        museums = sorted(set(a['museum'] for a in self.data['artifacts']))
        for museum in museums:
            html += f'                <option value="{museum}">{museum}</option>\n'

        html += """
            </select>

            <label for="period-filter">Filter by Period:</label>
            <select id="period-filter" onchange="filterArtifacts()">
                <option value="all">All Periods</option>
"""

        # Get unique periods
        periods = sorted(set(a['period'] for a in self.data['artifacts']))
        for period in periods:
            html += f'                <option value="{period}">{period}</option>\n'

        html += """
            </select>
        </div>

        <div class="artifact-list">
"""

        for artifact in self.data['artifacts']:
            geom = ', '.join(artifact['geometric_elements'])
            deities = ', '.join(artifact['deity_connections']) if artifact['deity_connections'] else 'None'

            html += f"""
            <div class="artifact-card" data-museum="{artifact['museum']}" data-period="{artifact['period']}">
                <h4>{artifact['name']}</h4>
                <p class="meta"><strong>Museum:</strong> {artifact['museum']} • <strong>Accession:</strong> {artifact['accession']}</p>
                <p class="meta"><strong>Period:</strong> {artifact['period']} • <strong>Location:</strong> {artifact['location']}</p>
                <p style="margin: 0.8rem 0;">{artifact['description']}</p>
                <p class="meta"><strong>Geometric Elements:</strong> {geom}</p>
                <p class="meta"><strong>Deity Connections:</strong> {deities}</p>
                <p style="margin-top: 0.8rem;"><strong>Educational Value:</strong> {artifact['educational_value']}</p>
                <p style="margin-top: 0.5rem;"><a href="{artifact['url']}" target="_blank">→ View at Museum</a></p>
            </div>
"""

        html += """
        </div>
    </section>

<script>
function filterArtifacts() {
    const museumFilter = document.getElementById('museum-filter').value;
    const periodFilter = document.getElementById('period-filter').value;
    const artifacts = document.querySelectorAll('.artifact-card');

    artifacts.forEach(artifact => {
        const museum = artifact.getAttribute('data-museum');
        const period = artifact.getAttribute('data-period');

        const museumMatch = museumFilter === 'all' || museum === museumFilter;
        const periodMatch = periodFilter === 'all' || period === periodFilter;

        if (museumMatch && periodMatch) {
            artifact.style.display = 'block';
        } else {
            artifact.style.display = 'none';
        }
    });
}
</script>
"""
        return html

    def generate_patterns_section(self):
        """Generate patterns section"""
        html = """
    <section id="patterns" class="section">
        <h2>🎨 Decorative Patterns</h2>
        <p>Traditional Mesopotamian patterns found on artifacts and architecture</p>

        <div class="gallery">
"""

        if 'patterns_decorative' in self.data:
            for pattern in self.data['patterns_decorative']:
                html += f"""
            <div class="gallery-item">
                <img src="svg_outputs/patterns/{pattern['id']}.svg" alt="{pattern['name']}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'200\\' height=\\'200\\'%3E%3Crect width=\\'200\\' height=\\'200\\' fill=\\'%23f0f0f0\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dy=\\'.3em\\' fill=\\'%23999\\' font-family=\\'Arial\\' font-size=\\'14\\'%3E{pattern['name']}%3C/text%3E%3C/svg%3E'">
                <h4>{pattern['name']}</h4>
                <p>{pattern['description']}</p>
                <div style="margin-top: 0.5rem;">
                    <span class="badge">{pattern['complexity'].title()}</span>
                </div>
            </div>
"""

        html += """
        </div>
    </section>
"""
        return html

    def generate_tools_section(self):
        """Generate tools and technology section"""
        html = """
    <section id="constructions" class="section">
        <h2>🔧 Tools & Technology</h2>
        <p>Mesopotamian inventions and their geometric principles</p>

        <div class="gallery">
"""

        if 'tools_technology' in self.data:
            for tool in self.data['tools_technology']:
                geom = ', '.join(tool['geometric_principles'])
                html += f"""
            <div class="gallery-item">
                <img src="svg_outputs/tools/{tool['id']}.svg" alt="{tool['name']}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'200\\' height=\\'200\\'%3E%3Crect width=\\'200\\' height=\\'200\\' fill=\\'%23f0f0f0\\'/%3E%3Ctext x=\\'50%25\\' y=\\'50%25\\' text-anchor=\\'middle\\' dy=\\'.3em\\' fill=\\'%23999\\' font-family=\\'Arial\\' font-size=\\'14\\'%3E{tool['name']}%3C/text%3E%3C/svg%3E'">
                <h4>{tool['name']}</h4>
                <p>{tool['description']}</p>
                <p class="meta"><strong>Geometry:</strong> {geom}</p>
                <div style="margin-top: 0.5rem;">
                    <span class="badge grade-{tool['grade_level']}">Grade {tool['grade_level']}</span>
                </div>
            </div>
"""

        html += """
        </div>
    </section>
"""
        return html


def main():
    """Main execution"""
    print("\n" + "=" * 70)
    print("GENERATING HTML GALLERY")
    print("=" * 70)
    print()

    generator = HTMLGalleryGenerator()
    generator.generate_html()

    print()
    print("✅ HTML Gallery created successfully!")
    print("   Open 'visual_gallery.html' in your web browser")
    print("=" * 70)


if __name__ == "__main__":
    main()
