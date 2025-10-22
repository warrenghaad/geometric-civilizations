import streamlit as st
from graph_manager import GraphManager
from data_store import DataStore
import re

st.set_page_config(page_title="Verb Network", page_icon="🔗", layout="wide")

# Ensure session state
if 'graph_manager' not in st.session_state:
    st.session_state.graph_manager = GraphManager()
    st.session_state.data_store = DataStore()
    st.session_state.graph_manager.load_from_store(st.session_state.data_store)

st.title("🔗 Verb Network Search")
st.markdown("### Search by Cognitive Verb Across All Layers")

st.markdown("""
Search for verbs like **spot**, **analyze**, **create**, **compare**, **justify** to see:
- Which objectives use that cognitive action
- How the verb appears across grade levels
- Dimensional distribution (D1a → D4)
- Cross-layer connections
""")

# Extract all verbs from objectives
def extract_verbs_from_text(text):
    """Extract potential verbs from text"""
    common_verbs = [
        'spot', 'notice', 'identify', 'name', 'retell', 'draw', 'build', 'clap',
        'sort', 'listen', 'choose', 'extend', 'tell', 'compare', 'write', 'label',
        'describe', 'use', 'find', 'classify', 'present', 'create', 'map', 'partition',
        'explain', 'ask', 'measure', 'revise', 'paraphrase', 'cite', 'extract',
        'distinguish', 'summarize', 'plan', 'analyze', 'support', 'construct',
        'evaluate', 'justify', 'assemble', 'argue', 'critique', 'integrate',
        'annotate', 'facilitate', 'categorize', 'trace', 'model', 'prove',
        'craft', 'adapt', 'produce', 'guide'
    ]
    
    found_verbs = []
    text_lower = text.lower()
    for verb in common_verbs:
        if verb in text_lower:
            found_verbs.append(verb)
    return found_verbs

# Get all unique verbs from objectives
all_nodes = st.session_state.graph_manager.get_all_nodes()
all_verbs = set()
for node in all_nodes:
    node_data = st.session_state.graph_manager.get_node_data(node)
    if node_data:
        # Check stored verbs
        if node_data.get('verbs'):
            all_verbs.update(node_data['verbs'])
        # Also extract from description
        desc = node_data.get('description', '')
        all_verbs.update(extract_verbs_from_text(node + ' ' + desc))

all_verbs = sorted(list(all_verbs))

# Search interface
col1, col2 = st.columns([3, 1])
with col1:
    if all_verbs:
        selected_verb = st.selectbox("Select a verb to search", [""] + all_verbs)
    else:
        selected_verb = st.text_input("Enter a verb to search (e.g., analyze, create)")
with col2:
    st.markdown("&nbsp;")
    search_button = st.button("🔍 Search", type="primary", use_container_width=True)

st.divider()

if selected_verb:
    # Find all nodes containing this verb
    matching_nodes = []
    for node in all_nodes:
        node_data = st.session_state.graph_manager.get_node_data(node)
        if node_data:
            text_to_search = (node + ' ' + node_data.get('description', '')).lower()
            stored_verbs = [v.lower() for v in node_data.get('verbs', [])]
            
            if selected_verb.lower() in text_to_search or selected_verb.lower() in stored_verbs:
                matching_nodes.append((node, node_data))
    
    if matching_nodes:
        st.success(f"Found **{len(matching_nodes)}** objectives using verb: **{selected_verb}**")
        
        # Show dimensional distribution
        dim_distribution = {}
        grade_distribution = {}
        
        for node, data in matching_nodes:
            dim = data.get('dimensional_level', 'Not set')
            dim_distribution[dim] = dim_distribution.get(dim, 0) + 1
            
            grade = data.get('grade_level', 'Not set')
            if not grade:
                # Try to extract from node name
                for g in ['K', '1', '2', '3', '4', '5', '6', '7', '8']:
                    if g in node:
                        grade = g
                        break
                if not grade or grade == 'Not set':
                    grade = 'Not set'
            grade_distribution[grade] = grade_distribution.get(grade, 0) + 1
        
        # Display distribution
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("#### Dimensional Distribution")
            for dim, count in sorted(dim_distribution.items()):
                st.metric(dim, count)
        
        with col_b:
            st.markdown("#### Grade Distribution")
            for grade, count in sorted(grade_distribution.items()):
                st.metric(f"Grade {grade}", count)
        
        st.divider()
        
        # Display matching objectives
        st.markdown("#### Matching Objectives")
        
        for node, data in matching_nodes:
            with st.expander(f"**{node}**"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.caption(f"**Type:** {data.get('type', 'N/A')}")
                    st.caption(f"**Grade:** {data.get('grade_level', 'Not set')}")
                
                with col2:
                    st.caption(f"**Dimension:** {data.get('dimensional_level', 'Not set')}")
                    if data.get('variables'):
                        st.caption(f"**Variables:** {', '.join(data['variables'])}")
                
                with col3:
                    if data.get('historical_era'):
                        st.caption(f"**Era:** {data['historical_era']}")
                    if data.get('verbs'):
                        st.caption(f"**Verbs:** {', '.join(data['verbs'])}")
                
                st.markdown(data.get('description', ''))
                
                # Show connections
                connections = st.session_state.graph_manager.get_node_connections(node)
                if connections['incoming'] or connections['outgoing']:
                    st.caption("**Connections:**")
                    if connections['outgoing']:
                        st.caption(f"→ Points to: {', '.join([t for t, _ in connections['outgoing'][:3]])}")
                    if connections['incoming']:
                        st.caption(f"← From: {', '.join([s for s, _ in connections['incoming'][:3]])}")
    else:
        st.warning(f"No objectives found using the verb: **{selected_verb}**")
        st.info("Objectives need to be tagged with verbs. Use the Manage Content page to add verb tags.")
else:
    st.info("👆 Select or enter a verb to search across all curriculum layers")

st.divider()
st.caption("💡 Verbs are automatically extracted from objective descriptions. You can also manually tag objectives with specific verbs using the Manage Content page.")
