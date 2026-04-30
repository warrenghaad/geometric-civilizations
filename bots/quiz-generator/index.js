#!/usr/bin/env node

/**
 * Quiz Generator Bot
 * 
 * This bot generates interactive quizzes and puzzles for the curriculum
 * using AI to ensure educational value and engagement.
 */

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);

function parseArgs(args) {
  const parsed = {};
  for (let i = 0; i < args.length; i += 2) {
    const key = args[i].replace('--', '');
    const value = args[i + 1];
    parsed[key] = value;
  }
  return parsed;
}

function displayHelp() {
  console.log(`
Quiz Generator Bot - Creates interactive quizzes and puzzles

Usage:
  npm run bot:quiz -- --topic <topic> [options]

Required Arguments:
  --topic          The topic for the quiz
                   Examples: pythagorean-theorem, circles, geometric-patterns

Optional Arguments:
  --civilization   Focus on a specific civilization (optional)
  --questions      Number of questions (default: 10)
  --difficulty     Difficulty level (default: intermediate)
                   Options: beginner, intermediate, advanced, mixed
  --type          Quiz type (default: mixed)
                   Options: multiple-choice, true-false, short-answer, mixed
  --output        Output file path (default: auto-generated)

Examples:
  npm run bot:quiz -- --topic pythagorean-theorem --questions 10
  npm run bot:quiz -- --topic circles --civilization ancient-egypt --difficulty beginner
  npm run bot:quiz -- --topic geometric-patterns --type multiple-choice --questions 15

Note: Run 'npm run tutor' for help with setup!
`);
}

function loadConfig() {
  const configPath = path.join(__dirname, '../../config.json');
  
  if (!fs.existsSync(configPath)) {
    console.error('❌ Error: config.json not found!');
    console.error('Run: cp config.example.json config.json');
    console.error('Then configure your settings.');
    process.exit(1);
  }
  
  try {
    return JSON.parse(fs.readFileSync(configPath, 'utf8'));
  } catch (error) {
    console.error('❌ Error parsing config.json:', error.message);
    process.exit(1);
  }
}

async function generateQuiz(options) {
  console.log('📝 Quiz Generator Bot Starting...\n');
  
  const { 
    topic, 
    civilization = 'general',
    questions = '10',
    difficulty = 'intermediate',
    type = 'mixed'
  } = options;
  
  console.log(`Generating quiz for:`);
  console.log(`  📚 Topic: ${topic}`);
  if (civilization !== 'general') console.log(`  🏛️  Civilization: ${civilization}`);
  console.log(`  🔢 Questions: ${questions}`);
  console.log(`  📊 Difficulty: ${difficulty}`);
  console.log(`  📋 Type: ${type}\n`);
  
  const numQuestions = parseInt(questions);
  const quiz = {
    metadata: {
      topic: topic,
      civilization: civilization,
      difficulty: difficulty,
      questionCount: numQuestions,
      generatedDate: new Date().toISOString(),
      version: '1.0'
    },
    quiz: {
      title: `${capitalize(topic.replace(/-/g, ' '))} Quiz`,
      instructions: 'Answer all questions to test your understanding. Some questions may have multiple parts.',
      timeLimit: numQuestions * 2, // 2 minutes per question
      questions: []
    }
  };
  
  // Generate sample questions
  for (let i = 1; i <= numQuestions; i++) {
    const questionType = type === 'mixed' ? getRandomQuestionType() : type;
    quiz.quiz.questions.push(generateQuestion(i, topic, questionType, difficulty));
  }
  
  // Determine output path
  const outputDir = path.join(__dirname, '../../curriculum', civilization !== 'general' ? civilization : 'quizzes');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const outputFile = options.output || path.join(outputDir, `${topic}-quiz.json`);
  fs.writeFileSync(outputFile, JSON.stringify(quiz, null, 2), 'utf8');
  
  console.log('✅ Quiz generated successfully!');
  console.log(`📁 Saved to: ${outputFile}\n`);
  console.log('Next steps:');
  console.log('  • Review the quiz questions');
  console.log('  • Test the quiz with students');
  console.log('  • Use the assessment bot to check quality\n');
}

function getRandomQuestionType() {
  const types = ['multiple-choice', 'true-false', 'short-answer'];
  return types[Math.floor(Math.random() * types.length)];
}

function generateQuestion(number, topic, type, difficulty) {
  const question = {
    id: number,
    type: type,
    difficulty: difficulty,
    points: type === 'short-answer' ? 5 : 2
  };
  
  if (type === 'multiple-choice') {
    question.question = `Question ${number} about ${topic.replace(/-/g, ' ')}?`;
    question.options = ['Option A', 'Option B', 'Option C', 'Option D'];
    question.correctAnswer = 'A';
    question.explanation = 'Explanation of why this answer is correct.';
  } else if (type === 'true-false') {
    question.question = `Statement about ${topic.replace(/-/g, ' ')}`;
    question.correctAnswer = true;
    question.explanation = 'Explanation of the concept.';
  } else if (type === 'short-answer') {
    question.question = `Explain a concept related to ${topic.replace(/-/g, ' ')}`;
    question.sampleAnswer = 'Sample answer showing expected response.';
    question.rubric = [
      'Clear explanation (2 points)',
      'Use of examples (2 points)',
      'Correct terminology (1 point)'
    ];
  }
  
  return question;
}

function capitalize(str) {
  return str.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

async function main() {
  if (args.includes('--help') || args.includes('-h') || args.length === 0) {
    displayHelp();
    process.exit(0);
  }
  
  const options = parseArgs(args);
  
  if (!options.topic) {
    console.error('❌ Error: Missing required argument: --topic\n');
    displayHelp();
    process.exit(1);
  }
  
  const config = loadConfig();
  
  if (!config.bots.quizGenerator.enabled) {
    console.error('❌ Error: Quiz Generator Bot is disabled in config.json');
    process.exit(1);
  }
  
  try {
    await generateQuiz(options);
  } catch (error) {
    console.error('❌ Error generating quiz:', error.message);
    process.exit(1);
  }
}

main();
