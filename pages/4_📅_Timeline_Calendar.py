import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore

st.set_page_config(page_title="Timeline Calendar", page_icon="📅", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("📅 Timeline Calendar")
st.markdown("### Twice-Weekly Schedule Across 36 Weeks")

st.markdown("""
Plan your 72 lessons per grade (twice weekly, 36 weeks) aligned with historical eras.
Track status, priority, and notes for each lesson slot.
""")

# Grade selector
grade = st.selectbox(
    "Select Grade",
    ["K", "1", "2", "3", "4", "5", "6", "7", "8"],
    index=0
)

# Get objectives for this grade
all_nodes = st.session_state.graph_manager.get_all_nodes()
grade_objectives = [n for n in all_nodes if f"{grade}.O" in n or f"Grade {grade}" in n]

st.metric(f"Grade {grade} Objectives Loaded", len(grade_objectives))

st.divider()

# Quarter tabs
quarter_tabs = st.tabs(["Q1: Foundations", "Q2: Cultural Math", "Q3: Applied Math", "Q4: Future Math"])

quarters = [
    {"name": "Q1: Foundations", "weeks": 9, "themes": [
        "Nature's Patterns", "Maya Number Systems", "Calendar Mathematics",
        "Geometric Patterns in Architecture", "Phoenix Desert Mathematics",
        "Indigenous Knowledge Systems", "Fibonacci in Nature", "Fractals and Self-Similarity",
        "Quarter 1 Assessment"
    ]},
    {"name": "Q2: Cultural Mathematics", "weeks": 9, "themes": [
        "Egyptian Geometry & Pyramids", "Islamic Geometric Patterns", "Chinese Mathematical Innovations",
        "Native American Star Knowledge", "African Mathematical Traditions", "European Renaissance Mathematics",
        "Modern Mathematical Art", "Technology & Visualization", "Quarter 2 Synthesis"
    ]},
    {"name": "Q3: Applied Mathematics", "weeks": 9, "themes": [
        "Architecture & Engineering", "Music & Mathematical Ratios", "Sports Statistics & Probability",
        "Environmental Mathematics", "Economics & Financial Literacy", "Medical Mathematics",
        "Space Exploration Mathematics", "Artificial Intelligence Basics", "Quarter 3 Capstone"
    ]},
    {"name": "Q4: Future Mathematics", "weeks": 9, "themes": [
        "Climate Change Modeling", "Quantum Mathematics Intro", "Biotechnology & Genetics",
        "Robotics & Programming", "Virtual Reality Mathematics", "Student-Led Research",
        "Community Problem Solving", "Portfolio Presentations", "Year Reflection & Celebration"
    ]}
]

for idx, tab in enumerate(quarter_tabs):
    with tab:
        quarter = quarters[idx]
        st.markdown(f"### {quarter['name']}")
        st.caption(f"{quarter['weeks']} weeks • 18 lessons (twice weekly)")
        
        for week_num, theme in enumerate(quarter['themes'], 1):
            global_week = (idx * 9) + week_num
            
            with st.expander(f"**Week {global_week}: {theme}**", expanded=(global_week == 1)):
                # Assign objectives to this week (simplified - you'd customize this)
                week_start = (global_week - 1) * 2
                week_end = week_start + 2
                week_objectives = grade_objectives[week_start:week_end] if week_start < len(grade_objectives) else []
                
                # Status selector
                col1, col2, col3 = st.columns(3)
                with col1:
                    status = st.selectbox(
                        "Status",
                        ["not-started", "planned", "in-progress", "complete"],
                        key=f"status_{grade}_{global_week}"
                    )
                with col2:
                    priority = st.selectbox(
                        "Priority",
                        ["low", "medium", "high"],
                        key=f"priority_{grade}_{global_week}",
                        index=1
                    )
                with col3:
                    lessons_ready = st.number_input(
                        "Lessons Ready",
                        min_value=0,
                        max_value=2,
                        value=0 if status == "not-started" else (2 if status == "complete" else 1),
                        key=f"lessons_{grade}_{global_week}"
                    )
                
                # Show assigned objectives
                if week_objectives:
                    st.markdown("**Assigned Objectives:**")
                    for obj in week_objectives:
                        node_data = st.session_state.graph_manager.get_node_data(obj)
                        st.caption(f"• {obj}")
                        if node_data and node_data.get('dimensional_level'):
                            st.caption(f"  → Dimension: {node_data['dimensional_level']}")
                else:
                    st.info("No objectives assigned to this week yet")
                
                # Notes
                notes = st.text_area(
                    "Notes & Resources",
                    placeholder="Add planning notes, resource links, or ideas for this week...",
                    key=f"notes_{grade}_{global_week}",
                    height=100
                )
                
                # Historical era tag
                era = st.selectbox(
                    "Historical Era Focus",
                    ["", "Ancient Mesopotamia (~3500 BCE)", "Ancient Egypt (~3000 BCE)", 
                     "Ancient Greece (~500 BCE)", "Islamic Golden Age (8th-13th c.)",
                     "Renaissance Europe (14th-17th c.)", "Modern Era (20th c.)", "Contemporary"],
                    key=f"era_{grade}_{global_week}"
                )

st.divider()

# Summary statistics
st.markdown("### Year Progress Summary")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Weeks", "36")
with col2:
    st.metric("Total Lessons", "72 (2x/week)")
with col3:
    st.metric("Objectives Created", len(grade_objectives))
with col4:
    completion_pct = int((len(grade_objectives) / 72) * 100) if len(grade_objectives) < 72 else 100
    st.metric("Objectives Completion", f"{completion_pct}%")

st.caption("💡 Use the Manage Content page to create more objectives and align them with specific weeks.")
