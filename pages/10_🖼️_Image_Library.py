import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore
import os

st.set_page_config(page_title="Image Library", page_icon="🖼️", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("🖼️ Image Library & Builder")
st.markdown("### Search, preview, and organize visual resources for curriculum")

# Create tabs for different functions
tab1, tab2 = st.tabs(["🔍 Find New Images", "📂 Browse Library"])

# TAB 1: Find New Images
with tab1:
    st.markdown("### Search for Historical Design Motifs")
    
    st.markdown("""
    Search for images of historical design motifs, architectural elements, and cultural symbols.
    These images can be linked to curriculum objectives, lessons, and mapping resources.
    """)
    
    # Historical Era Categories
    st.markdown("#### Quick Search by Era")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Ancient Civilizations**")
        if st.button("🏛️ Egyptian Motifs"):
            st.session_state.search_query = "ancient egyptian lotus papyrus hieroglyphs"
        if st.button("🏺 Greek Patterns"):
            st.session_state.search_query = "ancient greek key meander pattern"
        if st.button("🏟️ Roman Architecture"):
            st.session_state.search_query = "ancient roman arches columns"
    
    with col2:
        st.markdown("**Medieval & Islamic**")
        if st.button("🕌 Islamic Geometry"):
            st.session_state.search_query = "islamic geometric patterns arabesque"
        if st.button("⛪ Gothic Architecture"):
            st.session_state.search_query = "gothic rose window cathedral"
        if st.button("✨ Byzantine Art"):
            st.session_state.search_query = "byzantine mosaic art"
    
    with col3:
        st.markdown("**Renaissance & Modern**")
        if st.button("🎨 Renaissance Design"):
            st.session_state.search_query = "renaissance architecture symmetry"
        if st.button("🔶 Art Nouveau"):
            st.session_state.search_query = "art nouveau patterns motifs"
        if st.button("📐 Modern Geometry"):
            st.session_state.search_query = "modern geometric abstract patterns"
    
    st.divider()
    
    # Custom search
    search_query = st.text_input(
        "🔍 Or enter custom search terms",
        value=st.session_state.get('search_query', ''),
        placeholder="e.g., 'acanthus leaf', 'trefoil gothic', 'ziggurat mesopotamia'"
    )
    
    col_search, col_link = st.columns([2, 1])
    
    with col_search:
        num_images = st.slider("Number of images to find", 1, 10, 3)
    
    with col_link:
        # Get all objectives for linking
        all_nodes = st.session_state.graph_manager.get_all_nodes()
        all_objectives = ["None - Just download"] + sorted([n for n in all_nodes if ".O" in n])
        link_to_objective = st.selectbox("Link images to:", all_objectives)
    
    if st.button("🔎 Search for Images", type="primary"):
        if search_query:
            with st.spinner(f"Searching for {num_images} images of '{search_query}'..."):
                try:
                    # Use stock_image_tool to fetch images
                    from stock_image_tool import stock_image_tool
                    
                    # This will download images to attached_assets/stock_images
                    result = stock_image_tool(
                        description=search_query,
                        limit=num_images,
                        orientation="horizontal"
                    )
                    
                    st.success(f"✅ Found {num_images} images!")
                    
                    # Store search result in session state
                    st.session_state.latest_search_results = {
                        'query': search_query,
                        'num_images': num_images,
                        'link_to': link_to_objective
                    }
                    
                    st.info("""
                    **Images have been downloaded!**
                    
                    📁 Images are saved to: `attached_assets/stock_images/`
                    
                    You can now:
                    1. View them in the "Browse Library" tab
                    2. Upload them to link with curriculum objectives in "Manage Content"
                    3. Use them in your lesson materials
                    """)
                    
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"Error searching for images: {str(e)}")
                    st.info("Please try a different search term or reduce the number of images.")
        else:
            st.warning("Please enter search terms")
    
    st.divider()
    
    # Quick reference for common motifs
    with st.expander("📖 Common Design Motifs Reference", expanded=False):
        st.markdown("""
        ### Ancient Egypt & Mesopotamia
        - **Lotus**: Rebirth and renewal
        - **Papyrus**: Growth and nature
        - **Chevron**: Protection or water
        - **Rosette**: Harmony and cosmic order
        - **Spiral**: Eternity or journey
        - **Ziggurat**: Connection to divine
        - **Pyramids**: Power and eternity
        
        ### Ancient Greece
        - **Meander (Greek key)**: Eternity and flow
        - **Palmette**: Victory and triumph
        - **Acanthus**: Immortality and endurance
        - **Classical columns**: Order and balance
        
        ### Ancient Rome
        - **Arches, Domes, Vaults**: Strength and innovation
        - **Laurel**: Victory and honor
        - **Mosaic**: Unity in diversity
        - **Corinthian capital**: Elegance
        
        ### Byzantine Empire
        - **Mosaics**: Divine beauty
        - **Domes**: Heaven and eternity
        - **Greek cross**: Christian faith
        
        ### Islamic World
        - **Star polygons**: Infinite nature of God
        - **Arabesques**: Unity and harmony
        - **Calligraphy**: Sacred word
        - **Tilework**: Interconnectedness
        
        ### Medieval Europe (Gothic)
        - **Rose window**: Divine light
        - **Trefoil**: Holy Trinity
        - **Pointed arch**: Aspiration to heaven
        - **Stained glass**: Illumination of faith
        
        ### Renaissance
        - **Grids & Symmetry**: Order and reason
        - **Perspective**: Realism and depth
        - **Classical revival**: Ancient wisdom
        - **Proportions**: Mathematical harmony
        """)

# TAB 2: Browse Library
with tab2:
    st.markdown("### Browse Existing Images")
    
    # Check for images in data/images directory
    images_dir = "data/images"
    stock_images_dir = "attached_assets/stock_images"
    
    all_image_files = []
    
    # Get images from data/images
    if os.path.exists(images_dir):
        for filename in os.listdir(images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                all_image_files.append(os.path.join(images_dir, filename))
    
    # Get images from stock_images
    if os.path.exists(stock_images_dir):
        for filename in os.listdir(stock_images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                all_image_files.append(os.path.join(stock_images_dir, filename))
    
    if not all_image_files:
        st.info("No images in library yet. Use the 'Find New Images' tab to search for historical motifs.")
    else:
        st.markdown(f"**{len(all_image_files)} images** in library")
        
        # Search/filter
        filter_term = st.text_input("🔍 Filter images by name", "")
        
        # Filter images
        displayed_images = all_image_files
        if filter_term:
            displayed_images = [img for img in all_image_files if filter_term.lower() in img.lower()]
        
        st.markdown(f"Showing {len(displayed_images)} images")
        
        # Display images in grid
        cols_per_row = 3
        
        for i in range(0, len(displayed_images), cols_per_row):
            cols = st.columns(cols_per_row)
            
            for j, col in enumerate(cols):
                if i + j < len(displayed_images):
                    img_path = displayed_images[i + j]
                    filename = os.path.basename(img_path)
                    
                    with col:
                        try:
                            st.image(img_path, caption=filename, use_container_width=True)
                            
                            # Show which objectives use this image
                            linked_nodes = []
                            for node_name in st.session_state.graph_manager.get_all_nodes():
                                node_data = st.session_state.graph_manager.get_node_data(node_name)
                                if img_path in node_data.get('images', []):
                                    linked_nodes.append(node_name)
                            
                            if linked_nodes:
                                st.caption(f"🔗 Linked to: {', '.join(linked_nodes[:2])}")
                                if len(linked_nodes) > 2:
                                    st.caption(f"... and {len(linked_nodes) - 2} more")
                            else:
                                st.caption("Not linked to any objectives")
                            
                        except Exception as e:
                            st.error(f"Error loading {filename}")
        
        st.divider()
        
        # Image management
        st.markdown("### Image Management")
        st.info("""
        **To link images to curriculum objectives:**
        1. Go to "✏️ Manage Content" page
        2. Select "Upload Image" tab
        3. Choose an objective and upload/link the image
        
        **Image locations:**
        - `data/images/` - Manually uploaded images
        - `attached_assets/stock_images/` - Downloaded stock images
        """)

st.divider()

# Statistics
st.markdown("### Library Statistics")
col_stat1, col_stat2, col_stat3 = st.columns(3)

with col_stat1:
    st.metric("Total Images", len(all_image_files))

with col_stat2:
    # Count linked images
    linked_count = 0
    for img in all_image_files:
        for node in st.session_state.graph_manager.get_all_nodes():
            node_data = st.session_state.graph_manager.get_node_data(node)
            if img in node_data.get('images', []):
                linked_count += 1
                break
    st.metric("Linked to Objectives", linked_count)

with col_stat3:
    unlinked = len(all_image_files) - linked_count
    st.metric("Unlinked Images", unlinked)
