import streamlit as st
import os
from graph_manager import GraphManager
from data_store import DataStore

# Must be the first Streamlit command
st.set_page_config(
    page_title="SDA Mesa/Phoenix Curriculum Mapper",
    page_icon="🏫",
    layout="wide"
)

# Initialize session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.selected_node = None
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("🏫 SDA Mesa/Phoenix K-8 Curriculum Mapper")
st.markdown("### 2025-2026 School Year • 180 Days • Twice Weekly (72 Teaching Days)")

st.markdown("""
This is your curriculum mapping and visualization tool for the SDA Mesa/Phoenix integrated K-8 program.

Map **SDA Standards** and **AZ Common Core** to a **180-day calendar**, organized across:
- **4 Variables**: Math, Arts, Mythology, Power
- **9 Cognitive Domains**: Neuroscience-based learning targets
- **Dimensional Levels**: D1a → D4 complexity assessment
- **School Building Metaphor**: Open floor plan showing horizontal (weekly) and vertical (K-8) alignment

### Navigation

Use the sidebar to explore:

- **📚 Library Navigator**: Browse curriculum by category (Lessons, Research, Slides, Mapping, etc.)
- **📆 School Calendar**: Map standards to the 180-day calendar (view by week, month, or SDA/AZ CC)
- **🏫 School Building**: 2D grid views showing standards coverage across grade-week cells
- **⚙️ Variables Dashboard**: Explore the 4 Variables and their intersections
- **✏️ Manage Content**: Add/edit objectives, standards, and relationships

### School Building Metaphor

Think of curriculum as an **open floor plan school building**:
- **Grades = Rooms** (K through 8)
- **Weeks = Hallways** (horizontal alignment)
- **Standards = Plumbing** (vertical progression K→8)
- **Cognitive Domains = Wiring** (neural activation patterns)
- **Students = Objectives** (placed in grade-week rooms)

### Cross-Cutting Networks

- **9 Cognitive Domains**: Attention, Memory, Executive Functions, Language, Learning, 
  Visuospatial Processing, Social Cognition, Emotional Processing, Metacognition
- **Dimensional Assessment**: D1a (atomic) → D1b (molecular) → D2 (How) → D3 (Why) → D4 (What-if)
- **Historical Eras**: Babylonian, Egyptian, Greek, Islamic, Renaissance, etc.
- **Verb Search**: Analyze, create, justify, compare, etc. across all layers

### Current Status
""")

# Statistics
nodes = st.session_state.graph_manager.get_all_nodes()
edges_count = st.session_state.graph_manager.get_edge_count()
type_counts = st.session_state.graph_manager.get_node_type_counts()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Nodes", len(nodes))
with col2:
    st.metric("Relationships", edges_count)
with col3:
    st.metric("Node Types", len(type_counts))
with col4:
    objectives = sum(1 for n in nodes if 'O' in n and ':' in n)
    st.metric("Objectives", objectives)

st.markdown("---")
st.markdown("👈 **Select a page from the sidebar to begin exploring your curriculum.**")
