#!/usr/bin/env python3
"""
OpenAI DALL-E 3 Client - Generate photorealistic images
Part of the Multi-Provider AI Image Generation System
"""

import os
import time
from typing import Dict, Any, Optional
from pathlib import Path
import requests
import json


class OpenAIClient:
    """Client for OpenAI DALL-E 3 image generation."""

    def __init__(self, api_key: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize OpenAI client.

        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            config: Configuration dict from provider_settings.yaml
        """
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key required (set OPENAI_API_KEY env var)")

        self.config = config or {
            "model": "dall-e-3",
            "quality": "standard",
            "size": "1792x1024",
            "max_concurrent": 5,
            "timeout": 120,
            "retry_attempts": 3,
            "retry_delay": 2
        }

        self.base_url = "https://api.openai.com/v1/images/generations"

    def generate_image(self, prompt: str, output_path: Path, **kwargs) -> Dict[str, Any]:
        """
        Generate an image using DALL-E 3.

        Args:
            prompt: Text prompt for image generation
            output_path: Where to save the generated image
            **kwargs: Additional parameters (size, quality, etc.)

        Returns:
            Dict with generation metadata (url, revised_prompt, etc.)
        """
        params = {
            "model": kwargs.get("model", self.config["model"]),
            "prompt": prompt,
            "quality": kwargs.get("quality", self.config["quality"]),
            "size": kwargs.get("size", self.config["size"]),
            "n": 1,
            "response_format": "url"
        }

        # Make API request with retries
        for attempt in range(self.config["retry_attempts"]):
            try:
                response = requests.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json"
                    },
                    json=params,
                    timeout=self.config["timeout"]
                )

                response.raise_for_status()
                result = response.json()

                # Download the generated image
                image_url = result["data"][0]["url"]
                self._download_image(image_url, output_path)

                return {
                    "success": True,
                    "url": image_url,
                    "revised_prompt": result["data"][0].get("revised_prompt"),
                    "output_path": str(output_path),
                    "provider": "openai",
                    "model": params["model"],
                    "cost": self._calculate_cost(params)
                }

            except requests.exceptions.RequestException as e:
                if attempt < self.config["retry_attempts"] - 1:
                    delay = self.config["retry_delay"] * (2 ** attempt)  # exponential backoff
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    return {
                        "success": False,
                        "error": str(e),
                        "provider": "openai"
                    }

    def _download_image(self, url: str, output_path: Path):
        """Download image from URL to local file."""
        response = requests.get(url, timeout=60)
        response.raise_for_status()

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)

    def _calculate_cost(self, params: Dict[str, Any]) -> float:
        """Calculate cost based on quality and size."""
        # DALL-E 3 pricing (as of 2024)
        if params["quality"] == "hd":
            if params["size"] == "1024x1024":
                return 0.080
            else:  # 1792x1024 or 1024x1792
                return 0.120
        else:  # standard quality
            if params["size"] == "1024x1024":
                return 0.040
            else:  # 1792x1024 or 1024x1792
                return 0.080

    def generate_batch(self, prompts: List[Dict[str, Any]], output_dir: Path) -> List[Dict[str, Any]]:
        """
        Generate multiple images in batch.

        Args:
            prompts: List of dicts with 'prompt' and 'filename' keys
            output_dir: Directory to save images

        Returns:
            List of generation results
        """
        results = []

        for i, item in enumerate(prompts):
            print(f"Generating {i+1}/{len(prompts)}: {item['filename']}")

            output_path = output_dir / item['filename']
            result = self.generate_image(item['prompt'], output_path)
            results.append(result)

            # Rate limiting: wait between requests
            if i < len(prompts) - 1:
                time.sleep(1)  # 1 second between requests

        return results


def main():
    """Command-line interface for OpenAI client."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate images with DALL-E 3')
    parser.add_argument('prompt', type=str, help='Image generation prompt')
    parser.add_argument('--output', type=Path, required=True, help='Output image path')
    parser.add_argument('--quality', choices=['standard', 'hd'], default='standard')
    parser.add_argument('--size', choices=['1024x1024', '1792x1024', '1024x1792'], default='1792x1024')

    args = parser.parse_args()

    # Generate image
    client = OpenAIClient()
    result = client.generate_image(
        args.prompt,
        args.output,
        quality=args.quality,
        size=args.size
    )

    if result["success"]:
        print(f"\n✓ Image generated successfully!")
        print(f"Saved to: {result['output_path']}")
        print(f"Cost: ${result['cost']:.3f}")
        print(f"Revised prompt: {result['revised_prompt']}")
    else:
        print(f"\n✗ Generation failed: {result['error']}")


if __name__ == '__main__':
    main()
