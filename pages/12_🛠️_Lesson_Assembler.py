import streamlit as st
import sqlite3
import os
import json
import base64
from datetime import datetime

st.set_page_config(page_title="Lesson Assembler", page_icon="🛠️", layout="wide")

MESO_DB_PATH = "attached_assets/meso_curriculum/MESO_Curriculum_2025-01-05/05_Database_Files/meso_ssot_complete.db"
MESO_IMAGES_DIR = "attached_assets/meso_curriculum/MESO_Curriculum_2025-01-05/03_Image_Download"
ASSEMBLED_DIR = "data/assembled_lessons"

os.makedirs(ASSEMBLED_DIR, exist_ok=True)

BLOCK_TYPES = ["TEXT", "MYTH", "DIAGRAM", "ACTIVITY", "WORKSHEET", "IMAGE", "ASSESSMENT", "TEACHER_NOTE"]
BLOCK_ICONS = {
    "TEXT": "📝", "MYTH": "📖", "DIAGRAM": "📐", "ACTIVITY": "✋",
    "WORKSHEET": "📄", "IMAGE": "🖼️", "ASSESSMENT": "📊", "TEACHER_NOTE": "🗒️"
}
DIMENSION_LEVELS = ["D1a", "D1b", "D2", "D3", "D4"]
VARIABLES = ["Math", "Arts", "Mythology", "Power"]
OUTPUT_TYPES = ["HTML Slideshow", "Lesson Plan (Print)", "Teacher Guide", "Student Handout"]


def get_db_connection():
    if not os.path.exists(MESO_DB_PATH):
        return None
    return sqlite3.connect(MESO_DB_PATH)


def load_lessons():
    conn = get_db_connection()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute("SELECT lesson_id, lesson_name, grade, week, lesson_letter, geometric_concept FROM lessons ORDER BY grade, week, lesson_letter")
    rows = cur.fetchall()
    conn.close()
    return rows


def load_lesson_detail(lesson_id):
    conn = get_db_connection()
    if not conn:
        return None, [], []
    cur = conn.cursor()
    cur.execute("SELECT * FROM lessons WHERE lesson_id = ?", (lesson_id,))
    lesson = cur.fetchone()
    cur.execute("SELECT * FROM content_blocks WHERE lesson_id = ? ORDER BY block_order", (lesson_id,))
    blocks = cur.fetchall()
    cur.execute("SELECT * FROM assets WHERE lesson_id = ?", (lesson_id,))
    assets = cur.fetchall()
    conn.close()
    return lesson, blocks, assets


def find_image_file(filename_hint):
    for root, dirs, files in os.walk(MESO_IMAGES_DIR):
        for f in files:
            if filename_hint.lower() in f.lower():
                return os.path.join(root, f)
    return None


def image_to_base64(path):
    try:
        with open(path, "rb") as f:
            ext = os.path.splitext(path)[1].lower().strip(".")
            mime = "image/svg+xml" if ext == "svg" else f"image/{ext}"
            return f"data:{mime};base64,{base64.b64encode(f.read()).decode()}"
    except Exception:
        return None


def save_assembled_lesson(lesson_data):
    filename = f"{lesson_data['lesson_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    path = os.path.join(ASSEMBLED_DIR, filename)
    with open(path, "w") as f:
        json.dump(lesson_data, f, indent=2)
    return path


def load_assembled_lessons():
    files = []
    if os.path.exists(ASSEMBLED_DIR):
        for f in sorted(os.listdir(ASSEMBLED_DIR), reverse=True):
            if f.endswith(".json"):
                files.append(f)
    return files


def export_html_slideshow(lesson_data):
    slides_html = ""
    for i, block in enumerate(lesson_data.get("blocks", [])):
        img_html = ""
        if block.get("image_b64"):
            img_html = f'<img src="{block["image_b64"]}" style="max-width:100%;max-height:340px;border-radius:8px;margin-bottom:12px;" />'
        slides_html += f"""
        <div class="slide" id="slide-{i}" style="display:{'block' if i == 0 else 'none'}">
          <div class="slide-type">{BLOCK_ICONS.get(block['type'], '📝')} {block['type']}</div>
          <h2>{block.get('title','')}</h2>
          {img_html}
          <p style="font-size:1.1em;line-height:1.7">{block.get('body','')}</p>
          {'<div class="teacher-note">🗒️ <b>Teacher:</b> ' + block.get('instructions','') + '</div>' if block.get('instructions') else ''}
          {'<div class="dimension">' + block.get('dimension','') + '</div>' if block.get('dimension') else ''}
        </div>
        """
    total = len(lesson_data.get("blocks", []))
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{lesson_data.get('title','Lesson')}</title>
<style>
  body {{ font-family: 'Segoe UI', sans-serif; background:#1a1a2e; color:#eee; margin:0; padding:0; }}
  .header {{ background:#16213e; padding:20px 40px; border-bottom:2px solid #FFD24A; }}
  .header h1 {{ margin:0; color:#FFD24A; font-size:1.8em; }}
  .header .meta {{ color:#aaa; font-size:0.9em; margin-top:6px; }}
  .container {{ max-width:900px; margin:40px auto; padding:0 20px; }}
  .slide {{ background:#16213e; border-radius:12px; padding:36px; margin-bottom:20px; border:1px solid #333; min-height:400px; }}
  .slide-type {{ color:#FFD24A; font-size:0.85em; font-weight:bold; text-transform:uppercase; letter-spacing:2px; margin-bottom:12px; }}
  h2 {{ color:#fff; margin-top:0; font-size:1.6em; }}
  .teacher-note {{ background:#0f3460; border-left:4px solid #FFD24A; padding:12px 16px; border-radius:6px; margin-top:16px; font-size:0.95em; color:#ccc; }}
  .dimension {{ display:inline-block; background:#e94560; color:#fff; padding:4px 12px; border-radius:20px; font-size:0.8em; margin-top:12px; }}
  .nav {{ display:flex; justify-content:center; gap:16px; padding:20px; position:sticky; bottom:0; background:#1a1a2e; border-top:1px solid #333; }}
  .nav button {{ background:#FFD24A; color:#1a1a2e; border:none; padding:10px 28px; border-radius:6px; font-size:1em; font-weight:bold; cursor:pointer; }}
  .nav button:hover {{ background:#ffc107; }}
  .counter {{ color:#aaa; font-size:0.9em; align-self:center; }}
  .variables {{ display:flex; gap:8px; flex-wrap:wrap; margin-top:8px; }}
  .var-tag {{ background:#0f3460; border:1px solid #FFD24A44; color:#FFD24A; padding:3px 10px; border-radius:12px; font-size:0.8em; }}
</style>
</head>
<body>
<div class="header">
  <h1>🏫 {lesson_data.get('title','Lesson')}</h1>
  <div class="meta">Grade {lesson_data.get('grade','')} · Week {lesson_data.get('week','')} · {lesson_data.get('geometric_concept','')}</div>
  <div class="meta">Standards: {lesson_data.get('standards','')} · {lesson_data.get('duration',50)} min</div>
  <div class="variables">{''.join(f'<span class="var-tag">{v}</span>' for v in lesson_data.get('variables',[]))}</div>
</div>
<div class="container">
{slides_html}
</div>
<div class="nav">
  <button onclick="navigate(-1)">← Prev</button>
  <span class="counter" id="counter">1 / {total}</span>
  <button onclick="navigate(1)">Next →</button>
</div>
<script>
  let current = 0;
  const total = {total};
  function navigate(dir) {{
    document.getElementById('slide-' + current).style.display = 'none';
    current = Math.max(0, Math.min(total - 1, current + dir));
    document.getElementById('slide-' + current).style.display = 'block';
    document.getElementById('counter').textContent = (current + 1) + ' / ' + total;
  }}
</script>
</body>
</html>"""
    return html


def export_lesson_plan(lesson_data):
    lines = [f"# LESSON PLAN: {lesson_data.get('title','')}",
             f"Grade: {lesson_data.get('grade','')}  |  Week: {lesson_data.get('week','')}  |  Duration: {lesson_data.get('duration',50)} min",
             f"Standards: {lesson_data.get('standards','')}",
             f"Geometric Concept: {lesson_data.get('geometric_concept','')}",
             f"Variables: {', '.join(lesson_data.get('variables',[]))}",
             f"Dimension Levels: {', '.join(lesson_data.get('dimensions',[]))}",
             "", "---", ""]
    for block in lesson_data.get("blocks", []):
        icon = BLOCK_ICONS.get(block['type'], '•')
        lines.append(f"## {icon} {block['type']}: {block.get('title','')}")
        if block.get('body'):
            lines.append(block['body'])
        if block.get('instructions'):
            lines.append(f"\n**Teacher Instructions:** {block['instructions']}")
        if block.get('dimension'):
            lines.append(f"*Dimension Level: {block['dimension']}*")
        lines.append("")
    return "\n".join(lines)


# ── Session state init ──────────────────────────────────────────
if "assembler_blocks" not in st.session_state:
    st.session_state.assembler_blocks = []
if "assembler_meta" not in st.session_state:
    st.session_state.assembler_meta = {}


# ── Page Header ─────────────────────────────────────────────────
st.title("🛠️ Lesson Assembler")
st.markdown("### Build, design, and export complete lessons")

tab_build, tab_preview, tab_export, tab_saved = st.tabs(
    ["🧱 Build", "👁️ Preview", "📤 Export", "💾 Saved Lessons"]
)


# ══════════════════════════════════════════════════════════════
# TAB 1 — BUILD
# ══════════════════════════════════════════════════════════════
with tab_build:
    col_meta, col_blocks = st.columns([1, 2], gap="large")

    with col_meta:
        st.subheader("Lesson Info")

        lessons = load_lessons()
        lesson_options = {f"Grade {r[2]} · Wk {r[3]}{r[4]} — {r[1]}": r[0] for r in lessons}
        lesson_options["➕ New lesson (blank)"] = None

        selected_label = st.selectbox("Start from existing lesson", list(lesson_options.keys()))
        selected_id = lesson_options[selected_label]

        if selected_id and st.button("Load from database", use_container_width=True):
            lesson, blocks, assets = load_lesson_detail(selected_id)
            if lesson:
                cols = ["lesson_id","chapter_id","ssot_id","lesson_key","lesson_name","grade","week",
                        "lesson_letter","deity_name","geometric_concept","math_standard","artifact_type",
                        "measurement_focus","myth_theme","activity_medium","canva_color_scheme",
                        "duration_minutes","standards","compliance_tags","estimated_images",
                        "lesson_structure","created_at","updated_at"]
                ld = dict(zip(cols, lesson))
                st.session_state.assembler_meta = {
                    "lesson_id": ld["lesson_id"],
                    "title": ld["lesson_name"],
                    "grade": ld["grade"],
                    "week": ld["week"],
                    "geometric_concept": ld["geometric_concept"],
                    "standards": ld["standards"],
                    "duration": ld["duration_minutes"],
                    "variables": [],
                    "dimensions": [],
                }
                block_cols = ["content_id","lesson_id","chapter_id","block_type","block_order",
                              "section_name","title","body_text","instructions","duration_seconds",
                              "interactivity_level","accessibility_notes","metadata_json","created_at"]
                loaded_blocks = []
                for b in blocks:
                    bd = dict(zip(block_cols, b))
                    loaded_blocks.append({
                        "type": bd["block_type"],
                        "title": bd["title"] or "",
                        "body": bd["body_text"] or "",
                        "instructions": bd["instructions"] or "",
                        "dimension": "",
                        "image_path": "",
                        "image_b64": "",
                    })
                st.session_state.assembler_blocks = loaded_blocks
                st.success(f"Loaded {len(loaded_blocks)} blocks from database")
                st.rerun()

        st.divider()
        st.markdown("**Lesson metadata**")

        meta = st.session_state.assembler_meta
        title = st.text_input("Title", value=meta.get("title", ""))
        grade = st.selectbox("Grade", list(range(0, 9)), index=int(meta.get("grade", 3)))
        week = st.number_input("Week", min_value=1, max_value=36, value=int(meta.get("week", 1)))
        geo_concept = st.text_input("Geometric Concept", value=meta.get("geometric_concept", ""))
        standards = st.text_input("Standards", value=meta.get("standards", ""))
        duration = st.number_input("Duration (min)", min_value=5, max_value=120, value=int(meta.get("duration", 50)))
        variables = st.multiselect("Variables", VARIABLES, default=meta.get("variables", []))
        dimensions = st.multiselect("Dimension Levels", DIMENSION_LEVELS, default=meta.get("dimensions", []))

        if st.button("💾 Save metadata", use_container_width=True):
            st.session_state.assembler_meta = {
                "lesson_id": meta.get("lesson_id", f"custom_{datetime.now().strftime('%Y%m%d%H%M%S')}"),
                "title": title, "grade": grade, "week": week,
                "geometric_concept": geo_concept, "standards": standards,
                "duration": duration, "variables": variables, "dimensions": dimensions,
            }
            st.success("Metadata saved")

    with col_blocks:
        st.subheader("Content Blocks")

        blocks = st.session_state.assembler_blocks

        # Add new block
        with st.expander("➕ Add a content block", expanded=len(blocks) == 0):
            new_type = st.selectbox("Block type", BLOCK_TYPES, key="new_block_type")
            new_title = st.text_input("Block title", key="new_block_title")
            new_body = st.text_area("Content / body text", key="new_block_body", height=100)
            new_instr = st.text_area("Teacher instructions (optional)", key="new_block_instr", height=60)
            new_dim = st.selectbox("Dimension level", [""] + DIMENSION_LEVELS, key="new_block_dim")

            st.markdown("**Image for this block**")
            img_source = st.radio("Image source", ["None", "Library (search)", "Upload", "AI Generate (coming soon)"],
                                  horizontal=True, key="new_img_source")
            image_b64 = ""
            image_path = ""

            if img_source == "Library (search)":
                search_term = st.text_input("Search image library", key="new_img_search")
                if search_term:
                    found = find_image_file(search_term)
                    if found:
                        st.image(found, width=200)
                        image_path = found
                        image_b64 = image_to_base64(found) or ""
                        st.success(f"Found: {os.path.basename(found)}")
                    else:
                        st.warning("No image found — try a different search term")

            elif img_source == "Upload":
                uploaded = st.file_uploader("Upload image", type=["jpg","jpeg","png","svg","webp"], key="new_img_upload")
                if uploaded:
                    save_path = os.path.join(ASSEMBLED_DIR, "images", uploaded.name)
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    with open(save_path, "wb") as f:
                        f.write(uploaded.read())
                    image_path = save_path
                    image_b64 = image_to_base64(save_path) or ""
                    st.image(save_path, width=200)

            elif img_source == "AI Generate (coming soon)":
                st.info("AI image generation will connect here once the API key is configured. You'll describe the image and it will be generated and embedded directly into the lesson.")

            if st.button("Add block", type="primary", use_container_width=True):
                if new_title or new_body:
                    st.session_state.assembler_blocks.append({
                        "type": new_type,
                        "title": new_title,
                        "body": new_body,
                        "instructions": new_instr,
                        "dimension": new_dim,
                        "image_path": image_path,
                        "image_b64": image_b64,
                    })
                    st.success(f"Added {new_type} block: {new_title}")
                    st.rerun()
                else:
                    st.warning("Add a title or body text before adding the block")

        st.divider()

        # Display and edit existing blocks
        if not blocks:
            st.info("No blocks yet — add your first content block above, or load from an existing lesson.")
        else:
            st.markdown(f"**{len(blocks)} block(s) in this lesson**")
            for i, block in enumerate(blocks):
                icon = BLOCK_ICONS.get(block["type"], "📝")
                with st.expander(f"{icon} {i+1}. [{block['type']}] {block.get('title','(no title)')}", expanded=False):
                    c1, c2 = st.columns(2)
                    with c1:
                        block["type"] = st.selectbox("Type", BLOCK_TYPES,
                            index=BLOCK_TYPES.index(block["type"]) if block["type"] in BLOCK_TYPES else 0,
                            key=f"type_{i}")
                        block["title"] = st.text_input("Title", value=block.get("title",""), key=f"title_{i}")
                        block["dimension"] = st.selectbox("Dimension", [""] + DIMENSION_LEVELS,
                            index=([""] + DIMENSION_LEVELS).index(block.get("dimension","")) if block.get("dimension","") in [""] + DIMENSION_LEVELS else 0,
                            key=f"dim_{i}")
                    with c2:
                        block["body"] = st.text_area("Body text", value=block.get("body",""), key=f"body_{i}", height=100)
                        block["instructions"] = st.text_area("Teacher instructions", value=block.get("instructions",""), key=f"instr_{i}", height=60)

                    if block.get("image_b64"):
                        st.image(block["image_b64"], width=180, caption="Current image")
                        if st.button("Remove image", key=f"rm_img_{i}"):
                            block["image_path"] = ""
                            block["image_b64"] = ""
                            st.rerun()

                    move_col, del_col = st.columns(2)
                    with move_col:
                        m1, m2 = st.columns(2)
                        with m1:
                            if st.button("⬆️ Up", key=f"up_{i}", disabled=i == 0):
                                blocks[i], blocks[i-1] = blocks[i-1], blocks[i]
                                st.rerun()
                        with m2:
                            if st.button("⬇️ Down", key=f"dn_{i}", disabled=i == len(blocks)-1):
                                blocks[i], blocks[i+1] = blocks[i+1], blocks[i]
                                st.rerun()
                    with del_col:
                        if st.button("🗑️ Remove block", key=f"del_{i}"):
                            st.session_state.assembler_blocks.pop(i)
                            st.rerun()


# ══════════════════════════════════════════════════════════════
# TAB 2 — PREVIEW
# ══════════════════════════════════════════════════════════════
with tab_preview:
    meta = st.session_state.assembler_meta
    blocks = st.session_state.assembler_blocks

    if not meta and not blocks:
        st.info("Build your lesson in the **Build** tab first.")
    else:
        st.markdown(f"## {meta.get('title','Untitled Lesson')}")
        cols = st.columns(4)
        cols[0].metric("Grade", f"Grade {meta.get('grade','—')}")
        cols[1].metric("Week", meta.get("week", "—"))
        cols[2].metric("Duration", f"{meta.get('duration','—')} min")
        cols[3].metric("Blocks", len(blocks))

        if meta.get("variables"):
            st.markdown("**Variables:** " + " · ".join(f"`{v}`" for v in meta["variables"]))
        if meta.get("dimensions"):
            st.markdown("**Dimension Levels:** " + " · ".join(f"`{d}`" for d in meta["dimensions"]))
        if meta.get("standards"):
            st.markdown(f"**Standards:** {meta['standards']}")
        if meta.get("geometric_concept"):
            st.markdown(f"**Concept:** {meta['geometric_concept']}")

        st.divider()

        for i, block in enumerate(blocks):
            icon = BLOCK_ICONS.get(block["type"], "📝")
            st.markdown(f"### {icon} {block.get('title','') or block['type']}")
            if block.get("dimension"):
                st.caption(f"Dimension: {block['dimension']}")
            if block.get("image_b64"):
                st.image(block["image_b64"], width=400)
            if block.get("body"):
                st.markdown(block["body"])
            if block.get("instructions"):
                st.info(f"🗒️ **Teacher:** {block['instructions']}")
            st.divider()


# ══════════════════════════════════════════════════════════════
# TAB 3 — EXPORT
# ══════════════════════════════════════════════════════════════
with tab_export:
    meta = st.session_state.assembler_meta
    blocks = st.session_state.assembler_blocks

    if not blocks:
        st.info("Build your lesson in the **Build** tab first.")
    else:
        st.subheader("Export your lesson")
        st.markdown(f"**{meta.get('title','Untitled')}** · {len(blocks)} blocks")

        lesson_data = {**meta, "blocks": blocks}

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("#### 🎬 HTML Slideshow")
            st.caption("Interactive presentation with navigation — opens in any browser")
            if st.button("Generate HTML Slideshow", use_container_width=True, type="primary"):
                html = export_html_slideshow(lesson_data)
                st.download_button(
                    "⬇️ Download Slideshow HTML",
                    data=html,
                    file_name=f"{meta.get('lesson_id','lesson')}_slideshow.html",
                    mime="text/html",
                    use_container_width=True
                )

            st.markdown("#### 📝 Lesson Plan (Markdown)")
            st.caption("Printable structured lesson plan — paste into Word/Google Docs")
            if st.button("Generate Lesson Plan", use_container_width=True):
                plan_text = export_lesson_plan(lesson_data)
                st.download_button(
                    "⬇️ Download Lesson Plan",
                    data=plan_text,
                    file_name=f"{meta.get('lesson_id','lesson')}_plan.md",
                    mime="text/markdown",
                    use_container_width=True
                )

        with col_b:
            st.markdown("#### 📊 Teacher Guide")
            st.caption("Teacher-focused view with instructions and dimension notes")
            if st.button("Generate Teacher Guide", use_container_width=True):
                teacher_blocks = [b for b in blocks if b.get("instructions")]
                guide_lines = [f"# TEACHER GUIDE: {meta.get('title','')}",
                               f"Grade {meta.get('grade','')} · Week {meta.get('week','')} · {meta.get('duration',50)} min",
                               f"Standards: {meta.get('standards','')}", "", "---", ""]
                for b in teacher_blocks:
                    guide_lines.append(f"## {b.get('title','')}")
                    guide_lines.append(f"**Instruction:** {b['instructions']}")
                    if b.get("dimension"):
                        guide_lines.append(f"*Targets {b['dimension']}*")
                    guide_lines.append("")
                st.download_button(
                    "⬇️ Download Teacher Guide",
                    data="\n".join(guide_lines),
                    file_name=f"{meta.get('lesson_id','lesson')}_teacher_guide.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            st.markdown("#### 📄 Student Handout")
            st.caption("Student-facing content — body text and activities only")
            if st.button("Generate Student Handout", use_container_width=True):
                student_types = {"TEXT", "MYTH", "DIAGRAM", "ACTIVITY", "WORKSHEET"}
                handout_lines = [f"# {meta.get('title','')}", f"Name: _______________  Date: _______________", "", "---", ""]
                for b in blocks:
                    if b["type"] in student_types:
                        handout_lines.append(f"## {b.get('title','')}")
                        if b.get("body"):
                            handout_lines.append(b["body"])
                        handout_lines.append("")
                st.download_button(
                    "⬇️ Download Student Handout",
                    data="\n".join(handout_lines),
                    file_name=f"{meta.get('lesson_id','lesson')}_student.md",
                    mime="text/markdown",
                    use_container_width=True
                )

        st.divider()
        st.markdown("#### 💾 Save to workspace")
        if st.button("Save assembled lesson (JSON)", use_container_width=True):
            path = save_assembled_lesson(lesson_data)
            st.success(f"Saved to {path}")


# ══════════════════════════════════════════════════════════════
# TAB 4 — SAVED LESSONS
# ══════════════════════════════════════════════════════════════
with tab_saved:
    st.subheader("Saved Assembled Lessons")
    saved = load_assembled_lessons()

    if not saved:
        st.info("No assembled lessons saved yet. Build and save a lesson from the Build tab.")
    else:
        for fname in saved:
            fpath = os.path.join(ASSEMBLED_DIR, fname)
            try:
                with open(fpath) as f:
                    data = json.load(f)
                with st.expander(f"📋 {data.get('title','Untitled')} — {fname}"):
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Grade", f"Grade {data.get('grade','—')}")
                    c2.metric("Blocks", len(data.get("blocks", [])))
                    c3.metric("Duration", f"{data.get('duration','—')} min")
                    if st.button("Load into assembler", key=f"load_{fname}"):
                        st.session_state.assembler_meta = {k: v for k, v in data.items() if k != "blocks"}
                        st.session_state.assembler_blocks = data.get("blocks", [])
                        st.success("Loaded — go to Build tab to continue editing")
                        st.rerun()
            except Exception as e:
                st.error(f"Could not load {fname}: {e}")
