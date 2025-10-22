import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore

st.set_page_config(page_title="Library Navigator", page_icon="📚", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("📚 Curriculum Library Navigator")
st.markdown("### Drill down: Shelf → Row → Book → Page")

st.markdown("""
Explore your curriculum like a library:
- **Shelves** = Grade Bands (K-1, 2-3, 4-5, 6, 7, 8)
- **Rows** = The 4 Variables (History/Mythology, Geometry/Math, Art, SEL)
- **Books** = Content Types (Lessons, Activities, Assessments, Integration Points)
- **Pages** = Individual objectives with dimensional depth
""")

# Search and filter controls
col1, col2 = st.columns([3, 1])
with col1:
    search_term = st.text_input("🔍 Search objectives, eras, or concepts", "")
with col2:
    show_all = st.checkbox("Show all details", value=False)

st.divider()

# Define the library structure based on grade bands
grade_bands = {
    "K-1": ["Kindergarten", "Grade 1"],
    "2-3": ["Grade 2", "Grade 3"],
    "4-5": ["Grade 4", "Grade 5"],
    "6": ["Grade 6"],
    "7": ["Grade 7"],
    "8": ["Grade 8"]
}

variables = ["History/Mythology", "Geometry/Math", "Art", "SEL"]

# Get all nodes
all_nodes = st.session_state.graph_manager.get_all_nodes()

# Organize nodes by grade and variable
for shelf_name, grades in grade_bands.items():
    with st.expander(f"📚 **Shelf: {shelf_name}**", expanded=(shelf_name == "K-1")):
        
        # Get objectives for this grade band
        shelf_objectives = []
        for grade in grades:
            grade_nodes = [n for n in all_nodes if grade in n]
            shelf_objectives.extend(grade_nodes)
        
        if search_term:
            shelf_objectives = [n for n in shelf_objectives 
                              if search_term.lower() in n.lower() or 
                              search_term.lower() in st.session_state.graph_manager.get_node_data(n).get('description', '').lower()]
        
        if not shelf_objectives:
            st.info(f"No objectives found for {shelf_name}")
            continue
        
        st.markdown(f"**{len(shelf_objectives)} objectives** in this shelf")
        
        # Organize by variable (rows)
        for variable in variables:
            st.markdown(f"#### 📖 Row: {variable}")
            
            # Filter objectives by variable
            if variable == "History/Mythology":
                var_keywords = ["myth", "retell", "story", "culture", "hero", "character"]
            elif variable == "Geometry/Math":
                var_keywords = ["shape", "pattern", "symmetry", "angle", "measure", "classify", 
                               "quadrilateral", "tessellation", "coordinate", "ratio"]
            elif variable == "Art":
                var_keywords = ["draw", "create", "design", "border", "motif", "visual"]
            else:  # SEL
                var_keywords = ["calm", "breathing", "feeling", "mindful", "emotion", "respectful"]
            
            row_objectives = [n for n in shelf_objectives 
                            if any(kw in n.lower() or 
                                  kw in st.session_state.graph_manager.get_node_data(n).get('description', '').lower()
                                  for kw in var_keywords)]
            
            if row_objectives:
                # Group by content type (simulated - could be enhanced with actual tags)
                for obj_name in row_objectives[:10]:  # Limit display
                    node_data = st.session_state.graph_manager.get_node_data(obj_name)
                    
                    col_a, col_b, col_c = st.columns([3, 1, 1])
                    with col_a:
                        st.markdown(f"**📄 {obj_name}**")
                        if show_all:
                            st.caption(node_data.get('description', '')[:200])
                    with col_b:
                        dim_level = node_data.get('dimensional_level', 'Not set')
                        if dim_level:
                            st.badge(dim_level, type="secondary")
                    with col_c:
                        status = node_data.get('status', 'not-started')
                        status_colors = {
                            'complete': '🟢',
                            'in-progress': '🟡',
                            'planned': '🔵',
                            'not-started': '⚪'
                        }
                        st.markdown(f"{status_colors.get(status, '⚪')} {status}")
                
                if len(row_objectives) > 10:
                    st.caption(f"... and {len(row_objectives) - 10} more")
            else:
                st.caption(f"_No {variable} objectives yet_")
            
            st.markdown("")  # Spacing

st.divider()
st.caption("💡 Use the Manage Content page to add more objectives and tag them with variables, dimensions, and eras.")
