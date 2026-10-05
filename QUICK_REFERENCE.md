# Quick Reference Card

Fast lookup for common commands and tasks.

## Installation

```bash
# Install Node.js from https://nodejs.org (LTS version)

# Install dependencies
npm install

# Setup configuration
cp config.example.json config.json
# Then edit config.json with your API key
```

## Common Commands

### AI Tutor
```bash
npm run tutor                    # Start interactive learning companion
```

### Content Generation
```bash
# Generate lesson
npm run bot:content -- --civilization ancient-egypt --topic circles

# With options
npm run bot:content -- --civilization ancient-greece --topic pythagorean-theorem --difficulty beginner --format html
```

### Quiz Creation
```bash
# Generate quiz
npm run bot:quiz -- --topic circles --questions 10

# With options
npm run bot:quiz -- --topic pythagorean-theorem --civilization ancient-greece --difficulty beginner --type multiple-choice
```

### Visualizations
```bash
# Create visualization
npm run bot:visualize -- --shape hexagon

# With options
npm run bot:visualize -- --shape star --civilization islamic-golden-age --interactive true
```

### Assessment
```bash
# Assess content quality
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json

# With criteria
npm run bot:assess -- --file curriculum/quiz.json --criteria readability
```

### Image Decomposition (NEW - Grades 3-5)
```bash
# Create demo lesson
npm run bot:decompose -- --demo

# Process your image
npm run bot:decompose -- --image photos/house.jpg --outline outlines/shapes.txt

# With options
npm run bot:decompose -- --image photos/robot.jpg --outline outlines/lesson.json --grade 4 --shapes 2d
```

## Help Commands

```bash
# Get help on any bot
npm run bot:content -- --help
npm run bot:quiz -- --help
npm run bot:visualize -- --help
npm run bot:assess -- --help
npm run bot:decompose -- --help

# Main project info
npm start
```

## File Structure

```
geometric-civilizations/
├── README.md                   # Full documentation
├── QUICK_REFERENCE.md          # This file
├── package.json                # Project configuration
├── config.json                 # Your settings (create from config.example.json)
│
├── bots/                       # Automation bots
│   ├── content-generator/      # Lesson creation
│   ├── quiz-generator/         # Quiz creation
│   ├── visualization-generator/# Diagram creation
│   └── assessment/             # Quality checking
│
├── curriculum/                 # Generated content
│   ├── templates/              # Starting templates
│   └── [civilizations]/        # Content by civilization
│
├── tutor/                      # AI Tutor system
├── docs/                       # Documentation
│   ├── beginner-guide.md       # For new programmers
│   ├── bot-guide.md            # Bot usage details
│   ├── curriculum-guide.md     # Content creation guide
│   └── troubleshooting.md      # Common issues
│
└── examples/                   # Sample outputs
```

## Supported Options

### Civilizations
- `ancient-egypt`
- `ancient-greece`
- `ancient-china`
- `islamic-golden-age`
- `maya`
- `indian`

### Topics
- `circles`
- `triangles`
- `pythagorean-theorem`
- `geometric-patterns`
- `polygons`
- `symmetry`
- `fractals`

### Difficulty Levels
- `beginner`
- `intermediate`
- `advanced`

### Formats
- `json`
- `markdown`
- `html`

### Question Types
- `multiple-choice`
- `true-false`
- `short-answer`
- `mixed`

## Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "npm: command not found" | Install Node.js from nodejs.org |
| "Cannot find config.json" | Run: `cp config.example.json config.json` |
| "API key invalid" | Edit config.json with valid OpenAI API key |
| "Module not found" | Run: `npm install` |
| Bot won't run | Check config.json has bot enabled |
| Need help | Run: `npm run tutor` |

## Learning Path

1. **Day 1**: Install, configure, run tutor
2. **Day 2**: Generate first lesson
3. **Day 3**: Create quiz and visualization
4. **Day 4**: Customize content
5. **Day 5**: Explore the code

## Essential Links

- **Node.js**: https://nodejs.org
- **OpenAI API**: https://platform.openai.com/api-keys
- **Documentation**: See docs/ folder
- **Examples**: See examples/ folder

## Getting Help

1. Run the AI Tutor: `npm run tutor`
2. Check documentation in docs/
3. Use `--help` flag on any command
4. Read error messages carefully

---

**Remember**: The AI Tutor (`npm run tutor`) is always available to help! 🤖
