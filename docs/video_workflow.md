# Video Generation Workflow
## Geometric Civilizations Lesson Videos

### Overview
Transform lesson JSON → PowerPoint slides → Video with overlays, narration, and transitions.

### Pipeline Stages

```
Lesson JSON
    ↓
PowerPoint Generation (python-pptx)
    ↓
Slide Export (PNG images)
    ↓
Overlay Composition (SVG → PNG layer)
    ↓
Video Assembly (FFmpeg or CapCut)
    ↓
Final Lesson Video (MP4)
```

---

## 1. PowerPoint Generation (`pptx_generator.py`)

### Input
- Lesson JSON (`G3-01.json`)
- Design system specs (`design_system.json`)

### Process
```python
from pptx import Presentation
from pptx.util import Inches, Pt

def generate_lesson_slides(lesson_json, design_system):
    prs = Presentation()
    prs.slide_width = Inches(16)
    prs.slide_height = Inches(9)

    # Title Slide
    add_title_slide(prs, lesson)

    # SEL Slide
    add_sel_slide(prs, lesson['sel'])

    # Hook Slide
    add_hook_slide(prs, lesson['hook'])

    # Myth Slides (5 scenes)
    for scene in lesson['myth']['scenes']:
        add_myth_slide(prs, scene)

    # Artifact Slides (with overlays)
    for artifact in lesson['artifacts']:
        add_artifact_slide(prs, artifact)

    # Activity Slides
    add_math_activity_slide(prs, lesson['mathActivity'])
    add_art_activity_slide(prs, lesson['artActivity'])
    add_geometry_activity_slide(prs, lesson['geometryActivity'])

    # Bridge Slide
    add_bridge_slide(prs, lesson['bridge'])

    # Exit Slide
    add_exit_slide(prs, lesson['exit'])

    prs.save(f"{lesson['lessonId']}.pptx")
```

### Slide Layouts

#### Title Slide
- **Layout**: `slideLayouts.titleSlide`
- **Elements**:
  - Lesson ID (top left)
  - Math concept (large, center)
  - Geometric concept (subtitle)
  - Civilization badge (bottom)
  - Decorative geometric shape

#### SEL Slide
- **Layout**: `slideLayouts.selSlide`
- **Elements**:
  - Prompt text (large, readable)
  - Illustration (mood shapes)
  - Duration indicator

#### Hook Slide
- **Layout**: `slideLayouts.hookSlide`
- **Elements**:
  - Character image (left 30%)
  - Narrative text (right 50%)
  - Question prompt (bottom)

#### Myth Slide
- **Layout**: `slideLayouts.mythSlide`
- **Elements**:
  - Artifact/scene image (left 50%)
  - Narration text (right 35%)
  - Caption (bottom 10%)

#### Artifact Slide
- **Layout**: `slideLayouts.artifactSlide`
- **Elements**:
  - Artifact image (left 45%)
  - Overlay placeholder (right 35%)
  - Metadata (bottom 20%): museum, date, accession

#### Activity Slide
- **Layout**: `slideLayouts.activitySlide`
- **Elements**:
  - Instructions (top left 40%)
  - Workspace diagram (bottom 45%)
  - Tools/materials (top right 40%)

#### Bridge Slide
- **Layout**: `slideLayouts.bridgeSlide`
- **Elements**:
  - Math concept (left)
  - Connector arrow (center)
  - Art concept (right)
  - Synthesis text (bottom)

---

## 2. Slide Export (`export_slides.py`)

### Export slides as PNG images

```python
# Option 1: PowerPoint COM automation (Windows only)
import win32com.client

def export_slides_windows(pptx_path, output_dir):
    powerpoint = win32com.client.Dispatch("PowerPoint.Application")
    presentation = powerpoint.Presentations.Open(pptx_path)

    for i, slide in enumerate(presentation.Slides, 1):
        slide.Export(f"{output_dir}/slide-{i:03d}.png", "PNG")

    presentation.Close()
    powerpoint.Quit()

# Option 2: LibreOffice headless (cross-platform)
def export_slides_libreoffice(pptx_path, output_dir):
    import subprocess
    subprocess.run([
        "libreoffice",
        "--headless",
        "--convert-to", "png",
        "--outdir", output_dir,
        pptx_path
    ])

# Option 3: Use aspose.slides (Python library, paid)
```

### Output
- `assets/slides/G3-01/slide-001.png` (1920×1080)
- `assets/slides/G3-01/slide-002.png`
- ...

---

## 3. Overlay Composition (`compose_overlays.py`)

### Composite SVG overlays onto artifact slides

```python
from PIL import Image
import cairosvg

def composite_overlay(slide_image_path, overlay_svg_path, output_path):
    # Load base slide image
    base_img = Image.open(slide_image_path)

    # Convert SVG overlay to PNG with transparency
    overlay_png = cairosvg.svg2png(url=overlay_svg_path)
    overlay_img = Image.open(io.BytesIO(overlay_png))

    # Composite
    base_img.paste(overlay_img, (0, 0), overlay_img)
    base_img.save(output_path)
```

### Animated Overlay Drawing (for video)

```python
def create_overlay_animation(overlay_svg_path, duration_sec=2, fps=30):
    # Parse SVG elements
    elements = parse_svg_elements(overlay_svg_path)

    # Generate frames where elements "draw" progressively
    frames = []
    total_frames = duration_sec * fps

    for frame_idx in range(total_frames):
        progress = frame_idx / total_frames
        frame_svg = render_svg_at_progress(elements, progress)
        frame_png = cairosvg.svg2png(bytestring=frame_svg)
        frames.append(Image.open(io.BytesIO(frame_png)))

    return frames
```

---

## 4. Narration Generation (`generate_narration.py`)

### Text-to-Speech for lesson narration

```python
# Option 1: OpenAI TTS API
from openai import OpenAI

def generate_narration_openai(text, voice="alloy", output_path="narration.mp3"):
    client = OpenAI()
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,  # alloy, echo, fable, onyx, nova, shimmer
        input=text
    )
    response.stream_to_file(output_path)

# Option 2: Google Cloud TTS
from google.cloud import texttospeech

def generate_narration_google(text, output_path="narration.mp3"):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_path, "wb") as out:
        out.write(response.audio_content)

# Option 3: Microsoft Azure TTS
# Option 4: Amazon Polly
```

### Narration Script Generation

```python
def generate_narration_script(lesson):
    script = []

    # Hook narration
    script.append({
        "slide": 2,
        "text": lesson['hook']['narrative'],
        "duration": 30  # seconds
    })

    # Myth scene narrations
    for idx, scene in enumerate(lesson['myth']['scenes'], 3):
        script.append({
            "slide": idx,
            "text": scene['narration'],
            "duration": 25
        })

    # Artifact descriptions
    for idx, artifact in enumerate(lesson['artifacts'], 8):
        script.append({
            "slide": idx,
            "text": artifact.get('teachingNotes', ''),
            "duration": 20
        })

    return script
```

---

## 5. Video Assembly (`assemble_video.py`)

### Combine slides, overlays, narration, transitions

```python
import ffmpeg

def assemble_lesson_video(slides_dir, narration_audio, output_video, lesson_json):
    """
    Use FFmpeg to create video from slides + audio
    """

    # Generate input file list
    with open("slides.txt", "w") as f:
        for slide in sorted(Path(slides_dir).glob("*.png")):
            duration = 5  # seconds per slide (adjust based on narration)
            f.write(f"file '{slide}'\n")
            f.write(f"duration {duration}\n")

    # FFmpeg command
    ffmpeg.input("slides.txt", format='concat', safe=0) \
        .output(
            output_video,
            vcodec='libx264',
            pix_fmt='yuv420p',
            r=30,  # 30 fps
            **{'b:v': '5M'}  # 5 Mbps bitrate
        ) \
        .overwrite_output() \
        .run()

    # Add audio narration
    video = ffmpeg.input(output_video)
    audio = ffmpeg.input(narration_audio)

    ffmpeg.output(
        video, audio,
        f"{output_video.replace('.mp4', '-final.mp4')}",
        vcodec='copy',
        acodec='aac'
    ).overwrite_output().run()
```

### Advanced: Overlay Animation with FFmpeg

```python
def add_animated_overlays(base_video, overlay_frames_dir, output_video):
    """
    Overlay animated SVG drawings onto artifact slides
    """

    overlay_video = ffmpeg.input(f"{overlay_frames_dir}/frame-%03d.png", framerate=30)
    base = ffmpeg.input(base_video)

    # Composite overlay on top with fade-in
    ffmpeg.filter([base, overlay_video], 'overlay',
                  x=0, y=0,
                  enable='between(t,10,15)') \
        .output(output_video, vcodec='libx264') \
        .run()
```

---

## 6. CapCut Automation (Alternative)

### Export slides + overlays as image sequence
### Import into CapCut Desktop via project file

```json
{
  "project": {
    "name": "G3-01 Lesson Video",
    "timeline": {
      "tracks": [
        {
          "type": "video",
          "clips": [
            {
              "source": "assets/slides/G3-01/slide-001.png",
              "duration": 5000,
              "transitions": {
                "in": {"type": "fade", "duration": 500},
                "out": {"type": "fade", "duration": 500}
              },
              "effects": []
            },
            {
              "source": "assets/slides/G3-01/slide-002.png",
              "duration": 30000,
              "effects": [
                {
                  "type": "pan_zoom",
                  "start": {"x": 0, "y": 0, "scale": 1.0},
                  "end": {"x": -100, "y": -50, "scale": 1.2},
                  "easing": "ease_in_out"
                }
              ]
            }
          ]
        },
        {
          "type": "audio",
          "clips": [
            {
              "source": "assets/narration/G3-01-narration.mp3",
              "volume": 1.0,
              "fadeIn": 500,
              "fadeOut": 500
            },
            {
              "source": "assets/music/background-ambient.mp3",
              "volume": 0.15,
              "loop": true
            }
          ]
        },
        {
          "type": "overlay",
          "clips": [
            {
              "source": "assets/overlays/G3-01-artifact-01-overlay-01.svg",
              "start": 45000,
              "duration": 5000,
              "animation": {
                "type": "draw",
                "duration": 2000,
                "stagger": 200
              }
            }
          ]
        }
      ]
    }
  }
}
```

---

## 7. Complete Automation Script

### `build_lesson_video.py`

```python
#!/usr/bin/env python3
"""
Complete lesson video builder
"""

def build_lesson_video(lesson_id):
    lesson_path = f"lessons/{lesson_id}.json"

    print(f"Building video for {lesson_id}...")

    # 1. Generate PowerPoint
    print("  1. Generating slides...")
    generate_pptx(lesson_path, f"output/{lesson_id}.pptx")

    # 2. Export slides to PNG
    print("  2. Exporting slides...")
    export_slides(f"output/{lesson_id}.pptx", f"output/{lesson_id}/slides")

    # 3. Generate overlays
    print("  3. Generating overlays...")
    generate_overlays(lesson_path, f"output/{lesson_id}/overlays")

    # 4. Composite overlays onto slides
    print("  4. Compositing overlays...")
    composite_overlays(
        f"output/{lesson_id}/slides",
        f"output/{lesson_id}/overlays",
        f"output/{lesson_id}/composited"
    )

    # 5. Generate narration
    print("  5. Generating narration...")
    generate_narration(lesson_path, f"output/{lesson_id}/narration.mp3")

    # 6. Assemble final video
    print("  6. Assembling video...")
    assemble_video(
        f"output/{lesson_id}/composited",
        f"output/{lesson_id}/narration.mp3",
        f"output/{lesson_id}-final.mp4"
    )

    print(f"✓ Video complete: output/{lesson_id}-final.mp4")

if __name__ == "__main__":
    import sys
    lesson_id = sys.argv[1] if len(sys.argv) > 1 else "G3-01"
    build_lesson_video(lesson_id)
```

---

## 8. Video Specifications (from design_system.json)

```json
"videoSpecs": {
  "slideTransitions": {
    "duration": "0.5s",
    "default": "fade",
    "options": ["fade", "slide", "zoom", "wipe"]
  },
  "panZoom": {
    "duration": "3s",
    "easing": "easeInOutCubic",
    "maxZoom": 1.5
  },
  "overlayAnimation": {
    "drawDuration": "2s",
    "fadeDuration": "0.3s",
    "stagger": "0.2s"
  },
  "voiceOver": {
    "wpm": 150,
    "pauseAfterSentence": "0.5s",
    "pauseAfterSlide": "1s"
  },
  "backgroundMusic": {
    "volume": 0.15,
    "fadeIn": "2s",
    "fadeOut": "2s"
  }
}
```

---

## Summary

### Tools Required
- **Python-PPTX**: Slide generation
- **LibreOffice or PowerPoint COM**: Slide export
- **Cairo / CairoSVG**: SVG rendering
- **Pillow (PIL)**: Image composition
- **FFmpeg**: Video assembly
- **OpenAI TTS / Google TTS**: Narration generation

### Full Pipeline Command

```bash
# Generate all components for one lesson
./build_lesson.sh G3-01

# Pipeline steps:
python generate_curriculum.py              # Generate 54 lesson JSONs
python pptx_generator.py G3-01             # Generate PowerPoint
python export_slides.py G3-01.pptx         # Export PNGs
python overlay_generator.py G3-01          # Generate SVG overlays
python compose_overlays.py G3-01           # Composite layers
python generate_narration.py G3-01         # TTS narration
python assemble_video.py G3-01             # FFmpeg video
```

### Output Structure

```
output/
├── G3-01/
│   ├── G3-01.pptx
│   ├── slides/
│   │   ├── slide-001.png
│   │   ├── slide-002.png
│   │   └── ...
│   ├── overlays/
│   │   ├── overlay-001.svg
│   │   └── overlay-001-animated/ (frames)
│   ├── composited/
│   │   ├── slide-001.png
│   │   └── ...
│   ├── narration.mp3
│   └── G3-01-final.mp4
```

---

## Next Steps

1. Implement `pptx_generator.py` with full layout support
2. Choose slide export method (LibreOffice recommended for cross-platform)
3. Implement overlay animation frame generation
4. Select TTS provider and implement narration script parsing
5. Test FFmpeg pipeline with sample lesson
6. Optionally: Create CapCut project template generator
