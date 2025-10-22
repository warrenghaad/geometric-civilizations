import streamlit as st
import os
from graph_manager import GraphManager
from data_store import DataStore

# Must be the first Streamlit command
st.set_page_config(
    page_title="Pyramidic Curriculum Ziggurat",
    page_icon="🏛️",
    layout="wide"
)

# Initialize session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.selected_node = None
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("🏛️ Pyramidic Curriculum Ziggurat")
st.markdown("### Multi-Dimensional K-8 Integrated Curriculum Design System")

st.markdown("""
Welcome to your curriculum design ziggurat—a multi-layered visualization and planning tool 
that maps **Standards**, **Variables** (Math, Arts, Mythology, Power), **Cognitive Domains**, 
**Historical Eras**, and **Dimensional Complexity** across 9 grades.

### Navigation

Use the sidebar to explore different views of your curriculum:

- **🏛️ Ziggurat View (3D)**: See the full pyramid structure with all layers stacked
- **📚 Library Navigator**: Drill down shelf → row → content (grade → variable → lesson type)
- **🔍 Layer Slicer**: View horizontal slices (just standards, just D4 peaks, etc.)
- **🔗 Verb Network**: Search by cognitive verb to see connections
- **📅 Timeline Calendar**: Twice-weekly schedule with historical eras
- **⚙️ Variables Dashboard**: Explore Math, Arts, Mythology, Power interactions
- **✏️ Manage Content**: Add/edit nodes and relationships

### The Pyramid Structure

**Foundation (Bottom)**  
Arizona Common Core + SDA School Standards — 72 twice-weekly lessons per grade

**Layer 2: The 4 Variables**  
Math • Arts • Mythology • Power (woven as context/gatekeeping)

**Layer 3: 2D Work Squares**  
Variable pairs creating "area of work" (Math+Arts, Myth+Power, etc.)

**Layer 4: Truncated Pyramids**  
Incremental improvements stacking (smaller work squares)

**Peak: Invention**  
Where all 4 variables align → breakthrough insight

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
