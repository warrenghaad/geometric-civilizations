import networkx as nx
from typing import Dict, List, Tuple, Optional, Any

class GraphManager:
    """Manages the graph structure for curriculum and database relationships"""
    
    def __init__(self):
        self.graph = nx.DiGraph()
        self.node_attributes = {}
        
    def add_node(self, node_name: str, node_type: str, description: str = "", 
                 variables: List[str] = None, dimensional_level: str = None,
                 historical_era: str = None, cognitive_domains: Dict[str, str] = None,
                 verbs: List[str] = None, grade_level: str = None) -> bool:
        """Add a new node to the graph with extended pyramidic metadata"""
        if node_name in self.graph:
            return False
        
        self.graph.add_node(node_name)
        self.node_attributes[node_name] = {
            'type': node_type,
            'description': description,
            'images': [],
            'variables': variables or [],  # Math, Arts, Mythology, Power
            'dimensional_level': dimensional_level or '',  # D1a, D1b, D2, D3, D4
            'historical_era': historical_era or '',  # Egyptian, Babylonian, Greek, Islamic, etc.
            'cognitive_domains': cognitive_domains or {},  # {domain: weight} e.g., {"Attention": "high", "Memory": "medium"}
            'verbs': verbs or [],  # spot, analyze, create, compare, etc.
            'grade_level': grade_level or '',  # K, 1, 2, ..., 8
            'status': 'not-started',  # complete, in-progress, planned, not-started
            'priority': 'medium',  # high, medium, low
            'notes': ''
        }
        return True
    
    def remove_node(self, node_name: str) -> bool:
        """Remove a node from the graph"""
        if node_name not in self.graph:
            return False
        
        self.graph.remove_node(node_name)
        if node_name in self.node_attributes:
            del self.node_attributes[node_name]
        return True
    
    def update_node(self, node_name: str, **kwargs) -> bool:
        """Update node attributes flexibly"""
        if node_name not in self.node_attributes:
            return False
        
        # Update any provided attributes
        for key, value in kwargs.items():
            if value is not None:
                self.node_attributes[node_name][key] = value
        return True
    
    def add_edge(self, source: str, target: str, relationship_type: str = "") -> bool:
        """Add an edge (relationship) between two nodes"""
        if source not in self.graph or target not in self.graph:
            return False
        
        self.graph.add_edge(source, target, relationship_type=relationship_type)
        return True
    
    def remove_edge(self, source: str, target: str) -> bool:
        """Remove an edge between two nodes"""
        if not self.graph.has_edge(source, target):
            return False
        
        self.graph.remove_edge(source, target)
        return True
    
    def add_image_to_node(self, node_name: str, image_path: str) -> bool:
        """Add an image reference to a node"""
        if node_name not in self.node_attributes:
            return False
        
        if image_path not in self.node_attributes[node_name]['images']:
            self.node_attributes[node_name]['images'].append(image_path)
        return True
    
    def get_node_data(self, node_name: str) -> Optional[Dict[str, Any]]:
        """Get all data for a specific node"""
        if node_name not in self.node_attributes:
            return None
        return self.node_attributes[node_name]
    
    def get_all_nodes(self) -> List[str]:
        """Get list of all node names"""
        return list(self.graph.nodes())
    
    def get_all_edges(self) -> List[Tuple[str, str, str]]:
        """Get list of all edges with their relationship types"""
        edges = []
        for source, target, data in self.graph.edges(data=True):
            rel_type = data.get('relationship_type', '')
            edges.append((source, target, rel_type))
        return edges
    
    def get_node_connections(self, node_name: str) -> Dict[str, List[Tuple[str, str]]]:
        """Get all incoming and outgoing connections for a node"""
        if node_name not in self.graph:
            return {'incoming': [], 'outgoing': []}
        
        incoming = []
        for source in self.graph.predecessors(node_name):
            rel_type = self.graph[source][node_name].get('relationship_type', '')
            incoming.append((source, rel_type))
        
        outgoing = []
        for target in self.graph.successors(node_name):
            rel_type = self.graph[node_name][target].get('relationship_type', '')
            outgoing.append((target, rel_type))
        
        return {
            'incoming': incoming,
            'outgoing': outgoing
        }
    
    def get_node_type_counts(self) -> Dict[str, int]:
        """Get count of nodes by type"""
        type_counts = {}
        for node_name, attrs in self.node_attributes.items():
            node_type = attrs.get('type', 'Other')
            type_counts[node_type] = type_counts.get(node_type, 0) + 1
        return type_counts
    
    def get_edge_count(self) -> int:
        """Get total number of edges"""
        return self.graph.number_of_edges()
    
    def filter_nodes_by(self, **criteria) -> List[str]:
        """Filter nodes by various criteria"""
        filtered = []
        for node_name, attrs in self.node_attributes.items():
            match = True
            for key, value in criteria.items():
                if key == 'variables':
                    # Check if any of the requested variables are present
                    if not any(v in attrs.get('variables', []) for v in value):
                        match = False
                elif key == 'verbs':
                    # Check if any of the requested verbs are present
                    if not any(v in attrs.get('verbs', []) for v in value):
                        match = False
                elif key == 'cognitive_domains':
                    # Check if any of the requested domains are present
                    if not any(d in attrs.get('cognitive_domains', {}) for d in value):
                        match = False
                else:
                    # Exact match for other fields
                    if attrs.get(key) != value:
                        match = False
            if match:
                filtered.append(node_name)
        return filtered
    
    def get_unique_values(self, field: str) -> List[str]:
        """Get all unique values for a given field"""
        values = set()
        for attrs in self.node_attributes.values():
            if field in attrs:
                value = attrs[field]
                if isinstance(value, list):
                    values.update(value)
                elif isinstance(value, dict):
                    values.update(value.keys())
                elif value:
                    values.add(value)
        return sorted(list(values))
    
    def get_graph_data(self) -> Dict[str, Any]:
        """Export graph data for visualization"""
        return {
            'nodes': self.node_attributes,
            'edges': self.get_all_edges()
        }
    
    def save_to_store(self, data_store):
        """Save graph data to persistent storage"""
        graph_data = {
            'nodes': self.node_attributes,
            'edges': self.get_all_edges()
        }
        data_store.save_graph_data(graph_data)
    
    def load_from_store(self, data_store):
        """Load graph data from persistent storage"""
        graph_data = data_store.load_graph_data()
        
        if graph_data:
            self.node_attributes = graph_data.get('nodes', {})
            
            # Rebuild graph
            self.graph.clear()
            for node_name in self.node_attributes.keys():
                self.graph.add_node(node_name)
            
            for source, target, rel_type in graph_data.get('edges', []):
                self.graph.add_edge(source, target, relationship_type=rel_type)
