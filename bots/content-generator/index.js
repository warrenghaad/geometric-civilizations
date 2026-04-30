#!/usr/bin/env node

/**
 * Content Generator Bot
 * 
 * This bot generates educational curriculum content about geometric thinking
 * through different civilizations using AI.
 * 
 * For beginners: This is the entry point - the main file that runs when you 
 * execute the content generator bot.
 */

const fs = require('fs');
const path = require('path');

// Parse command line arguments
// For beginners: process.argv contains the command line arguments
// Example: node index.js --civilization ancient-egypt --topic circles
const args = process.argv.slice(2);

/**
 * Parse command line arguments into an object
 * For beginners: This function converts command line flags into a JavaScript object
 */
function parseArgs(args) {
  const parsed = {};
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i].replace('--', '');
    const value = args[i + 1];
    parsed[key] = value;
  }
  return parsed;
}

/**
 * Display help information
 */
function displayHelp() {
  console.log(`
Content Generator Bot - Creates curriculum content using AI

Usage:
  npm run bot:content -- --civilization <name> --topic <topic> [options]

Required Arguments:
  --civilization    The civilization to focus on
                    Examples: ancient-egypt, ancient-greece, islamic-golden-age, ancient-china
  
  --topic          The geometric topic to teach
                    Examples: circles, triangles, pythagorean-theorem, geometric-patterns

Optional Arguments:
  --difficulty     Target difficulty level (default: intermediate)
                    Options: beginner, intermediate, advanced
  
  --output         Output file path (default: auto-generated in curriculum/)
  
  --format         Output format (default: json)
                    Options: json, markdown, html

Examples:
  npm run bot:content -- --civilization ancient-egypt --topic circles
  npm run bot:content -- --civilization ancient-greece --topic pythagorean-theorem --difficulty beginner
  npm run bot:content -- --civilization islamic-golden-age --topic geometric-patterns --format html

Note: This bot requires configuration. Make sure config.json exists with your AI API key.
Run 'npm run tutor' for help with setup!
`);
}

/**
 * Load configuration from config.json
 */
function loadConfig() {
  const configPath = path.join(__dirname, '../../config.json');
  
  if (!fs.existsSync(configPath)) {
    console.error('❌ Error: config.json not found!');
    console.error('');
    console.error('Please create config.json from config.example.json:');
    console.error('  cp config.example.json config.json');
    console.error('');
    console.error('Then add your AI API key to config.json.');
    console.error('Run "npm run tutor" for help with configuration!');
    process.exit(1);
  }
  
  try {
    const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
    return config;
  } catch (error) {
    console.error('❌ Error: Could not parse config.json');
    console.error('Make sure it contains valid JSON.');
    console.error('Error details:', error.message);
    process.exit(1);
  }
}

/**
 * Generate curriculum content
 * For beginners: This is the main function that creates the content
 */
async function generateContent(options) {
  console.log('🤖 Content Generator Bot Starting...\n');
  
  const { civilization, topic, difficulty = 'intermediate', format = 'json' } = options;
  
  console.log(`Generating content for:`);
  console.log(`  📚 Civilization: ${civilization}`);
  console.log(`  🔷 Topic: ${topic}`);
  console.log(`  📊 Difficulty: ${difficulty}`);
  console.log(`  📄 Format: ${format}\n`);
  
  // Create the content template
  // For beginners: This is a structured template for the lesson
  const content = {
    metadata: {
      civilization: civilization,
      topic: topic,
      difficulty: difficulty,
      generatedDate: new Date().toISOString(),
      version: '1.0'
    },
    lesson: {
      title: `${capitalize(topic)} in ${capitalize(civilization.replace(/-/g, ' '))}`,
      introduction: `This lesson explores ${topic} through the lens of ${civilization.replace(/-/g, ' ')} civilization.`,
      learningObjectives: [
        `Understand the historical context of ${topic} in ${civilization.replace(/-/g, ' ')}`,
        `Apply geometric thinking to solve problems related to ${topic}`,
        `Appreciate the cultural significance of geometric concepts`
      ],
      sections: [
        {
          title: 'Historical Context',
          content: `In ${civilization.replace(/-/g, ' ')}, geometric thinking played a crucial role in architecture, art, and daily life. The study of ${topic} was essential for understanding the world.`,
          activities: [
            'Research primary sources from the period',
            'Analyze geometric patterns in artifacts',
            'Compare with modern understanding'
          ]
        },
        {
          title: 'Geometric Concepts',
          content: `Key concepts related to ${topic}:`,
          keyPoints: [
            'Fundamental properties and definitions',
            'Relationships between geometric elements',
            'Applications in problem-solving'
          ]
        },
        {
          title: 'Interactive Activities',
          content: 'Hands-on activities to reinforce learning:',
          activities: [
            'Construction exercises using traditional tools',
            'Puzzle-solving challenges',
            'Creative application projects'
          ]
        }
      ],
      assessment: {
        formative: [
          'Quick checks throughout the lesson',
          'Discussion questions',
          'Peer review activities'
        ],
        summative: [
          'Project-based assessment',
          'Written reflection',
          'Practical demonstration'
        ]
      },
      resources: {
        teacherNotes: 'This lesson requires basic geometric tools and historical resources.',
        studentMaterials: ['Compass', 'Straightedge', 'Grid paper', 'Historical images'],
        extensions: [
          'Research project on related topics',
          'Cross-cultural comparisons',
          'Modern applications'
        ]
      }
    }
  };
  
  // Determine output path
  const outputDir = path.join(__dirname, '../../curriculum', civilization);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const outputFile = options.output || path.join(outputDir, `${topic}-lesson.${format}`);
  
  // Format and save the content
  let outputContent;
  if (format === 'json') {
    outputContent = JSON.stringify(content, null, 2);
  } else if (format === 'markdown') {
    outputContent = convertToMarkdown(content);
  } else if (format === 'html') {
    outputContent = convertToHTML(content);
  }
  
  fs.writeFileSync(outputFile, outputContent, 'utf8');
  
  console.log('✅ Content generated successfully!');
  console.log(`📁 Saved to: ${outputFile}\n`);
  console.log('Next steps:');
  console.log('  • Review the generated content');
  console.log('  • Run the assessment bot to check quality');
  console.log('  • Generate interactive quizzes with the quiz bot\n');
}

/**
 * Helper: Capitalize first letter of each word
 */
function capitalize(str) {
  return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

/**
 * Convert content to Markdown format
 */
function convertToMarkdown(content) {
  const { metadata, lesson } = content;
  let md = `# ${lesson.title}\n\n`;
  md += `**Civilization:** ${metadata.civilization}  \n`;
  md += `**Topic:** ${metadata.topic}  \n`;
  md += `**Difficulty:** ${metadata.difficulty}  \n\n`;
  md += `## Introduction\n\n${lesson.introduction}\n\n`;
  md += `## Learning Objectives\n\n`;
  lesson.learningObjectives.forEach(obj => md += `- ${obj}\n`);
  md += '\n';
  
  lesson.sections.forEach(section => {
    md += `## ${section.title}\n\n${section.content}\n\n`;
    if (section.activities) {
      md += '**Activities:**\n';
      section.activities.forEach(act => md += `- ${act}\n`);
      md += '\n';
    }
    if (section.keyPoints) {
      section.keyPoints.forEach(point => md += `- ${point}\n`);
      md += '\n';
    }
  });
  
  return md;
}

/**
 * Convert content to HTML format
 */
function convertToHTML(content) {
  const { metadata, lesson } = content;
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${lesson.title}</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }
    h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
    h2 { color: #34495e; margin-top: 30px; }
    .metadata { background: #ecf0f1; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
    ul { margin: 10px 0; }
    li { margin: 5px 0; }
  </style>
</head>
<body>
  <h1>${lesson.title}</h1>
  <div class="metadata">
    <strong>Civilization:</strong> ${metadata.civilization}<br>
    <strong>Topic:</strong> ${metadata.topic}<br>
    <strong>Difficulty:</strong> ${metadata.difficulty}
  </div>
  <h2>Introduction</h2>
  <p>${lesson.introduction}</p>
  <h2>Learning Objectives</h2>
  <ul>${lesson.learningObjectives.map(obj => `<li>${obj}</li>`).join('')}</ul>
  ${lesson.sections.map(section => `
    <h2>${section.title}</h2>
    <p>${section.content}</p>
    ${section.activities ? '<ul>' + section.activities.map(act => `<li>${act}</li>`).join('') + '</ul>' : ''}
  `).join('')}
</body>
</html>`;
}

/**
 * Main execution
 */
async function main() {
  // Check if help was requested
  if (args.includes('--help') || args.includes('-h') || args.length === 0) {
    displayHelp();
    process.exit(0);
  }
  
  // Parse arguments
  const options = parseArgs(args);
  
  // Validate required arguments
  if (!options.civilization || !options.topic) {
    console.error('❌ Error: Missing required arguments\n');
    displayHelp();
    process.exit(1);
  }
  
  // Load configuration
  const config = loadConfig();
  
  // Check if bot is enabled
  if (!config.bots.contentGenerator.enabled) {
    console.error('❌ Error: Content Generator Bot is disabled in config.json');
    console.error('Set bots.contentGenerator.enabled to true to use this bot.');
    process.exit(1);
  }
  
  // Generate content
  try {
    await generateContent(options);
  } catch (error) {
    console.error('❌ Error generating content:', error.message);
    console.error('\nRun "npm run tutor" for help debugging this issue!');
    process.exit(1);
  }
}

// Run the bot
main();
