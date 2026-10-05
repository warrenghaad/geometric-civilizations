# Bot Usage Guide

Complete guide to using the curriculum generation bots.

## Overview

The Geometric Civilizations project includes four main bots:

1. **Content Generator** - Creates lesson plans and educational content
2. **Quiz Generator** - Makes interactive quizzes and assessments
3. **Visualization Generator** - Creates geometric diagrams and animations
4. **Assessment Bot** - Evaluates content quality

## Content Generator Bot

### Purpose
Generates comprehensive lesson plans about geometric concepts through different civilizations.

### Basic Usage
```bash
npm run bot:content -- --civilization <name> --topic <topic>
```

### Arguments

#### Required
- `--civilization`: Which civilization to focus on
  - `ancient-egypt`
  - `ancient-greece`
  - `ancient-china`
  - `islamic-golden-age`
  - `maya`
  - `indian`

- `--topic`: The geometric concept to teach
  - `circles`
  - `triangles`
  - `pythagorean-theorem`
  - `geometric-patterns`
  - `polygons`
  - `symmetry`
  - `fractals`

#### Optional
- `--difficulty`: Target difficulty
  - `beginner`
  - `intermediate` (default)
  - `advanced`

- `--format`: Output format
  - `json` (default)
  - `markdown`
  - `html`

- `--output`: Custom output path

### Examples

```bash
# Basic lesson
npm run bot:content -- --civilization ancient-egypt --topic circles

# Beginner-level HTML output
npm run bot:content -- --civilization ancient-greece --topic pythagorean-theorem --difficulty beginner --format html

# Custom output location
npm run bot:content -- --civilization islamic-golden-age --topic geometric-patterns --output my-lesson.json
```

### Output Structure

The bot generates structured lesson content:

```json
{
  "metadata": {
    "civilization": "ancient-egypt",
    "topic": "circles",
    "difficulty": "intermediate",
    "generatedDate": "2024-01-01T00:00:00.000Z"
  },
  "lesson": {
    "title": "Circles in Ancient Egypt",
    "introduction": "...",
    "learningObjectives": [...],
    "sections": [...],
    "assessment": {...},
    "resources": {...}
  }
}
```

## Quiz Generator Bot

### Purpose
Creates interactive quizzes and assessments for testing student understanding.

### Basic Usage
```bash
npm run bot:quiz -- --topic <topic> [options]
```

### Arguments

#### Required
- `--topic`: The topic for the quiz

#### Optional
- `--civilization`: Focus on specific civilization
- `--questions`: Number of questions (default: 10)
- `--difficulty`: Question difficulty
  - `beginner`
  - `intermediate`
  - `advanced`
  - `mixed` (default)
- `--type`: Question type
  - `multiple-choice`
  - `true-false`
  - `short-answer`
  - `mixed` (default)

### Examples

```bash
# Basic quiz
npm run bot:quiz -- --topic pythagorean-theorem

# Customized quiz
npm run bot:quiz -- --topic circles --civilization ancient-egypt --questions 15 --difficulty beginner

# Multiple choice only
npm run bot:quiz -- --topic geometric-patterns --type multiple-choice --questions 20
```

### Output Structure

```json
{
  "metadata": {
    "topic": "pythagorean-theorem",
    "questionCount": 10,
    "difficulty": "intermediate"
  },
  "quiz": {
    "title": "Pythagorean Theorem Quiz",
    "instructions": "...",
    "timeLimit": 20,
    "questions": [...]
  }
}
```

## Visualization Generator Bot

### Purpose
Creates interactive geometric visualizations and diagrams.

### Basic Usage
```bash
npm run bot:visualize -- --shape <shape> [options]
```

### Arguments

#### Required
- `--shape`: The geometric shape
  - `circle`
  - `triangle`
  - `square`
  - `hexagon`
  - `pentagon`
  - `pyramid`
  - `star`

#### Optional
- `--civilization`: Cultural context
- `--interactive`: Make it interactive (default: true)
- `--output`: Custom output path

### Examples

```bash
# Basic visualization
npm run bot:visualize -- --shape hexagon

# With cultural context
npm run bot:visualize -- --shape star --civilization islamic-golden-age

# Non-interactive
npm run bot:visualize -- --shape pyramid --civilization ancient-egypt --interactive false
```

### Output
Generates an HTML file with interactive canvas-based visualization.

## Assessment Bot

### Purpose
Evaluates content quality and suggests improvements.

### Basic Usage
```bash
npm run bot:assess -- --file <path>
```

### Arguments

#### Required
- `--file`: Path to content file to assess

#### Optional
- `--criteria`: Assessment criteria
  - `readability`
  - `accuracy`
  - `engagement`
  - `all` (default)

### Examples

```bash
# Assess a lesson
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json

# Focus on readability
npm run bot:assess -- --file curriculum/quizzes/pythagorean-quiz.json --criteria readability
```

## Workflow Examples

### Creating Complete Curriculum

#### 1. Generate Lesson
```bash
npm run bot:content -- --civilization ancient-egypt --topic circles --difficulty beginner
```

#### 2. Create Quiz
```bash
npm run bot:quiz -- --topic circles --civilization ancient-egypt --questions 10
```

#### 3. Add Visualization
```bash
npm run bot:visualize -- --shape circle --civilization ancient-egypt
```

#### 4. Assess Quality
```bash
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json
```

### Rapid Content Generation

Generate multiple lessons:

```bash
# Lesson 1
npm run bot:content -- --civilization ancient-greece --topic triangles

# Lesson 2
npm run bot:content -- --civilization ancient-greece --topic pythagorean-theorem

# Lesson 3
npm run bot:content -- --civilization ancient-greece --topic symmetry

# Generate quizzes for all
npm run bot:quiz -- --topic triangles --civilization ancient-greece
npm run bot:quiz -- --topic pythagorean-theorem --civilization ancient-greece
npm run bot:quiz -- --topic symmetry --civilization ancient-greece
```

## Tips and Best Practices

### 1. Start Simple
Begin with basic commands before adding options:
```bash
npm run bot:content -- --civilization ancient-egypt --topic circles
```

### 2. Use Help
Every bot has a help command:
```bash
npm run bot:content -- --help
npm run bot:quiz -- --help
```

### 3. Review Before Using
Always review generated content before using with students:
```bash
# Generate
npm run bot:content -- --civilization ancient-egypt --topic circles

# Assess
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json
```

### 4. Organize Your Output
Use consistent naming and organization:
```
curriculum/
├── ancient-egypt/
│   ├── circles-lesson.json
│   ├── circles-quiz.json
│   └── circle-visualization.html
├── ancient-greece/
│   ├── triangles-lesson.json
│   └── triangles-quiz.json
```

### 5. Batch Processing
Create scripts for generating multiple pieces:
```bash
#!/bin/bash
# generate-egypt-curriculum.sh

civilizations=("ancient-egypt")
topics=("circles" "triangles" "pyramids" "symmetry")

for civ in "${civilizations[@]}"; do
  for topic in "${topics[@]}"; do
    echo "Generating $topic for $civ..."
    npm run bot:content -- --civilization $civ --topic $topic
    npm run bot:quiz -- --topic $topic --civilization $civ
  done
done
```

## Troubleshooting

### Bot Won't Run
**Issue**: "Command not found" or "Cannot find module"
**Solution**:
```bash
npm install
```

### Configuration Error
**Issue**: "config.json not found"
**Solution**:
```bash
cp config.example.json config.json
# Then edit config.json with your settings
```

### Bot Disabled
**Issue**: "Bot is disabled in config.json"
**Solution**: Edit config.json and set the bot's `enabled` to `true`:
```json
{
  "bots": {
    "contentGenerator": {
      "enabled": true
    }
  }
}
```

### Invalid Arguments
**Issue**: Error about missing or invalid arguments
**Solution**: Check the help command and verify required arguments:
```bash
npm run bot:content -- --help
```

## Advanced Usage

### Scripting with Bots
Create automated workflows:

```javascript
// generate-curriculum.js
const { exec } = require('child_process');

const civilizations = ['ancient-egypt', 'ancient-greece'];
const topics = ['circles', 'triangles', 'polygons'];

civilizations.forEach(civ => {
  topics.forEach(topic => {
    const cmd = `npm run bot:content -- --civilization ${civ} --topic ${topic}`;
    exec(cmd, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error: ${error}`);
        return;
      }
      console.log(stdout);
    });
  });
});
```

### Custom Configuration
Modify config.json for your needs:

```json
{
  "bots": {
    "contentGenerator": {
      "enabled": true,
      "outputFormat": "markdown",
      "includeTeacherNotes": true,
      "defaultDifficulty": "intermediate"
    }
  }
}
```

## Getting Help

1. **Check the help command**: `npm run bot:content -- --help`
2. **Ask the AI Tutor**: `npm run tutor`
3. **Read the documentation**: See docs/beginner-guide.md
4. **Review examples**: Check the examples/ directory

Happy bot-ing! 🤖
