#!/usr/bin/env python3
"""
Image Sourcing Pipeline - Geometric Civilizations
Fetches artifact images from Met API, Wikimedia Commons, and other sources
"""

import json
import requests
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import quote
import hashlib


class ImageSourcer:
    def __init__(self, output_dir: str, cache_dir: str = None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.cache_dir = Path(cache_dir) if cache_dir else self.output_dir / ".cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.met_base_url = "https://collectionapi.metmuseum.org/public/collection/v1"
        self.wikimedia_base_url = "https://commons.wikimedia.org/w/api.php"

        # Session for connection pooling
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'GeometricCivilizations/1.0 (Educational; mailto:contact@example.org)'
        })

    def search_met(self, query: str, has_images: bool = True) -> List[int]:
        """Search Met Museum collection"""
        print(f"🔍 Searching Met Museum for: {query}")

        url = f"{self.met_base_url}/search"
        params = {
            'q': query,
            'hasImages': 'true' if has_images else 'false'
        }

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            object_ids = data.get('objectIDs', [])
            print(f"✓ Found {len(object_ids) if object_ids else 0} objects")

            return object_ids[:20]  # Return first 20 results

        except requests.exceptions.RequestException as e:
            print(f"✗ Met search failed: {e}")
            return []

    def get_met_object(self, object_id: int) -> Optional[Dict]:
        """Get Met object details"""
        url = f"{self.met_base_url}/objects/{object_id}"

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"✗ Failed to get object {object_id}: {e}")
            return None

    def download_met_image(self, object_data: Dict, output_path: Path) -> bool:
        """Download image from Met object data"""
        image_url = object_data.get('primaryImage') or object_data.get('primaryImageSmall')

        if not image_url:
            print(f"✗ No image URL found")
            return False

        try:
            print(f"⬇ Downloading: {image_url}")
            response = self.session.get(image_url, timeout=30, stream=True)
            response.raise_for_status()

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"✓ Downloaded: {output_path.name}")
            return True

        except requests.exceptions.RequestException as e:
            print(f"✗ Download failed: {e}")
            return False

    def search_wikimedia(self, query: str, limit: int = 10) -> List[Dict]:
        """Search Wikimedia Commons"""
        print(f"🔍 Searching Wikimedia Commons for: {query}")

        params = {
            'action': 'query',
            'format': 'json',
            'generator': 'search',
            'gsrsearch': query,
            'gsrnamespace': 6,  # File namespace
            'gsrlimit': limit,
            'prop': 'imageinfo',
            'iiprop': 'url|size|mime|extmetadata',
            'iiurlwidth': 1920
        }

        try:
            response = self.session.get(self.wikimedia_base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            pages = data.get('query', {}).get('pages', {})
            results = []

            for page_id, page_data in pages.items():
                imageinfo = page_data.get('imageinfo', [{}])[0]
                results.append({
                    'title': page_data.get('title', ''),
                    'url': imageinfo.get('url', ''),
                    'thumburl': imageinfo.get('thumburl', ''),
                    'width': imageinfo.get('width', 0),
                    'height': imageinfo.get('height', 0),
                    'mime': imageinfo.get('mime', ''),
                    'descriptionurl': imageinfo.get('descriptionurl', '')
                })

            print(f"✓ Found {len(results)} images")
            return results

        except requests.exceptions.RequestException as e:
            print(f"✗ Wikimedia search failed: {e}")
            return []

    def download_wikimedia_image(self, image_data: Dict, output_path: Path) -> bool:
        """Download image from Wikimedia"""
        image_url = image_data.get('thumburl') or image_data.get('url')

        if not image_url:
            print(f"✗ No image URL found")
            return False

        try:
            print(f"⬇ Downloading: {image_url}")
            response = self.session.get(image_url, timeout=30, stream=True)
            response.raise_for_status()

            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"✓ Downloaded: {output_path.name}")
            return True

        except requests.exceptions.RequestException as e:
            print(f"✗ Download failed: {e}")
            return False

    def search_and_download(self, query: str, output_filename: str, source: str = "met") -> Optional[Dict]:
        """Search and download image, return metadata"""
        output_path = self.output_dir / output_filename

        # Check if already downloaded
        if output_path.exists():
            print(f"✓ Already exists: {output_filename}")
            return {"path": str(output_path), "source": source}

        if source == "met":
            object_ids = self.search_met(query)

            for obj_id in object_ids:
                time.sleep(0.5)  # Rate limiting

                obj_data = self.get_met_object(obj_id)
                if not obj_data:
                    continue

                if self.download_met_image(obj_data, output_path):
                    return {
                        "path": str(output_path),
                        "source": "Met",
                        "objectId": obj_id,
                        "title": obj_data.get('title', ''),
                        "artist": obj_data.get('artistDisplayName', ''),
                        "date": obj_data.get('objectDate', ''),
                        "culture": obj_data.get('culture', ''),
                        "accessionNumber": obj_data.get('accessionNumber', ''),
                        "url": obj_data.get('objectURL', ''),
                        "license": "CC0 1.0"  # Met is CC0
                    }

        elif source == "wikimedia":
            results = self.search_wikimedia(query)

            for img_data in results:
                time.sleep(0.5)  # Rate limiting

                if self.download_wikimedia_image(img_data, output_path):
                    return {
                        "path": str(output_path),
                        "source": "Wikimedia",
                        "title": img_data.get('title', ''),
                        "url": img_data.get('descriptionurl', ''),
                        "width": img_data.get('width', 0),
                        "height": img_data.get('height', 0),
                        "license": "Various - check page"
                    }

        print(f"✗ No suitable image found for: {query}")
        return None

    def source_lesson_artifacts(self, lesson_path: str):
        """Source all images for a lesson's artifacts"""
        with open(lesson_path, 'r') as f:
            lesson = json.load(f)

        lesson_id = lesson['lessonId']
        print(f"\n{'='*60}")
        print(f"Sourcing images for {lesson_id}")
        print(f"{'='*60}\n")

        artifacts = lesson.get('artifacts', [])
        metadata_log = []

        for artifact in artifacts:
            artifact_id = artifact['artifactId']
            artifact_title = artifact['title']
            civilization = artifact['civilization']

            # Construct search query
            query = f"{artifact_title} {civilization}"

            # Determine source (prefer Met for most artifacts)
            source = "met" if civilization in ["Egypt", "Greece", "Rome", "Mesopotamia"] else "wikimedia"

            # Generate filename
            filename = f"{lesson_id}-{artifact_id}.jpg"

            print(f"\n📦 Artifact: {artifact_title}")
            print(f"   Query: {query}")
            print(f"   Source: {source}")

            metadata = self.search_and_download(query, filename, source)

            if metadata:
                metadata_log.append({
                    "lessonId": lesson_id,
                    "artifactId": artifact_id,
                    "artifactTitle": artifact_title,
                    **metadata
                })

                # Update lesson JSON with actual path
                artifact['imageUrl'] = f"assets/artifacts/{filename}"
                if 'metadata' in artifact:
                    artifact['metadata'].update({
                        k: v for k, v in metadata.items()
                        if k not in ['path', 'lessonId', 'artifactId', 'artifactTitle']
                    })

        # Save updated lesson
        with open(lesson_path, 'w') as f:
            json.dump(lesson, f, indent=2)

        # Save metadata log
        log_path = self.output_dir / f"{lesson_id}-image-metadata.json"
        with open(log_path, 'w') as f:
            json.dump(metadata_log, f, indent=2)

        print(f"\n✓ Image sourcing complete for {lesson_id}")
        print(f"✓ Downloaded {len(metadata_log)} images")
        print(f"✓ Metadata saved: {log_path}")

    def generate_placeholder(self, output_filename: str, text: str, width: int = 1600, height: int = 1200):
        """Generate a placeholder image using dummyimage.com or similar"""
        output_path = self.output_dir / output_filename

        if output_path.exists():
            print(f"✓ Placeholder exists: {output_filename}")
            return

        # Use placeholder service
        url = f"https://via.placeholder.com/{width}x{height}/CCCCCC/333333?text={quote(text)}"

        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            with open(output_path, 'wb') as f:
                f.write(response.content)

            print(f"✓ Generated placeholder: {output_filename}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Placeholder generation failed: {e}")


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python image_sourcer.py <lesson_json_path>")
        sys.exit(1)

    lesson_path = sys.argv[1]
    root_dir = Path(__file__).parent.parent
    output_dir = root_dir / "assets" / "artifacts"

    sourcer = ImageSourcer(str(output_dir))
    sourcer.source_lesson_artifacts(lesson_path)


if __name__ == "__main__":
    main()
