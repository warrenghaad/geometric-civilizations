import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore
from visualization import create_3d_visualization
from PIL import Image
import os

st.set_page_config(page_title="Ziggurat View", page_icon="🏛️", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.selected_node = None
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("🏛️ Ziggurat 3D View")
st.markdown("### The Full Pyramid Structure")

st.markdown("""
This view shows all curriculum layers stacked like a ziggurat:
- **Foundation**: Standards (Common Core + SDA)
- **Layer 2**: The 4 Variables (Math, Arts, Mythology, Power)
- **Layer 3**: Work Squares (variable intersections)
- **Layer 4**: Cognitive Domains
- **Layer 5**: Vertical Threads
- **Peak**: Invention/Integration moments
""")

# Filter controls
col1, col2, col3 = st.columns(3)
with col1:
    layer_filter = st.multiselect(
        "Show Layers",
        ["All", "Standards", "Variables", "Domains", "Threads", "Objectives"],
        default=["All"]
    )
with col2:
    grade_filter = st.selectbox(
        "Grade Focus",
        ["All Grades", "K", "1", "2", "3", "4", "5", "6", "7", "8"]
    )
with col3:
    dimension_filter = st.selectbox(
        "Dimensional Level",
        ["All Levels", "D1a (Atomic)", "D1b (Molecular)", "D2 (How)", "D3 (Why)", "D4 (What-if)"]
    )

st.divider()

# Main 3D visualization
col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("3D Network Graph")
    
    # Create and display 3D visualization
    fig = create_3d_visualization(st.session_state.graph_manager)
    
    if fig:
        # Display the plot
        selected_points = st.plotly_chart(
            fig,
            use_container_width=True,
            key="ziggurat_plot",
            on_select="rerun",
            selection_mode="points"
        )
        
        # Handle node selection from plot clicks
        if selected_points and selected_points.selection and selected_points.selection.points:
            if len(selected_points.selection.points) > 0:
                point = selected_points.selection.points[0]
                if 'customdata' in point and point['customdata']:
                    st.session_state.selected_node = point['customdata'][0]
    else:
        st.info("No nodes to display. Use the Manage Content page to add curriculum components.")

with col_right:
    st.subheader("Selected Node Details")
    
    if st.session_state.selected_node:
        node_data = st.session_state.graph_manager.get_node_data(st.session_state.selected_node)
        
        if node_data:
            st.markdown(f"### {st.session_state.selected_node}")
            st.markdown(f"**Type:** {node_data.get('type', 'N/A')}")
            
            # Show pyramidic metadata
            if node_data.get('variables'):
                st.markdown(f"**Variables:** {', '.join(node_data['variables'])}")
            if node_data.get('dimensional_level'):
                st.markdown(f"**Dimension:** {node_data['dimensional_level']}")
            if node_data.get('historical_era'):
                st.markdown(f"**Era:** {node_data['historical_era']}")
            if node_data.get('grade_level'):
                st.markdown(f"**Grade:** {node_data['grade_level']}")
            
            # Cognitive domains
            if node_data.get('cognitive_domains'):
                st.markdown("**Cognitive Domains:**")
                for domain, weight in node_data['cognitive_domains'].items():
                    st.caption(f"• {domain}: {weight}")
            
            # Verbs
            if node_data.get('verbs'):
                st.markdown(f"**Verbs:** {', '.join(node_data['verbs'])}")
            
            # Description
            description = node_data.get('description', '')
            if description:
                st.markdown("**Description:**")
                st.markdown(description)
            
            # Display relationships
            connections = st.session_state.graph_manager.get_node_connections(st.session_state.selected_node)
            if connections['incoming'] or connections['outgoing']:
                st.markdown("**Connections:**")
                
                if connections['outgoing']:
                    st.markdown("*Points to:*")
                    for target, rel_type in connections['outgoing']:
                        rel_label = f" ({rel_type})" if rel_type else ""
                        st.caption(f"→ {target}{rel_label}")
                
                if connections['incoming']:
                    st.markdown("*Pointed from:*")
                    for source, rel_type in connections['incoming']:
                        rel_label = f" ({rel_type})" if rel_type else ""
                        st.caption(f"← {source}{rel_label}")
            
            # Display images
            images = node_data.get('images', [])
            if images:
                st.markdown("**Associated Images:**")
                for img_path in images:
                    if os.path.exists(img_path):
                        try:
                            image = Image.open(img_path)
                            st.image(image, use_container_width=True)
                        except Exception as e:
                            st.error(f"Error loading image: {str(e)}")
            
            if st.button("Clear Selection"):
                st.session_state.selected_node = None
                st.rerun()
    else:
        st.info("Click on a node in the graph to view its details")

st.divider()

# Statistics
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
all_nodes = st.session_state.graph_manager.get_all_nodes()

with stats_col1:
    st.metric("Total Nodes", len(all_nodes))
with stats_col2:
    st.metric("Relationships", st.session_state.graph_manager.get_edge_count())
with stats_col3:
    objectives = sum(1 for n in all_nodes if 'O' in n and ':' in n)
    st.metric("Objectives", objectives)
with stats_col4:
    node_types = st.session_state.graph_manager.get_node_type_counts()
    st.metric("Node Types", len(node_types))
