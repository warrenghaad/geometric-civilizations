#!/usr/bin/env python3
"""
E-Textbook Generator - Geometric Civilizations
Generates interactive HTML e-textbook from lesson JSONs (SSOT)
"""

import json
from pathlib import Path
from typing import Dict, List
from datetime import datetime


class ETextbookGenerator:
    def __init__(self, lessons_dir: str, output_path: str, design_system_path: str):
        self.lessons_dir = Path(lessons_dir)
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(design_system_path, 'r') as f:
            self.design_system = json.load(f)

    def load_all_lessons(self) -> Dict[int, List[Dict]]:
        """Load all lesson JSONs organized by grade"""
        lessons_by_grade = {3: [], 4: [], 5: []}

        for lesson_file in sorted(self.lessons_dir.glob("G*.json")):
            with open(lesson_file, 'r') as f:
                lesson = json.load(f)
                grade = lesson['metadata']['grade']
                lessons_by_grade[grade].append(lesson)

        # Sort by lesson number
        for grade in lessons_by_grade:
            lessons_by_grade[grade].sort(key=lambda x: x['metadata']['lessonNumber'])

        return lessons_by_grade

    def generate_css(self) -> str:
        """Generate CSS from design system"""
        grade3_palette = self.design_system['colorPalettes']['grade3']
        grade4_palette = self.design_system['colorPalettes']['grade4']
        grade5_palette = self.design_system['colorPalettes']['grade5']
        civ_palette = self.design_system['colorPalettes']['civilization']

        typography = self.design_system['typography']
        spacing = self.design_system['spacing']

        css = f'''
:root {{
  /* Grade 3 Colors */
  --g3-primary: {grade3_palette['primary']};
  --g3-secondary: {grade3_palette['secondary']};
  --g3-accent: {grade3_palette['accent']};

  /* Grade 4 Colors */
  --g4-primary: {grade4_palette['primary']};
  --g4-secondary: {grade4_palette['secondary']};
  --g4-accent: {grade4_palette['accent']};

  /* Grade 5 Colors */
  --g5-primary: {grade5_palette['primary']};
  --g5-secondary: {grade5_palette['secondary']};
  --g5-accent: {grade5_palette['accent']};

  /* Civilization Colors */
  --civ-mesopotamia: {civ_palette['mesopotamia']};
  --civ-egypt: {civ_palette['egypt']};
  --civ-greece: {civ_palette['greece']};
  --civ-india: {civ_palette['india']};
  --civ-islamic: {civ_palette['islamic']};
  --civ-china: {civ_palette['china']};
  --civ-renaissance: {civ_palette['renaissance']};

  /* Typography */
  --font-primary: {typography['fontFamilies']['primary']};
  --font-headings: {typography['fontFamilies']['headings']};
  --font-display: {typography['fontFamilies']['display']};

  /* Spacing */
  --space-sm: {spacing['sm']};
  --space-md: {spacing['md']};
  --space-lg: {spacing['lg']};
  --space-xl: {spacing['xl']};
  --space-2xl: {spacing['2xl']};
}}

* {{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}}

body {{
  font-family: var(--font-primary);
  line-height: 1.6;
  color: #1a202c;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}}

.container {{
  max-width: 1400px;
  margin: 0 auto;
  padding: var(--space-xl);
}}

/* Header */
.header {{
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: var(--space-2xl);
  text-align: center;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}}

.header h1 {{
  font-family: var(--font-display);
  font-size: 3em;
  margin-bottom: var(--space-md);
  text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}}

.header p {{
  font-size: 1.2em;
  opacity: 0.95;
}}

/* Navigation */
.nav {{
  background: white;
  padding: var(--space-lg);
  margin: var(--space-xl) 0;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  position: sticky;
  top: 20px;
  z-index: 100;
}}

.grade-tabs {{
  display: flex;
  gap: var(--space-md);
  margin-bottom: var(--space-lg);
  border-bottom: 2px solid #e2e8f0;
}}

.grade-tab {{
  padding: var(--space-md) var(--space-lg);
  background: none;
  border: none;
  font-size: 1.1em;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  border-bottom: 3px solid transparent;
}}

.grade-tab.active {{
  border-bottom-color: var(--g4-primary);
  color: var(--g4-primary);
}}

.lesson-list {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: var(--space-sm);
}}

.lesson-link {{
  padding: var(--space-sm);
  background: #f7fafc;
  border-radius: 6px;
  text-align: center;
  text-decoration: none;
  color: #2d3748;
  font-weight: 500;
  transition: all 0.2s;
}}

.lesson-link:hover {{
  background: #e2e8f0;
  transform: translateY(-2px);
}}

/* Lesson Content */
.lesson {{
  background: white;
  border-radius: 16px;
  padding: var(--space-2xl);
  margin: var(--space-xl) 0;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}}

.lesson-header {{
  border-left: 4px solid var(--g4-primary);
  padding-left: var(--space-lg);
  margin-bottom: var(--space-xl);
}}

.lesson-id {{
  font-size: 0.9em;
  color: #718096;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 1px;
}}

.lesson-title {{
  font-family: var(--font-display);
  font-size: 2.5em;
  color: #1a202c;
  margin: var(--space-sm) 0;
}}

.lesson-subtitle {{
  font-size: 1.2em;
  color: #4a5568;
}}

.lesson-meta {{
  display: flex;
  gap: var(--space-lg);
  flex-wrap: wrap;
  margin-top: var(--space-md);
  padding-top: var(--space-md);
  border-top: 1px solid #e2e8f0;
}}

.meta-item {{
  display: flex;
  align-items: center;
  gap: var(--space-sm);
}}

.meta-label {{
  font-weight: 600;
  color: #718096;
}}

.meta-value {{
  color: #2d3748;
}}

.civ-badge {{
  display: inline-block;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 600;
  color: white;
}}

.civ-mesopotamia {{ background: var(--civ-mesopotamia); }}
.civ-egypt {{ background: var(--civ-egypt); }}
.civ-greece {{ background: var(--civ-greece); }}
.civ-india {{ background: var(--civ-india); }}
.civ-islamic {{ background: var(--civ-islamic); }}
.civ-china {{ background: var(--civ-china); }}

/* Lesson Sections */
.lesson-section {{
  margin: var(--space-2xl) 0;
  padding: var(--space-xl);
  border-radius: 12px;
  background: #f7fafc;
}}

.section-title {{
  font-family: var(--font-headings);
  font-size: 1.8em;
  color: #2d3748;
  margin-bottom: var(--space-lg);
  display: flex;
  align-items: center;
  gap: var(--space-md);
}}

.section-icon {{
  font-size: 1.2em;
}}

.section-content {{
  line-height: 1.8;
}}

/* Artifacts */
.artifacts-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: var(--space-xl);
  margin-top: var(--space-lg);
}}

.artifact-card {{
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s;
}}

.artifact-card:hover {{
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15);
}}

.artifact-image {{
  width: 100%;
  height: 300px;
  object-fit: cover;
  background: #e2e8f0;
}}

.artifact-info {{
  padding: var(--space-lg);
}}

.artifact-title {{
  font-size: 1.3em;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: var(--space-sm);
}}

.artifact-meta {{
  font-size: 0.9em;
  color: #718096;
  margin-bottom: var(--space-md);
}}

.artifact-overlays {{
  margin-top: var(--space-md);
}}

.overlay-tag {{
  display: inline-block;
  padding: 4px 8px;
  background: #edf2f7;
  border-radius: 4px;
  font-size: 0.85em;
  margin: 2px;
}}

/* Activities */
.activity {{
  background: white;
  border-radius: 8px;
  padding: var(--space-lg);
  margin: var(--space-md) 0;
}}

.activity-title {{
  font-size: 1.3em;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: var(--space-md);
}}

.procedure {{
  list-style: none;
  counter-reset: step-counter;
}}

.procedure li {{
  counter-increment: step-counter;
  padding-left: var(--space-xl);
  margin: var(--space-sm) 0;
  position: relative;
}}

.procedure li::before {{
  content: counter(step-counter);
  position: absolute;
  left: 0;
  top: 0;
  width: 24px;
  height: 24px;
  background: var(--g4-primary);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.85em;
  font-weight: 600;
}}

/* Bridge */
.bridge {{
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: var(--space-2xl);
  border-radius: 12px;
  margin: var(--space-2xl) 0;
}}

.bridge-title {{
  font-size: 1.8em;
  margin-bottom: var(--space-lg);
}}

.bridge-connection {{
  margin: var(--space-lg) 0;
  padding: var(--space-lg);
  background: rgba(255,255,255,0.1);
  border-radius: 8px;
}}

.bridge-label {{
  font-weight: 600;
  font-size: 1.1em;
  margin-bottom: var(--space-sm);
}}

/* Print Styles */
@media print {{
  .nav, .grade-tabs {{ display: none; }}
  .lesson {{ page-break-inside: avoid; }}
  body {{ background: white; }}
}}

/* Responsive */
@media (max-width: 768px) {{
  .container {{ padding: var(--space-md); }}
  .lesson-title {{ font-size: 1.8em; }}
  .artifacts-grid {{ grid-template-columns: 1fr; }}
  .lesson-meta {{ flex-direction: column; gap: var(--space-sm); }}
}}
'''
        return css

    def generate_lesson_html(self, lesson: Dict) -> str:
        """Generate HTML for a single lesson"""
        metadata = lesson['metadata']
        civilization = metadata['civilization'].lower().replace(' ', '-')

        html = f'''
<div class="lesson" id="{lesson['lessonId']}">
  <div class="lesson-header">
    <div class="lesson-id">{lesson['lessonId']}</div>
    <h2 class="lesson-title">{metadata['mathConcept']}</h2>
    <div class="lesson-subtitle">{metadata['geometricConcept']}</div>

    <div class="lesson-meta">
      <div class="meta-item">
        <span class="meta-label">Week:</span>
        <span class="meta-value">{metadata['weekNumber']}</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Duration:</span>
        <span class="meta-value">{metadata['duration']} min</span>
      </div>
      <div class="meta-item">
        <span class="meta-label">Civilization:</span>
        <span class="civ-badge civ-{civilization}">{metadata['civilization']}</span>
      </div>
    </div>
  </div>

  <!-- SEL -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">❤️</span> Social-Emotional Learning</h3>
    <div class="section-content">
      <p><strong>Prompt:</strong> {lesson['sel']['prompt']}</p>
      <p><strong>Duration:</strong> {lesson['sel']['duration']} minutes</p>
      <p><strong>Materials:</strong> {', '.join(lesson['sel']['materials'])}</p>
    </div>
  </div>

  <!-- Hook -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">🎣</span> Hook</h3>
    <div class="section-content">
      <p><strong>Character:</strong> {lesson['hook']['character']['name']} – {lesson['hook']['character']['role']}</p>
      <p>{lesson['hook']['narrative']}</p>
      <p><strong>Question:</strong> {lesson['hook']['questionPrompt']}</p>
    </div>
  </div>

  <!-- Myth -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">📖</span> Myth: {lesson['myth']['title']}</h3>
    <div class="section-content">
      <p>{lesson['myth']['summary']}</p>
    </div>
  </div>

  <!-- Artifacts -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">🏺</span> Cultural Artifacts</h3>
    <div class="artifacts-grid">
'''

        for artifact in lesson.get('artifacts', []):
            html += f'''
      <div class="artifact-card">
        <img src="{artifact['imageUrl']}" alt="{artifact['title']}" class="artifact-image" loading="lazy">
        <div class="artifact-info">
          <div class="artifact-title">{artifact['title']}</div>
          <div class="artifact-meta">{artifact['civilization']} – {artifact.get('period', 'Date TBD')}</div>
          <p>{artifact.get('teachingNotes', '')}</p>
          <div class="artifact-overlays">
            {' '.join([f'<span class="overlay-tag">{o["type"]}</span>' for o in artifact.get('overlays', [])])}
          </div>
        </div>
      </div>
'''

        html += '''
    </div>
  </div>

  <!-- Math Activity -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">🔢</span> Math Activity</h3>
    <div class="activity">
'''

        html += f'''
      <div class="activity-title">{lesson['mathActivity']['title']}</div>
      <p><strong>Objective:</strong> {lesson['mathActivity']['objective']}</p>
      <p><strong>Duration:</strong> {lesson['mathActivity']['duration']} minutes</p>
      <ol class="procedure">
'''

        for step in lesson['mathActivity']['procedure']:
            html += f'        <li>{step}</li>\n'

        html += '''
      </ol>
    </div>
  </div>

  <!-- Art Activity -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">🎨</span> Art Activity</h3>
    <div class="activity">
'''

        html += f'''
      <div class="activity-title">{lesson['artActivity']['title']}</div>
      <p><strong>Technique:</strong> {lesson['artActivity']['technique']}</p>
      <p><strong>Duration:</strong> {lesson['artActivity']['duration']} minutes</p>
      <ol class="procedure">
'''

        for step in lesson['artActivity']['procedure']:
            html += f'        <li>{step}</li>\n'

        html += '''
      </ol>
    </div>
  </div>

  <!-- Bridge -->
  <div class="bridge">
    <h3 class="bridge-title">🌉 Bridge: Making Connections</h3>
'''

        html += f'''
    <div class="bridge-connection">
      <div class="bridge-label">Math → Art</div>
      <p>{lesson['bridge']['mathToArt']}</p>
    </div>
    <div class="bridge-connection">
      <div class="bridge-label">Art → Geometry</div>
      <p>{lesson['bridge']['artToGeometry']}</p>
    </div>
    <div class="bridge-connection">
      <div class="bridge-label">Synthesis</div>
      <p>{lesson['bridge']['synthesis']}</p>
    </div>
  </div>

  <!-- Exit -->
  <div class="lesson-section">
    <h3 class="section-title"><span class="section-icon">🚪</span> Exit Reflection</h3>
    <div class="section-content">
      <p><strong>Prompt:</strong> {lesson['exit']['prompt']}</p>
      <p><strong>Format:</strong> {lesson['exit']['format']}</p>
    </div>
  </div>
</div>
'''

        return html

    def generate_etextbook(self):
        """Generate complete interactive e-textbook"""
        lessons_by_grade = self.load_all_lessons()

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Geometric Civilizations - Interactive Curriculum</title>
  <style>
{self.generate_css()}
  </style>
</head>
<body>
  <div class="header">
    <h1>🔺 Geometric Civilizations 🔺</h1>
    <p>Quarter 2 Pilot: Grades 3–5 Integrated Geometry–Myth–Art Curriculum</p>
    <p>54 lessons total | 18 per grade | Generated {datetime.now().strftime("%Y-%m-%d")}</p>
  </div>

  <div class="container">
    <nav class="nav">
      <div class="grade-tabs">
        <button class="grade-tab active" onclick="showGrade(3)">Grade 3</button>
        <button class="grade-tab" onclick="showGrade(4)">Grade 4</button>
        <button class="grade-tab" onclick="showGrade(5)">Grade 5</button>
      </div>

      <div id="lesson-nav-3" class="lesson-list">
'''

        # Generate navigation for Grade 3
        for lesson in lessons_by_grade[3]:
            html += f'        <a href="#{lesson["lessonId"]}" class="lesson-link">{lesson["lessonId"]}</a>\n'

        html += '''
      </div>

      <div id="lesson-nav-4" class="lesson-list" style="display: none;">
'''

        # Generate navigation for Grade 4
        for lesson in lessons_by_grade[4]:
            html += f'        <a href="#{lesson["lessonId"]}" class="lesson-link">{lesson["lessonId"]}</a>\n'

        html += '''
      </div>

      <div id="lesson-nav-5" class="lesson-list" style="display: none;">
'''

        # Generate navigation for Grade 5
        for lesson in lessons_by_grade[5]:
            html += f'        <a href="#{lesson["lessonId"]}" class="lesson-link">{lesson["lessonId"]}</a>\n'

        html += '''
      </div>
    </nav>

    <!-- Grade 3 Lessons -->
    <div id="grade-3-lessons">
'''

        for lesson in lessons_by_grade[3]:
            html += self.generate_lesson_html(lesson)

        html += '''
    </div>

    <!-- Grade 4 Lessons -->
    <div id="grade-4-lessons" style="display: none;">
'''

        for lesson in lessons_by_grade[4]:
            html += self.generate_lesson_html(lesson)

        html += '''
    </div>

    <!-- Grade 5 Lessons -->
    <div id="grade-5-lessons" style="display: none;">
'''

        for lesson in lessons_by_grade[5]:
            html += self.generate_lesson_html(lesson)

        html += '''
    </div>
  </div>

  <script>
    function showGrade(grade) {
      // Hide all grade content
      for (let g = 3; g <= 5; g++) {
        document.getElementById(`grade-${g}-lessons`).style.display = 'none';
        document.getElementById(`lesson-nav-${g}`).style.display = 'none';
      }

      // Remove active class from all tabs
      document.querySelectorAll('.grade-tab').forEach(tab => {
        tab.classList.remove('active');
      });

      // Show selected grade
      document.getElementById(`grade-${grade}-lessons`).style.display = 'block';
      document.getElementById(`lesson-nav-${grade}`).style.display = 'grid';

      // Add active class to selected tab
      event.target.classList.add('active');

      // Scroll to top
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Smooth scroll for lesson links
    document.querySelectorAll('.lesson-link').forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  </script>
</body>
</html>
'''

        with open(self.output_path, 'w') as f:
            f.write(html)

        print(f"✓ E-textbook generated: {self.output_path}")
        print(f"✓ Total lessons: {sum(len(lessons) for lessons in lessons_by_grade.values())}")


def main():
    root_dir = Path(__file__).parent.parent
    lessons_dir = root_dir / "lessons"
    output_path = root_dir / "etextbook" / "index.html"
    design_system_path = root_dir / "schemas" / "design_system.json"

    generator = ETextbookGenerator(
        lessons_dir=str(lessons_dir),
        output_path=str(output_path),
        design_system_path=str(design_system_path)
    )

    generator.generate_etextbook()


if __name__ == "__main__":
    main()
