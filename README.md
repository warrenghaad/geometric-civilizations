# Geometric Civilizations - AI-Powered Curriculum System

Welcome! This project helps you create an interactive curriculum about geometric thinking through different civilizations, powered by AI bots and an AI tutor to help you learn as you go.

## 🌟 What This Project Does

This system provides:
- **AI Curriculum Bots**: Automated content generation for your geometric civilizations curriculum
- **AI Tutor**: An interactive learning companion that helps you understand the code and concepts
- **Infrastructure**: All the technological setup needed to run and manage the system
- **Templates**: Ready-to-use curriculum templates and examples

## 🚀 Quick Start (For Beginners)

### What You Need
1. A computer (Windows, Mac, or Linux)
2. Internet connection
3. Basic willingness to learn!

### Installation Steps

#### Step 1: Install Node.js
Node.js lets you run JavaScript on your computer (not just in a web browser).
- Go to [nodejs.org](https://nodejs.org)
- Download the "LTS" (Long Term Support) version
- Run the installer and follow the prompts

#### Step 2: Set Up the Project
```bash
# Open your terminal/command prompt and run:
npm install
```

This command installs all the tools the project needs.

#### Step 3: Configure Your AI Assistant
```bash
# Copy the example configuration
cp config.example.json config.json

# Edit config.json with your AI API keys
# (The AI Tutor will help guide you through this!)
```

#### Step 4: Start the AI Tutor
```bash
npm run tutor
```

The AI Tutor will help you:
- Understand how the system works
- Configure the bots
- Create curriculum content
- Learn programming concepts along the way

## 📚 Learning Path

### For Complete Beginners
The AI Tutor will guide you through:
1. **Day 1**: Understanding the project structure
2. **Day 2**: Running your first bot
3. **Day 3**: Creating simple curriculum content
4. **Day 4**: Customizing bot behavior
5. **Day 5**: Understanding the code behind the scenes

### Key Concepts You'll Learn
- **APIs**: How programs talk to each other
- **JSON**: A simple way to store data
- **Automation**: Making computers do repetitive tasks
- **Version Control**: Tracking changes to your project
- **AI Integration**: Using AI to help create content

## 🤖 The Bot System

### What Are Bots?
Bots are automated programs that help create curriculum content. Think of them as tireless assistants!

### Available Bots
1. **Content Generator Bot** (`bots/content-generator/`)
   - Creates lesson plans and educational content
   - Uses AI to ensure quality and engagement

2. **Quiz Bot** (`bots/quiz-generator/`)
   - Generates interactive quizzes and puzzles
   - Adapts difficulty based on curriculum level

3. **Visualization Bot** (`bots/visualization-generator/`)
   - Creates geometric diagrams and animations
   - Helps visualize complex concepts

4. **Assessment Bot** (`bots/assessment/`)
   - Evaluates curriculum quality
   - Suggests improvements

### Running Bots
```bash
# Generate content for a specific civilization
npm run bot:content -- --civilization ancient-egypt --topic circles

# Create a quiz set
npm run bot:quiz -- --topic pythagorean-theorem --questions 10

# Generate visualizations
npm run bot:visualize -- --shape hexagon --civilization islamic
```

## 🧑‍🏫 AI Tutor

### What Is the AI Tutor?
An interactive assistant that:
- Answers your questions about the code
- Explains programming concepts in simple terms
- Helps debug issues
- Suggests improvements
- Teaches you as you build

### Using the Tutor
```bash
# Start the tutor
npm run tutor

# Ask questions like:
# "How do I add a new civilization?"
# "What does this code do?"
# "How can I customize the quiz format?"
# "I'm getting an error, can you help?"
```

The tutor remembers your conversation and adapts to your learning level!

## 📁 Project Structure

```
geometric-civilizations/
├── README.md                 # This file - start here!
├── package.json              # Project configuration
├── config.json               # Your settings (create from config.example.json)
├── config.example.json       # Example configuration
│
├── bots/                     # All the automation bots
│   ├── content-generator/    # Creates curriculum content
│   ├── quiz-generator/       # Makes quizzes and puzzles
│   ├── visualization-generator/  # Creates diagrams
│   └── assessment/           # Quality checks
│
├── curriculum/               # Your curriculum content
│   ├── templates/            # Starting templates
│   ├── ancient-egypt/        # Content by civilization
│   ├── ancient-greece/
│   ├── islamic-golden-age/
│   └── ancient-china/
│
├── tutor/                    # AI Tutor system
│   ├── tutor.js              # Main tutor program
│   ├── lessons/              # Learning modules
│   └── context/              # Knowledge base
│
├── docs/                     # Documentation
│   ├── beginner-guide.md     # Start here if new to programming
│   ├── bot-guide.md          # How to use the bots
│   ├── curriculum-guide.md   # Creating curriculum content
│   └── troubleshooting.md    # Common issues and fixes
│
└── examples/                 # Example outputs
    ├── sample-lesson.json
    ├── sample-quiz.json
    └── sample-visualization.html
```

## 🎯 Common Tasks

### Task 1: Generate a Lesson
```bash
npm run bot:content -- --civilization ancient-greece --topic triangles
```

### Task 2: Create Interactive Quizzes
```bash
npm run bot:quiz -- --civilization islamic-golden-age --topic geometric-patterns
```

### Task 3: Get Help from AI Tutor
```bash
npm run tutor
# Then ask: "How do I create a custom visualization?"
```

### Task 4: Review and Improve Content
```bash
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json
```

## 🔧 Configuration

### config.json Structure
```json
{
  "ai": {
    "provider": "openai",
    "apiKey": "your-api-key-here",
    "model": "gpt-4"
  },
  "curriculum": {
    "difficulty": "adaptive",
    "languages": ["en"],
    "includeVisualizations": true
  },
  "bots": {
    "contentGenerator": {
      "enabled": true,
      "outputFormat": "json"
    },
    "quizGenerator": {
      "enabled": true,
      "defaultQuestions": 10
    }
  },
  "tutor": {
    "learningLevel": "beginner",
    "verbosity": "detailed",
    "interactive": true
  }
}
```

## 🤝 Getting Help

### AI Tutor (Built-in)
Your first stop for questions!
```bash
npm run tutor
```

### Documentation
- [Beginner's Guide](docs/beginner-guide.md)
- [Bot Usage Guide](docs/bot-guide.md)
- [Troubleshooting](docs/troubleshooting.md)

### Common Questions

**Q: I don't know how to program. Can I use this?**
A: Yes! The AI Tutor is designed to teach you as you go. Start with `npm run tutor` and tell it you're a beginner.

**Q: What if I get stuck?**
A: Ask the AI Tutor! It's designed to help debug issues and explain solutions.

**Q: How do I customize the curriculum?**
A: Edit the templates in `curriculum/templates/` or ask the AI Tutor to help you create custom templates.

**Q: Can I add my own civilizations?**
A: Absolutely! The AI Tutor can guide you through the process.

## 🌍 Supported Civilizations

- Ancient Egypt
- Ancient Greece
- Ancient China
- Islamic Golden Age
- Maya Civilization
- Indian Mathematics
- And more! (Extensible system)

## 🎓 Learning Resources

### Programming Concepts Covered
- Variables and data types
- Functions and modules
- JSON and configuration
- API calls and async programming
- File system operations
- Error handling

### Curriculum Concepts
- Geometric thinking through history
- Cultural perspectives on mathematics
- Interactive learning design
- Assessment and feedback

## 📝 Next Steps

1. **Install the dependencies**: `npm install`
2. **Configure your settings**: Copy and edit `config.example.json`
3. **Start the AI Tutor**: `npm run tutor`
4. **Generate your first content**: Follow the tutor's guidance
5. **Explore and learn**: The tutor adapts to your pace!

## 🎉 Welcome to Your Learning Journey!

Remember: This system is designed to teach you while you build. Don't hesitate to ask the AI Tutor questions - even if they seem basic. That's what it's here for!

Happy learning and creating!

---

## License

MIT License - Feel free to use and modify for your educational needs.

## Contributing

Contributions welcome! The AI Tutor can help you understand how to contribute code.
