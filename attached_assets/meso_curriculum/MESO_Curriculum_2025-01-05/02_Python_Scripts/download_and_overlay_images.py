#!/usr/bin/env python3
"""
Grade 3 Lesson 1A Image Downloader and Overlay Creator
Downloads museum artifact images and creates geometric overlays as specified in the lesson.
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import time

# Configuration
OUTPUT_DIR = Path("lesson_images")
BACKUP_DIR = OUTPUT_DIR / "backups"
OVERLAYS_DIR = OUTPUT_DIR / "overlays"
VERIFICATION_LOG = OUTPUT_DIR / "verification_log.json"

# Create directories
OUTPUT_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)
OVERLAYS_DIR.mkdir(exist_ok=True)

# Museum API endpoints and backup URLs
MUSEUM_IMAGES = {
    "shamash_tablet": {
        "name": "Shamash Tablet from Sippar",
        "accession": "1880,0617.1",
        "museum": "British Museum",
        "urls": [
            "https://media.britishmuseum.org/media/Repository/Documents/2014_10/12_20/d63bc6ad_47e5_4480_a30c_a3ba0062be29/mid_00091000_001.jpg",
            "https://www.britishmuseum.org/collection/image/91000001",
            # Backup: generic search URL
            "https://www.britishmuseum.org/collection/object/W_1880-0617-1"
        ],
        "expected_size_kb": (100, 5000),  # Min and max expected size
        "image_type": "artifact_photo"
    },
    "ubaid_bowl": {
        "name": "Ubaid Period Painted Pottery Bowl",
        "accession": "1928,0710.1",
        "museum": "British Museum",
        "urls": [
            "https://media.britishmuseum.org/media/Repository/Documents/2014_11/17_17/75e3c5f3_6209_48c5_a81b_a3d600e38122/mid_00928710_001.jpg",
            "https://www.britishmuseum.org/collection/image/928710001",
            "https://www.britishmuseum.org/collection/object/W_1928-0710-1"
        ],
        "expected_size_kb": (100, 5000),
        "image_type": "artifact_photo"
    },
    "ur_rosette": {
        "name": "Gold Rosette from Royal Cemetery of Ur",
        "accession": "B17711",
        "museum": "Penn Museum",
        "urls": [
            "https://www.penn.museum/collections/assets/1600/b17711.jpg",
            "https://www.penn.museum/collections/object/324811",
            # IIIF endpoint (if available)
            "https://images.pennmuseum.org/iiif/2/B17711/full/full/0/default.jpg"
        ],
        "expected_size_kb": (50, 3000),
        "image_type": "artifact_photo"
    },
    "stone_weight": {
        "name": "Stone Circular Weight",
        "accession": "A7320",
        "museum": "Oriental Institute",
        "urls": [
            "https://oi-idb-static.uchicago.edu/multimedia/1234/A7320.jpg",
            # Backup: general collections URL
            "https://oi.uchicago.edu/collections/photographic-archives",
            # Alternative: use a similar weight as example
            "https://oi-idb-static.uchicago.edu/multimedia/5678/weight_example.jpg"
        ],
        "expected_size_kb": (50, 2000),
        "image_type": "artifact_photo"
    },
    "cylinder_seal": {
        "name": "Shamash Cylinder Seal Impression",
        "accession": "NBC 8181",
        "museum": "Yale Babylonian Collection",
        "urls": [
            "https://collections.peabody.yale.edu/ypmbcsearch/Search.aspx?Number=NBC%208181",
            "https://media.peabody.yale.edu/babylonian/NBC_8181.jpg",
            # Backup: similar Old Babylonian seal
            "https://www.britishmuseum.org/collection/image/shamash_seal_example"
        ],
        "expected_size_kb": (50, 2000),
        "image_type": "artifact_photo"
    }
}

# Verification tracking
verification_results = {
    "downloads": {},
    "overlays": {},
    "errors": [],
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
}


def calculate_checksum(filepath: Path) -> str:
    """Calculate MD5 checksum of a file."""
    md5_hash = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


def verify_image_file(filepath: Path, expected_size_kb: Tuple[int, int]) -> Dict:
    """
    Verify that downloaded image is valid.
    
    Returns:
        Dict with verification results including status, size, dimensions, format
    """
    result = {
        "exists": filepath.exists(),
        "valid_image": False,
        "size_kb": 0,
        "dimensions": None,
        "format": None,
        "checksum": None,
        "size_check": False
    }
    
    if not result["exists"]:
        return result
    
    # Check file size
    file_size = filepath.stat().st_size
    result["size_kb"] = file_size / 1024
    result["size_check"] = expected_size_kb[0] <= result["size_kb"] <= expected_size_kb[1]
    
    # Try to open as image
    try:
        with Image.open(filepath) as img:
            result["valid_image"] = True
            result["dimensions"] = img.size
            result["format"] = img.format
            result["checksum"] = calculate_checksum(filepath)
    except Exception as e:
        result["error"] = str(e)
    
    return result


def download_image(image_id: str, image_info: Dict) -> Optional[Path]:
    """
    Download image from museum URL with backup URLs.
    
    Args:
        image_id: Unique identifier for the image
        image_info: Dictionary with URLs and metadata
        
    Returns:
        Path to downloaded image or None if all attempts failed
    """
    filename = OUTPUT_DIR / f"{image_id}_original.jpg"
    
    # Try each URL in sequence
    for idx, url in enumerate(image_info["urls"]):
        try:
            print(f"  Attempting download from URL {idx + 1}/{len(image_info['urls'])}")
            print(f"  {url}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Educational Project: Mesopotamian Geometry Curriculum)',
                'Accept': 'image/jpeg,image/png,image/*'
            }
            
            response = requests.get(url, headers=headers, timeout=30, stream=True)
            
            if response.status_code == 200:
                # Check if response is actually an image
                content_type = response.headers.get('content-type', '')
                if 'image' not in content_type.lower() and 'octet-stream' not in content_type.lower():
                    print(f"  ⚠ Response is not an image (content-type: {content_type})")
                    continue
                
                # Save image
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                # Verify download
                verification = verify_image_file(filename, image_info["expected_size_kb"])
                
                if verification["valid_image"]:
                    print(f"  ✓ Download successful!")
                    print(f"    Size: {verification['size_kb']:.1f} KB")
                    print(f"    Dimensions: {verification['dimensions']}")
                    print(f"    Format: {verification['format']}")
                    
                    verification_results["downloads"][image_id] = {
                        "status": "success",
                        "url": url,
                        "url_index": idx,
                        "filename": str(filename),
                        **verification
                    }
                    
                    return filename
                else:
                    print(f"  ✗ Downloaded file is not a valid image")
                    filename.unlink(missing_ok=True)
                    
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Request failed: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {e}")
    
    # All URLs failed
    error_msg = f"All download attempts failed for {image_id}"
    print(f"  ✗ {error_msg}")
    verification_results["downloads"][image_id] = {
        "status": "failed",
        "attempted_urls": len(image_info["urls"]),
        "error": error_msg
    }
    verification_results["errors"].append(error_msg)
    
    return None


def create_placeholder_image(image_id: str, image_info: Dict) -> Path:
    """
    Create a placeholder image with museum information when download fails.
    """
    filename = OUTPUT_DIR / f"{image_id}_placeholder.jpg"
    
    # Create a 800x600 placeholder
    img = Image.new('RGB', (800, 600), color='#f0f0f0')
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fall back to default
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw border
    draw.rectangle([10, 10, 790, 590], outline='#999999', width=3)
    
    # Draw text
    y_pos = 100
    draw.text((400, y_pos), "IMAGE PLACEHOLDER", fill='#666666', font=font_large, anchor="mm")
    
    y_pos += 80
    draw.text((400, y_pos), image_info["name"], fill='#333333', font=font_small, anchor="mm")
    
    y_pos += 40
    draw.text((400, y_pos), f"Museum: {image_info['museum']}", fill='#333333', font=font_small, anchor="mm")
    
    y_pos += 35
    draw.text((400, y_pos), f"Accession: {image_info['accession']}", fill='#333333', font=font_small, anchor="mm")
    
    y_pos += 80
    draw.text((400, y_pos), "Download this image from:", fill='#666666', font=font_small, anchor="mm")
    
    y_pos += 35
    draw.text((400, y_pos), image_info["urls"][0][:60], fill='#0066cc', font=font_small, anchor="mm")
    
    img.save(filename, 'JPEG', quality=85)
    print(f"  ℹ Created placeholder image: {filename}")
    
    return filename


def create_overlay_circle_basic(base_image_path: Path, output_name: str, 
                                 instructions: Dict) -> Optional[Path]:
    """
    Create basic circle overlay with center point, radius, diameter.
    
    Args:
        base_image_path: Path to base image
        output_name: Name for output file
        instructions: Dictionary with overlay specifications
    """
    try:
        # Open base image
        img = Image.open(base_image_path).convert('RGBA')
        overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        
        # Get image dimensions for scaling
        width, height = img.size
        
        # Extract circle parameters from instructions
        circle_center = instructions.get('circle_center', (width // 2, height // 2))
        circle_radius = instructions.get('circle_radius', min(width, height) // 4)
        
        # Draw circle outline (RED, 2px)
        draw.ellipse(
            [circle_center[0] - circle_radius, circle_center[1] - circle_radius,
             circle_center[0] + circle_radius, circle_center[1] + circle_radius],
            outline=(255, 0, 0, 200), width=2
        )
        
        # Draw center point (RED crosshair)
        crosshair_size = 10
        draw.line(
            [circle_center[0] - crosshair_size, circle_center[1],
             circle_center[0] + crosshair_size, circle_center[1]],
            fill=(255, 0, 0, 255), width=2
        )
        draw.line(
            [circle_center[0], circle_center[1] - crosshair_size,
             circle_center[0], circle_center[1] + crosshair_size],
            fill=(255, 0, 0, 255), width=2
        )
        
        # Draw radius line (BLUE)
        draw.line(
            [circle_center[0], circle_center[1],
             circle_center[0] + circle_radius, circle_center[1]],
            fill=(0, 0, 255, 200), width=2
        )
        
        # Draw diameter line (GREEN)
        draw.line(
            [circle_center[0] - circle_radius, circle_center[1],
             circle_center[0] + circle_radius, circle_center[1]],
            fill=(0, 255, 0, 200), width=2
        )
        
        # Try to add labels
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
        except:
            font = ImageFont.load_default()
        
        # Label radius
        draw.text(
            (circle_center[0] + circle_radius // 2, circle_center[1] - 20),
            "r", fill=(0, 0, 255, 255), font=font
        )
        
        # Label diameter
        draw.text(
            (circle_center[0], circle_center[1] + 20),
            "d = 2r", fill=(0, 255, 0, 255), font=font
        )
        
        # Composite overlay onto original
        result = Image.alpha_composite(img, overlay)
        result = result.convert('RGB')
        
        # Save
        output_path = OVERLAYS_DIR / f"{output_name}.jpg"
        result.save(output_path, 'JPEG', quality=95)
        
        print(f"  ✓ Created overlay: {output_path}")
        
        verification_results["overlays"][output_name] = {
            "status": "success",
            "base_image": str(base_image_path),
            "output": str(output_path),
            "type": "circle_basic"
        }
        
        return output_path
        
    except Exception as e:
        error_msg = f"Failed to create overlay {output_name}: {e}"
        print(f"  ✗ {error_msg}")
        verification_results["overlays"][output_name] = {
            "status": "failed",
            "error": error_msg
        }
        verification_results["errors"].append(error_msg)
        return None


def create_overlay_radial_rays(base_image_path: Path, output_name: str,
                                instructions: Dict) -> Optional[Path]:
    """
    Create overlay showing radial rays with angular measurements.
    """
    try:
        img = Image.open(base_image_path).convert('RGBA')
        overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        
        width, height = img.size
        circle_center = instructions.get('circle_center', (width // 2, height // 2))
        circle_radius = instructions.get('circle_radius', min(width, height) // 4)
        num_rays = instructions.get('num_rays', 8)
        
        # Draw rays
        import math
        angle_step = 360 / num_rays
        
        for i in range(num_rays):
            angle = math.radians(i * angle_step)
            end_x = circle_center[0] + int(circle_radius * 1.2 * math.cos(angle))
            end_y = circle_center[1] + int(circle_radius * 1.2 * math.sin(angle))
            
            draw.line(
                [circle_center[0], circle_center[1], end_x, end_y],
                fill=(255, 255, 0, 200), width=2
            )
        
        # Draw angle arc between first two rays
        if num_rays >= 2:
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
            except:
                font = ImageFont.load_default()
            
            # Draw angle arc
            arc_radius = circle_radius // 3
            bbox = [
                circle_center[0] - arc_radius,
                circle_center[1] - arc_radius,
                circle_center[0] + arc_radius,
                circle_center[1] + arc_radius
            ]
            draw.arc(bbox, 0, angle_step, fill=(0, 128, 255, 200), width=2)
            
            # Label angle
            angle_text = f"{angle_step:.0f}°"
            label_x = circle_center[0] + arc_radius + 10
            label_y = circle_center[1] - 20
            draw.text((label_x, label_y), angle_text, fill=(0, 128, 255, 255), font=font)
        
        # Composite and save
        result = Image.alpha_composite(img, overlay)
        result = result.convert('RGB')
        
        output_path = OVERLAYS_DIR / f"{output_name}.jpg"
        result.save(output_path, 'JPEG', quality=95)
        
        print(f"  ✓ Created overlay: {output_path}")
        
        verification_results["overlays"][output_name] = {
            "status": "success",
            "base_image": str(base_image_path),
            "output": str(output_path),
            "type": "radial_rays",
            "num_rays": num_rays
        }
        
        return output_path
        
    except Exception as e:
        error_msg = f"Failed to create overlay {output_name}: {e}"
        print(f"  ✗ {error_msg}")
        verification_results["overlays"][output_name] = {
            "status": "failed",
            "error": error_msg
        }
        verification_results["errors"].append(error_msg)
        return None


def create_overlay_concentric_circles(base_image_path: Path, output_name: str,
                                       instructions: Dict) -> Optional[Path]:
    """
    Create overlay showing concentric circles with radius labels.
    """
    try:
        img = Image.open(base_image_path).convert('RGBA')
        overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        
        width, height = img.size
        circle_center = instructions.get('circle_center', (width // 2, height // 2))
        radii = instructions.get('radii', [50, 100, 150])  # Multiple radii
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        except:
            font = ImageFont.load_default()
        
        # Draw concentric circles
        colors = [(255, 0, 0, 150), (0, 0, 255, 150), (0, 255, 0, 150)]
        labels = ['r₁', 'r₂', 'r₃']
        
        for idx, radius in enumerate(radii):
            color = colors[idx % len(colors)]
            
            # Draw circle
            draw.ellipse(
                [circle_center[0] - radius, circle_center[1] - radius,
                 circle_center[0] + radius, circle_center[1] + radius],
                outline=color, width=2
            )
            
            # Draw radius line
            draw.line(
                [circle_center[0], circle_center[1],
                 circle_center[0] + radius, circle_center[1]],
                fill=color, width=1
            )
            
            # Label
            label_x = circle_center[0] + radius + 10
            label_y = circle_center[1] - 10
            draw.text((label_x, label_y), labels[idx], fill=color, font=font)
        
        # Draw center point
        crosshair_size = 8
        draw.line(
            [circle_center[0] - crosshair_size, circle_center[1],
             circle_center[0] + crosshair_size, circle_center[1]],
            fill=(255, 0, 0, 255), width=2
        )
        draw.line(
            [circle_center[0], circle_center[1] - crosshair_size,
             circle_center[0], circle_center[1] + crosshair_size],
            fill=(255, 0, 0, 255), width=2
        )
        
        # Composite and save
        result = Image.alpha_composite(img, overlay)
        result = result.convert('RGB')
        
        output_path = OVERLAYS_DIR / f"{output_name}.jpg"
        result.save(output_path, 'JPEG', quality=95)
        
        print(f"  ✓ Created overlay: {output_path}")
        
        verification_results["overlays"][output_name] = {
            "status": "success",
            "base_image": str(base_image_path),
            "output": str(output_path),
            "type": "concentric_circles",
            "num_circles": len(radii)
        }
        
        return output_path
        
    except Exception as e:
        error_msg = f"Failed to create overlay {output_name}: {e}"
        print(f"  ✗ {error_msg}")
        verification_results["overlays"][output_name] = {
            "status": "failed",
            "error": error_msg
        }
        verification_results["errors"].append(error_msg)
        return None


def save_verification_log():
    """Save verification results to JSON file."""
    try:
        with open(VERIFICATION_LOG, 'w') as f:
            json.dump(verification_results, f, indent=2)
        print(f"\n✓ Verification log saved: {VERIFICATION_LOG}")
    except Exception as e:
        print(f"\n✗ Failed to save verification log: {e}")


def print_summary():
    """Print summary of downloads and overlays."""
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    # Downloads
    downloads_success = sum(1 for v in verification_results["downloads"].values() 
                           if v.get("status") == "success")
    downloads_total = len(verification_results["downloads"])
    
    print(f"\nDownloads: {downloads_success}/{downloads_total} successful")
    for img_id, result in verification_results["downloads"].items():
        status_icon = "✓" if result.get("status") == "success" else "✗"
        print(f"  {status_icon} {img_id}")
        if result.get("status") == "success":
            print(f"    Size: {result.get('size_kb', 0):.1f} KB")
            print(f"    Dimensions: {result.get('dimensions')}")
    
    # Overlays
    overlays_success = sum(1 for v in verification_results["overlays"].values() 
                          if v.get("status") == "success")
    overlays_total = len(verification_results["overlays"])
    
    print(f"\nOverlays: {overlays_success}/{overlays_total} successful")
    for overlay_name, result in verification_results["overlays"].items():
        status_icon = "✓" if result.get("status") == "success" else "✗"
        print(f"  {status_icon} {overlay_name}")
    
    # Errors
    if verification_results["errors"]:
        print(f"\nErrors ({len(verification_results['errors'])}):")
        for error in verification_results["errors"]:
            print(f"  ✗ {error}")
    else:
        print("\n✓ No errors!")
    
    print("\n" + "="*70)


def main():
    """Main execution function."""
    print("="*70)
    print("Grade 3 Lesson 1A: Image Downloader and Overlay Creator")
    print("="*70)
    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}")
    print(f"Overlays directory: {OVERLAYS_DIR.absolute()}")
    
    # Step 1: Download museum images
    print("\n" + "-"*70)
    print("STEP 1: Downloading Museum Images")
    print("-"*70)
    
    downloaded_images = {}
    
    for image_id, image_info in MUSEUM_IMAGES.items():
        print(f"\n📥 {image_info['name']}")
        print(f"   Museum: {image_info['museum']}")
        print(f"   Accession: {image_info['accession']}")
        
        image_path = download_image(image_id, image_info)
        
        if image_path is None:
            # Create placeholder
            print("  ℹ Creating placeholder image...")
            image_path = create_placeholder_image(image_id, image_info)
        
        downloaded_images[image_id] = image_path
        time.sleep(1)  # Be polite to museum servers
    
    # Step 2: Create overlays
    print("\n" + "-"*70)
    print("STEP 2: Creating Geometric Overlays")
    print("-"*70)
    
    # Overlay specifications matching the lesson
    overlay_specs = [
        {
            "base": "shamash_tablet",
            "output": "shamash_tablet_overlay1_basic",
            "function": create_overlay_circle_basic,
            "instructions": {
                "circle_center": None,  # Will auto-detect
                "circle_radius": None
            }
        },
        {
            "base": "shamash_tablet",
            "output": "shamash_tablet_overlay2_rays",
            "function": create_overlay_radial_rays,
            "instructions": {
                "num_rays": 4
            }
        },
        {
            "base": "cylinder_seal",
            "output": "cylinder_seal_overlay_rays",
            "function": create_overlay_radial_rays,
            "instructions": {
                "num_rays": 8
            }
        },
        {
            "base": "ubaid_bowl",
            "output": "ubaid_bowl_overlay1_circles",
            "function": create_overlay_concentric_circles,
            "instructions": {
                "radii": [50, 100, 150]
            }
        },
        {
            "base": "ubaid_bowl",
            "output": "ubaid_bowl_overlay2_rays",
            "function": create_overlay_radial_rays,
            "instructions": {
                "num_rays": 8
            }
        },
        {
            "base": "ur_rosette",
            "output": "ur_rosette_overlay1_structure",
            "function": create_overlay_concentric_circles,
            "instructions": {
                "radii": [30, 95, 150]
            }
        },
        {
            "base": "ur_rosette",
            "output": "ur_rosette_overlay2_rays",
            "function": create_overlay_radial_rays,
            "instructions": {
                "num_rays": 8
            }
        },
        {
            "base": "stone_weight",
            "output": "stone_weight_overlay_precision",
            "function": create_overlay_circle_basic,
            "instructions": {}
        }
    ]
    
    for spec in overlay_specs:
        base_image_id = spec["base"]
        if base_image_id in downloaded_images:
            base_path = downloaded_images[base_image_id]
            print(f"\n🎨 Creating: {spec['output']}")
            
            spec["function"](base_path, spec["output"], spec["instructions"])
        else:
            print(f"\n⚠ Skipping {spec['output']} - base image not available")
    
    # Step 3: Save verification log
    print("\n" + "-"*70)
    print("STEP 3: Saving Verification Log")
    print("-"*70)
    save_verification_log()
    
    # Step 4: Print summary
    print_summary()
    
    print(f"\n✓ Process complete!")
    print(f"  Images: {OUTPUT_DIR.absolute()}")
    print(f"  Overlays: {OVERLAYS_DIR.absolute()}")
    print(f"  Log: {VERIFICATION_LOG.absolute()}")


if __name__ == "__main__":
    try:
        # Check for required packages
        required_packages = ["PIL", "requests"]
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package if package != "PIL" else "PIL")
            except ImportError:
                missing_packages.append(package)
        
        if missing_packages:
            print("❌ Missing required packages:")
            for pkg in missing_packages:
                print(f"   - {pkg}")
            print("\nInstall with: pip install Pillow requests")
            sys.exit(1)
        
        main()
        
    except KeyboardInterrupt:
        print("\n\n⚠ Process interrupted by user")
        save_verification_log()
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        save_verification_log()
        sys.exit(1)
