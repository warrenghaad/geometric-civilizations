import streamlit as st
import os
from graph_manager import GraphManager
from data_store import DataStore
from visualization import create_3d_visualization
import base64
from PIL import Image
import io

# Initialize session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.selected_node = None
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

# Page configuration
st.set_page_config(
    page_title="3D Curriculum & Database Mapper",
    page_icon="🔮",
    layout="wide"
)

st.title("🔮 3D Curriculum & Database Relationship Mapper")

# Sidebar for controls
with st.sidebar:
    st.header("Controls")
    
    # Tab selection
    tab = st.radio("Select Action", ["View Graph", "Add Node", "Add Relationship", "Upload Image", "Edit Node"])
    
    st.divider()
    
    if tab == "Add Node":
        st.subheader("Add New Node")
        
        node_name = st.text_input("Node Name", key="new_node_name")
        node_type = st.selectbox(
            "Node Type",
            ["Course", "Module", "Concept", "Database", "Table", "Schema", "Other"],
            key="new_node_type"
        )
        node_description = st.text_area("Description", key="new_node_desc")
        
        if st.button("Add Node", type="primary"):
            if node_name:
                success = st.session_state.graph_manager.add_node(
                    node_name,
                    node_type,
                    node_description
                )
                if success:
                    st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                    st.success(f"Node '{node_name}' added successfully!")
                    st.rerun()
                else:
                    st.error("Node already exists!")
            else:
                st.error("Please enter a node name")
    
    elif tab == "Add Relationship":
        st.subheader("Add Relationship")
        
        nodes = st.session_state.graph_manager.get_all_nodes()
        if len(nodes) < 2:
            st.info("You need at least 2 nodes to create a relationship")
        else:
            source = st.selectbox("Source Node", nodes, key="rel_source")
            target = st.selectbox("Target Node", nodes, key="rel_target")
            rel_type = st.text_input("Relationship Type (optional)", key="rel_type")
            
            if st.button("Add Relationship", type="primary"):
                if source != target:
                    st.session_state.graph_manager.add_edge(source, target, rel_type)
                    st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                    st.success(f"Relationship added: {source} → {target}")
                    st.rerun()
                else:
                    st.error("Source and target must be different")
    
    elif tab == "Upload Image":
        st.subheader("Upload & Link Image")
        
        nodes = st.session_state.graph_manager.get_all_nodes()
        if not nodes:
            st.info("Add nodes first before uploading images")
        else:
            selected_node_for_image = st.selectbox("Select Node", nodes, key="img_node")
            uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg', 'gif', 'webp'])
            
            if uploaded_file and st.button("Upload & Link", type="primary"):
                # Save image
                image_path = st.session_state.data_store.save_image(uploaded_file, selected_node_for_image)
                
                # Link to node
                st.session_state.graph_manager.add_image_to_node(selected_node_for_image, image_path)
                st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                
                st.success(f"Image uploaded and linked to '{selected_node_for_image}'")
                st.rerun()
    
    elif tab == "Edit Node":
        st.subheader("Edit Node")
        
        nodes = st.session_state.graph_manager.get_all_nodes()
        if not nodes:
            st.info("No nodes to edit")
        else:
            node_to_edit = st.selectbox("Select Node", nodes, key="edit_node_select")
            node_data = st.session_state.graph_manager.get_node_data(node_to_edit)
            
            if node_data:
                new_description = st.text_area(
                    "Description",
                    value=node_data.get('description', ''),
                    key="edit_desc"
                )
                new_type = st.selectbox(
                    "Node Type",
                    ["Course", "Module", "Concept", "Database", "Table", "Schema", "Other"],
                    index=["Course", "Module", "Concept", "Database", "Table", "Schema", "Other"].index(node_data.get('type', 'Other')),
                    key="edit_type"
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Update Node", type="primary"):
                        st.session_state.graph_manager.update_node(
                            node_to_edit,
                            new_type,
                            new_description
                        )
                        st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                        st.success(f"Node '{node_to_edit}' updated!")
                        st.rerun()
                
                with col2:
                    if st.button("Delete Node", type="secondary"):
                        st.session_state.graph_manager.remove_node(node_to_edit)
                        st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                        st.success(f"Node '{node_to_edit}' deleted!")
                        st.session_state.selected_node = None
                        st.rerun()

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("3D Relationship Graph")
    
    # Create and display 3D visualization
    fig = create_3d_visualization(st.session_state.graph_manager)
    
    if fig:
        # Display the plot
        selected_points = st.plotly_chart(
            fig,
            use_container_width=True,
            key="graph_plot",
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
        st.info("👈 Add nodes using the sidebar to start building your graph!")
        st.markdown("""
        ### Getting Started
        1. **Add Nodes**: Create curriculum components (courses, modules, concepts) or database entities
        2. **Add Relationships**: Connect nodes to show how they relate to each other
        3. **Upload Images**: Attach visual resources to your nodes
        4. **Explore**: Click on nodes in the 3D graph to view details and images
        
        ### Node Types
        - **Course**: Top-level curriculum items
        - **Module**: Sections within courses
        - **Concept**: Individual learning concepts
        - **Database**: Database systems
        - **Table**: Database tables
        - **Schema**: Database schemas
        """)

with col2:
    st.subheader("Node Details")
    
    if st.session_state.selected_node:
        node_data = st.session_state.graph_manager.get_node_data(st.session_state.selected_node)
        
        if node_data:
            st.markdown(f"### {st.session_state.selected_node}")
            st.markdown(f"**Type:** {node_data.get('type', 'N/A')}")
            
            description = node_data.get('description', '')
            if description:
                st.markdown(f"**Description:**")
                st.markdown(description)
            
            # Display relationships
            connections = st.session_state.graph_manager.get_node_connections(st.session_state.selected_node)
            if connections['incoming'] or connections['outgoing']:
                st.markdown("**Connections:**")
                
                if connections['outgoing']:
                    st.markdown("*Points to:*")
                    for target, rel_type in connections['outgoing']:
                        rel_label = f" ({rel_type})" if rel_type else ""
                        st.markdown(f"- {target}{rel_label}")
                
                if connections['incoming']:
                    st.markdown("*Pointed from:*")
                    for source, rel_type in connections['incoming']:
                        rel_label = f" ({rel_type})" if rel_type else ""
                        st.markdown(f"- {source}{rel_label}")
            
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

# Footer statistics
st.divider()
stats_col1, stats_col2, stats_col3 = st.columns(3)

with stats_col1:
    st.metric("Total Nodes", len(st.session_state.graph_manager.get_all_nodes()))

with stats_col2:
    st.metric("Total Relationships", st.session_state.graph_manager.get_edge_count())

with stats_col3:
    node_types = st.session_state.graph_manager.get_node_type_counts()
    st.metric("Node Types", len(node_types))
