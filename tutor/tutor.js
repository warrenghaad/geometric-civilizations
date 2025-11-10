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
║        Your Interactive Learning Companion                 ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
${colors.reset}`);
  
  console.log(`\n${colors.green}Welcome! I'm here to help you learn and build.${colors.reset}\n`);
  console.log('I can help you with:\n');
  console.log('  📚 Understanding how this system works');
  console.log('  💻 Learning programming concepts');
  console.log('  🤖 Setting up and using the curriculum bots');
  console.log('  🐛 Debugging issues and errors');
  console.log('  ✨ Creating amazing curriculum content\n');
  console.log(`${colors.yellow}Type 'help' for a list of commands, or just ask me anything!${colors.reset}`);
  console.log(`${colors.yellow}Type 'exit' or 'quit' to leave the tutor.${colors.reset}\n`);
}

/**
 * Display help information
 */
function displayHelp() {
  console.log(`\n${colors.bright}${colors.blue}Available Commands:${colors.reset}\n`);
  console.log('  help              - Show this help message');
  console.log('  guide             - Show beginner\'s guide');
  console.log('  structure         - Explain the project structure');
  console.log('  bots              - Learn about the bot system');
  console.log('  config            - Help with configuration');
  console.log('  example           - Show usage examples');
  console.log('  concept <topic>   - Explain a programming concept');
  console.log('  debug             - Help debug an issue');
  console.log('  clear             - Clear the screen');
  console.log('  exit/quit         - Exit the tutor\n');
  console.log(`${colors.yellow}Or just type your question naturally!${colors.reset}\n`);
}

/**
 * Show beginner's guide
 */
function showBeginnerGuide() {
  console.log(`\n${colors.bright}${colors.magenta}Beginner's Guide${colors.reset}\n`);
  console.log('If you\'re new to programming, here\'s what you need to know:\n');
  console.log('1️⃣  ${colors.bright}JavaScript${colors.reset} - The programming language we use');
  console.log('   It runs in Node.js (JavaScript outside the browser)\n');
  console.log('2️⃣  ${colors.bright}npm${colors.reset} - Node Package Manager');
  console.log('   It installs tools and libraries we need');
  console.log('   Run: npm install\n');
  console.log('3️⃣  ${colors.bright}Bots${colors.reset} - Automated programs that help create content');
  console.log('   They use AI to generate curriculum materials\n');
  console.log('4️⃣  ${colors.bright}Configuration${colors.reset} - Settings for the system');
  console.log('   Stored in config.json (create from config.example.json)\n');
  console.log(`${colors.green}Ready to start? Try: npm install${colors.reset}\n`);
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
  console.log('Here are some common tasks:\n');
  console.log('${colors.bright}Example 1: Generate a lesson about circles in Ancient Egypt${colors.reset}');
  console.log('  ${colors.green}npm run bot:content -- --civilization ancient-egypt --topic circles${colors.reset}\n');
  console.log('${colors.bright}Example 2: Create a quiz on the Pythagorean theorem${colors.reset}');
  console.log('  ${colors.green}npm run bot:quiz -- --topic pythagorean-theorem --questions 15${colors.reset}\n');
  console.log('${colors.bright}Example 3: Visualize Islamic geometric patterns${colors.reset}');
  console.log('  ${colors.green}npm run bot:visualize -- --civilization islamic --pattern star${colors.reset}\n');
  console.log('${colors.bright}Example 4: Check the quality of a lesson${colors.reset}');
  console.log('  ${colors.green}npm run bot:assess -- --file curriculum/ancient-egypt/circles.json${colors.reset}\n');
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
    console.log(`\n${colors.yellow}Concept "${concept}" not found. Try: api, json, async, function, or npm${colors.reset}\n`);
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
  } else if (command === 'structure') {
    explainStructure();
  } else if (command === 'bots') {
    explainBots();
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
