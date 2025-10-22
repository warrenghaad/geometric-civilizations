import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore
from PIL import Image
import os

st.set_page_config(page_title="Manage Content", page_icon="✏️", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.selected_node = None
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("✏️ Manage Curriculum Content")
st.markdown("### Add, Edit, and Connect Nodes")

# Tab selection
tab = st.radio(
    "Action",
    ["Add Node", "Edit Node", "Add Relationship", "Upload Image", "Bulk Operations"],
    horizontal=True
)

st.divider()

if tab == "Add Node":
    st.subheader("Add New Curriculum Node")
    
    col1, col2 = st.columns(2)
    
    with col1:
        node_name = st.text_input("Node Name/ID", placeholder="e.g., 5.O6 or Babylonian Star Maps")
        node_type = st.selectbox(
            "Node Type",
            ["Table", "Course", "Module", "Concept", "Database", "Schema", "Other"]
        )
        grade_level = st.selectbox(
            "Grade Level",
            ["", "K", "1", "2", "3", "4", "5", "6", "7", "8"]
        )
        dimensional_level = st.selectbox(
            "Dimensional Level",
            ["", "D1a (Atomic)", "D1b (Molecular)", "D2 (How)", "D3 (Why)", "D4 (What-if)"]
        )
    
    with col2:
        variables = st.multiselect(
            "Variables Engaged",
            ["Math", "Arts", "Mythology", "Power"]
        )
        historical_era = st.selectbox(
            "Historical Era",
            ["", "Ancient Mesopotamia (~3500 BCE)", "Ancient Egypt (~3000 BCE)", 
             "Ancient Greece (~500 BCE)", "Islamic Golden Age (8th-13th c.)",
             "Renaissance Europe (14th-17th c.)", "Modern Era (20th c.)", "Contemporary"]
        )
        status = st.selectbox(
            "Status",
            ["not-started", "planned", "in-progress", "complete"]
        )
        priority = st.selectbox(
            "Priority",
            ["low", "medium", "high"],
            index=1
        )
    
    node_description = st.text_area(
        "Description",
        placeholder="Student objective (I can...) or component description",
        height=100
    )
    
    # Cognitive domains
    st.markdown("**Cognitive Domains (select which apply heavily)**")
    domain_cols = st.columns(3)
    cognitive_domains = {}
    
    domains = ["Attention", "Memory", "Executive Functions", "Language", "Learning",
               "Visuospatial Processing", "Social Cognition", "Emotional Processing", "Metacognition"]
    
    for idx, domain in enumerate(domains):
        with domain_cols[idx % 3]:
            weight = st.selectbox(
                domain,
                ["none", "low", "medium", "high"],
                key=f"domain_{domain}"
            )
            if weight != "none":
                cognitive_domains[domain] = weight
    
    # Verbs
    verbs_input = st.text_input(
        "Verbs (comma-separated)",
        placeholder="e.g., analyze, create, compare, justify"
    )
    verbs = [v.strip() for v in verbs_input.split(",")] if verbs_input else []
    
    notes = st.text_area("Notes", height=80)
    
    if st.button("Add Node", type="primary"):
        if node_name:
            success = st.session_state.graph_manager.add_node(
                node_name=node_name,
                node_type=node_type,
                description=node_description,
                variables=variables,
                dimensional_level=dimensional_level,
                historical_era=historical_era,
                cognitive_domains=cognitive_domains,
                verbs=verbs,
                grade_level=grade_level
            )
            if success:
                # Update status, priority, notes
                st.session_state.graph_manager.update_node(
                    node_name,
                    status=status,
                    priority=priority,
                    notes=notes
                )
                st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                st.success(f"Node '{node_name}' added successfully!")
                st.rerun()
            else:
                st.error("Node already exists!")
        else:
            st.error("Please enter a node name")

elif tab == "Edit Node":
    st.subheader("Edit Existing Node")
    
    nodes = st.session_state.graph_manager.get_all_nodes()
    if not nodes:
        st.info("No nodes to edit. Add some nodes first.")
    else:
        node_to_edit = st.selectbox("Select Node", [""] + sorted(nodes))
        
        if node_to_edit:
            node_data = st.session_state.graph_manager.get_node_data(node_to_edit)
            
            if node_data:
                col1, col2 = st.columns(2)
                
                with col1:
                    new_type = st.selectbox(
                        "Node Type",
                        ["Table", "Course", "Module", "Concept", "Database", "Schema", "Other"],
                        index=["Table", "Course", "Module", "Concept", "Database", "Schema", "Other"].index(
                            node_data.get('type', 'Other'))
                    )
                    new_grade = st.selectbox(
                        "Grade Level",
                        ["", "K", "1", "2", "3", "4", "5", "6", "7", "8"],
                        index=["", "K", "1", "2", "3", "4", "5", "6", "7", "8"].index(
                            node_data.get('grade_level', ''))
                    )
                    new_dim = st.selectbox(
                        "Dimensional Level",
                        ["", "D1a (Atomic)", "D1b (Molecular)", "D2 (How)", "D3 (Why)", "D4 (What-if)"],
                        index=["", "D1a (Atomic)", "D1b (Molecular)", "D2 (How)", "D3 (Why)", "D4 (What-if)"].index(
                            node_data.get('dimensional_level', '')) if node_data.get('dimensional_level', '') in 
                            ["", "D1a (Atomic)", "D1b (Molecular)", "D2 (How)", "D3 (Why)", "D4 (What-if)"] else 0
                    )
                
                with col2:
                    new_variables = st.multiselect(
                        "Variables",
                        ["Math", "Arts", "Mythology", "Power"],
                        default=node_data.get('variables', [])
                    )
                    new_era = st.text_input(
                        "Historical Era",
                        value=node_data.get('historical_era', '')
                    )
                    new_status = st.selectbox(
                        "Status",
                        ["not-started", "planned", "in-progress", "complete"],
                        index=["not-started", "planned", "in-progress", "complete"].index(
                            node_data.get('status', 'not-started'))
                    )
                
                new_description = st.text_area(
                    "Description",
                    value=node_data.get('description', ''),
                    height=100
                )
                
                new_verbs = st.text_input(
                    "Verbs (comma-separated)",
                    value=", ".join(node_data.get('verbs', []))
                )
                verbs_list = [v.strip() for v in new_verbs.split(",")] if new_verbs else []
                
                new_notes = st.text_area(
                    "Notes",
                    value=node_data.get('notes', ''),
                    height=80
                )
                
                col_a, col_b = st.columns(2)
                with col_a:
                    if st.button("Update Node", type="primary"):
                        st.session_state.graph_manager.update_node(
                            node_to_edit,
                            type=new_type,
                            description=new_description,
                            variables=new_variables,
                            dimensional_level=new_dim,
                            historical_era=new_era,
                            verbs=verbs_list,
                            grade_level=new_grade,
                            status=new_status,
                            notes=new_notes
                        )
                        st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                        st.success(f"Node '{node_to_edit}' updated!")
                        st.rerun()
                
                with col_b:
                    if st.button("Delete Node", type="secondary"):
                        st.session_state.graph_manager.remove_node(node_to_edit)
                        st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                        st.success(f"Node '{node_to_edit}' deleted!")
                        st.session_state.selected_node = None
                        st.rerun()

elif tab == "Add Relationship":
    st.subheader("Connect Nodes")
    
    nodes = st.session_state.graph_manager.get_all_nodes()
    if len(nodes) < 2:
        st.info("You need at least 2 nodes to create a relationship")
    else:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            source = st.selectbox("Source Node", [""] + sorted(nodes))
        with col2:
            target = st.selectbox("Target Node", [""] + sorted(nodes))
        with col3:
            rel_type = st.selectbox(
                "Relationship Type",
                ["", "builds-on", "requires", "aligned-to", "implements", "contains", "activates", "nested-in"]
            )
        
        if st.button("Add Relationship", type="primary"):
            if source and target and source != target:
                st.session_state.graph_manager.add_edge(source, target, rel_type)
                st.session_state.graph_manager.save_to_store(st.session_state.data_store)
                st.success(f"Relationship added: {source} → {target}")
                st.rerun()
            else:
                st.error("Please select different source and target nodes")

elif tab == "Upload Image":
    st.subheader("Upload & Link Images")
    
    nodes = st.session_state.graph_manager.get_all_nodes()
    if not nodes:
        st.info("Add nodes first before uploading images")
    else:
        selected_node = st.selectbox("Link image to node", [""] + sorted(nodes))
        uploaded_file = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg', 'gif', 'webp'])
        
        if uploaded_file and selected_node and st.button("Upload & Link", type="primary"):
            # Save image
            image_path = st.session_state.data_store.save_image(uploaded_file, selected_node)
            
            # Link to node
            st.session_state.graph_manager.add_image_to_node(selected_node, image_path)
            st.session_state.graph_manager.save_to_store(st.session_state.data_store)
            
            st.success(f"Image uploaded and linked to '{selected_node}'")
            st.rerun()

elif tab == "Bulk Operations":
    st.subheader("Bulk Operations")
    
    st.markdown("#### Export/Import")
    
    if st.button("Export Graph Data (JSON)"):
        import json
        graph_data = st.session_state.graph_manager.get_graph_data()
        json_str = json.dumps(graph_data, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_str,
            file_name="curriculum_graph.json",
            mime="application/json"
        )
    
    st.markdown("#### Quick Stats")
    all_nodes = st.session_state.graph_manager.get_all_nodes()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Nodes", len(all_nodes))
    with col2:
        tagged_with_dims = sum(1 for n in all_nodes 
                               if st.session_state.graph_manager.get_node_data(n).get('dimensional_level'))
        st.metric("Nodes with Dimensions", tagged_with_dims)
    with col3:
        tagged_with_vars = sum(1 for n in all_nodes 
                              if st.session_state.graph_manager.get_node_data(n).get('variables'))
        st.metric("Nodes with Variables", tagged_with_vars)
