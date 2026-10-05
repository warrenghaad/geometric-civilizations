# Curriculum Templates

This directory contains templates for creating curriculum content.

## Available Templates

### lesson-template.json
Base structure for creating lessons:
- Metadata (civilization, topic, difficulty)
- Learning objectives
- Content sections
- Assessment strategies
- Resources and materials

**Usage:**
1. Copy the template
2. Fill in your content
3. Save with descriptive name
4. Or use the Content Generator Bot to auto-populate

### quiz-template.json
Base structure for creating quizzes:
- Metadata (topic, difficulty, question count)
- Quiz instructions
- Question structures
- Answer keys and explanations

**Usage:**
1. Copy the template
2. Add your questions
3. Save in appropriate location
4. Or use the Quiz Generator Bot to auto-populate

## Creating Custom Templates

You can create your own templates for:
- Different lesson formats
- Specific grade levels
- Alternative assessment types
- Project-based learning
- Lab activities

### Example Custom Template

```json
{
  "type": "project-based-lesson",
  "metadata": {
    "title": "",
    "duration": "2 weeks",
    "groupSize": "3-4 students"
  },
  "project": {
    "overview": "",
    "challenge": "",
    "constraints": [],
    "deliverables": [],
    "rubric": []
  }
}
```

## Using Templates with Bots

The bots use these templates as a foundation. When you run:

```bash
npm run bot:content -- --civilization ancient-egypt --topic circles
```

The bot:
1. Loads the lesson template
2. Populates it with AI-generated content
3. Saves the complete lesson

## Best Practices

1. **Keep templates flexible** - Don't over-specify
2. **Document fields** - Add comments explaining each section
3. **Version control** - Track changes to templates
4. **Share templates** - Let others benefit from your work
5. **Test thoroughly** - Ensure bots can parse your templates

## Contributing Templates

If you create useful templates:
1. Document them well
2. Include example usage
3. Share with the community
4. Consider adding bot support

## Need Help?

Ask the AI Tutor:
```bash
npm run tutor
```

Then ask: "How do I create a custom curriculum template?"
