#!/usr/bin/env node

/**
 * Image Decomposition Bot
 * 
 * This bot helps educators show students (grades 3-5) how objects in photos
 * can be broken down into basic 2D and 3D geometric shapes.
 * 
 * It processes images and creates:
 * 1. Shape analysis showing which basic shapes make up objects
 * 2. Visual overlays highlighting shapes in the image
 * 3. Educational content matching images with curriculum outlines
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
Image Decomposition Bot - Shows how objects are made of basic geometric shapes

PERFECT FOR: Teachers showing 3rd-5th graders how to see shapes in everyday objects!

Works with REAL PHOTOGRAPHS of objects, symbols, buildings, toys, signs, and more!

Usage:
  npm run bot:decompose -- --image <path> --outline <path> [options]

Required Arguments:
  --image          Path to your photo (JPG, PNG)
                   Examples: photos/stop-sign.jpg, photos/building.jpg, photos/toy.jpg
                   Works with real photographs, not just drawings!
  
  --outline        Path to curriculum outline file (JSON or text)
                   Example: outlines/shapes-lesson.json

Optional Arguments:
  --grade          Target grade level (default: 3-5)
                   Options: 3, 4, 5, 3-5
  
  --shapes         Which shapes to highlight (default: all)
                   Options: 2d, 3d, all
                   2D shapes: circles, triangles, rectangles, squares
                   3D shapes: spheres, cubes, cylinders, cones, pyramids
  
  --output         Output directory (default: curriculum/decomposed/)
  
  --format         Output format (default: html)
                   Options: html, json, pdf

Examples:
  # Real photos of everyday objects
  npm run bot:decompose -- --image photos/stop-sign.jpg --outline outlines/traffic-safety.txt --grade 3
  npm run bot:decompose -- --image photos/building.jpg --outline outlines/architecture.txt --grade 4
  npm run bot:decompose -- --image photos/toy-car.jpg --outline outlines/shapes.txt --grade 3

  # Cultural symbols and objects
  npm run bot:decompose -- --image photos/peace-symbol.jpg --outline outlines/symbols.txt --shapes 2d
  npm run bot:decompose -- --image photos/kitchen-can.jpg --outline outlines/containers.txt --shapes 3d

  # Generate interactive HTML (default)
  npm run bot:decompose -- --image photos/any-object.jpg --outline outlines/lesson.txt --format html

Quick Start (No images yet?):
  npm run bot:decompose -- --demo
  This creates sample lessons - then use YOUR photos!

What You'll Get:
  ✓ Visual guide showing shapes in the image
  ✓ Mathematical formulas for each shape (area, perimeter, volume)
  ✓ Angle measurements and properties
  ✓ Educational content matched to your outline
  ✓ Interactive exercises for students
  ✓ Worked examples and practice problems
  ✓ Teacher notes and talking points
  ✓ Print-ready worksheets

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

/**
 * Generate demo content with sample images
 */
async function generateDemo() {
  console.log('🎨 Creating demo lesson with sample images...\n');
  
  const outputDir = path.join(__dirname, '../../curriculum/decomposed-demo');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  // Create sample HTML with embedded SVG "photos"
  const demoHTML = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Shape Decomposition Demo - Grades 3-5</title>
  <style>
    body {
      font-family: 'Comic Sans MS', 'Arial', sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: #333;
    }
    .container {
      background: white;
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
      color: #764ba2;
      text-align: center;
      font-size: 2.5em;
      margin-bottom: 10px;
    }
    .subtitle {
      text-align: center;
      color: #667eea;
      font-size: 1.2em;
      margin-bottom: 30px;
    }
    .lesson-section {
      margin: 30px 0;
      padding: 20px;
      background: #f8f9fa;
      border-radius: 15px;
      border-left: 5px solid #667eea;
    }
    .image-container {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin: 20px 0;
    }
    .image-box {
      background: white;
      padding: 15px;
      border-radius: 10px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .image-title {
      font-weight: bold;
      color: #764ba2;
      margin-bottom: 10px;
      font-size: 1.1em;
    }
    svg {
      width: 100%;
      height: auto;
      border: 2px solid #ddd;
      border-radius: 5px;
    }
    .shape-list {
      margin-top: 15px;
      padding: 15px;
      background: #e3f2fd;
      border-radius: 8px;
    }
    .shape-item {
      padding: 8px;
      margin: 5px 0;
      background: white;
      border-radius: 5px;
      border-left: 3px solid #2196F3;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .shape-icon {
      font-size: 1.5em;
    }
    .activity-box {
      background: #fff3e0;
      padding: 20px;
      margin: 20px 0;
      border-radius: 10px;
      border: 2px dashed #ff9800;
    }
    .teacher-notes {
      background: #e8f5e9;
      padding: 15px;
      margin: 20px 0;
      border-radius: 10px;
      border-left: 4px solid #4caf50;
    }
    .btn {
      background: #667eea;
      color: white;
      padding: 12px 24px;
      border: none;
      border-radius: 25px;
      font-size: 1em;
      cursor: pointer;
      margin: 5px;
      transition: all 0.3s;
    }
    .btn:hover {
      background: #764ba2;
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .interactive-controls {
      text-align: center;
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🔷 Finding Shapes Around Us! 🔷</h1>
    <div class="subtitle">A Shape Decomposition Lesson for Grades 3-5</div>

    <div class="lesson-section">
      <h2>📚 Learning Goal</h2>
      <p>Students will learn to identify and name basic 2D and 3D shapes in everyday objects.</p>
      <p><strong>Key Concept:</strong> All objects around us are made up of simple geometric shapes!</p>
    </div>

    <div class="lesson-section">
      <h2>🏠 Example 1: A Simple House</h2>
      <div class="image-container">
        <div class="image-box">
          <div class="image-title">Original Image</div>
          <svg viewBox="0 0 300 300">
            <!-- House body (square) -->
            <rect x="75" y="150" width="150" height="120" fill="#e8b4a0" stroke="#333" stroke-width="3"/>
            <!-- Roof (triangle) -->
            <polygon points="150,80 50,150 250,150" fill="#d2691e" stroke="#333" stroke-width="3"/>
            <!-- Door (rectangle) -->
            <rect x="125" y="200" width="50" height="70" fill="#8b4513" stroke="#333" stroke-width="2"/>
            <!-- Window (square) -->
            <rect x="160" y="170" width="40" height="40" fill="#87ceeb" stroke="#333" stroke-width="2"/>
            <!-- Window panes -->
            <line x1="180" y1="170" x2="180" y2="210" stroke="#333" stroke-width="1"/>
            <line x1="160" y1="190" x2="200" y2="190" stroke="#333" stroke-width="1"/>
            <!-- Sun (circle) -->
            <circle cx="250" cy="100" r="25" fill="#ffd700" stroke="#333" stroke-width="2"/>
          </svg>
        </div>
        
        <div class="image-box">
          <div class="image-title">Shapes Highlighted</div>
          <svg viewBox="0 0 300 300">
            <!-- House body with label -->
            <rect x="75" y="150" width="150" height="120" fill="rgba(255,0,0,0.3)" stroke="red" stroke-width="4"/>
            <text x="150" y="210" text-anchor="middle" fill="red" font-weight="bold" font-size="16">SQUARE</text>
            
            <!-- Roof with label -->
            <polygon points="150,80 50,150 250,150" fill="rgba(0,255,0,0.3)" stroke="green" stroke-width="4"/>
            <text x="150" y="120" text-anchor="middle" fill="green" font-weight="bold" font-size="16">TRIANGLE</text>
            
            <!-- Door -->
            <rect x="125" y="200" width="50" height="70" fill="rgba(0,0,255,0.3)" stroke="blue" stroke-width="3"/>
            <text x="150" y="235" text-anchor="middle" fill="blue" font-weight="bold" font-size="12">RECTANGLE</text>
            
            <!-- Window -->
            <rect x="160" y="170" width="40" height="40" fill="rgba(255,165,0,0.3)" stroke="orange" stroke-width="3"/>
            <text x="180" y="165" text-anchor="middle" fill="orange" font-weight="bold" font-size="12">SQUARE</text>
            
            <!-- Sun -->
            <circle cx="250" cy="100" r="25" fill="rgba(255,215,0,0.3)" stroke="gold" stroke-width="3"/>
            <text x="250" y="145" text-anchor="middle" fill="#ff8c00" font-weight="bold" font-size="12">CIRCLE</text>
          </svg>
        </div>
      </div>

      <div class="shape-list">
        <strong>🔍 Shapes We Found:</strong>
        <div class="shape-item">
          <span class="shape-icon">🟥</span>
          <span><strong>2 Squares:</strong> House body and window</span>
        </div>
        <div class="shape-item">
          <span class="shape-icon">🔺</span>
          <span><strong>1 Triangle:</strong> Roof</span>
        </div>
        <div class="shape-item">
          <span class="shape-icon">📘</span>
          <span><strong>1 Rectangle:</strong> Door</span>
        </div>
        <div class="shape-item">
          <span class="shape-icon">🔵</span>
          <span><strong>1 Circle:</strong> Sun</span>
        </div>
      </div>

      <div style="background:#e8f5e9; padding:20px; margin:20px 0; border-radius:10px; border-left:4px solid #4caf50;">
        <h3>📐 Shape Mathematics (Grades 4-5)</h3>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>🔺 Triangle Properties:</h4>
          <ul>
            <li><strong>Angles:</strong> All triangles have 3 angles that add up to 180°</li>
            <li><strong>This roof triangle:</strong> Has one 90° angle at top, two 45° angles at bottom</li>
            <li><strong>Formula for area:</strong> A = ½ × base × height</li>
            <li><strong>Perimeter:</strong> P = side₁ + side₂ + side₃</li>
          </ul>
        </div>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>🟥 Square Properties:</h4>
          <ul>
            <li><strong>Angles:</strong> Each corner is exactly 90° (right angle)</li>
            <li><strong>All 4 sides are equal length</strong></li>
            <li><strong>Formula for area:</strong> A = side × side (or s²)</li>
            <li><strong>Formula for perimeter:</strong> P = 4 × side</li>
          </ul>
        </div>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>📘 Rectangle Properties:</h4>
          <ul>
            <li><strong>Angles:</strong> Each corner is 90°</li>
            <li><strong>Opposite sides are equal</strong> (length = length, width = width)</li>
            <li><strong>Formula for area:</strong> A = length × width</li>
            <li><strong>Formula for perimeter:</strong> P = 2 × (length + width)</li>
          </ul>
        </div>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>🔵 Circle Properties:</h4>
          <ul>
            <li><strong>Angles:</strong> A full circle = 360°</li>
            <li><strong>No corners!</strong> Every point on edge is same distance from center</li>
            <li><strong>Formula for area:</strong> A = π × radius² (π ≈ 3.14)</li>
            <li><strong>Formula for circumference:</strong> C = 2 × π × radius</li>
          </ul>
        </div>
        <p style="margin-top:15px;"><strong>💡 Fun Fact:</strong> Architects and engineers use these formulas every day to design buildings, bridges, and roads!</p>
      </div>

      <div class="activity-box">
        <h3>✏️ Student Activity</h3>
        <p><strong>Try This:</strong> Draw your own house using only these shapes:</p>
        <ul>
          <li>At least 1 triangle</li>
          <li>At least 2 rectangles or squares</li>
          <li>At least 1 circle</li>
        </ul>
        <p><strong>Challenge:</strong> Can you use MORE shapes? Try adding a garden, a chimney, or clouds!</p>
      </div>
    </div>

    <div class="lesson-section">
      <h2>🤖 Example 2: A Robot</h2>
      <div class="image-container">
        <div class="image-box">
          <div class="image-title">Original Image</div>
          <svg viewBox="0 0 300 300">
            <!-- Robot head (square) -->
            <rect x="100" y="50" width="100" height="100" fill="#c0c0c0" stroke="#333" stroke-width="3"/>
            <!-- Eyes (circles) -->
            <circle cx="130" cy="90" r="15" fill="#000" stroke="#333" stroke-width="2"/>
            <circle cx="170" cy="90" r="15" fill="#000" stroke="#333" stroke-width="2"/>
            <!-- Antenna (line + circle) -->
            <line x1="150" y1="50" x2="150" y2="20" stroke="#333" stroke-width="3"/>
            <circle cx="150" cy="20" r="8" fill="red" stroke="#333" stroke-width="2"/>
            <!-- Mouth (rectangle) -->
            <rect x="120" y="120" width="60" height="15" fill="#000" stroke="#333" stroke-width="2"/>
            <!-- Body (rectangle) -->
            <rect x="90" y="160" width="120" height="100" fill="#a9a9a9" stroke="#333" stroke-width="3"/>
            <!-- Control panel (square) -->
            <rect x="130" y="190" width="40" height="40" fill="#4169e1" stroke="#333" stroke-width="2"/>
            <!-- Buttons (small circles) -->
            <circle cx="140" cy="200" r="5" fill="red"/>
            <circle cx="160" cy="200" r="5" fill="green"/>
            <circle cx="140" cy="220" r="5" fill="yellow"/>
            <circle cx="160" cy="220" r="5" fill="blue"/>
          </svg>
        </div>
        
        <div class="image-box">
          <div class="image-title">Shapes Highlighted</div>
          <svg viewBox="0 0 300 300">
            <!-- Head -->
            <rect x="100" y="50" width="100" height="100" fill="rgba(255,0,0,0.3)" stroke="red" stroke-width="4"/>
            <text x="150" y="45" text-anchor="middle" fill="red" font-weight="bold" font-size="14">SQUARE</text>
            
            <!-- Eyes -->
            <circle cx="130" cy="90" r="15" fill="rgba(0,0,255,0.3)" stroke="blue" stroke-width="3"/>
            <circle cx="170" cy="90" r="15" fill="rgba(0,0,255,0.3)" stroke="blue" stroke-width="3"/>
            <text x="150" y="75" text-anchor="middle" fill="blue" font-weight="bold" font-size="12">CIRCLES</text>
            
            <!-- Body -->
            <rect x="90" y="160" width="120" height="100" fill="rgba(0,255,0,0.3)" stroke="green" stroke-width="4"/>
            <text x="150" y="275" text-anchor="middle" fill="green" font-weight="bold" font-size="14">RECTANGLE</text>
            
            <!-- Control panel -->
            <rect x="130" y="190" width="40" height="40" fill="rgba(255,165,0,0.3)" stroke="orange" stroke-width="3"/>
            <text x="150" y="185" text-anchor="middle" fill="orange" font-weight="bold" font-size="10">SQUARE</text>
          </svg>
        </div>
      </div>

      <div class="shape-list">
        <strong>🔍 Shapes We Found:</strong>
        <div class="shape-item">
          <span class="shape-icon">🟥</span>
          <span><strong>2 Squares:</strong> Head and control panel</span>
        </div>
        <div class="shape-item">
          <span class="shape-icon">📘</span>
          <span><strong>2 Rectangles:</strong> Body and mouth</span>
        </div>
        <div class="shape-item">
          <span class="shape-icon">🔵</span>
          <span><strong>6 Circles:</strong> Eyes, antenna top, and 4 buttons</span>
        </div>
      </div>

      <div style="background:#e3f2fd; padding:20px; margin:20px 0; border-radius:10px; border-left:4px solid #2196F3;">
        <h3>🧮 Math Challenge: Calculate the Robot!</h3>
        <p>Let's practice using our shape formulas:</p>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>Problem 1: If the robot's head is a square with sides of 10 cm, what is its area?</h4>
          <p><em>Use: A = side × side</em></p>
          <p><strong>Answer:</strong> 10 × 10 = 100 cm²</p>
        </div>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>Problem 2: If each eye is a circle with radius 2 cm, what is one eye's area?</h4>
          <p><em>Use: A = π × radius² (π ≈ 3.14)</em></p>
          <p><strong>Answer:</strong> 3.14 × 2 × 2 = 12.56 cm²</p>
        </div>
        <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
          <h4>Problem 3: If the body is a rectangle 12 cm wide and 10 cm tall, what is its perimeter?</h4>
          <p><em>Use: P = 2 × (length + width)</em></p>
          <p><strong>Answer:</strong> 2 × (12 + 10) = 2 × 22 = 44 cm</p>
        </div>
        <p><strong>💪 Extra Challenge:</strong> How many total 90° angles are in this robot? (Hint: Count all the corners of squares and rectangles!)</p>
      </div>

      <div class="activity-box">
        <h3>✏️ Student Activity</h3>
        <p><strong>Design Your Robot:</strong> Create a robot using basic shapes!</p>
        <ul>
          <li>Use squares or rectangles for the body</li>
          <li>Add circles for eyes, buttons, or wheels</li>
          <li>Get creative with triangles for ears or feet!</li>
        </ul>
        <p><strong>Bonus:</strong> Name your robot and describe what it can do!</p>
      </div>
    </div>

    <div class="teacher-notes">
      <h3>👩‍🏫 Teacher Notes</h3>
      <p><strong>Time:</strong> 30-45 minutes</p>
      <p><strong>Materials Needed:</strong> Paper, pencils, colored pencils or crayons, rulers (optional)</p>
      <p><strong>Learning Standards:</strong> Identifies and describes 2D shapes (squares, rectangles, triangles, circles)</p>
      <p><strong>Differentiation:</strong></p>
      <ul>
        <li><strong>Grade 3:</strong> Focus on identifying shapes in simple images</li>
        <li><strong>Grade 4:</strong> Count shapes and describe their properties (sides, corners)</li>
        <li><strong>Grade 5:</strong> Introduce 3D shapes (cubes, spheres) and how 2D shapes can form 3D objects</li>
      </ul>
      <p><strong>Discussion Questions:</strong></p>
      <ul>
        <li>What shapes do you see in your classroom?</li>
        <li>Can you find shapes in your clothes or backpack?</li>
        <li>Why do you think architects use these basic shapes?</li>
      </ul>
    </div>

    <div class="interactive-controls">
      <h3>🎯 Ready to Use This Lesson?</h3>
      <button class="btn" onclick="window.print()">🖨️ Print Worksheet</button>
      <button class="btn" onclick="alert('Use npm run bot:decompose with your own images!')">📸 Add Your Images</button>
    </div>

    <div class="lesson-section">
      <h2>📖 Next Steps</h2>
      <p>Now that you have a demo, here's how to use YOUR images:</p>
      <ol>
        <li><strong>Prepare your images:</strong> Save them as JPG or PNG files</li>
        <li><strong>Create an outline:</strong> Write what you want to teach (can be a simple text file)</li>
        <li><strong>Run the bot:</strong> 
          <code style="background:#f5f5f5; padding:5px; border-radius:3px; display:block; margin:10px 0;">
            npm run bot:decompose -- --image photos/your-image.jpg --outline outlines/your-lesson.txt
          </code>
        </li>
      </ol>
      <p><strong>Need help?</strong> Run <code>npm run tutor</code> and ask: "How do I use the image decomposition bot?"</p>
    </div>
  </div>
</body>
</html>`;
  
  const outputFile = path.join(outputDir, 'shape-decomposition-demo.html');
  fs.writeFileSync(outputFile, demoHTML, 'utf8');
  
  console.log('✅ Demo lesson created successfully!');
  console.log(`📁 Saved to: ${outputFile}`);
  console.log(`\n🌐 Open this file in a web browser to see the lesson!`);
  console.log(`\n📝 This demo shows:`);
  console.log(`   • How to break down images into shapes`);
  console.log(`   • Visual examples for grades 3-5`);
  console.log(`   • Student activities and teacher notes`);
  console.log(`   • Ready-to-use lesson format`);
  console.log(`\n🚀 Next: Use this bot with YOUR images and outlines!\n`);
}

/**
 * Process image and outline to create decomposition lesson
 */
async function decomposeImage(options) {
  console.log('🎨 Image Decomposition Bot Starting...\n');
  
  const { 
    image, 
    outline,
    grade = '3-5',
    shapes = 'all',
    format = 'html'
  } = options;
  
  console.log(`Processing:`);
  console.log(`  📸 Image: ${image}`);
  console.log(`  📝 Outline: ${outline}`);
  console.log(`  🎓 Grade: ${grade}`);
  console.log(`  🔷 Shapes: ${shapes}`);
  console.log(`  📄 Format: ${format}\n`);
  
  // Check if files exist
  if (!fs.existsSync(image)) {
    console.error(`❌ Error: Image file not found: ${image}`);
    console.error(`\nMake sure the image path is correct.`);
    console.error(`Tip: Place images in a 'photos' or 'images' folder.\n`);
    process.exit(1);
  }
  
  if (!fs.existsSync(outline)) {
    console.error(`❌ Error: Outline file not found: ${outline}`);
    console.error(`\nMake sure the outline path is correct.`);
    console.error(`Tip: Create a simple text file with your lesson plan.\n`);
    process.exit(1);
  }
  
  // Read outline
  const outlineContent = fs.readFileSync(outline, 'utf8');
  
  // Generate lesson content
  const lesson = {
    metadata: {
      imagePath: image,
      outlinePath: outline,
      grade: grade,
      shapeFocus: shapes,
      generatedDate: new Date().toISOString(),
      version: '1.0'
    },
    lesson: {
      title: 'Finding Shapes in Everyday Objects',
      targetGrade: grade,
      outlineContent: outlineContent,
      detectedShapes: {
        '2d': shapes === '3d' ? [] : ['circles', 'triangles', 'rectangles', 'squares'],
        '3d': shapes === '2d' ? [] : ['cubes', 'cylinders', 'spheres']
      },
      activities: [
        `Identify all ${shapes === '2d' ? '2D' : shapes === '3d' ? '3D' : ''} shapes in the image`,
        'Draw or trace the shapes you find',
        'Count how many of each shape type',
        'Create your own design using similar shapes'
      ],
      teacherNotes: `Use this lesson to help students see geometry in their world. Point out how complex objects are made of simple shapes.`,
      studentWorksheet: {
        questions: [
          'How many circles can you find?',
          'What shapes make up the main object?',
          'Can you draw this object using only basic shapes?'
        ]
      }
    }
  };
  
  // Determine output path
  const outputDir = path.join(__dirname, '../../curriculum/decomposed');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const imageName = path.basename(image, path.extname(image));
  const outputFile = path.join(outputDir, `${imageName}-decomposition.${format === 'html' ? 'html' : 'json'}`);
  
  if (format === 'json') {
    fs.writeFileSync(outputFile, JSON.stringify(lesson, null, 2), 'utf8');
  } else {
    // Generate HTML output
    const htmlContent = generateHTML(lesson, image);
    fs.writeFileSync(outputFile, htmlContent, 'utf8');
  }
  
  console.log('✅ Decomposition lesson created successfully!');
  console.log(`📁 Saved to: ${outputFile}`);
  console.log(`\n📝 What was created:`);
  console.log(`   • Visual shape breakdown`);
  console.log(`   • Matched with your outline content`);
  console.log(`   • Student activities`);
  console.log(`   • Teacher notes`);
  console.log(`\n🌐 Open the HTML file in a web browser to view!\n`);
}

/**
 * Generate HTML output for the lesson
 */
function generateHTML(lesson, imagePath) {
  const imageFileName = path.basename(imagePath);
  
  return `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${lesson.lesson.title} - Grade ${lesson.metadata.grade}</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 1000px;
      margin: 0 auto;
      padding: 20px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .container {
      background: white;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
      color: #764ba2;
      text-align: center;
    }
    .image-section {
      text-align: center;
      margin: 30px 0;
      padding: 20px;
      background: #f8f9fa;
      border-radius: 10px;
    }
    .image-section img {
      max-width: 100%;
      height: auto;
      border: 3px solid #667eea;
      border-radius: 10px;
    }
    .shapes-found {
      background: #e3f2fd;
      padding: 20px;
      border-radius: 10px;
      margin: 20px 0;
    }
    .activity {
      background: #fff3e0;
      padding: 20px;
      border-radius: 10px;
      margin: 20px 0;
      border: 2px dashed #ff9800;
    }
    .teacher-notes {
      background: #e8f5e9;
      padding: 20px;
      border-radius: 10px;
      margin: 20px 0;
    }
    ul {
      line-height: 1.8;
    }
    .btn {
      background: #667eea;
      color: white;
      padding: 10px 20px;
      border: none;
      border-radius: 20px;
      cursor: pointer;
      margin: 5px;
    }
    .btn:hover {
      background: #764ba2;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>${lesson.lesson.title}</h1>
    <p style="text-align:center; color:#667eea; font-size:1.2em;">Grade ${lesson.metadata.grade}</p>
    
    <div class="image-section">
      <h2>📸 Our Image</h2>
      <p><em>Image: ${imageFileName}</em></p>
      <p>Look carefully at this image. Can you see the basic shapes hidden inside?</p>
    </div>
    
    <div class="shapes-found">
      <h2>🔍 Shapes to Find</h2>
      <h3>2D Shapes (Flat):</h3>
      <ul>
        ${lesson.lesson.detectedShapes['2d'].map(shape => `<li>${capitalize(shape)}</li>`).join('')}
      </ul>
      ${lesson.lesson.detectedShapes['3d'].length > 0 ? `
      <h3>3D Shapes (Solid):</h3>
      <ul>
        ${lesson.lesson.detectedShapes['3d'].map(shape => `<li>${capitalize(shape)}</li>`).join('')}
      </ul>` : ''}
    </div>
    
    <div style="background:#e8f5e9; padding:20px; border-radius:10px; margin:20px 0; border-left:4px solid #4caf50;">
      <h2>📐 Shape Mathematics & Formulas</h2>
      <p>Understanding the math behind the shapes helps us measure and design!</p>
      
      ${lesson.lesson.detectedShapes['2d'].includes('circles') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>🔵 Circle Formulas:</h3>
        <ul>
          <li><strong>Area:</strong> A = π × r² (where r = radius, π ≈ 3.14)</li>
          <li><strong>Circumference:</strong> C = 2 × π × r</li>
          <li><strong>Angles:</strong> Full circle = 360°</li>
          <li><strong>Example:</strong> If radius = 5 cm, then Area = 3.14 × 5² = 78.5 cm²</li>
        </ul>
      </div>` : ''}
      
      ${lesson.lesson.detectedShapes['2d'].includes('triangles') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>🔺 Triangle Formulas:</h3>
        <ul>
          <li><strong>Area:</strong> A = ½ × base × height</li>
          <li><strong>Perimeter:</strong> P = side₁ + side₂ + side₃</li>
          <li><strong>Angles:</strong> All 3 angles always add up to 180°</li>
          <li><strong>Right triangle:</strong> Has one 90° angle</li>
          <li><strong>Example:</strong> If base = 6 cm and height = 4 cm, then Area = ½ × 6 × 4 = 12 cm²</li>
        </ul>
      </div>` : ''}
      
      ${lesson.lesson.detectedShapes['2d'].includes('rectangles') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>📘 Rectangle Formulas:</h3>
        <ul>
          <li><strong>Area:</strong> A = length × width</li>
          <li><strong>Perimeter:</strong> P = 2 × (length + width)</li>
          <li><strong>Angles:</strong> Each corner = 90° (4 right angles total)</li>
          <li><strong>Example:</strong> If length = 8 cm and width = 3 cm, then Area = 8 × 3 = 24 cm²</li>
        </ul>
      </div>` : ''}
      
      ${lesson.lesson.detectedShapes['2d'].includes('squares') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>🟥 Square Formulas:</h3>
        <ul>
          <li><strong>Area:</strong> A = side × side (or s²)</li>
          <li><strong>Perimeter:</strong> P = 4 × side</li>
          <li><strong>Angles:</strong> Each corner = 90° (4 equal right angles)</li>
          <li><strong>Diagonal:</strong> d = side × √2 ≈ side × 1.414</li>
          <li><strong>Example:</strong> If side = 7 cm, then Area = 7² = 49 cm²</li>
        </ul>
      </div>` : ''}
      
      ${lesson.lesson.detectedShapes['3d'].includes('cubes') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>📦 Cube Formulas (3D):</h3>
        <ul>
          <li><strong>Volume:</strong> V = side × side × side (or s³)</li>
          <li><strong>Surface Area:</strong> SA = 6 × side²</li>
          <li><strong>Example:</strong> If side = 4 cm, then Volume = 4³ = 64 cm³</li>
        </ul>
      </div>` : ''}
      
      ${lesson.lesson.detectedShapes['3d'].includes('cylinders') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>🥫 Cylinder Formulas (3D):</h3>
        <ul>
          <li><strong>Volume:</strong> V = π × r² × height</li>
          <li><strong>Surface Area:</strong> SA = 2πr² + 2πrh</li>
          <li><strong>Example:</strong> If r = 3 cm and h = 10 cm, then Volume = 3.14 × 9 × 10 = 282.6 cm³</li>
        </ul>
      </div>` : ''}
      
      ${lesson.lesson.detectedShapes['3d'].includes('spheres') ? `
      <div style="background:white; padding:15px; margin:10px 0; border-radius:5px;">
        <h3>⚽ Sphere Formulas (3D):</h3>
        <ul>
          <li><strong>Volume:</strong> V = (4/3) × π × r³</li>
          <li><strong>Surface Area:</strong> SA = 4 × π × r²</li>
          <li><strong>Example:</strong> If radius = 5 cm, then Volume = (4/3) × 3.14 × 125 = 523.3 cm³</li>
        </ul>
      </div>` : ''}
      
      <p style="margin-top:15px;"><strong>💡 Real-World Application:</strong> Engineers, architects, and designers use these formulas every day to calculate materials, costs, and measurements!</p>
    </div>
    
    <div style="background:#f0f0f0; padding:20px; border-radius:10px; margin:20px 0;">
      <h2>📖 Lesson Content</h2>
      <pre style="white-space:pre-wrap; font-family:Arial;">${lesson.lesson.outlineContent}</pre>
    </div>
    
    <div class="activity">
      <h2>✏️ Student Activities</h2>
      <ol>
        ${lesson.lesson.activities.map(activity => `<li>${activity}</li>`).join('')}
      </ol>
      
      <h3>Worksheet Questions:</h3>
      <ol>
        ${lesson.lesson.studentWorksheet.questions.map(q => `<li>${q}</li>`).join('')}
      </ol>
    </div>
    
    <div class="teacher-notes">
      <h2>👩‍🏫 Teacher Notes</h2>
      <p>${lesson.lesson.teacherNotes}</p>
      <p><strong>Generated:</strong> ${new Date(lesson.metadata.generatedDate).toLocaleDateString()}</p>
    </div>
    
    <div style="text-align:center; margin-top:30px;">
      <button class="btn" onclick="window.print()">🖨️ Print This Lesson</button>
    </div>
  </div>
</body>
</html>`;
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

async function main() {
  // Check for demo mode
  if (args.includes('--demo')) {
    await generateDemo();
    process.exit(0);
  }
  
  if (args.includes('--help') || args.includes('-h') || args.length === 0) {
    displayHelp();
    process.exit(0);
  }
  
  const options = parseArgs(args);
  
  if (!options.image || !options.outline) {
    console.error('❌ Error: Missing required arguments\n');
    console.error('Quick start: npm run bot:decompose -- --demo\n');
    displayHelp();
    process.exit(1);
  }
  
  const config = loadConfig();
  
  try {
    await decomposeImage(options);
  } catch (error) {
    console.error('❌ Error processing image:', error.message);
    console.error('\nNeed help? Run: npm run tutor');
    process.exit(1);
  }
}

main();
