# Geometric Civilizations

An educational curriculum combining Mesopotamian history and geometry for Grades 3-5 (96 lessons).

---

## Claude Desktop Setup

To use Claude Desktop with this project for research, writing, and image viewing:

### Prerequisites

- [Node.js](https://nodejs.org/) installed (`brew install node` on Mac)
- Claude Desktop app installed

### Step 1: Clone the Repository

```bash
cd ~/Documents
git clone https://github.com/warrenghaad/geometric-civilizations.git
```

### Step 2: Configure Claude Desktop

Copy the contents of `claude_desktop_config.example.json` to:

```
/Users/YOUR_USERNAME/Library/Application Support/Claude/claude_desktop_config.json
```

**Update the path** in the filesystem server to match your actual clone location.

### Step 3: Restart Claude Desktop

The following capabilities will be available:

| MCP Server | Purpose |
|------------|---------|
| **filesystem** | Read/write project files, view images |
| **fetch** | Research - fetch web pages, academic sources |
| **memory** | Persistent memory across sessions |

---

## Capabilities

### Research
- Fetch and analyze web pages
- Pull academic sources
- Web search integration

### Writing
- Create and edit curriculum documents
- Generate lesson plans
- Update taxonomy specifications

### Image Viewing
- View local images in the project
- Analyze Mesopotamian artifacts
- Reference museum collection images

---

## Project Structure

```
geometric-civilizations/
├── GE_TAXONOMY_SPECIFICATION.md    # Graph node taxonomy
├── MESOPOTAMIAN_CURRICULUM_MAPPING_FOR_PERPLEXITY.md
├── script_cross_reference.py        # Curriculum automation
├── shell_script_manager.sh          # Pipeline management
├── Geometric Civilizations - Interactive Home Page (1).html
└── CURRICULUM_SYSTEM_ORGANIZED/
    ├── 01_ETEXTBOOK_PIPELINE/
    └── 02_VISUAL_ASSETS_PIPELINE/
```

---

## Graph Node Taxonomy

See [GE_TAXONOMY_SPECIFICATION.md](./GE_TAXONOMY_SPECIFICATION.md) for the complete specification of how to categorize graph nodes:

- **GEA** - Atomic geometric elements (shapes, insignia)
- **GEM** - Molecular composites
- **Operators** - Transformation and representation verbs
- **Carriers** - Where geometry lands (wall, seal, tablet)
- **Lenses** - GEK (function), GEpHR (meaning), GEU (ubiquity)
- **Skills** - Human production capacities
- **Visual Rhetoric** - Perceptual effects
- **F(ge)** - Functional outputs
- **Process markers** - Insight, Ingenuity, Creativity
