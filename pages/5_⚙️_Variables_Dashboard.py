import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore

st.set_page_config(page_title="Variables Dashboard", page_icon="⚙️", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("⚙️ Variables Dashboard")
st.markdown("### The 4 Forces of Cultural Innovation")

st.markdown("""
Explore how **Math**, **Arts**, **Mythology**, and **Power** interact across your curriculum.

**Variable Interactions:**  
- **2 variables** interact → create a 2D Work Square (area = labor required)
- **Incremental discoveries** → build understanding over time
- **All 4 variables align** → emergent insight → INVENTION moment
""")

# Variable selector
variable_tabs = st.tabs(["📐 Math", "🎨 Arts", "📖 Mythology", "⚡ Power", "🔄 Work Squares"])

all_nodes = st.session_state.graph_manager.get_all_nodes()

with variable_tabs[0]:  # Math
    st.markdown("### 📐 Math Variable")
    st.markdown("""
    **Logical Relationships & Pattern Recognition**
    - Understanding quantitative relationships
    - Recognizing patterns in nature, design, and structure
    - Formalizing observations into rules and proofs
    - Measuring, calculating, and predicting outcomes
    """)
    
    math_nodes = [n for n in all_nodes if 'Math' in n or 'Geometry' in n]
    st.metric("Math/Geometry Nodes", len(math_nodes))
    
    if math_nodes:
        st.markdown("#### Key Math Nodes:")
        for node in math_nodes[:10]:
            node_data = st.session_state.graph_manager.get_node_data(node)
            with st.expander(node):
                st.caption(f"**Type:** {node_data.get('type', 'N/A')}")
                st.markdown(node_data.get('description', ''))

with variable_tabs[1]:  # Arts
    st.markdown("### 🎨 Arts Variable")
    st.markdown("""
    **Cultural Aesthetics & Visual Internalization**
    - Visual language in objects, textiles, fashion, architecture
    - Cultural aesthetics that differentiate societies
    - How beauty and design choices are internalized
    - Stylistic differences (Greek, Babylonian, Islamic art)
    """)
    
    arts_nodes = [n for n in all_nodes if 'Art' in n or 'Architecture' in n]
    st.metric("Arts/Architecture Nodes", len(arts_nodes))
    
    if arts_nodes:
        st.markdown("#### Key Arts Nodes:")
        for node in arts_nodes[:10]:
            node_data = st.session_state.graph_manager.get_node_data(node)
            with st.expander(node):
                st.caption(f"**Type:** {node_data.get('type', 'N/A')}")
                st.markdown(node_data.get('description', ''))

with variable_tabs[2]:  # Mythology
    st.markdown("### 📖 Mythology Variable")
    st.markdown("""
    **Belief Systems & Meaning-Making**
    - Worldview, stories, and belief systems
    - Provides inspiration, purpose, and meaning
    - Reveals culture's values, hierarchies, cosmic order
    - Connected to SEL (emotions, ethics, meaning)
    
    *Why build monuments? Why perfect astronomy? Why create cathedrals?*
    """)
    
    myth_nodes = [n for n in all_nodes if 'Myth' in n or 'Culture' in n or 'SEL' in n]
    st.metric("Mythology/Culture/SEL Nodes", len(myth_nodes))
    
    if myth_nodes:
        st.markdown("#### Key Mythology/Culture Nodes:")
        for node in myth_nodes[:10]:
            node_data = st.session_state.graph_manager.get_node_data(node)
            with st.expander(node):
                st.caption(f"**Type:** {node_data.get('type', 'N/A')}")
                st.markdown(node_data.get('description', ''))

with variable_tabs[3]:  # Power
    st.markdown("### ⚡ Power Variable")
    st.markdown("""
    **Resource Allocation & Gatekeeping**
    - Who controls resources and decides what gets built
    - Who acts as gatekeepers to knowledge and materials
    - How labor is organized, who funds innovation
    - Social hierarchies reinforced through objects and spaces
    
    *Power is woven as context throughout all lessons—not a standalone day.*
    """)
    
    power_nodes = [n for n in all_nodes if 'Power' in n or 'Society' in n]
    st.metric("Power/Society Nodes", len(power_nodes))
    
    st.info("""
    **Power as Gatekeeping Context:**
    - Who told these myths? *Priests*
    - Who had access to sacred texts? *Scribes*
    - Who could afford purple dye? *Royalty*
    - Who controlled mathematical knowledge? *Guilds*
    """)
    
    if power_nodes:
        st.markdown("#### Key Power/Society Nodes:")
        for node in power_nodes[:10]:
            node_data = st.session_state.graph_manager.get_node_data(node)
            with st.expander(node):
                st.caption(f"**Type:** {node_data.get('type', 'N/A')}")
                st.markdown(node_data.get('description', ''))

with variable_tabs[4]:  # Work Squares
    st.markdown("### 🔄 2D Work Squares")
    st.markdown("""
    When **2 variables interact**, they create a **2D Work Square**:
    - **Area** = Total labor required to accomplish something
    - **Diagonal** = Efficiency (shorter = more efficient)
    
    Examples:
    - **Math + Arts:** Potter learns circular motion → symmetrical vessels
    - **Mythology + Power:** Divine kingship belief → pharaoh organizes monumental labor
    - **Arts + Power:** Fashion/textiles → reinforce class hierarchies
    """)
    
    # Show potential work square combinations
    work_squares = [
        ("Math + Arts", "Geometric patterns in art, tessellations, symmetry in design"),
        ("Math + Mythology", "Sacred geometry, cosmic proportions, divine numbers"),
        ("Math + Power", "Standardized measurements, architectural planning, resource calculation"),
        ("Arts + Mythology", "Religious iconography, symbolic motifs, cultural aesthetics"),
        ("Arts + Power", "Fashion as hierarchy, material objects as status, court aesthetics"),
        ("Mythology + Power", "Divine right, religious authority, belief-justified social order")
    ]
    
    for combo, description in work_squares:
        with st.expander(f"**Work Square: {combo}**"):
            st.markdown(description)
            st.caption("*Add objectives that engage both these variables to fill this work square*")

st.divider()
st.markdown("### Next Steps")
st.info("""
**To build your curriculum:**
1. Tag objectives with the variables they engage (use Manage Content page)
2. Look for moments where all 4 variables align → mark as D4 (What-if/Invention)
3. Map historical eras where each variable was particularly strong
4. Track which work squares are well-developed vs. need more objectives
""")
