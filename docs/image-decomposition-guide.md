# Image Decomposition Bot Guide

**Perfect for grades 3-5! Show students how everyday objects are made of basic shapes.**

## What This Bot Does

The Image Decomposition Bot helps you:
- Combine your images with curriculum outlines
- Show students how objects decompose into 2D and 3D shapes
- Create ready-to-use visual lessons
- Save time creating engaging materials

## Quick Start (5 Minutes!)

### Step 1: See a Demo
```bash
npm run bot:decompose -- --demo
```

This creates a complete sample lesson showing:
- A house broken down into shapes (triangle roof, square body, etc.)
- A robot made of rectangles and circles
- Student activities and teacher notes
- Everything ready to use!

Open the generated HTML file in your browser to see it!

### Step 2: Use Your Own Images

#### Prepare Your Files

1. **Images**: Place your photos in a folder
   - JPG or PNG format
   - Clear, simple objects work best
   - Examples: house, robot, car, building, toy

2. **Outline**: Create a simple text file with your lesson plan
   - Can be plain text or JSON
   - Include what you want students to learn
   - Add any talking points or activities

#### Example Outline (save as `outlines/shapes-lesson.txt`):

```
Lesson: Finding Shapes in Our World

Learning Goals:
- Identify basic 2D shapes (circles, triangles, rectangles, squares)
- Understand that complex objects are made of simple shapes
- Practice counting and naming shapes

Key Points:
- All objects can be broken down into basic shapes
- The same shapes appear in many different objects
- Artists and engineers use basic shapes to design things

Activities:
1. Find shapes in the classroom
2. Draw an object using only basic shapes
3. Count how many of each shape type
```

### Step 3: Run the Bot

```bash
npm run bot:decompose -- --image photos/house.jpg --outline outlines/shapes-lesson.txt
```

The bot will:
1. Read your image
2. Read your outline
3. Create an interactive lesson combining both
4. Save it as HTML you can open in any browser

## Command Options

### Basic Usage
```bash
npm run bot:decompose -- --image <photo> --outline <lesson-plan>
```

### For Different Grades
```bash
# 3rd grade (simpler)
npm run bot:decompose -- --image photos/toy.jpg --outline outlines/lesson.txt --grade 3

# 5th grade (more advanced)
npm run bot:decompose -- --image photos/building.jpg --outline outlines/lesson.txt --grade 5
```

### Focus on Specific Shapes
```bash
# 2D shapes only (flat shapes)
npm run bot:decompose -- --image photos/drawing.jpg --outline outlines/2d-shapes.txt --shapes 2d

# 3D shapes (solid objects)
npm run bot:decompose -- --image photos/blocks.jpg --outline outlines/3d-shapes.txt --shapes 3d
```

### Choose Output Format
```bash
# Interactive HTML (default - best for classroom)
npm run bot:decompose -- --image photos/house.jpg --outline outlines/lesson.txt --format html

# JSON data (for programmers)
npm run bot:decompose -- --image photos/house.jpg --outline outlines/lesson.txt --format json
```

## What You Get

### The Generated Lesson Includes:

1. **Visual Breakdown**
   - Original image
   - Same image with shapes highlighted and labeled
   - Color-coded for easy identification

2. **Shape List**
   - Count of each shape type
   - Names and descriptions
   - 2D and 3D shapes separated

3. **Your Outline Content**
   - Integrated seamlessly with visuals
   - Matched to the images
   - Ready to teach

4. **Student Activities**
   - Questions to answer
   - Drawing exercises
   - Counting tasks
   - Creative challenges

5. **Teacher Notes**
   - Grade-appropriate suggestions
   - Differentiation ideas
   - Discussion questions
   - Time estimates

## Real-World Examples

### Example 1: House Photo
**Image**: photo of a house  
**Shapes Found**: triangle (roof), rectangles (walls, door, windows), circle (sun)  
**Grade**: 3  
**Activity**: "Draw your dream house using only these shapes!"

### Example 2: Robot Toy
**Image**: photo of a toy robot  
**Shapes Found**: squares (head, body), rectangles (arms, legs), circles (eyes, buttons)  
**Grade**: 4  
**Activity**: "Design a robot that can help in your classroom. What shapes will you use?"

### Example 3: Building
**Image**: photo of a building  
**Shapes Found**: rectangles (windows), cylinders (columns), triangular prism (roof section)  
**Grade**: 5  
**Activity**: "Research famous buildings. What shapes do architects use most often and why?"

## Tips for Best Results

### Choosing Good Images

✅ **Good Images:**
- Clear, well-lit photos
- Objects with distinct shapes
- Simple composition
- Appropriate for age group

❌ **Avoid:**
- Blurry or dark images
- Too many objects in one photo
- Complex patterns that obscure shapes
- Inappropriate content

### Writing Effective Outlines

**Keep it simple:**
- 3-5 learning goals
- 2-3 key points
- 3-5 activities
- Age-appropriate language

**Include:**
- What students should learn
- Why it matters
- How to assess understanding
- Extension activities

### Organizing Your Files

```
your-project/
├── photos/
│   ├── house.jpg
│   ├── robot.jpg
│   └── building.jpg
├── outlines/
│   ├── shapes-lesson.txt
│   ├── 2d-shapes.txt
│   └── 3d-shapes.txt
└── curriculum/
    └── decomposed/
        ├── house-decomposition.html
        ├── robot-decomposition.html
        └── building-decomposition.html
```

## Classroom Usage

### Before Class
1. Generate 2-3 example lessons
2. Print one copy or prepare to project
3. Review teacher notes
4. Gather materials (paper, pencils, rulers)

### During Class
1. **Introduction (5 min)**
   - Show the original image
   - Ask: "What do you see?"
   
2. **Shape Discovery (10 min)**
   - Reveal highlighted version
   - Count shapes together
   - Discuss properties

3. **Activity Time (20-30 min)**
   - Students complete worksheet
   - Draw their own designs
   - Share with partners

4. **Wrap-up (5 min)**
   - Review what was learned
   - Preview next lesson
   - Assign homework (find shapes at home)

### Assessment Ideas
- Have students photograph objects at home
- Create a "shape scavenger hunt"
- Build 3D models using basic shapes
- Design a poster showing shapes in their world

## Troubleshooting

### "Image file not found"
- Check the file path is correct
- Use forward slashes: `photos/house.jpg`
- Make sure the file exists

### "Outline file not found"
- Check the file path
- File can be .txt or .json
- Make sure you created the outline

### Output looks wrong
- Try the demo first: `npm run bot:decompose -- --demo`
- Check your image is clear and well-lit
- Simplify your outline if needed

### Need more help?
```bash
npm run tutor
# Then ask: "How do I use the image decomposition bot?"
```

## Time-Saving Tips

### Batch Processing
Create multiple lessons quickly:

```bash
# Lesson 1
npm run bot:decompose -- --image photos/house.jpg --outline outlines/shapes.txt

# Lesson 2
npm run bot:decompose -- --image photos/robot.jpg --outline outlines/shapes.txt

# Lesson 3
npm run bot:decompose -- --image photos/car.jpg --outline outlines/shapes.txt
```

### Reuse Outlines
One good outline can work with many images!

### Build a Library
Create a collection of lessons for:
- Different grade levels
- Different shape types
- Different themes (buildings, toys, nature)

## Next Steps

1. **Start with the demo**: See what's possible
2. **Try with one image**: Use a simple photo
3. **Create a series**: Build multiple related lessons
4. **Share with colleagues**: Help others save time too!

## Getting Help

- **Run the demo**: `npm run bot:decompose -- --demo`
- **Get help**: `npm run bot:decompose -- --help`
- **Ask the tutor**: `npm run tutor`
- **Read examples**: Check the generated demo lesson

## FAQ

**Q: Do I need special software to use the generated lessons?**  
A: No! The HTML files open in any web browser (Chrome, Firefox, Safari, Edge).

**Q: Can I edit the generated lessons?**  
A: Yes! Open the HTML in a text editor to customize it.

**Q: What if my photos show copyright material?**  
A: Use your own photos or images with appropriate licenses for education.

**Q: Can students use this too?**  
A: Absolutely! It's a great project for students to find shapes in their world.

**Q: How long does it take to create a lesson?**  
A: About 2-3 minutes per lesson after your initial setup.

## Remember

This bot is designed to **save you time** so you can focus on teaching. It handles the technical work of creating visual materials while you focus on what matters: helping students learn!

Happy teaching! 🎓📐🔷
