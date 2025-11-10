#!/usr/bin/env node

/**
 * Geometric Civilizations - Main Entry Point
 * 
 * This is the main file for the Geometric Civilizations curriculum system.
 * For most tasks, you'll want to use the specific bots or the AI tutor.
 */

console.log(`
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║    Geometric Civilizations - AI Curriculum System  🎓     ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

Welcome to the Geometric Civilizations curriculum system!

This system helps you create educational content about geometric
thinking through different civilizations.

Available Commands:
  npm run tutor          - Start the AI Tutor (recommended for beginners!)
  npm run bot:content    - Generate curriculum content
  npm run bot:quiz       - Create interactive quizzes
  npm run bot:visualize  - Generate geometric visualizations
  npm run bot:assess     - Assess content quality
  npm run setup          - Run setup wizard

For detailed help:
  • Run: npm run tutor
  • Read: README.md
  • Check: docs/beginner-guide.md

Quick Examples:
  npm run bot:content -- --civilization ancient-egypt --topic circles
  npm run bot:quiz -- --topic pythagorean-theorem --questions 10
  npm run bot:visualize -- --shape hexagon --civilization islamic

Get Started:
  1. Make sure you've run 'npm install'
  2. Copy config.example.json to config.json
  3. Add your OpenAI API key to config.json
  4. Run 'npm run tutor' for interactive help!

Happy learning! 🚀
`);
