# Beginner's Guide to Geometric Civilizations

Welcome! This guide is designed for people who are new to programming and want to learn while building an educational curriculum system.

## What You'll Learn

This project will teach you:
- **Basic Programming**: Understanding code structure and logic
- **JavaScript**: The programming language we use
- **Node.js**: Running JavaScript outside a web browser
- **Automation**: Making computers do repetitive tasks
- **AI Integration**: Using artificial intelligence to create content
- **Project Management**: Organizing and building a real system

## Before You Start

### Required Knowledge
**Nothing!** This guide assumes you're completely new to programming.

### Required Software
1. **Node.js** - Lets you run JavaScript programs
   - Download from: https://nodejs.org
   - Choose the "LTS" version (recommended for most users)
   - Install and verify: Open terminal/command prompt and type `node --version`

2. **Text Editor** - For viewing and editing code
   - Recommended: VS Code (https://code.visualstudio.com)
   - Alternatives: Notepad++, Sublime Text, or even Notepad

3. **Terminal/Command Prompt** - For running commands
   - Windows: Command Prompt or PowerShell
   - Mac: Terminal
   - Linux: Your favorite terminal

## Understanding the Basics

### What is Programming?
Programming is writing instructions for computers to follow. Think of it like writing a recipe - you tell the computer exactly what to do, step by step.

### What is JavaScript?
JavaScript is a programming language - a way to write those instructions. It's popular because:
- It's relatively easy to learn
- It's powerful and flexible
- It runs almost everywhere

### What is Node.js?
Node.js lets you run JavaScript programs on your computer (not just in web browsers). Our curriculum bots run using Node.js.

### What is npm?
npm (Node Package Manager) is like an app store for JavaScript code. It helps you:
- Install libraries (pre-written code) that others have created
- Manage your project's dependencies (other code your project needs)
- Run scripts and commands

### What is a Bot?
In our project, a "bot" is an automated program that helps create curriculum content. Think of them as tireless assistants that:
- Generate lesson plans
- Create quizzes
- Make visualizations
- Check quality

## Getting Started: Step by Step

### Step 1: Install Node.js
1. Go to https://nodejs.org
2. Download the "LTS" version
3. Run the installer
4. Follow the installation wizard
5. Verify installation:
   ```bash
   node --version
   npm --version
   ```
   You should see version numbers for both.

### Step 2: Get the Project Code
If you cloned from GitHub, you already have it!

If not:
1. Download the project as a ZIP file from GitHub
2. Extract it to a folder you'll remember (like `Documents/geometric-civilizations`)

### Step 3: Open Terminal in Project Folder
Navigate to your project folder:

**Windows:**
```bash
cd C:\Users\YourName\Documents\geometric-civilizations
```

**Mac/Linux:**
```bash
cd ~/Documents/geometric-civilizations
```

Tip: In VS Code, you can open a terminal from the menu: Terminal → New Terminal

### Step 4: Install Dependencies
Dependencies are other people's code that our project uses. Install them:

```bash
npm install
```

This command:
- Reads the `package.json` file
- Downloads all required libraries
- Saves them in a `node_modules` folder

**Note:** This might take a minute. That's normal!

### Step 5: Configure the System
Copy the example configuration:

```bash
cp config.example.json config.json
```

**Windows users:** Use this instead:
```bash
copy config.example.json config.json
```

Now edit `config.json`:
- Open it in your text editor
- Find `"apiKey": "YOUR_API_KEY_HERE"`
- Replace with your actual OpenAI API key
- Save the file

**Getting an API Key:**
1. Go to https://platform.openai.com
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy and paste it into config.json

### Step 6: Start the AI Tutor
The AI Tutor is your learning companion!

```bash
npm run tutor
```

This will:
- Start an interactive session
- Let you ask questions
- Guide you through the system

## Understanding the Code

### File Structure
```
geometric-civilizations/
├── package.json          # Project configuration
├── config.json           # Your settings (DO NOT share - contains API key!)
├── README.md             # Overview and documentation
├── bots/                 # Automation bots
├── curriculum/           # Generated curriculum content
├── tutor/                # AI Tutor system
└── docs/                 # Documentation (you're reading it!)
```

### What is package.json?
This file describes your project:
- Name and version
- Dependencies (other code you need)
- Scripts (commands you can run)

Example from our project:
```json
{
  "name": "geometric-civilizations",
  "version": "1.0.0",
  "scripts": {
    "tutor": "node tutor/tutor.js",
    "bot:content": "node bots/content-generator/index.js"
  }
}
```

When you run `npm run tutor`, npm looks at the `scripts` section and runs `node tutor/tutor.js`.

### What is JSON?
JSON (JavaScript Object Notation) is a way to store data:
- It's human-readable
- Computers can easily parse it
- Used for configuration and data storage

Example:
```json
{
  "name": "John",
  "age": 30,
  "hobbies": ["reading", "coding", "teaching"]
}
```

### Understanding a Simple Bot

Let's look at a simplified bot:

```javascript
// This is a comment - it explains code but doesn't run

// Import modules (pre-written code we use)
const fs = require('fs');  // File system - for reading/writing files

// Function - a reusable block of code
function generateLesson(topic) {
  console.log("Generating lesson about " + topic);
  
  // Create lesson content
  const lesson = {
    title: topic,
    content: "This is about " + topic
  };
  
  // Save to file
  fs.writeFileSync('lesson.json', JSON.stringify(lesson));
}

// Call the function
generateLesson("circles");
```

**Key Concepts:**
- **Comments**: Lines starting with `//` - notes for humans
- **Variables**: Named storage (`const lesson = ...`)
- **Functions**: Reusable code blocks (`function generateLesson(...)`)
- **Objects**: Organized data (`{ title: ..., content: ... }`)

## Common Commands

### Install Dependencies
```bash
npm install
```
Downloads all required code libraries.

### Start AI Tutor
```bash
npm run tutor
```
Opens interactive learning companion.

### Generate Content
```bash
npm run bot:content -- --civilization ancient-egypt --topic circles
```
Creates a lesson about circles in Ancient Egypt.

### Generate Quiz
```bash
npm run bot:quiz -- --topic pythagorean-theorem --questions 10
```
Creates a 10-question quiz.

### Create Visualization
```bash
npm run bot:visualize -- --shape hexagon --civilization islamic
```
Generates an interactive hexagon visualization.

### Assess Content
```bash
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json
```
Checks quality of generated content.

## Understanding Command Syntax

Let's break down a command:
```bash
npm run bot:content -- --civilization ancient-egypt --topic circles
```

- `npm run` - Run a script from package.json
- `bot:content` - The script name
- `--` - Separates npm arguments from script arguments
- `--civilization ancient-egypt` - An argument with value
- `--topic circles` - Another argument with value

Think of arguments like filling in a form - you're giving the bot information it needs.

## Learning Path

### Week 1: Exploration
1. Install everything
2. Start the AI Tutor
3. Run each bot with `--help` to see what they do
4. Generate simple content
5. Look at the output files

### Week 2: Understanding
1. Open bot files in your text editor
2. Read the comments
3. Ask the AI Tutor to explain specific parts
4. Try modifying simple things (like text in console.log)
5. See what changes

### Week 3: Customization
1. Modify templates
2. Add new civilizations
3. Change output formats
4. Experiment with settings

### Week 4: Creation
1. Create your own content templates
2. Customize bot behavior
3. Add new features
4. Share your improvements!

## Tips for Success

### 1. Don't Be Afraid to Break Things
- You can't break your computer by editing code
- If something doesn't work, you can always revert changes
- Breaking things is how you learn!

### 2. Read Error Messages
Errors tell you what went wrong:
```
Error: Cannot find module 'fs'
```
This means a required module isn't available.

### 3. Use the AI Tutor
When stuck, ask the tutor:
- "Why am I getting this error?"
- "How do I [do something]?"
- "Explain [concept] to me"

### 4. Take It Slow
- Don't try to understand everything at once
- Master one concept before moving to the next
- It's okay to feel overwhelmed - everyone does at first!

### 5. Practice
- Run commands multiple times
- Experiment with different options
- Read the code even if you don't understand it all

## Common Mistakes and Solutions

### "Command not found"
**Problem:** Terminal can't find the command.
**Solution:** 
- Make sure Node.js is installed
- Check you're in the right directory
- Verify with `node --version`

### "Module not found"
**Problem:** A required library isn't installed.
**Solution:** Run `npm install`

### "Cannot find config.json"
**Problem:** Configuration file doesn't exist.
**Solution:** Copy from example: `cp config.example.json config.json`

### "API key invalid"
**Problem:** Your OpenAI API key isn't working.
**Solution:** 
- Check it's correct in config.json
- Verify it's active on OpenAI's website
- Make sure there are no extra spaces

## Next Steps

1. **Complete the setup** above
2. **Start the AI Tutor** and ask questions
3. **Generate your first lesson** using a bot
4. **Explore the code** with the tutor's guidance
5. **Customize something** small and see what changes
6. **Share your success** with others!

## Getting Help

### In the Project
1. **AI Tutor**: `npm run tutor` - Your first resource!
2. **Help Commands**: Add `--help` to any bot command
3. **Documentation**: Read the docs/ folder

### Online Resources
- [Node.js Documentation](https://nodejs.org/docs)
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [npm Documentation](https://docs.npmjs.com)

### Remember
Every expert programmer was once a beginner. The only difference is practice and persistence. You've got this! 🚀

## Glossary

- **API**: Application Programming Interface - how programs talk to each other
- **Bot**: Automated program that performs tasks
- **CLI**: Command Line Interface - text-based way to interact with programs
- **Dependency**: Code your project needs from others
- **Function**: Reusable block of code
- **JSON**: Data format for storing structured information
- **Node.js**: JavaScript runtime for running JS outside browsers
- **npm**: Package manager for JavaScript
- **Variable**: Named storage for data
- **Script**: File containing code to be executed

Happy learning! 🎓
