import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore
import os

st.set_page_config(page_title="Library Navigator", page_icon="📚", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("📚 Curriculum Library Navigator")
st.markdown("### Browse curriculum resources by category")

st.markdown("""
Browse organized curriculum materials:
- **Lessons** - Daily lesson plans and instructional materials
- **Research** - Background research and theoretical foundations
- **Slides** - Presentation materials for instruction
- **Mapping** - Standards alignment and curriculum maps
- **Implementation Guides** - How-to guides for teachers
- **Assessments** - Evaluation tools and rubrics
- **Hands on Activities** - Physical and interactive projects
- **Images** - Visual resources and references
- **Combined Content** - Mythology, Art, Math, History General, Innovation
""")

# Get all nodes first
all_nodes = st.session_state.graph_manager.get_all_nodes()

# Search and filter controls
col1, col2 = st.columns([3, 1])
with col1:
    search_term = st.text_input("🔍 Search objectives, eras, or concepts", "")
with col2:
    show_all = st.checkbox("Show all details", value=False)

st.divider()

# Download button
import json
mapping_data = {
    "objectives": {},
    "standards": {},
    "calendar": {}
}

# Collect all objectives
for node in all_nodes:
    if ".O" in node:
        node_data = st.session_state.graph_manager.get_node_data(node)
        mapping_data["objectives"][node] = node_data

# Create downloadable JSON
json_str = json.dumps(mapping_data, indent=2)
st.download_button(
    label="📥 Download Mapping",
    data=json_str,
    file_name="curriculum_mapping.json",
    mime="application/json",
    type="primary"
)

st.divider()

# Define curriculum categories
curriculum_categories = {
    "📖 Lessons": "lesson",
    "🔬 Research": "research", 
    "📊 Slides": "slides",
    "🗺️ Mapping": "mapping",
    "📋 Implementation Guides": "guide",
    "📝 Assessments": "assessment",
    "🎨 Hands on Activities": "activity",
    "🖼️ Images": "image",
    "🌍 Combined: Mythology": "mythology",
    "🎭 Combined: Art": "art",
    "📐 Combined: Math": "math",
    "📚 Combined: History General": "history",
    "💡 Combined: Innovation": "innovation"
}

# Get all objectives
all_objectives = [n for n in all_nodes if ".O" in n]

if search_term:
    all_objectives = [n for n in all_objectives 
                      if search_term.lower() in n.lower() or 
                      search_term.lower() in st.session_state.graph_manager.get_node_data(n).get('description', '').lower()]

st.markdown(f"**{len(all_objectives)} total objectives** in library")
st.divider()

# Organize by category
for category_name, category_key in curriculum_categories.items():
    with st.expander(f"{category_name}", expanded=False):
        
        # Special handling for Images category
        if category_key == "image":
            st.markdown("### Visual Resources Gallery")
            
            # Get all images from both directories
            all_image_files = []
            images_dir = "data/images"
            stock_images_dir = "attached_assets/stock_images"
            
            if os.path.exists(images_dir):
                for filename in os.listdir(images_dir):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                        all_image_files.append(os.path.join(images_dir, filename))
            
            if os.path.exists(stock_images_dir):
                for filename in os.listdir(stock_images_dir):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                        all_image_files.append(os.path.join(stock_images_dir, filename))
            
            if not all_image_files:
                st.info("No images yet. Visit the 🖼️ Image Library page to find historical design motifs.")
            else:
                st.markdown(f"**{len(all_image_files)} images** in library")
                
                # Display in grid
                cols_per_row = 4
                for i in range(0, min(12, len(all_image_files)), cols_per_row):
                    cols = st.columns(cols_per_row)
                    
                    for j, col in enumerate(cols):
                        if i + j < len(all_image_files):
                            img_path = all_image_files[i + j]
                            filename = os.path.basename(img_path)
                            
                            with col:
                                try:
                                    st.image(img_path, use_container_width=True)
                                    st.caption(filename[:30])
                                    
                                    # Show linked objectives
                                    linked = []
                                    for node in all_objectives:
                                        node_data = st.session_state.graph_manager.get_node_data(node)
                                        if img_path in node_data.get('images', []):
                                            linked.append(node)
                                    
                                    if linked:
                                        st.caption(f"🔗 {linked[0]}")
                                except:
                                    st.caption(f"⚠️ {filename}")
                
                if len(all_image_files) > 12:
                    st.caption(f"... and {len(all_image_files) - 12} more images. Visit 🖼️ Image Library to browse all.")
            
            continue
        
        # Filter objectives by category keywords
        category_objectives = []
        
        for obj_name in all_objectives:
            node_data = st.session_state.graph_manager.get_node_data(obj_name)
            description = node_data.get('description', '').lower()
            obj_type = node_data.get('type', '').lower()
            
            # Match based on category
            if category_key in ["mythology", "art", "math", "history", "innovation"]:
                # Subject-based filtering
                if category_key == "mythology" and any(kw in description for kw in ["myth", "story", "hero", "culture", "retell"]):
                    category_objectives.append(obj_name)
                elif category_key == "art" and any(kw in description for kw in ["draw", "create", "design", "visual", "border", "motif"]):
                    category_objectives.append(obj_name)
                elif category_key == "math" and any(kw in description for kw in ["shape", "pattern", "symmetry", "angle", "measure", "classify"]):
                    category_objectives.append(obj_name)
                elif category_key == "history" and any(kw in description for kw in ["civilization", "timeline", "era", "period"]):
                    category_objectives.append(obj_name)
                elif category_key == "innovation" and any(kw in description for kw in ["invent", "create", "design", "problem", "solution"]):
                    category_objectives.append(obj_name)
            else:
                # Resource type filtering (placeholder - could be enhanced with actual tags)
                category_objectives.append(obj_name)
        
        if not category_objectives:
            st.info(f"No content yet in this category")
            continue
        
        st.markdown(f"**{len(category_objectives)} items** in this category")
        
        # Display objectives grouped by grade
        grades = ['K', '1', '2', '3', '4', '5', '6', '7', '8']
        for grade in grades:
            grade_objs = [o for o in category_objectives if o.startswith(f"{grade}.O")]
            
            if grade_objs:
                st.markdown(f"#### Grade {grade}")
                
                for obj_name in grade_objs[:5]:  # Show first 5 per grade
                    node_data = st.session_state.graph_manager.get_node_data(obj_name)
                    
                    col_a, col_b, col_c = st.columns([3, 1, 1])
                    with col_a:
                        st.markdown(f"**{obj_name}**")
                        if show_all:
                            st.caption(node_data.get('description', '')[:150])
                        
                        # Show image thumbnails if any
                        if node_data.get('images'):
                            img_count = len(node_data['images'])
                            st.caption(f"🖼️ {img_count} image{'s' if img_count > 1 else ''}")
                            
                            if show_all and img_count > 0:
                                try:
                                    st.image(node_data['images'][0], width=100)
                                except:
                                    pass
                    
                    with col_b:
                        dim_level = node_data.get('dimensional_level', '')
                        if dim_level:
                            st.caption(f"📊 {dim_level}")
                    with col_c:
                        if node_data.get('variables'):
                            st.caption(f"🏷️ {', '.join(node_data['variables'][:2])}")
                
                if len(grade_objs) > 5:
                    st.caption(f"... and {len(grade_objs) - 5} more for Grade {grade}")
                
                st.markdown("")

st.divider()
st.caption("💡 Use the Manage Content page to add more objectives and tag them with variables, dimensions, and eras.")
