import plotly.graph_objects as go
import networkx as nx
import numpy as np
from typing import Optional

def get_color_for_type(node_type: str) -> str:
    """Return color code for different node types"""
    color_map = {
        'Course': '#FF6B6B',      # Red
        'Module': '#4ECDC4',      # Teal
        'Concept': '#45B7D1',     # Blue
        'Database': '#FFA07A',    # Light Salmon
        'Table': '#98D8C8',       # Mint
        'Schema': '#C7CEEA',      # Lavender
        'Other': '#95E1D3'        # Aqua
    }
    return color_map.get(node_type, '#95E1D3')

def create_3d_visualization(graph_manager):
    """Create a 3D plotly visualization of the graph"""
    
    nodes = graph_manager.get_all_nodes()
    
    if not nodes:
        return None
    
    # Get graph data
    G = graph_manager.graph
    
    # Calculate 3D layout using spring layout
    if len(nodes) == 1:
        pos_2d = {nodes[0]: (0, 0)}
    else:
        pos_2d = nx.spring_layout(G, dim=2, iterations=50, seed=42)
    
    # Add z-coordinate based on node hierarchy or type
    pos_3d = {}
    for node in nodes:
        x, y = pos_2d[node]
        node_data = graph_manager.get_node_data(node)
        node_type = node_data.get('type', 'Other')
        
        # Assign z-coordinate based on type for better visualization
        z_map = {
            'Course': 2.0,
            'Module': 1.0,
            'Concept': 0.0,
            'Database': 2.0,
            'Schema': 1.0,
            'Table': 0.0,
            'Other': 0.5
        }
        z = z_map.get(node_type, 0.5)
        pos_3d[node] = (x, y, z)
    
    # Prepare edge traces
    edge_traces = []
    for source, target, rel_type in graph_manager.get_all_edges():
        x0, y0, z0 = pos_3d[source]
        x1, y1, z1 = pos_3d[target]
        
        edge_trace = go.Scatter3d(
            x=[x0, x1, None],
            y=[y0, y1, None],
            z=[z0, z1, None],
            mode='lines',
            line=dict(color='#888', width=2),
            hoverinfo='none',
            showlegend=False
        )
        edge_traces.append(edge_trace)
    
    # Prepare node trace
    node_x = []
    node_y = []
    node_z = []
    node_colors = []
    node_text = []
    node_names = []
    node_sizes = []
    
    for node in nodes:
        x, y, z = pos_3d[node]
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)
        
        node_data = graph_manager.get_node_data(node)
        node_type = node_data.get('type', 'Other')
        node_colors.append(get_color_for_type(node_type))
        
        # Create hover text
        description = node_data.get('description', 'No description')
        connections = graph_manager.get_node_connections(node)
        num_connections = len(connections['incoming']) + len(connections['outgoing'])
        
        hover_text = f"<b>{node}</b><br>"
        hover_text += f"Type: {node_type}<br>"
        hover_text += f"Connections: {num_connections}<br>"
        if description:
            hover_text += f"Description: {description[:100]}..."
        
        node_text.append(hover_text)
        node_names.append(node)
        
        # Size based on number of connections
        size = 10 + (num_connections * 2)
        node_sizes.append(min(size, 30))  # Cap at 30
    
    node_trace = go.Scatter3d(
        x=node_x,
        y=node_y,
        z=node_z,
        mode='markers+text',
        marker=dict(
            size=node_sizes,
            color=node_colors,
            line=dict(color='white', width=2),
            opacity=0.9
        ),
        text=[name[:20] for name in node_names],  # Show abbreviated names
        textposition="top center",
        textfont=dict(size=10, color='black'),
        hovertext=node_text,
        hoverinfo='text',
        customdata=[[name] for name in node_names],
        showlegend=False
    )
    
    # Create figure
    data = edge_traces + [node_trace]
    
    fig = go.Figure(data=data)
    
    # Update layout
    fig.update_layout(
        title={
            'text': "Interactive 3D Relationship Graph",
            'x': 0.5,
            'xanchor': 'center'
        },
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, l=0, r=0, t=40),
        scene=dict(
            xaxis=dict(showgrid=False, showticklabels=False, title=''),
            yaxis=dict(showgrid=False, showticklabels=False, title=''),
            zaxis=dict(showgrid=False, showticklabels=False, title=''),
            bgcolor='rgba(240, 240, 240, 0.9)'
        ),
        height=600
    )
    
    # Add legend for node types
    node_types = graph_manager.get_node_type_counts()
    annotations = []
    y_pos = 0.95
    
    legend_text = "Node Types:<br>"
    for node_type, count in sorted(node_types.items()):
        color = get_color_for_type(node_type)
        legend_text += f"<span style='color:{color}'>●</span> {node_type} ({count})<br>"
    
    fig.add_annotation(
        text=legend_text,
        xref="paper", yref="paper",
        x=0.02, y=0.98,
        showarrow=False,
        align="left",
        bgcolor="rgba(255, 255, 255, 0.8)",
        bordercolor="#888",
        borderwidth=1,
        borderpad=10
    )
    
    return fig
