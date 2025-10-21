import json
import os
from typing import Dict, Any, Optional
from pathlib import Path

class DataStore:
    """Handles data persistence for the graph application"""
    
    def __init__(self, data_dir: str = "data", images_dir: str = "data/images"):
        self.data_dir = data_dir
        self.images_dir = images_dir
        self.graph_file = os.path.join(data_dir, "graph_data.json")
        
        # Ensure directories exist
        os.makedirs(data_dir, exist_ok=True)
        os.makedirs(images_dir, exist_ok=True)
    
    def save_graph_data(self, graph_data: Dict[str, Any]) -> bool:
        """Save graph data to JSON file"""
        try:
            with open(self.graph_file, 'w') as f:
                json.dump(graph_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving graph data: {e}")
            return False
    
    def load_graph_data(self) -> Optional[Dict[str, Any]]:
        """Load graph data from JSON file"""
        if not os.path.exists(self.graph_file):
            return None
        
        try:
            with open(self.graph_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading graph data: {e}")
            return None
    
    def save_image(self, uploaded_file, node_name: str) -> str:
        """Save uploaded image and return its path"""
        # Create safe filename
        file_extension = os.path.splitext(uploaded_file.name)[1]
        safe_node_name = "".join(c for c in node_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_node_name = safe_node_name.replace(' ', '_')
        
        # Generate unique filename
        base_filename = f"{safe_node_name}{file_extension}"
        filepath = os.path.join(self.images_dir, base_filename)
        
        # If file exists, add number suffix
        counter = 1
        while os.path.exists(filepath):
            base_filename = f"{safe_node_name}_{counter}{file_extension}"
            filepath = os.path.join(self.images_dir, base_filename)
            counter += 1
        
        # Save file
        with open(filepath, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        return filepath
    
    def delete_image(self, image_path: str) -> bool:
        """Delete an image file"""
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
                return True
        except Exception as e:
            print(f"Error deleting image: {e}")
        return False
    
    def get_all_images(self) -> list:
        """Get list of all image files"""
        if not os.path.exists(self.images_dir):
            return []
        
        image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.bmp'}
        images = []
        
        for file in os.listdir(self.images_dir):
            if os.path.splitext(file)[1].lower() in image_extensions:
                images.append(os.path.join(self.images_dir, file))
        
        return images
