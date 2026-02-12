#!/usr/bin/env python3
"""
MESO Curriculum Image Downloader
Downloads and tracks all images for MESO lessons with metadata
"""

import requests
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import time
import json
import hashlib
from datetime import datetime

class MESOImageDownloader:
    def __init__(self, lesson_id, output_dir="meso_images"):
        self.lesson_id = lesson_id
        self.output_dir = Path(output_dir) / lesson_id
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.downloads = {}
        self.overlays = {}
        self.errors = []
        
    def download_image(self, url, filename, alt_text, backup_urls=None):
        """Download image with backup URL support"""
        filepath = self.output_dir / filename
        
        if filepath.exists():
            print(f"⏭️  Exists: {filename}")
            return str(filepath)
        
        urls_to_try = [url] + (backup_urls or [])
        
        for i, try_url in enumerate(urls_to_try):
            try:
                print(f"⚡ Downloading: {filename} (attempt {i+1}/{len(urls_to_try)})")
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh) MESO Educational Project'
                }
                
                r = requests.get(try_url, headers=headers, timeout=30, allow_redirects=True)
                r.raise_for_status()
                
                if len(r.content) < 1000:
                    print(f"   ✗ Too small ({len(r.content)} bytes)")
                    continue
                
                filepath.write_bytes(r.content)
                
                # Verify it's a valid image
                img = Image.open(filepath)
                width, height = img.size
                
                # Calculate checksum
                checksum = hashlib.md5(r.content).hexdigest()
                
                self.downloads[filename] = {
                    'status': 'success',
                    'url': try_url,
                    'url_index': i,
                    'filepath': str(filepath),
                    'size_kb': len(r.content) / 1024,
                    'dimensions': [width, height],
                    'format': img.format,
                    'checksum': checksum,
                    'alt_text': alt_text,
                    'timestamp': datetime.now().isoformat()
                }
                
                print(f"   ✓ {len(r.content)//1024} KB ({width}×{height})")
                time.sleep(0.5)
                return str(filepath)
                
            except Exception as e:
                print(f"   ✗ Attempt {i+1} failed: {str(e)[:50]}")
                if i == len(urls_to_try) - 1:
                    self.errors.append({
                        'filename': filename,
                        'urls_tried': urls_to_try,
                        'error': str(e)
                    })
        
        print(f"   ❌ All attempts failed for {filename}")
        return None
        
    def create_placeholder(self, filename, width, height, text, color='#FFD24A'):
        """Create placeholder image"""
        filepath = self.output_dir / filename
        
        img = Image.new('RGB', (width, height), color)
        draw = ImageDraw.Draw(img)
        
        # Try to load a font, fall back to default
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        except:
            font = ImageFont.load_default()
        
        # Draw text
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        draw.text((x, y), text, fill='#2B6CB0', font=font)
        
        img.save(filepath)
        print(f"   ✓ Created placeholder: {filename}")
        
        return str(filepath)
        
    def create_circle_overlay(self, base_image_path, overlay_type, output_filename):
        """Create geometric overlay on image"""
        if not base_image_path or not Path(base_image_path).exists():
            print(f"   ✗ Base image not found for overlay: {output_filename}")
            return None
        
        base_img = Image.open(base_image_path)
        width, height = base_img.size
        
        # Create transparent overlay
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        cx, cy = width // 2, height // 2
        radius = min(width, height) // 3
        
        if overlay_type == 'center_dot':
            # Center point
            dot_size = 10
            draw.ellipse([cx-dot_size, cy-dot_size, cx+dot_size, cy+dot_size], 
                        fill=(255, 0, 0, 255))
            draw.line([(cx-20, cy), (cx+20, cy)], fill=(255, 0, 0, 255), width=3)
            draw.line([(cx, cy-20), (cx, cy+20)], fill=(255, 0, 0, 255), width=3)
            
        elif overlay_type == 'circle':
            # Circle outline
            draw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius],
                        outline=(255, 0, 0, 255), width=5)
            
        elif overlay_type == 'halves':
            # Horizontal line through center
            draw.line([(cx-radius, cy), (cx+radius, cy)], 
                     fill=(0, 255, 0, 255), width=5)
            # Label
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
                draw.text((cx+radius+20, cy-20), "½", fill=(0, 255, 0, 255), font=font)
            except:
                pass
            
        elif overlay_type == 'fourths':
            # Two perpendicular lines
            draw.line([(cx-radius, cy), (cx+radius, cy)], 
                     fill=(0, 0, 255, 255), width=5)
            draw.line([(cx, cy-radius), (cx, cy+radius)], 
                     fill=(0, 0, 255, 255), width=5)
            # Label
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
                draw.text((cx+radius+20, cy-20), "¼", fill=(0, 0, 255, 255), font=font)
            except:
                pass
            
        elif overlay_type == 'radius':
            # Radius line
            draw.line([(cx, cy), (cx+radius, cy)], 
                     fill=(0, 255, 255, 255), width=4)
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
                draw.text((cx+radius//2, cy+10), "r", fill=(0, 255, 255, 255), font=font)
            except:
                pass
                
        elif overlay_type == 'diameter':
            # Diameter line
            draw.line([(cx-radius, cy), (cx+radius, cy)], 
                     fill=(255, 255, 0, 255), width=4)
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
                draw.text((cx, cy-30), "d", fill=(255, 255, 0, 255), font=font)
            except:
                pass
        
        # Composite
        output = Image.alpha_composite(base_img.convert('RGBA'), overlay)
        output_path = self.output_dir / output_filename
        output.save(output_path, 'PNG')
        
        self.overlays[output_filename] = {
            'status': 'success',
            'base_image': base_image_path,
            'overlay_type': overlay_type,
            'filepath': str(output_path),
            'dimensions': [width, height],
            'timestamp': datetime.now().isoformat()
        }
        
        print(f"   ✓ Created overlay: {output_filename}")
        return str(output_path)
        
    def save_verification_log(self):
        """Save verification log as JSON"""
        log_data = {
            'lesson_id': self.lesson_id,
            'downloads': self.downloads,
            'overlays': self.overlays,
            'errors': self.errors,
            'timestamp': datetime.now().isoformat(),
            'summary': {
                'total_downloads': len(self.downloads),
                'successful_downloads': sum(1 for d in self.downloads.values() if d['status'] == 'success'),
                'total_overlays': len(self.overlays),
                'total_errors': len(self.errors)
            }
        }
        
        log_file = self.output_dir / 'verification_log.json'
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\n✅ Verification log saved: {log_file}")
        return log_data


def download_grade1_lesson_images():
    """Download all images for Grade 3 Lesson 1A"""
    downloader = MESOImageDownloader('G3-1B')
    
    print("=" * 80)
    print("📥 MESO grade 3 LESSON 1A - IMAGE DOWNLOAD")
    print("=" * 80)
    print()
    
    # ========================================================================
    # SECTION 1: Look and Wonder
    # ========================================================================
    print("\n📸 SECTION 1: Look and Wonder")
    print("-" * 80)
    
    # Sun image
    downloader.download_image(
        'https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=2400',
        'meso_G3_1B-IMG-PHO_sun_bright.jpg',
        'Bright golden sun in clear blue sky',
        backup_urls=[
            'https://images.pexels.com/photos/158163/clouds-cloudporn-weather-lookup-158163.jpeg?w=2400'
        ]
    )
    
    # Plate (create placeholder)
    downloader.create_placeholder(
        'meso_G3_1B-IMG-PHO_plate_top.jpg',
        2400, 1600,
        'Round Plate\n(Top View)',
        '#FFFFFF'
    )
    
    # Wheel
    downloader.download_image(
        'https://images.unsplash.com/photo-1513828583688-c52646db42da?w=2400',
        'meso_G3_1B-IMG-PHO_wheel_round.jpg',
        'Round wheel showing circular shape',
        backup_urls=[
            'https://images.pexels.com/photos/210012/pexels-photo-210012.jpeg?w=2400'
        ]
    )
    
    # Drum
    downloader.download_image(
        'https://images.unsplash.com/photo-1519892300165-cb5542fb47c7?w=2400',
        'meso_G3_1B-IMG-PHO_drum_circle.jpg',
        'Round drum showing circular shape',
        backup_urls=[
            'https://images.pexels.com/photos/164821/pexels-photo-164821.jpeg?w=2400'
        ]
    )
    
    # Friends in circle (placeholder)
    downloader.create_placeholder(
        'meso_G3_1B-IMG-PHO_friends_ring.jpg',
        2400, 1600,
        'Children\nHolding Hands',
        '#FFD24A'
    )
    
    # ========================================================================
    # SECTION 4: Myth Sequence (14 scenes)
    # ========================================================================
    print("\n🎨 SECTION 4: Myth Illustrations")
    print("-" * 80)
    
    myth_scenes = [
        ('01_sun_river', 'Sun rising over river at dawn'),
        ('02_plate_loaf', 'Round loaf on round plate, top view'),
        ('03_hands_reach', 'Many hands reaching toward bread'),
        ('04_light_ring', 'Soft ring of sunlight on ground'),
        ('05_make_circle', 'Voice prompting children to form circle'),
        ('06_kids_ring', 'Children holding hands in circle'),
        ('07_center_loaf', 'Child placing loaf in center of circle'),
        ('08_half_string', 'String pulled across loaf to make halves'),
        ('09_halves_equal', 'Two equal halves of bread'),
        ('10_sun_moves', 'Sun moving across sky in steady arc'),
        ('11_four_shares', 'String crossing again to make fourths'),
        ('12_fourths_fair', 'Four equal parts, one for each friend'),
        ('13_crumbs_orbit', 'Crumbs traveling in circle pattern'),
        ('14_sun_high', 'Sun standing high and round in sky')
    ]
    
    for scene_id, description in myth_scenes:
        downloader.create_placeholder(
            f'meso_G3_1B-IMG-ILL_myth_{scene_id}.png',
            3840, 2160,
            f'Myth Scene {scene_id.split("_")[0]}\n{description}',
            '#FFD24A'
        )
    
    # ========================================================================
    # OVERLAYS
    # ========================================================================
    print("\n🎯 CREATING GEOMETRIC OVERLAYS")
    print("-" * 80)
    
    # Use plate image as base for overlays
    base_image = str(downloader.output_dir / 'meso_G3_1B-IMG-PHO_plate_top.jpg')
    
    overlays_to_create = [
        ('center_dot', 'meso_G3_1B-OVL-center_CENTER_Dot.png'),
        ('circle', 'meso_G3_1B-OVL-circle_outline.png'),
        ('halves', 'meso_G3_1B-OVL-line_LINE_Half.png'),
        ('fourths', 'meso_G3_1B-OVL-line_LINE_Quarter.png'),
        ('radius', 'meso_G3_1B-OVL-measure_radius.png'),
        ('diameter', 'meso_G3_1B-OVL-measure_diameter.png')
    ]
    
    for overlay_type, filename in overlays_to_create:
        downloader.create_circle_overlay(base_image, overlay_type, filename)
    
    # ========================================================================
    # SECTION 5: Artifacts
    # ========================================================================
    print("\n🏛️  SECTION 5: Ancient Artifacts")
    print("-" * 80)
    
    # Sun disc artifact
    downloader.download_image(
        'https://images.metmuseum.org/CRDImages/an/original/DT860.jpg',
        'meso_G3_1B-IMG-ART_sun_disc_ancient.jpg',
        'Ancient Mesopotamian sun disc with center dot motif',
        backup_urls=[
            'https://collectionapi.metmuseum.org/api/collection/v1/iiif/329090/711777/main-image'
        ]
    )
    
    # Modern bread (placeholder)
    downloader.create_placeholder(
        'meso_G3_1B-IMG-PHO_bread_plate.jpg',
        2400, 1600,
        'Round Bread\non Plate',
        '#B56533'
    )
    
    # ========================================================================
    # SECTION 6: Geometry Diagrams
    # ========================================================================
    print("\n📐 SECTION 6: Geometry Diagrams")
    print("-" * 80)
    
    diagram_steps = [
        ('step1_center', 'Step 1: Find the Center'),
        ('step2_halves', 'Step 2: Make Halves'),
        ('step3_fourths', 'Step 3: Make Fourths'),
        ('fold_test', 'Fold Test: Paper Folding')
    ]
    
    for step_id, description in diagram_steps:
        downloader.create_placeholder(
            f'meso_G3_1B-IMG-DGM_{step_id}.png',
            1920, 1080,
            description,
            '#FFFFFF'
        )
    
    # ========================================================================
    # SAVE VERIFICATION LOG
    # ========================================================================
    log_data = downloader.save_verification_log()
    
    # ========================================================================
    # SUMMARY
    # ========================================================================
    print("\n" + "=" * 80)
    print("📊 DOWNLOAD SUMMARY")
    print("=" * 80)
    print(f"✅ Downloads: {log_data['summary']['successful_downloads']}/{log_data['summary']['total_downloads']}")
    print(f"✅ Overlays: {log_data['summary']['total_overlays']}")
    print(f"❌ Errors: {log_data['summary']['total_errors']}")
    print(f"\n📁 Output: {downloader.output_dir}")
    print(f"📄 Log: {downloader.output_dir}/verification_log.json")
    print("=" * 80)
    
    return log_data


if __name__ == '__main__':
    download_grade1_lesson_images()
