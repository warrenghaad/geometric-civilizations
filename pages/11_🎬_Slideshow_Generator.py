import streamlit as st
import sqlite3
import os
import json
import base64
import glob as glob_module
import re

st.set_page_config(page_title="Slideshow Generator", page_icon="🎬", layout="wide")

MESO_DB_PATH = "attached_assets/meso_curriculum/MESO_Curriculum_2025-01-05/05_Database_Files/meso_ssot_complete.db"
MESO_IMAGES_DIR = "attached_assets/meso_curriculum/MESO_Curriculum_2025-01-05/03_Image_Download"
LESSON_CONTENT_DIR = "attached_assets/meso_curriculum/MESO_Curriculum_2025-01-05/06_Lesson_Content"

ARTIFACT_DATA = {
    "shamash_tablet": {
        "name": "Shamash Tablet (Sippar Tablet)",
        "date": "9th century BCE",
        "location": "British Museum, London",
        "description": "Stone tablet showing the sun god Shamash seated on his throne, receiving King Nabu-apla-iddina. Shamash holds measuring tools and his sun disk is prominently displayed above.",
        "geometric_connection": "The sun disk is a perfect circle with radiating lines (rays), demonstrating radial symmetry. The rays divide the circle into equal angular sections, showing how ancient artists understood angular division.",
        "image_file": "shamash_tablet_placeholder.jpg",
        "overlay_files": ["shamash_tablet_overlay2_rays.jpg"],
    },
    "ubaid_bowl": {
        "name": "Ubaid Period Painted Bowl",
        "date": "5500-4000 BCE (Ubaid Period)",
        "location": "Archaeological Collections",
        "description": "Painted ceramic bowl from the Ubaid period featuring concentric circles and radiating lines. Interior decoration shows sophisticated understanding of circular geometry.",
        "geometric_connection": "Multiple concentric circles demonstrate understanding of center point, radius, and diameter. The rings divide space into approximately equal visual areas. 8-fold rotational symmetry with 8 axes of mirror symmetry.",
        "image_file": "ubaid_bowl_placeholder.jpg",
        "overlay_files": ["ubaid_bowl_overlay1_circles.jpg", "ubaid_bowl_overlay2_rays.jpg"],
    },
    "ur_rosette": {
        "name": "Gold Rosette from Royal Cemetery of Ur",
        "date": "2600-2500 BCE (Early Dynastic III)",
        "location": "Penn Museum, Philadelphia (B17711)",
        "description": "Spectacular gold ornament from Queen Pu-abi's burial. 8-petal flower design hammered from gold sheet, originally part of an elaborate headdress. 7.5 cm diameter.",
        "geometric_connection": "8 identical petals arranged radially around a central circle demonstrate perfect 8-fold rotational symmetry. Each petal separated by 45 degrees (360/8). Shows ancient goldsmith's mastery of angular division and radial design.",
        "image_file": "ur_rosette_placeholder.jpg",
        "overlay_files": ["ur_rosette_overlay1_structure.jpg", "ur_rosette_overlay2_rays.jpg"],
    },
    "cylinder_seal": {
        "name": "Cylinder Seal with Sun God Motif",
        "date": "c. 2300-2000 BCE (Akkadian Period)",
        "location": "Various Museum Collections",
        "description": "Small stone cylinder carved with intricate scenes of the sun god. When rolled across wet clay, it creates a continuous impression featuring circular sun disks and divine figures.",
        "geometric_connection": "The cylinder itself is a 3D circle (circular cross-section). The sun disk impression demonstrates that ancient carvers could create precise circles at miniature scale. Rolling creates a linear transformation of circular design.",
        "image_file": "cylinder_seal_placeholder.jpg",
        "overlay_files": ["cylinder_seal_overlay_rays.jpg"],
    },
    "stone_weight": {
        "name": "Stone Circular Weight",
        "date": "c. 2000 BCE",
        "location": "British Museum, London",
        "description": "Precisely ground stone weight in near-perfect circular form with cuneiform inscription indicating its mass. Used in trade and commerce.",
        "geometric_connection": "Demonstrates Mesopotamians could create near-perfect circles through careful grinding. Precision assessment shows radius variation of less than 1%, achieving 99%+ circular accuracy without modern tools.",
        "image_file": "stone_weight_placeholder.jpg",
        "overlay_files": ["stone_weight_overlay_precision.jpg"],
    },
}

MYTH_SENTENCES = [
    {"num": 1, "text": "The sun wakes over the river, a bright round face that comes back each day in a steady way.", "image_key": "myth_01_sun_river", "geometric_note": "Circle: The sun's form as a perfect disk with no beginning or end"},
    {"num": 2, "text": "In the town, children gather around a round loaf on a round plate.", "image_key": "myth_02_plate_loaf", "geometric_note": "Concentric circles: plate and loaf share the same center point"},
    {"num": 3, "text": "So many hands reach at once that the loaf looks smaller just from the hurry.", "image_key": "myth_03_hands_reach", "geometric_note": "Circumference: hands positioned around the edge of a circle"},
    {"num": 4, "text": "The sun's light makes a soft ring on the ground, like a quiet line that goes all the way around.", "image_key": "myth_04_light_ring", "geometric_note": "Circle definition: a closed curve where all points are equal distance from center"},
    {"num": 5, "text": '"Make a circle," says an old kind voice the children feel more than hear.', "image_key": "myth_05_make_circle", "geometric_note": "Construction: creating a circle by maintaining equal distance from a center"},
    {"num": 6, "text": "They step back, hold hands, and make a round.", "image_key": "myth_06_kids_ring", "geometric_note": "Radius: the distance from center to edge, kept equal by arm length"},
    {"num": 7, "text": "The smallest child walks to the middle and sets the loaf in the center.", "image_key": "myth_07_center_loaf", "geometric_note": "Center point: the single point equidistant from all points on the circle"},
    {"num": 8, "text": '"Half and half," she says, and pulls a string straight across.', "image_key": "myth_08_half_string", "geometric_note": "Diameter: a line through the center dividing the circle into two equal halves"},
    {"num": 9, "text": "Two parts wait, each the same, and everyone breathes.", "image_key": "myth_09_halves_equal", "geometric_note": "Semicircles: two equal halves created by a diameter line"},
    {"num": 10, "text": "The sun moves a little \u2014 same distance, same pace.", "image_key": "myth_10_sun_moves", "geometric_note": "Arc: a portion of the circle's circumference, showing constant curvature"},
    {"num": 11, "text": '"Four fair shares," the voice whispers, and the string crosses the middle again.', "image_key": "myth_11_four_shares", "geometric_note": "Perpendicular diameters: two lines through center at 90 degrees creating four equal parts"},
    {"num": 12, "text": "Now there are four parts, just right for four friends, and no one is left out.", "image_key": "myth_12_fourths_fair", "geometric_note": "Quadrants: four equal quarter-circles, each with a 90-degree central angle"},
    {"num": 13, "text": "Crumbs travel around the circle, one by one, until the plate is light and clean.", "image_key": "myth_13_crumbs_orbit", "geometric_note": "Circumference traversal: moving along the edge of a circle, returning to starting point"},
    {"num": 14, "text": 'The sun stands high and round. "Keep the circle," says the voice, "and it will keep you."', "image_key": "myth_14_sun_high", "geometric_note": "Complete circle: perfection, equality, and continuity in geometric form"},
]

DIAGRAM_DATA = [
    {"key": "step1_center", "title": "Step 1: Find the Center", "description": "Every circle begins with a center point. This is the single point from which all edges of the circle are equally distant.", "geometric_note": "The center point is the defining feature of a circle."},
    {"key": "step2_halves", "title": "Step 2: Divide into Halves", "description": "A straight line through the center (diameter) creates two equal semicircles. Each half is a mirror image of the other.", "geometric_note": "The diameter is the longest chord and creates bilateral symmetry."},
    {"key": "step3_fourths", "title": "Step 3: Divide into Fourths", "description": "A second line through the center, perpendicular to the first, creates four equal quarter-circles (quadrants).", "geometric_note": "Each quadrant contains a 90-degree angle at the center."},
    {"key": "fold_test", "title": "The Fold Test", "description": "Fold the circle along any diameter line. Both halves match perfectly, proving the circle has infinite lines of symmetry.", "geometric_note": "Circles have infinite rotational and reflectional symmetry."},
]

OVERLAY_DATA = [
    {"key": "center_CENTER_Dot", "title": "Center Point", "description": "The center point marked at the exact middle of the circle. All radii begin here.", "type": "OVL"},
    {"key": "circle_outline", "title": "Circle Outline", "description": "The circumference traced around the center point, showing the complete circular boundary.", "type": "OVL"},
    {"key": "line_LINE_Half", "title": "Half Line (Diameter)", "description": "A straight line through the center, dividing the circle into two equal semicircles.", "type": "OVL"},
    {"key": "line_LINE_Quarter", "title": "Quarter Lines", "description": "Two perpendicular diameters creating four equal quadrants of 90 degrees each.", "type": "OVL"},
    {"key": "measure_radius", "title": "Radius Measurement", "description": "The distance from center to edge, shown as a measured line segment.", "type": "OVL"},
    {"key": "measure_diameter", "title": "Diameter Measurement", "description": "The full distance across the circle through the center, equal to two radii.", "type": "OVL"},
]


def find_image(filename_pattern, lesson_prefix=None):
    results = []
    for root, dirs, files in os.walk(MESO_IMAGES_DIR):
        for f in files:
            if filename_pattern in f:
                results.append(os.path.join(root, f))
    if not results:
        return None
    if lesson_prefix and len(results) > 1:
        scoped = [r for r in results if lesson_prefix in os.path.basename(r)]
        if scoped:
            return scoped[0]
    return results[0]


def image_to_base64(filepath):
    if filepath and os.path.exists(filepath):
        with open(filepath, "rb") as f:
            data = f.read()
        ext = filepath.rsplit(".", 1)[-1].lower()
        mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png"}.get(ext, "image/png")
        return f"data:{mime};base64,{base64.b64encode(data).decode()}"
    return None


def get_db_lessons():
    if not os.path.exists(MESO_DB_PATH):
        return []
    conn = sqlite3.connect(MESO_DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lessons ORDER BY grade, week, lesson_letter")
    lessons = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return lessons


def get_db_assets(lesson_id):
    if not os.path.exists(MESO_DB_PATH):
        return []
    conn = sqlite3.connect(MESO_DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets WHERE lesson_id = ?", (lesson_id,))
    assets = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return assets


def get_db_content_blocks(lesson_id):
    if not os.path.exists(MESO_DB_PATH):
        return []
    conn = sqlite3.connect(MESO_DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM content_blocks WHERE lesson_id = ? ORDER BY block_order", (lesson_id,))
    blocks = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return blocks


def build_slide_data(lesson):
    slides = []
    lesson_id = lesson.get("lesson_id", "")
    lesson_key = lesson.get("lesson_key", "")
    grade = lesson.get("grade", 3)
    week = lesson.get("week", 1)
    letter = lesson.get("lesson_letter", "A")
    lesson_prefix = f"G{grade}_{week}{letter}"

    db_assets = get_db_assets(lesson_id)
    db_blocks = get_db_content_blocks(lesson_id)

    slides.append({
        "type": "title",
        "title": lesson.get("lesson_name", "Untitled Lesson"),
        "subtitle": f"Grade {grade} \u2022 Week {week} \u2022 Lesson {letter}",
        "deity": lesson.get("deity_name", ""),
        "concept": lesson.get("geometric_concept", ""),
        "standards": lesson.get("standards", ""),
        "theme": lesson.get("myth_theme", ""),
        "color_scheme": lesson.get("canva_color_scheme", "Gold #FFD24A, Orange"),
    })

    for artifact_key, artifact in ARTIFACT_DATA.items():
        img_path = find_image(artifact["image_file"])
        img_b64 = image_to_base64(img_path) if img_path else None

        overlay_b64_list = []
        for ovl_file in artifact.get("overlay_files", []):
            ovl_path = find_image(ovl_file)
            if ovl_path:
                overlay_b64_list.append({
                    "src": image_to_base64(ovl_path),
                    "name": ovl_file.replace(".jpg", "").replace("_", " ").title(),
                })

        slides.append({
            "type": "artifact",
            "title": artifact["name"],
            "date": artifact["date"],
            "location": artifact["location"],
            "description": artifact["description"],
            "geometric_connection": artifact["geometric_connection"],
            "image": img_b64,
            "overlays": overlay_b64_list,
        })

    db_myth_assets = [a for a in db_assets if a.get("usage_role") == "myth" and a.get("asset_type") == "IMG"]

    for sentence in MYTH_SENTENCES:
        img_path = None
        db_match = [a for a in db_myth_assets if sentence["image_key"] in (a.get("asset_id") or "")]
        if db_match:
            img_path = find_image(db_match[0].get("filename", ""), lesson_prefix)
        if not img_path:
            img_path = find_image(f"{lesson_prefix}-IMG-ILL_{sentence['image_key']}", lesson_prefix)
        if not img_path:
            img_path = find_image(sentence["image_key"], lesson_prefix)
        img_b64 = image_to_base64(img_path) if img_path else None

        slides.append({
            "type": "myth",
            "num": sentence["num"],
            "text": sentence["text"],
            "geometric_note": sentence["geometric_note"],
            "image": img_b64,
        })

    for diagram in DIAGRAM_DATA:
        img_path = find_image(f"DGM_{diagram['key']}", lesson_prefix)
        img_b64 = image_to_base64(img_path) if img_path else None

        slides.append({
            "type": "diagram",
            "title": diagram["title"],
            "description": diagram["description"],
            "geometric_note": diagram["geometric_note"],
            "image": img_b64,
        })

    for overlay in OVERLAY_DATA:
        img_path = find_image(f"OVL-{overlay['key']}", lesson_prefix)
        img_b64 = image_to_base64(img_path) if img_path else None

        slides.append({
            "type": "overlay",
            "title": overlay["title"],
            "description": overlay["description"],
            "image": img_b64,
        })

    return slides


def generate_slideshow_html(slides, lesson):
    colors = lesson.get("canva_color_scheme", "Gold #FFD24A, Orange")
    primary_color = "#FFD24A"
    secondary_color = "#2B6CB0"
    if "#" in colors:
        hex_matches = re.findall(r"#[0-9A-Fa-f]{6}", colors)
        if len(hex_matches) >= 1:
            primary_color = hex_matches[0]
        if len(hex_matches) >= 2:
            secondary_color = hex_matches[1]

    slide_html_parts = []
    for i, slide in enumerate(slides):
        if slide["type"] == "title":
            slide_html_parts.append(f'''
            <div class="slide" data-index="{i}">
                <div class="title-slide">
                    <div class="title-badge">{slide.get("deity", "")}</div>
                    <h1>{slide["title"]}</h1>
                    <p class="subtitle">{slide["subtitle"]}</p>
                    <div class="title-details">
                        <div class="detail-chip"><strong>Geometry:</strong> {slide.get("concept", "")}</div>
                        <div class="detail-chip"><strong>Theme:</strong> {slide.get("theme", "")}</div>
                        <div class="detail-chip"><strong>Standards:</strong> {slide.get("standards", "")}</div>
                    </div>
                </div>
            </div>''')

        elif slide["type"] == "artifact":
            overlay_html = ""
            overlay_buttons = ""
            if slide.get("overlays"):
                for j, ovl in enumerate(slide["overlays"]):
                    overlay_html += f'<img class="overlay-img" id="ovl-{i}-{j}" src="{ovl["src"]}" alt="{ovl["name"]}">'
                    overlay_buttons += f'<button class="overlay-btn" onclick="toggleOverlay(\'ovl-{i}-{j}\', this)">{ovl["name"]}</button>'

            img_html = f'<img class="artifact-img" src="{slide["image"]}" alt="{slide["title"]}">' if slide.get("image") else '<div class="no-image">Image not available</div>'

            slide_html_parts.append(f'''
            <div class="slide" data-index="{i}">
                <div class="artifact-slide">
                    <div class="artifact-image-container">
                        {img_html}
                        {overlay_html}
                    </div>
                    <div class="artifact-info">
                        <div class="artifact-badge">ARTIFACT</div>
                        <h2>{slide["title"]}</h2>
                        <div class="artifact-meta">{slide.get("date", "")} &bull; {slide.get("location", "")}</div>
                        <p class="artifact-desc">{slide["description"]}</p>
                        <div class="geometric-box">
                            <div class="geometric-label">Geometric Connection</div>
                            <p>{slide["geometric_connection"]}</p>
                        </div>
                        {f'<div class="overlay-controls"><div class="overlay-label">Toggle Overlays:</div>{overlay_buttons}</div>' if overlay_buttons else ''}
                    </div>
                </div>
            </div>''')

        elif slide["type"] == "myth":
            img_html = f'<img class="myth-img" src="{slide["image"]}" alt="Myth illustration">' if slide.get("image") else '<div class="no-image myth-placeholder">Illustration</div>'
            slide_html_parts.append(f'''
            <div class="slide" data-index="{i}">
                <div class="myth-slide">
                    <div class="myth-image-area">
                        {img_html}
                    </div>
                    <div class="myth-content">
                        <div class="myth-badge">MYTH &bull; Sentence {slide["num"]}</div>
                        <p class="myth-text">"{slide["text"]}"</p>
                        <div class="geometric-box">
                            <div class="geometric-label">Geometry</div>
                            <p>{slide["geometric_note"]}</p>
                        </div>
                    </div>
                </div>
            </div>''')

        elif slide["type"] == "diagram":
            img_html = f'<img class="diagram-img" src="{slide["image"]}" alt="{slide["title"]}">' if slide.get("image") else '<div class="no-image">Diagram</div>'
            slide_html_parts.append(f'''
            <div class="slide" data-index="{i}">
                <div class="diagram-slide">
                    <div class="diagram-image-area">
                        {img_html}
                    </div>
                    <div class="diagram-content">
                        <div class="diagram-badge">GEOMETRIC CONSTRUCTION</div>
                        <h2>{slide["title"]}</h2>
                        <p>{slide["description"]}</p>
                        <div class="geometric-box">
                            <div class="geometric-label">Key Concept</div>
                            <p>{slide["geometric_note"]}</p>
                        </div>
                    </div>
                </div>
            </div>''')

        elif slide["type"] == "overlay":
            img_html = f'<img class="overlay-demo-img" src="{slide["image"]}" alt="{slide["title"]}">' if slide.get("image") else '<div class="no-image">Overlay</div>'
            slide_html_parts.append(f'''
            <div class="slide" data-index="{i}">
                <div class="overlay-slide">
                    <div class="overlay-image-area">
                        {img_html}
                    </div>
                    <div class="overlay-content">
                        <div class="overlay-badge-label">GEOMETRIC OVERLAY</div>
                        <h2>{slide["title"]}</h2>
                        <p>{slide["description"]}</p>
                    </div>
                </div>
            </div>''')

    all_slides = "\n".join(slide_html_parts)
    total = len(slides)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson.get("lesson_name", "Slideshow")}</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: 'Georgia', 'Times New Roman', serif;
    background: #1a1a2e;
    color: #eee;
    overflow: hidden;
    height: 100vh;
    width: 100vw;
}}
.slideshow-container {{
    width: 100vw;
    height: 100vh;
    position: relative;
}}
.slide {{
    display: none;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0; left: 0;
    animation: fadeIn 0.4s ease;
}}
.slide.active {{ display: flex; }}
@keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}

/* Title Slide */
.title-slide {{
    width: 100%; height: 100%;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    text-align: center; padding: 40px;
}}
.title-badge {{
    background: {primary_color};
    color: #1a1a2e;
    padding: 8px 24px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: bold;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
}}
.title-slide h1 {{
    font-size: 52px;
    color: {primary_color};
    margin-bottom: 15px;
    text-shadow: 0 2px 20px rgba(255,210,74,0.3);
}}
.title-slide .subtitle {{
    font-size: 22px;
    color: #aaa;
    margin-bottom: 30px;
}}
.title-details {{
    display: flex; gap: 15px; flex-wrap: wrap; justify-content: center;
}}
.detail-chip {{
    background: rgba(255,255,255,0.08);
    padding: 10px 20px;
    border-radius: 10px;
    font-size: 14px;
    border: 1px solid rgba(255,255,255,0.1);
}}

/* Artifact Slide */
.artifact-slide {{
    width: 100%; height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
}}
.artifact-image-container {{
    position: relative;
    display: flex; align-items: center; justify-content: center;
    padding: 30px;
    background: rgba(0,0,0,0.3);
    overflow: hidden;
}}
.artifact-img {{
    max-width: 90%; max-height: 85vh;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.5);
    z-index: 1;
}}
.overlay-img {{
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    max-width: 90%; max-height: 85vh;
    object-fit: contain;
    z-index: 2;
    opacity: 0;
    transition: opacity 0.4s ease;
    pointer-events: none;
    mix-blend-mode: screen;
}}
.overlay-img.visible {{ opacity: 0.85; }}
.artifact-info {{
    padding: 40px;
    display: flex; flex-direction: column;
    justify-content: center;
    overflow-y: auto;
}}
.artifact-badge {{
    background: {primary_color};
    color: #1a1a2e;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 2px;
    display: inline-block;
    margin-bottom: 12px;
}}
.artifact-info h2 {{
    font-size: 28px;
    color: {primary_color};
    margin-bottom: 8px;
}}
.artifact-meta {{
    font-size: 13px;
    color: #888;
    margin-bottom: 15px;
    font-style: italic;
}}
.artifact-desc {{
    font-size: 15px;
    line-height: 1.7;
    color: #ccc;
    margin-bottom: 20px;
}}
.geometric-box {{
    background: rgba(43,108,176,0.15);
    border-left: 4px solid {secondary_color};
    padding: 15px 20px;
    border-radius: 0 8px 8px 0;
    margin-bottom: 15px;
}}
.geometric-label {{
    font-size: 11px;
    color: {secondary_color};
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: bold;
    margin-bottom: 6px;
}}
.geometric-box p {{
    font-size: 14px;
    line-height: 1.6;
    color: #bbb;
}}
.overlay-controls {{
    margin-top: 10px;
}}
.overlay-label {{
    font-size: 12px;
    color: #888;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
}}
.overlay-btn {{
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.2);
    color: #ccc;
    padding: 8px 16px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 12px;
    margin-right: 8px;
    margin-bottom: 6px;
    transition: all 0.2s;
}}
.overlay-btn:hover {{ background: rgba(255,255,255,0.15); }}
.overlay-btn.active {{
    background: {secondary_color};
    color: white;
    border-color: {secondary_color};
}}

/* Myth Slide */
.myth-slide {{
    width: 100%; height: 100%;
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    background: linear-gradient(135deg, #1a1a2e, #0f3460);
}}
.myth-image-area {{
    display: flex; align-items: center; justify-content: center;
    padding: 20px;
    background: rgba(0,0,0,0.2);
}}
.myth-img {{
    max-width: 95%; max-height: 90vh;
    object-fit: contain;
    border-radius: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}}
.myth-content {{
    padding: 40px;
    display: flex; flex-direction: column;
    justify-content: center;
}}
.myth-badge {{
    background: #e74c3c;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin-bottom: 20px;
}}
.myth-text {{
    font-size: 22px;
    line-height: 1.8;
    color: #eee;
    font-style: italic;
    margin-bottom: 25px;
}}

/* Diagram Slide */
.diagram-slide {{
    width: 100%; height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    background: linear-gradient(135deg, #1a1a2e, #16213e);
}}
.diagram-image-area {{
    display: flex; align-items: center; justify-content: center;
    padding: 30px;
    background: rgba(255,255,255,0.03);
}}
.diagram-img {{
    max-width: 80%; max-height: 70vh;
    object-fit: contain;
    border-radius: 8px;
    background: white;
    padding: 20px;
}}
.diagram-content {{
    padding: 40px;
    display: flex; flex-direction: column;
    justify-content: center;
}}
.diagram-badge {{
    background: #27ae60;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin-bottom: 15px;
}}
.diagram-content h2 {{
    font-size: 28px;
    color: #27ae60;
    margin-bottom: 15px;
}}
.diagram-content > p {{
    font-size: 16px;
    line-height: 1.7;
    color: #ccc;
    margin-bottom: 20px;
}}

/* Overlay Demo Slide */
.overlay-slide {{
    width: 100%; height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    background: linear-gradient(135deg, #16213e, #1a1a2e);
}}
.overlay-image-area {{
    display: flex; align-items: center; justify-content: center;
    padding: 30px;
    background: rgba(0,0,0,0.2);
}}
.overlay-demo-img {{
    max-width: 80%; max-height: 70vh;
    object-fit: contain;
    border-radius: 8px;
}}
.overlay-content {{
    padding: 40px;
    display: flex; flex-direction: column;
    justify-content: center;
}}
.overlay-badge-label {{
    background: #8e44ad;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 1px;
    display: inline-block;
    margin-bottom: 15px;
}}
.overlay-content h2 {{
    font-size: 28px;
    color: #8e44ad;
    margin-bottom: 15px;
}}
.overlay-content p {{
    font-size: 16px;
    line-height: 1.7;
    color: #ccc;
}}

.no-image {{
    width: 300px; height: 200px;
    background: rgba(255,255,255,0.05);
    border: 2px dashed rgba(255,255,255,0.15);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    color: #555; font-size: 14px;
}}

/* Navigation */
.nav-bar {{
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(10px);
    padding: 12px 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 100;
}}
.nav-btn {{
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    color: #eee;
    padding: 10px 25px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    transition: all 0.2s;
}}
.nav-btn:hover {{ background: rgba(255,255,255,0.2); }}
.nav-btn:disabled {{ opacity: 0.3; cursor: not-allowed; }}
.slide-counter {{
    color: #888;
    font-size: 14px;
}}
.progress-bar {{
    position: fixed;
    top: 0; left: 0;
    height: 3px;
    background: {primary_color};
    transition: width 0.3s ease;
    z-index: 101;
}}
.section-indicator {{
    display: flex; gap: 8px; align-items: center;
}}
.section-dot {{
    width: 8px; height: 8px;
    border-radius: 50%;
    background: rgba(255,255,255,0.2);
    cursor: pointer;
    transition: all 0.2s;
}}
.section-dot.active {{ background: {primary_color}; transform: scale(1.3); }}
.section-dot.artifact {{ background: {primary_color}; opacity: 0.6; }}
.section-dot.myth {{ background: #e74c3c; opacity: 0.6; }}
.section-dot.diagram {{ background: #27ae60; opacity: 0.6; }}
.section-dot.overlay {{ background: #8e44ad; opacity: 0.6; }}

@media (max-width: 900px) {{
    .artifact-slide, .myth-slide, .diagram-slide, .overlay-slide {{
        grid-template-columns: 1fr;
        grid-template-rows: 1fr 1fr;
    }}
}}
</style>
</head>
<body>
<div class="progress-bar" id="progressBar"></div>
<div class="slideshow-container" id="slideshow">
{all_slides}
</div>
<div class="nav-bar">
    <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)">&larr; Previous</button>
    <div class="section-indicator" id="sectionDots"></div>
    <span class="slide-counter" id="counter">1 / {total}</span>
    <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)">Next &rarr;</button>
</div>
<script>
let current = 0;
const slides = document.querySelectorAll('.slide');
const total = slides.length;
const types = {json.dumps([s["type"] for s in slides])};

function buildDots() {{
    const container = document.getElementById('sectionDots');
    for (let i = 0; i < total; i++) {{
        const dot = document.createElement('div');
        dot.className = 'section-dot ' + types[i];
        dot.onclick = () => goToSlide(i);
        dot.title = 'Slide ' + (i + 1);
        container.appendChild(dot);
    }}
}}
buildDots();

function showSlide(n) {{
    slides.forEach(s => s.classList.remove('active'));
    slides[n].classList.add('active');
    document.getElementById('counter').textContent = (n + 1) + ' / ' + total;
    document.getElementById('prevBtn').disabled = n === 0;
    document.getElementById('nextBtn').disabled = n === total - 1;
    document.getElementById('progressBar').style.width = ((n + 1) / total * 100) + '%';
    const dots = document.querySelectorAll('.section-dot');
    dots.forEach((d, i) => d.classList.toggle('active', i === n));
}}

function changeSlide(dir) {{
    current = Math.max(0, Math.min(total - 1, current + dir));
    showSlide(current);
}}

function goToSlide(n) {{
    current = n;
    showSlide(n);
}}

function toggleOverlay(id, btn) {{
    const el = document.getElementById(id);
    el.classList.toggle('visible');
    btn.classList.toggle('active');
}}

document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowRight' || e.key === ' ') changeSlide(1);
    if (e.key === 'ArrowLeft') changeSlide(-1);
    if (e.key === 'Home') goToSlide(0);
    if (e.key === 'End') goToSlide(total - 1);
}});

showSlide(0);
</script>
</body>
</html>'''
    return html


st.title("🎬 Slideshow Generator")
st.markdown("Generate interactive slideshows from Mesopotamia curriculum content with artifact images, descriptions, geometric connections, and overlay toggles.")

lessons = get_db_lessons()

if not lessons:
    st.warning("No lessons found in the curriculum database. Make sure the Mesopotamia curriculum files are extracted.")
    st.stop()

st.sidebar.header("Lesson Selection")
lesson_options = {f"Grade {l['grade']} - Week {l['week']}{l['lesson_letter']}: {l['lesson_name']}": l for l in lessons}
selected_label = st.sidebar.selectbox("Choose a lesson:", list(lesson_options.keys()))
selected_lesson = lesson_options[selected_label]

st.sidebar.markdown("---")
st.sidebar.markdown("### Lesson Details")
st.sidebar.markdown(f"**Deity:** {selected_lesson.get('deity_name', 'N/A')}")
st.sidebar.markdown(f"**Geometry:** {selected_lesson.get('geometric_concept', 'N/A')}")
st.sidebar.markdown(f"**Standards:** {selected_lesson.get('standards', 'N/A')}")
st.sidebar.markdown(f"**Theme:** {selected_lesson.get('myth_theme', 'N/A')}")
st.sidebar.markdown(f"**Duration:** {selected_lesson.get('duration_minutes', 50)} min")

st.sidebar.markdown("---")
st.sidebar.markdown("### Slide Sections")
st.sidebar.markdown("""
- **Title** - Lesson overview
- **Artifacts** - Museum objects with overlays
- **Myth** - 14-sentence read-aloud
- **Diagrams** - Step-by-step constructions
- **Overlays** - Geometric annotations
""")

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.subheader(f"{selected_lesson['lesson_name']}")
    st.caption(f"Grade {selected_lesson['grade']} | Week {selected_lesson['week']} | {selected_lesson.get('deity_name', '')} | {selected_lesson.get('geometric_concept', '')}")

with col2:
    include_artifacts = st.checkbox("Include Artifacts", value=True)
    include_myth = st.checkbox("Include Myth Sequence", value=True)

with col3:
    include_diagrams = st.checkbox("Include Diagrams", value=True)
    include_overlays = st.checkbox("Include Overlays", value=True)

if st.button("Generate Slideshow", type="primary", use_container_width=True):
    with st.spinner("Building slideshow..."):
        slide_data = build_slide_data(selected_lesson)

        filtered_slides = []
        for s in slide_data:
            if s["type"] == "title":
                filtered_slides.append(s)
            elif s["type"] == "artifact" and include_artifacts:
                filtered_slides.append(s)
            elif s["type"] == "myth" and include_myth:
                filtered_slides.append(s)
            elif s["type"] == "diagram" and include_diagrams:
                filtered_slides.append(s)
            elif s["type"] == "overlay" and include_overlays:
                filtered_slides.append(s)

        html_content = generate_slideshow_html(filtered_slides, selected_lesson)

        st.session_state["slideshow_html"] = html_content
        st.session_state["slideshow_slides"] = filtered_slides
        st.session_state["slideshow_lesson"] = selected_lesson

    st.success(f"Slideshow generated with {len(filtered_slides)} slides!")

if "slideshow_html" in st.session_state:
    slides_data = st.session_state.get("slideshow_slides", [])
    lesson_data = st.session_state.get("slideshow_lesson", {})

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Preview", "Slide Overview", "Export"])

    with tab1:
        st.components.v1.html(st.session_state["slideshow_html"], height=650, scrolling=False)
        st.caption("Use arrow keys or click buttons to navigate. Click overlay buttons to toggle geometric annotations.")

    with tab2:
        type_counts = {}
        for s in slides_data:
            t = s["type"]
            type_counts[t] = type_counts.get(t, 0) + 1

        cols = st.columns(5)
        labels = {"title": "Title", "artifact": "Artifacts", "myth": "Myth", "diagram": "Diagrams", "overlay": "Overlays"}
        colors_map = {"title": "blue", "artifact": "orange", "myth": "red", "diagram": "green", "overlay": "violet"}
        for i, (key, label) in enumerate(labels.items()):
            with cols[i]:
                count = type_counts.get(key, 0)
                st.metric(label, count)

        st.markdown("### Slide List")
        for i, s in enumerate(slides_data):
            badge = labels.get(s["type"], s["type"])
            if s["type"] == "title":
                st.markdown(f"**{i+1}.** :blue[{badge}] — {s.get('title', '')}")
            elif s["type"] == "artifact":
                has_img = "has image" if s.get("image") else "no image"
                ovl_count = len(s.get("overlays", []))
                st.markdown(f"**{i+1}.** :orange[{badge}] — {s.get('title', '')} ({has_img}, {ovl_count} overlays)")
            elif s["type"] == "myth":
                has_img = "has image" if s.get("image") else "no image"
                st.markdown(f"**{i+1}.** :red[{badge}] — Sentence {s.get('num', '')} ({has_img})")
            elif s["type"] == "diagram":
                has_img = "has image" if s.get("image") else "no image"
                st.markdown(f"**{i+1}.** :green[{badge}] — {s.get('title', '')} ({has_img})")
            elif s["type"] == "overlay":
                has_img = "has image" if s.get("image") else "no image"
                st.markdown(f"**{i+1}.** :violet[{badge}] — {s.get('title', '')} ({has_img})")

    with tab3:
        st.markdown("### Download Slideshow")
        st.download_button(
            label="Download as HTML",
            data=st.session_state["slideshow_html"],
            file_name=f"{lesson_data.get('lesson_key', 'slideshow')}_slideshow.html",
            mime="text/html",
            use_container_width=True,
        )
        st.info("The downloaded HTML file is self-contained with all images embedded. Open it in any browser for full-screen presentation.")
