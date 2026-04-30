#!/usr/bin/env node

/**
 * Setup Script
 * Helps new users configure the system
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log(`
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     Welcome to Geometric Civilizations Setup! 🎓          ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

This script will help you set up the project.
`);

async function setup() {
  // Check if config.json exists
  const configPath = path.join(__dirname, '../config.json');
  
  if (fs.existsSync(configPath)) {
    console.log('✓ config.json already exists!\n');
  } else {
    console.log('Creating config.json from template...');
    const examplePath = path.join(__dirname, '../config.example.json');
    fs.copyFileSync(examplePath, configPath);
    console.log('✓ config.json created!\n');
    console.log('⚠️  Important: Edit config.json and add your OpenAI API key\n');
  }
  
  // Check Node.js version
  const version = process.version;
  console.log(`✓ Node.js version: ${version}`);
  
  if (parseInt(version.slice(1)) < 14) {
    console.log('⚠️  Warning: Node.js 14+ recommended\n');
  } else {
    console.log('✓ Node.js version is compatible\n');
  }
  
  // Check dependencies
  const nodeModulesPath = path.join(__dirname, '../node_modules');
  if (fs.existsSync(nodeModulesPath)) {
    console.log('✓ Dependencies installed\n');
  } else {
    console.log('⚠️  Dependencies not installed');
    console.log('   Run: npm install\n');
  }
  
  console.log('Setup complete! Next steps:\n');
  console.log('1. Edit config.json with your OpenAI API key');
  console.log('2. Run: npm run tutor (for interactive help)');
  console.log('3. Try generating content with the bots\n');
  console.log('Happy learning! 🚀\n');
  
  rl.close();
}

setup();
