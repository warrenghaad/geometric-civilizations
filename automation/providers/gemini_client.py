#!/usr/bin/env python3
"""
Google Gemini Client - Generate educational diagrams and technical illustrations
Part of the Multi-Provider AI Image Generation System
"""

import os
import time
from typing import Dict, Any, Optional, List
from pathlib import Path
import requests
import json
import base64


class GeminiClient:
    """Client for Google Gemini image generation."""

    def __init__(self, api_key: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize Gemini client.

        Args:
            api_key: Google Gemini API key (defaults to GOOGLE_GEMINI_API_KEY env var)
            config: Configuration dict from provider_settings.yaml
        """
        self.api_key = api_key or os.getenv('GOOGLE_GEMINI_API_KEY')
        if not self.api_key:
            raise ValueError("Google Gemini API key required (set GOOGLE_GEMINI_API_KEY env var)")

        self.config = config or {
            "model": "gemini-1.5-pro",
            "max_concurrent": 10,
            "timeout": 60,
            "retry_attempts": 3,
            "retry_delay": 1
        }

        self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.config['model']}:generateContent"

    def generate_image(self, prompt: str, output_path: Path, **kwargs) -> Dict[str, Any]:
        """
        Generate an image using Gemini.

        Note: Gemini 1.5 Pro primarily generates text. For image generation,
        we use it to create SVG code or detailed specifications that can be
        rendered programmatically.

        Args:
            prompt: Text prompt for image generation
            output_path: Where to save the generated image/SVG
            **kwargs: Additional parameters

        Returns:
            Dict with generation metadata
        """
        # Modify prompt to request SVG/technical output
        enhanced_prompt = f"""Generate precise SVG code for: {prompt}

Requirements:
- Clean, valid SVG markup
- Proper viewBox and dimensions
- Educational clarity
- Scalable and optimized
- Include comments for key elements

Return ONLY the SVG code, no explanations."""

        params = {
            "contents": [{
                "parts": [{
                    "text": enhanced_prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.4,  # Lower temperature for technical precision
                "topK": 40,
                "topP": 0.95,
                "maxOutputTokens": 8192
            }
        }

        # Make API request with retries
        for attempt in range(self.config["retry_attempts"]):
            try:
                response = requests.post(
                    f"{self.base_url}?key={self.api_key}",
                    headers={"Content-Type": "application/json"},
                    json=params,
                    timeout=self.config["timeout"]
                )

                response.raise_for_status()
                result = response.json()

                # Extract generated content
                content = result["candidates"][0]["content"]["parts"][0]["text"]

                # Extract SVG code if present
                svg_content = self._extract_svg(content)

                # Save to file
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(svg_content)

                return {
                    "success": True,
                    "output_path": str(output_path),
                    "provider": "gemini",
                    "model": self.config["model"],
                    "format": "svg",
                    "cost": 0.02  # Estimated cost per generation
                }

            except requests.exceptions.RequestException as e:
                if attempt < self.config["retry_attempts"] - 1:
                    delay = self.config["retry_delay"] * (2 ** attempt)
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
                else:
                    return {
                        "success": False,
                        "error": str(e),
                        "provider": "gemini"
                    }

    def _extract_svg(self, content: str) -> str:
        """Extract SVG code from response content."""
        # Look for SVG tags
        import re
        svg_match = re.search(r'<svg[^>]*>.*</svg>', content, re.DOTALL | re.IGNORECASE)

        if svg_match:
            return svg_match.group(0)

        # If no SVG found, check for code blocks
        code_block_match = re.search(r'```(?:svg|xml)?\n(.*?)\n```', content, re.DOTALL)
        if code_block_match:
            return code_block_match.group(1)

        # Return as-is if it looks like SVG
        if '<svg' in content.lower():
            return content

        # Otherwise, wrap in basic SVG structure
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <!-- Generated by Gemini -->
  <text x="400" y="300" text-anchor="middle" font-size="16" fill="#333">
    {content[:200]}
  </text>
</svg>"""

    def generate_diagram(self, description: str, output_path: Path, diagram_type: str = "technical") -> Dict[str, Any]:
        """
        Generate a technical diagram or educational illustration.

        Args:
            description: Description of the diagram
            output_path: Where to save the SVG
            diagram_type: Type of diagram (technical, educational, physics, geometry)

        Returns:
            Generation result dict
        """
        diagram_prompts = {
            "technical": "Create a precise technical diagram showing",
            "educational": "Create a clear educational illustration for K-8 students showing",
            "physics": "Create a physics diagram with force vectors and labels showing",
            "geometry": "Create a geometric diagram with precise measurements showing"
        }

        prefix = diagram_prompts.get(diagram_type, "Create a diagram showing")
        prompt = f"{prefix} {description}"

        return self.generate_image(prompt, output_path)

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

            # Rate limiting
            if i < len(prompts) - 1:
                time.sleep(0.5)  # 0.5 second between requests

        return results


def main():
    """Command-line interface for Gemini client."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate diagrams with Gemini')
    parser.add_argument('prompt', type=str, help='Diagram description')
    parser.add_argument('--output', type=Path, required=True, help='Output SVG path')
    parser.add_argument('--type', choices=['technical', 'educational', 'physics', 'geometry'],
                       default='educational', help='Diagram type')

    args = parser.parse_args()

    # Generate diagram
    client = GeminiClient()
    result = client.generate_diagram(args.prompt, args.output, args.type)

    if result["success"]:
        print(f"\n✓ Diagram generated successfully!")
        print(f"Saved to: {result['output_path']}")
        print(f"Format: {result['format']}")
    else:
        print(f"\n✗ Generation failed: {result['error']}")


if __name__ == '__main__':
    main()
