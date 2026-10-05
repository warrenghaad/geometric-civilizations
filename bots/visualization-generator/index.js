#!/usr/bin/env node

/**
 * Visualization Generator Bot
 * Creates geometric diagrams and interactive visualizations
 */

const fs = require('fs');
const path = require('path');

const args = process.argv.slice(2);

function displayHelp() {
  console.log(`
Visualization Generator Bot - Creates geometric diagrams and animations

Usage:
  npm run bot:visualize -- --shape <shape> [options]

Required Arguments:
  --shape          The geometric shape to visualize
                   Examples: circle, triangle, hexagon, pyramid, star

Optional Arguments:
  --civilization   Cultural context for the visualization
  --interactive    Make it interactive (default: true)
  --output        Output file path (default: auto-generated)

Examples:
  npm run bot:visualize -- --shape hexagon --civilization islamic
  npm run bot:visualize -- --shape pyramid --civilization ancient-egypt

Run 'npm run tutor' for help!
`);
}

async function generateVisualization(options) {
  console.log('🎨 Visualization Generator Bot Starting...\n');
  
  const { shape, civilization = 'general', interactive = 'true' } = options;
  
  console.log(`Generating visualization for:`);
  console.log(`  🔷 Shape: ${shape}`);
  if (civilization !== 'general') console.log(`  🏛️  Civilization: ${civilization}`);
  console.log(`  ⚡ Interactive: ${interactive}\n`);
  
  // Create HTML visualization
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${shape} Visualization - ${civilization}</title>
  <style>
    body { 
      margin: 0; 
      padding: 20px; 
      font-family: Arial, sans-serif; 
      display: flex; 
      flex-direction: column; 
      align-items: center;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
      color: white;
    }
    h1 { margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
    canvas { 
      background: white; 
      border-radius: 10px; 
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      cursor: ${interactive === 'true' ? 'pointer' : 'default'};
    }
    .controls {
      margin-top: 20px;
      background: rgba(255,255,255,0.1);
      padding: 15px;
      border-radius: 10px;
      backdrop-filter: blur(10px);
    }
    button {
      margin: 5px;
      padding: 10px 20px;
      border: none;
      border-radius: 5px;
      background: #4CAF50;
      color: white;
      cursor: pointer;
      font-size: 16px;
    }
    button:hover { background: #45a049; }
  </style>
</head>
<body>
  <h1>${shape.charAt(0).toUpperCase() + shape.slice(1)} - ${civilization}</h1>
  <canvas id="canvas" width="600" height="600"></canvas>
  ${interactive === 'true' ? `
  <div class="controls">
    <button onclick="rotate()">Rotate</button>
    <button onclick="scale()">Scale</button>
    <button onclick="reset()">Reset</button>
  </div>` : ''}
  <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    let rotation = 0;
    let scaleValue = 1;
    
    function drawShape() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.save();
      ctx.translate(canvas.width / 2, canvas.height / 2);
      ctx.rotate(rotation);
      ctx.scale(scaleValue, scaleValue);
      
      ctx.beginPath();
      ctx.strokeStyle = '#2196F3';
      ctx.lineWidth = 3;
      ctx.fillStyle = 'rgba(33, 150, 243, 0.3)';
      
      // Draw ${shape}
      const sides = ${shape === 'hexagon' ? 6 : shape === 'triangle' ? 3 : 4};
      const radius = 150;
      for (let i = 0; i <= sides; i++) {
        const angle = (i * 2 * Math.PI) / sides - Math.PI / 2;
        const x = radius * Math.cos(angle);
        const y = radius * Math.sin(angle);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      
      ctx.closePath();
      ctx.fill();
      ctx.stroke();
      ctx.restore();
    }
    
    function rotate() {
      rotation += Math.PI / 6;
      drawShape();
    }
    
    function scale() {
      scaleValue = scaleValue === 1 ? 1.5 : 1;
      drawShape();
    }
    
    function reset() {
      rotation = 0;
      scaleValue = 1;
      drawShape();
    }
    
    ${interactive === 'true' ? `
    canvas.addEventListener('click', rotate);
    ` : ''}
    
    drawShape();
  </script>
</body>
</html>`;
  
  const outputDir = path.join(__dirname, '../../curriculum', civilization !== 'general' ? civilization : 'visualizations');
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  const outputFile = options.output || path.join(outputDir, `${shape}-visualization.html`);
  fs.writeFileSync(outputFile, html, 'utf8');
  
  console.log('✅ Visualization generated successfully!');
  console.log(`📁 Saved to: ${outputFile}`);
  console.log(`🌐 Open in browser to view!\n`);
}

async function main() {
  if (args.includes('--help') || args.includes('-h') || args.length === 0) {
    displayHelp();
    process.exit(0);
  }
  
  const options = {};
  for (let i = 0; i < args.length; i += 2) {
    options[args[i].replace('--', '')] = args[i + 1];
  }
  
  if (!options.shape) {
    console.error('❌ Error: Missing required argument: --shape\n');
    displayHelp();
    process.exit(1);
  }
  
  await generateVisualization(options);
}

main();
