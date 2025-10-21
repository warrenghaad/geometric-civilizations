# 3D Curriculum & Database Relationship Mapper

## Overview

This is a Streamlit-based web application that creates interactive 3D visualizations of curriculum structures and database relationships. Users can build and explore knowledge graphs by adding nodes (courses, modules, concepts, databases, tables, schemas), defining relationships between them, and attaching images for reference. The application uses NetworkX for graph management and Plotly for 3D visualization, with persistent storage of graph data in JSON format.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology:** Streamlit web framework
- **Rationale:** Provides rapid development of interactive data applications with minimal frontend code
- **Pros:** Built-in state management, easy widget integration, fast prototyping
- **Cons:** Limited customization compared to traditional web frameworks

**Layout Pattern:** Sidebar navigation with main content area
- Sidebar contains action tabs (View Graph, Add Node, Add Relationship, Upload Image, Edit Node)
- Main area displays 3D graph visualization
- Session state manages application data across interactions

### Backend Architecture

**Graph Management:** NetworkX directed graph (DiGraph)
- **Component:** `GraphManager` class handles all graph operations
- **Rationale:** NetworkX provides robust graph algorithms and is well-suited for relationship mapping
- **Node Attributes:** Each node stores type, description, and associated images
- **Edge Attributes:** Relationships include a relationship_type field

**Visualization Engine:** Plotly 3D scatter plots
- **Component:** `visualization.py` module creates interactive 3D graph representations
- **Layout Algorithm:** Spring layout positions nodes with hierarchy-based z-coordinates
- **Color Coding:** Different node types (Course, Module, Concept, Database, Table, Schema) receive distinct colors for visual differentiation

### Data Storage Solutions

**Persistence Layer:** File-based JSON storage
- **Component:** `DataStore` class manages read/write operations
- **Storage Location:** `data/graph_data.json` for graph structure
- **Image Storage:** `data/images/` directory for uploaded images
- **Rationale:** Simple file-based approach suitable for single-user applications without need for concurrent access
- **Pros:** No database setup required, easy to backup and version control
- **Cons:** Not suitable for multi-user scenarios or large-scale deployments

**Session State:** Streamlit's built-in session state
- Maintains `graph_manager`, `data_store`, and UI state (selected_node) between reruns
- Ensures data persistence during user interactions within a session

### Authentication and Authorization

**Current State:** No authentication implemented
- Application assumes single-user local deployment
- No user management or access control mechanisms

## External Dependencies

**Core Libraries:**
- **streamlit:** Web application framework for the user interface
- **networkx:** Graph data structure and algorithms
- **plotly:** Interactive 3D visualization rendering
- **PIL (Pillow):** Image processing for uploaded files

**Data Format:**
- JSON for graph data serialization
- Standard image formats (determined by PIL) for node attachments

**File System:**
- Local file system for data persistence
- Structured directory layout: `data/` for graph data, `data/images/` for uploaded images

**Note:** No external APIs, databases, or cloud services are currently integrated. All data remains local to the deployment environment.