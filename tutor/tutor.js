#!/usr/bin/env node

/**
 * AI Tutor - Interactive Learning Companion
 * 
 * This program provides an AI-powered tutor that helps you:
 * - Understand the code and system
 * - Learn programming concepts
 * - Configure and use the bots
 * - Debug issues
 * - Create curriculum content
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

// For beginners: readline is a built-in Node.js module that lets us read user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// ANSI color codes for pretty console output
const colors = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  cyan: '\x1b[36m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  magenta: '\x1b[35m'
};

/**
 * Display a welcome message when the tutor starts
 */
function displayWelcome() {
  console.clear();
  console.log(`${colors.bright}${colors.cyan}
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║        🤖 Geometric Civilizations AI Tutor 🎓             ║
║                                                            ║
║        Your Personal Programming & Tech Guide              ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
${colors.reset}`);
  
  console.log(`\n${colors.green}Welcome! I'm YOUR personal tutor - here to help YOU learn programming${colors.reset}`);
  console.log(`${colors.green}and master this system, even if you're starting from scratch.${colors.reset}\n`);
  console.log('I can help you with:\n');
  console.log('  💻 Learning programming from the ground up (no experience needed)');
  console.log('  📚 Understanding how this system works step-by-step');
  console.log('  🤖 Setting up and using all the curriculum bots');
  console.log('  🐛 Debugging issues and errors (I explain what went wrong)');
  console.log('  🔧 Configuration and technical setup');
  console.log('  ✨ Creating curriculum content efficiently\n');
  console.log(`${colors.yellow}NOTE: This tutor is for YOU, the educator/developer - not for students.${colors.reset}`);
  console.log(`${colors.yellow}I'll explain technical concepts clearly so you can master this system.${colors.reset}\n`);
  console.log(`Type 'help' for commands, or just ask me anything in plain English!`);
  console.log(`Type 'exit' or 'quit' to leave.\n`);
}

/**
 * Display help information
 */
function displayHelp() {
  console.log(`\n${colors.bright}${colors.blue}Available Commands:${colors.reset}\n`);
  console.log('  help              - Show this help message');
  console.log('  guide             - Show beginner\'s programming guide');
  console.log('  walkthrough       - Step-by-step setup (recommended for new users!)');
  console.log('  structure         - Explain the project structure');
  console.log('  bots              - Learn about the bot system');
  console.log('  decompose         - Help with Image Decomposition Bot');
  console.log('  config            - Help with configuration');
  console.log('  example           - Show usage examples');
  console.log('  concept <topic>   - Explain a programming concept');
  console.log('  debug             - Help debug an issue');
  console.log('  clear             - Clear the screen');
  console.log('  exit/quit         - Exit the tutor\n');
  console.log(`${colors.yellow}Or just type your question in plain English - I understand natural language!${colors.reset}\n`);
}

/**
 * Show beginner's guide
 */
function showBeginnerGuide() {
  console.log(`\n${colors.bright}${colors.magenta}Your Personal Programming Guide${colors.reset}\n`);
  console.log('Starting from zero? No problem! Here\'s what you need to know:\n');
  console.log('${colors.bright}1️⃣  JavaScript${colors.reset} - The programming language we use');
  console.log('   Don\'t worry, you don\'t need to be an expert.');
  console.log('   The bots do the heavy lifting - you just run commands.\n');
  console.log('${colors.bright}2️⃣  Terminal/Command Line${colors.reset}');
  console.log('   This is where you type commands to run the bots.');
  console.log('   On Mac: Terminal app | On Windows: Command Prompt or PowerShell\n');
  console.log('${colors.bright}3️⃣  npm${colors.reset} - Node Package Manager');
  console.log('   Installs tools and libraries we need.');
  console.log('   You run: npm install (downloads everything)\n');
  console.log('${colors.bright}4️⃣  Bots${colors.reset} - Automated programs you\'ll use');
  console.log('   They generate curriculum content using AI.');
  console.log('   You don\'t write code - you run commands with options.\n');
  console.log('${colors.bright}5️⃣  Configuration${colors.reset} - One-time setup');
  console.log('   Copy config.example.json → config.json');
  console.log('   Add your API key and you\'re ready!\n');
  console.log(`${colors.green}First step: Run "npm install" in your terminal${colors.reset}\n`);
  console.log(`${colors.yellow}Type "walkthrough" for a step-by-step setup guide!${colors.reset}\n`);
}

/**
 * Explain project structure
 */
function explainStructure() {
  console.log(`\n${colors.bright}${colors.blue}Project Structure${colors.reset}\n`);
  console.log('Here\'s how the project is organized:\n');
  console.log('📁 ${colors.bright}bots/${colors.reset}');
  console.log('   Contains all automation bots');
  console.log('   - content-generator: Creates lessons and content');
  console.log('   - quiz-generator: Makes interactive quizzes');
  console.log('   - visualization-generator: Creates diagrams');
  console.log('   - assessment: Checks content quality\n');
  console.log('📁 ${colors.bright}curriculum/${colors.reset}');
  console.log('   Your curriculum content organized by civilization');
  console.log('   - templates: Starting templates');
  console.log('   - ancient-egypt, ancient-greece, etc.: Content by topic\n');
  console.log('📁 ${colors.bright}tutor/${colors.reset}');
  console.log('   That\'s me! The AI tutor system\n');
  console.log('📁 ${colors.bright}docs/${colors.reset}');
  console.log('   Documentation and guides\n');
  console.log('📁 ${colors.bright}examples/${colors.reset}');
  console.log('   Example outputs to learn from\n');
}

/**
 * Explain the bot system
 */
function explainBots() {
  console.log(`\n${colors.bright}${colors.green}Bot System Overview${colors.reset}\n`);
  console.log('Bots are automated programs that help you create curriculum content.\n');
  console.log('🤖 ${colors.bright}Content Generator Bot${colors.reset}');
  console.log('   Creates lesson plans and educational content');
  console.log('   Usage: npm run bot:content -- --civilization ancient-egypt --topic circles\n');
  console.log('📝 ${colors.bright}Quiz Generator Bot${colors.reset}');
  console.log('   Makes interactive quizzes and puzzles');
  console.log('   Usage: npm run bot:quiz -- --topic pythagorean-theorem --questions 10\n');
  console.log('🎨 ${colors.bright}Visualization Bot${colors.reset}');
  console.log('   Creates geometric diagrams and animations');
  console.log('   Usage: npm run bot:visualize -- --shape hexagon --civilization islamic\n');
  console.log('✅ ${colors.bright}Assessment Bot${colors.reset}');
  console.log('   Evaluates content quality and suggests improvements');
  console.log('   Usage: npm run bot:assess -- --file curriculum/lesson.json\n');
  console.log(`${colors.yellow}All bots use AI to ensure high-quality output!${colors.reset}\n`);
}

/**
 * Help with configuration
 */
function helpWithConfig() {
  console.log(`\n${colors.bright}${colors.cyan}Configuration Help${colors.reset}\n`);
  console.log('To configure the system:\n');
  console.log('1. Copy the example configuration:');
  console.log('   ${colors.green}cp config.example.json config.json${colors.reset}\n');
  console.log('2. Edit config.json with your settings:\n');
  console.log('   ${colors.bright}ai.apiKey${colors.reset} - Your OpenAI API key');
  console.log('     Get one at: https://platform.openai.com/api-keys\n');
  console.log('   ${colors.bright}curriculum.difficulty${colors.reset} - Target difficulty level');
  console.log('     Options: "beginner", "intermediate", "advanced", "adaptive"\n');
  console.log('   ${colors.bright}tutor.learningLevel${colors.reset} - Your programming level');
  console.log('     Options: "beginner", "intermediate", "advanced"\n');
  console.log('3. Save the file and you\'re ready to go!\n');
  console.log(`${colors.yellow}Note: config.json is ignored by git (keeps your API key safe)${colors.reset}\n`);
}

/**
 * Show usage examples
 */
function showExamples() {
  console.log(`\n${colors.bright}${colors.magenta}Usage Examples${colors.reset}\n`);
  console.log('Here are the most common tasks you\'ll do:\n');
  console.log('${colors.bright}Example 1: Decompose images into shapes (your main workflow!)${colors.reset}');
  console.log('  ${colors.green}npm run bot:decompose -- --demo${colors.reset}');
  console.log('  ${colors.green}npm run bot:decompose -- --image photos/house.jpg --outline outlines/lesson.txt${colors.reset}\n');
  console.log('${colors.bright}Example 2: Generate a lesson about circles${colors.reset}');
  console.log('  ${colors.green}npm run bot:content -- --civilization ancient-egypt --topic circles${colors.reset}\n');
  console.log('${colors.bright}Example 3: Create a quiz${colors.reset}');
  console.log('  ${colors.green}npm run bot:quiz -- --topic pythagorean-theorem --questions 15${colors.reset}\n');
  console.log('${colors.bright}Example 4: Create visualizations${colors.reset}');
  console.log('  ${colors.green}npm run bot:visualize -- --civilization islamic --pattern star${colors.reset}\n');
  console.log('${colors.bright}Example 5: Assess content quality${colors.reset}');
  console.log('  ${colors.green}npm run bot:assess -- --file curriculum/ancient-egypt/circles.json${colors.reset}\n');
}

/**
 * Step-by-step walkthrough for new users
 */
function showWalkthrough() {
  console.log(`\n${colors.bright}${colors.cyan}═══════════════════════════════════════════════════════════${colors.reset}`);
  console.log(`${colors.bright}${colors.cyan}          STEP-BY-STEP SETUP WALKTHROUGH${colors.reset}`);
  console.log(`${colors.bright}${colors.cyan}═══════════════════════════════════════════════════════════${colors.reset}\n`);
  
  console.log(`${colors.bright}STEP 1: Check Node.js is installed${colors.reset}`);
  console.log('  Open your terminal and type: ${colors.green}node --version${colors.reset}');
  console.log('  You should see something like "v18.x.x" or higher.');
  console.log('  ${colors.yellow}If not installed: Download from https://nodejs.org${colors.reset}\n');
  
  console.log(`${colors.bright}STEP 2: Install project dependencies${colors.reset}`);
  console.log('  In your terminal, navigate to this project folder and run:');
  console.log('  ${colors.green}npm install${colors.reset}');
  console.log('  This downloads all the code libraries we need.\n');
  
  console.log(`${colors.bright}STEP 3: Set up configuration${colors.reset}`);
  console.log('  Copy the example config file:');
  console.log('  ${colors.green}cp config.example.json config.json${colors.reset}');
  console.log('  Then open config.json and add your OpenAI API key.\n');
  
  console.log(`${colors.bright}STEP 4: Try the Image Decomposition demo${colors.reset}`);
  console.log('  Run this command to see a working example:');
  console.log('  ${colors.green}npm run bot:decompose -- --demo${colors.reset}');
  console.log('  This creates a lesson showing how to decompose shapes!\n');
  
  console.log(`${colors.bright}STEP 5: Use your own images${colors.reset}`);
  console.log('  Put your images in a "photos" folder, then run:');
  console.log('  ${colors.green}npm run bot:decompose -- --image photos/yourfile.jpg --outline outlines/lesson.txt${colors.reset}\n');
  
  console.log(`${colors.bright}${colors.green}That\'s it! You\'re ready to create curriculum content.${colors.reset}\n`);
  console.log(`${colors.yellow}Questions? Type 'decompose' for Image Bot help, or just ask me anything!${colors.reset}\n`);
}

/**
 * Help specifically with Image Decomposition Bot
 */
function helpWithDecompose() {
  console.log(`\n${colors.bright}${colors.magenta}Image Decomposition Bot - Your Main Tool${colors.reset}\n`);
  console.log('This bot takes photos and shows how objects break down into shapes.\n');
  
  console.log('${colors.bright}Quick Start:${colors.reset}');
  console.log('  ${colors.green}npm run bot:decompose -- --demo${colors.reset}');
  console.log('  (Creates a sample lesson - no images needed!)\n');
  
  console.log('${colors.bright}With Your Images:${colors.reset}');
  console.log('  ${colors.green}npm run bot:decompose -- --image photos/house.jpg --outline outlines/shapes.txt${colors.reset}\n');
  
  console.log('${colors.bright}What You Get:${colors.reset}');
  console.log('  ✓ Visual breakdown showing shapes in the image');
  console.log('  ✓ Mathematical formulas (area, perimeter, angles)');
  console.log('  ✓ Worked examples with real numbers');
  console.log('  ✓ Practice problems with solutions');
  console.log('  ✓ Student activities matched to your outline');
  console.log('  ✓ Teacher notes with grade differentiation');
  console.log('  ✓ Print-ready HTML format\n');
  
  console.log('${colors.bright}Options:${colors.reset}');
  console.log('  --grade 3|4|5     Target grade level');
  console.log('  --shapes 2d|3d    Focus on 2D or 3D shapes');
  console.log('  --format html     Output format (default: html)\n');
  
  console.log('${colors.bright}Example Workflow:${colors.reset}');
  console.log('  1. Take/download photos of objects (house, signs, toys, etc.)');
  console.log('  2. Save them in a "photos" folder');
  console.log('  3. Create a simple outline file with your learning goals');
  console.log('  4. Run the bot: npm run bot:decompose -- --image photos/your-image.jpg --outline outlines/your-outline.txt');
  console.log('  5. Open the generated HTML file in any browser!\n');
  
  console.log('${colors.bright}Process Multiple Images:${colors.reset}');
  console.log('  for img in photos/*.jpg; do');
  console.log('    npm run bot:decompose -- --image "$img" --outline outlines/lesson.txt');
  console.log('  done\n');
}

/**
 * Explain a programming concept
 */
function explainConcept(concept) {
  const concepts = {
    'api': {
      title: 'API (Application Programming Interface)',
      explanation: 'An API is like a waiter in a restaurant. You (the program) tell the waiter (API) what you want, and the waiter brings it from the kitchen (another program or service). In our case, we use APIs to communicate with AI services like OpenAI.',
      example: 'When a bot generates content, it sends a request to the OpenAI API asking for curriculum content, and the API sends back the generated text.'
    },
    'json': {
      title: 'JSON (JavaScript Object Notation)',
      explanation: 'JSON is a way to store and transfer data in a format that\'s easy for both humans and computers to read. Think of it like a structured list or filing system.',
      example: '{\n  "civilization": "ancient-egypt",\n  "topic": "circles",\n  "difficulty": "beginner"\n}'
    },
    'async': {
      title: 'Asynchronous Programming',
      explanation: 'Async programming is like ordering food online. You place the order (start the task), continue doing other things (other code runs), and get notified when the food arrives (task completes). You don\'t wait idle while the food is being prepared.',
      example: 'When a bot calls the AI API, it doesn\'t freeze - it continues running and handles the response when it arrives.'
    },
    'function': {
      title: 'Functions',
      explanation: 'A function is a reusable block of code that performs a specific task. Think of it like a recipe - you write it once and can use it many times.',
      example: 'function greet(name) {\n  return "Hello, " + name + "!";\n}\ngreet("Student"); // Returns "Hello, Student!"'
    },
    'npm': {
      title: 'npm (Node Package Manager)',
      explanation: 'npm is like an app store for JavaScript code. It helps you install, share, and manage code libraries (called packages) that others have written.',
      example: 'npm install openai - This installs the OpenAI library so we can use AI in our bots.'
    },
    'terminal': {
      title: 'Terminal / Command Line',
      explanation: 'The terminal is a text-based interface to control your computer. Instead of clicking buttons, you type commands. It\'s faster for many tasks once you learn the basics.',
      example: 'cd my-folder    - Navigate to a folder\nls              - List files\nnpm install     - Install project dependencies'
    },
    'html': {
      title: 'HTML (HyperText Markup Language)',
      explanation: 'HTML is the language used to create web pages. When the bots generate lessons, they output HTML files that you can open in any web browser (Chrome, Firefox, Safari, etc.).',
      example: 'The bot creates .html files you open in your browser to see the lessons.'
    }
  };

  const lower = concept.toLowerCase();
  if (concepts[lower]) {
    const c = concepts[lower];
    console.log(`\n${colors.bright}${colors.blue}${c.title}${colors.reset}\n`);
    console.log(`${c.explanation}\n`);
    console.log(`${colors.green}Example:${colors.reset}`);
    console.log(`${c.example}\n`);
  } else {
    console.log(`\n${colors.yellow}Concept "${concept}" not found.${colors.reset}`);
    console.log(`Try: api, json, async, function, npm, terminal, html\n`);
  }
}

/**
 * Process user input and provide responses
 */
function processInput(input) {
  const command = input.trim().toLowerCase();
  
  if (!command) {
    return;
  }

  // Handle commands
  if (command === 'help') {
    displayHelp();
  } else if (command === 'guide') {
    showBeginnerGuide();
  } else if (command === 'walkthrough' || command === 'setup') {
    showWalkthrough();
  } else if (command === 'structure') {
    explainStructure();
  } else if (command === 'bots') {
    explainBots();
  } else if (command === 'decompose' || command === 'image' || command === 'images') {
    helpWithDecompose();
  } else if (command === 'config') {
    helpWithConfig();
  } else if (command === 'example' || command === 'examples') {
    showExamples();
  } else if (command === 'clear') {
    console.clear();
    displayWelcome();
  } else if (command.startsWith('concept ')) {
    const concept = command.substring(8);
    explainConcept(concept);
  } else if (command === 'debug') {
    console.log(`\n${colors.bright}${colors.red}Debug Help${colors.reset}\n`);
    console.log('Tell me about the error you\'re seeing, and I\'ll help you fix it!\n');
    console.log('Common issues:\n');
    console.log('• "Module not found" - Run: npm install');
    console.log('• "Cannot find config.json" - Copy config.example.json to config.json');
    console.log('• "API key invalid" - Check your API key in config.json');
    console.log('• "Command not found" - Make sure Node.js is installed\n');
  } else if (command === 'exit' || command === 'quit') {
    console.log(`\n${colors.green}Thanks for learning with me! Happy coding! 🚀${colors.reset}\n`);
    rl.close();
    process.exit(0);
  } else {
    // Provide contextual responses to natural questions
    if (command.includes('how') || command.includes('what') || command.includes('why')) {
      console.log(`\n${colors.cyan}Great question!${colors.reset} Let me help you with that.\n`);
      
      if (command.includes('start') || command.includes('begin')) {
        console.log('To get started:\n');
        console.log('1. Run: ${colors.green}npm install${colors.reset}');
        console.log('2. Copy config.example.json to config.json');
        console.log('3. Add your OpenAI API key to config.json');
        console.log('4. Try running a bot: ${colors.green}npm run bot:content -- --help${colors.reset}\n');
      } else if (command.includes('bot')) {
        explainBots();
      } else if (command.includes('config')) {
        helpWithConfig();
      } else if (command.includes('install')) {
        console.log('To install dependencies:\n');
        console.log('${colors.green}npm install${colors.reset}\n');
        console.log('This downloads and installs all the code libraries the project needs.\n');
      } else {
        console.log('I can help you with:\n');
        console.log('• Getting started');
        console.log('• Understanding the code');
        console.log('• Using the bots');
        console.log('• Configuration');
        console.log('• Debugging issues\n');
        console.log(`Try typing: ${colors.yellow}help${colors.reset} for a list of commands.\n`);
      }
    } else {
      console.log(`\n${colors.yellow}I'm not sure about that. Type 'help' to see what I can do!${colors.reset}\n`);
    }
  }
}

/**
 * Main tutor loop
 */
function startTutor() {
  displayWelcome();
  
  // Prompt for user input
  const prompt = () => {
    rl.question(`${colors.bright}${colors.cyan}You: ${colors.reset}`, (input) => {
      processInput(input);
      prompt(); // Continue the conversation
    });
  };
  
  prompt();
}

// Start the tutor
startTutor();
