#!/usr/bin/env python3
"""
PYTHON SCRIPT CROSS-REFERENCE SYSTEM
===================================

This file fixes all the Python script references so they can properly call each other
in the geometric-civilizations curriculum automation pipeline.
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path so scripts can import each other
SCRIPT_DIR = Path(__file__).parent.absolute()
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# Script execution helper
def run_script(script_name, args=None):
    """Run another Python script in this directory with proper path resolution"""
    script_path = SCRIPT_DIR / script_name
    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")
    
    # Build command
    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)
    
    # Run with proper working directory
    import subprocess
    result = subprocess.run(cmd, cwd=str(SCRIPT_DIR), capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error running {script_name}:")
        print(result.stderr)
        return False
    
    return True

# SCRIPT DEPENDENCY MAP
# Maps each script to the other scripts it needs to call
SCRIPT_DEPENDENCIES = {
    # Main orchestrator
    "master_curriculum_builder.py": [
        "build_all.py",
        "download_curriculum_images.py", 
        "process_all_presentations.py",
        "ppt_to_etextbook_converter.py",
        "create_final_delivery_package.py"
    ],
    
    # Build scripts
    "build_all.py": [],
    "build_enhanced.py": ["build_all.py"],
    "build_from_template.py": [],
    
    # Image processing
    "download_curriculum_images.py": [],
    "download_curriculum_images_v2.py": ["download_curriculum_images.py"],
    "add_images_to_presentations.py": [],
    "insert_images_into_presentations.py": ["add_images_to_presentations.py"],
    "process_all_presentations.py": [
        "add_images_to_presentations.py",
        "insert_images_into_presentations.py"
    ],
    
    # Content generation
    "create_mesopotamian_lessons_complete.py": ["build_all.py"],
    "generate_all_48_enhanced_materials.py": [
        "create_mesopotamian_lessons_complete.py",
        "add_images_to_presentations.py"
    ],
    "create_complete_teaching_materials.py": ["generate_all_48_enhanced_materials.py"],
    "create_enhanced_teaching_materials.py": ["create_complete_teaching_materials.py"],
    
    # E-textbook conversion
    "ppt_to_etextbook_converter.py": [],
    
    # Delivery and packaging
    "create_final_delivery_package.py": [
        "ppt_to_etextbook_converter.py",
        "organize_curriculum_files.py"
    ],
    "organize_curriculum_files.py": [],
    "categorize_files.py": [],
    
    # Museum and Firebase
    "build_firebase_museum_database.py": [],
    "firebase_museum_uploader.py": ["build_firebase_museum_database.py"],
    "museum_api_client.py": [],
    "download_museum_images_api.py": ["museum_api_client.py"],
    
    # Specialized downloads
    "download_met_mythology.py": [],
    "download_myth_art_final.py": ["download_met_mythology.py"],
    "download_smarthistory_images.py": [],
    "download_verified_images.py": [
        "download_smarthistory_images.py",
        "download_myth_art_final.py"
    ],
    "massive_image_download.py": ["download_verified_images.py"],
    "emergency_image_download.py": ["massive_image_download.py"],
    
    # Review and enhancement
    "review_and_add_animations.py": [],
    "add_animations_timing.py": ["review_and_add_animations.py"],
    "review_and_fix_text_formatting.py": [],
    "final_comprehensive_review.py": [
        "review_and_add_animations.py",
        "review_and_fix_text_formatting.py"
    ]
}

# PROPER SCRIPT EXECUTION ORDER
EXECUTION_ORDER = [
    # Phase 1: Basic builds
    "build_all.py",
    "create_mesopotamian_lessons_complete.py", 
    
    # Phase 2: Image acquisition
    "download_curriculum_images.py",
    "download_verified_images.py",
    "massive_image_download.py",
    
    # Phase 3: Enhanced content creation
    "generate_all_48_enhanced_materials.py",
    "create_enhanced_teaching_materials.py",
    
    # Phase 4: Image integration
    "process_all_presentations.py",
    "add_images_to_presentations.py",
    
    # Phase 5: E-textbook conversion
    "ppt_to_etextbook_converter.py",
    
    # Phase 6: Review and polish
    "final_comprehensive_review.py",
    
    # Phase 7: Delivery
    "organize_curriculum_files.py",
    "create_final_delivery_package.py"
]

# SCRIPT DESCRIPTIONS
SCRIPT_DESCRIPTIONS = {
    "master_curriculum_builder.py": "Main orchestrator - runs entire pipeline",
    "build_all.py": "Converts JSON lessons to basic PowerPoints", 
    "build_enhanced.py": "Creates enhanced versions with animations",
    "download_curriculum_images.py": "Downloads images for curriculum content",
    "add_images_to_presentations.py": "Adds images to PowerPoint slides",
    "process_all_presentations.py": "Processes all presentations with images",
    "ppt_to_etextbook_converter.py": "Converts PowerPoints to e-textbooks",
    "create_final_delivery_package.py": "Creates final curriculum package",
    "generate_all_48_enhanced_materials.py": "Generates all 48 enhanced lessons",
    "create_enhanced_teaching_materials.py": "Creates enhanced teaching materials",
    "organize_curriculum_files.py": "Organizes curriculum files for delivery"
}

def get_script_dependencies(script_name):
    """Get list of scripts that this script depends on"""
    return SCRIPT_DEPENDENCIES.get(script_name, [])

def get_script_description(script_name):
    """Get description of what this script does"""
    return SCRIPT_DESCRIPTIONS.get(script_name, "No description available")

def run_full_pipeline():
    """Run the complete curriculum generation pipeline in proper order"""
    print("🚀 Running Complete Curriculum Pipeline")
    print("=" * 50)
    
    for i, script in enumerate(EXECUTION_ORDER, 1):
        print(f"\n📋 Step {i}: {script}")
        print(f"   {get_script_description(script)}")
        
        if not run_script(script):
            print(f"❌ Failed at step {i}: {script}")
            return False
        
        print(f"✅ Completed step {i}")
    
    print("\n🎉 Complete pipeline finished successfully!")
    return True

def validate_all_scripts():
    """Check that all referenced scripts actually exist"""
    print("🔍 Validating script references...")
    
    missing_scripts = []
    for script, deps in SCRIPT_DEPENDENCIES.items():
        script_path = SCRIPT_DIR / script
        if not script_path.exists():
            missing_scripts.append(script)
        
        for dep in deps:
            dep_path = SCRIPT_DIR / dep
            if not dep_path.exists():
                missing_scripts.append(dep)
    
    if missing_scripts:
        print(f"❌ Missing scripts: {missing_scripts}")
        return False
    
    print("✅ All scripts found")
    return True

if __name__ == "__main__":
    # Validate scripts exist
    if not validate_all_scripts():
        sys.exit(1)
    
    # Show usage
    if len(sys.argv) == 1:
        print("Python Script Cross-Reference System")
        print("Usage:")
        print("  python script_cross_reference.py validate    - Check all scripts exist")
        print("  python script_cross_reference.py run-all     - Run complete pipeline") 
        print("  python script_cross_reference.py run <script> - Run specific script")
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "validate":
        validate_all_scripts()
    elif command == "run-all":
        run_full_pipeline()
    elif command == "run" and len(sys.argv) > 2:
        script_name = sys.argv[2]
        if not script_name.endswith('.py'):
            script_name += '.py'
        run_script(script_name)
    else:
        print("Invalid command")
        sys.exit(1)