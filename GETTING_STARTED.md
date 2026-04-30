# Getting Started with Geometric Civilizations

Welcome! This guide will get you up and running in 10 minutes.

## What You'll Build

A system that uses AI to automatically generate educational curriculum about geometric thinking through different civilizations. Perfect for educators, curriculum developers, and anyone interested in mathematics education!

## Prerequisites

**You need:**
- A computer (Windows, Mac, or Linux)
- 30 minutes of your time
- Willingness to learn!

**You DON'T need:**
- Prior programming experience
- Advanced math knowledge
- Any specific software (we'll install it together)

## Step-by-Step Setup

### 1. Install Node.js (5 minutes)

Node.js lets you run the curriculum bots on your computer.

**Download:**
1. Go to https://nodejs.org
2. Click the big green button that says "LTS" (Long Term Support)
3. Download and run the installer
4. Accept all defaults and click through

**Verify Installation:**
Open your terminal/command prompt and type:
```bash
node --version
npm --version
```

You should see version numbers. If you do, you're ready! 🎉

**Need help?** The terminal is:
- **Windows**: Search for "Command Prompt" or "PowerShell"
- **Mac**: Search for "Terminal" in Spotlight
- **Linux**: You know what to do 😉

### 2. Get the Project (1 minute)

If you're reading this, you probably already have the project!

If not, download it from GitHub and extract to a folder you'll remember.

### 3. Install Dependencies (2 minutes)

Open your terminal in the project folder:
- **Windows**: Right-click the folder → "Open in Terminal" (or navigate using `cd`)
- **Mac/Linux**: Right-click the folder → "New Terminal at Folder" (or use `cd`)

Then run:
```bash
npm install
```

This downloads all the tools the bots need. It might take a minute or two. ☕

**What's happening?** npm (Node Package Manager) is downloading JavaScript libraries (pre-written code) that our bots use.

### 4. Configure Your Settings (2 minutes)

Copy the example configuration:
```bash
cp config.example.json config.json
```

**Windows users:** Use this instead:
```bash
copy config.example.json config.json
```

Now edit `config.json` in a text editor:
1. Find the line: `"apiKey": "YOUR_API_KEY_HERE"`
2. Replace with your OpenAI API key (see below)
3. Save the file

**Getting an OpenAI API Key:**
1. Go to https://platform.openai.com
2. Sign up or log in
3. Click on your profile → "API Keys"
4. Click "Create new secret key"
5. Copy the key (it looks like: `sk-...`)
6. Paste it into config.json

**Note:** Keep this key secret! Don't share it or commit it to git.

### 5. Test Your Setup (30 seconds)

Start the AI Tutor:
```bash
npm run tutor
```

You should see a colorful welcome message! 🎊

Try typing:
```
help
```

Then type `exit` when you're done exploring.

## Your First Bot Run

Let's generate some curriculum content!

### Generate a Lesson

```bash
npm run bot:content -- --civilization ancient-egypt --topic circles
```

**What this does:**
- Creates a complete lesson about circles in Ancient Egypt
- Saves it as a JSON file in `curriculum/ancient-egypt/`
- Includes learning objectives, activities, and assessments

**Check the output:**
Look in `curriculum/ancient-egypt/circles-lesson.json`

### Create a Quiz

```bash
npm run bot:quiz -- --topic circles --questions 5
```

**What this does:**
- Generates 5 quiz questions about circles
- Mix of multiple choice, true/false, and short answer
- Includes explanations for each answer

### Make a Visualization

```bash
npm run bot:visualize -- --shape hexagon
```

**What this does:**
- Creates an interactive HTML visualization
- Opens in any web browser
- Students can interact with the shape

**Try it:** Open `curriculum/visualizations/hexagon-visualization.html` in a browser!

## What's Next?

### Learn the System (Recommended)

```bash
npm run tutor
```

The AI Tutor will guide you through:
- Understanding the code
- Customizing content
- Learning programming concepts
- Debugging issues

Just ask it questions!

### Explore the Documentation

- **README.md** - Full project overview
- **QUICK_REFERENCE.md** - Fast command lookup
- **docs/beginner-guide.md** - Programming from scratch
- **docs/bot-guide.md** - Detailed bot instructions
- **docs/curriculum-guide.md** - Creating great content

### Try More Examples

```bash
# Ancient Greece - Pythagorean Theorem
npm run bot:content -- --civilization ancient-greece --topic pythagorean-theorem

# Islamic patterns
npm run bot:visualize -- --shape star --civilization islamic-golden-age

# Advanced quiz
npm run bot:quiz -- --topic geometric-patterns --difficulty advanced --questions 15
```

### Customize Your Content

1. Generate base content with a bot
2. Open the output file in a text editor
3. Modify it to fit your needs
4. Save and use!

### Assess Quality

```bash
npm run bot:assess -- --file curriculum/ancient-egypt/circles-lesson.json
```

Get feedback on:
- Readability
- Accuracy
- Engagement
- Areas for improvement

## Common Issues

### "npm: command not found"
**Solution:** Node.js isn't installed. Go back to Step 1.

### "Cannot find config.json"
**Solution:** You need to create it. Go back to Step 4.

### "API key invalid"
**Solution:** 
- Check you copied the full key (starts with `sk-`)
- Verify it's active on OpenAI's website
- Make sure there are no spaces or quotes around it

### Need More Help?

```bash
npm run tutor
```

Then ask: "I'm having trouble with [describe your problem]"

## Tips for Success

### 1. Start Simple
Don't try to generate everything at once. Start with:
- One lesson
- One quiz
- One visualization

Then build up!

### 2. Review Everything
Bots generate great content, but always review before using with students:
- Check facts
- Adjust difficulty
- Add your personal touch

### 3. Iterate
Generate → Review → Adjust → Regenerate

It's okay to run a bot multiple times!

### 4. Ask Questions
Use the AI Tutor whenever you're confused:
```bash
npm run tutor
```

### 5. Explore Examples
Check `examples/` and `examples/generated/` to see what's possible.

## What You Can Create

### Individual Lessons
- Historical context
- Geometric concepts
- Interactive activities
- Assessments

### Complete Units
- Multiple lessons on a theme
- Progressive difficulty
- Cultural connections
- Project-based learning

### Interactive Materials
- Visualizations
- Puzzles
- Animations
- Explorations

### Assessment Tools
- Quizzes
- Tests
- Projects
- Rubrics

## Learning Path

**Week 1: Explore**
- Install and setup
- Run all the bots
- Explore the outputs
- Read the documentation

**Week 2: Understand**
- Start the AI Tutor
- Learn programming basics
- Read the code
- Understand the structure

**Week 3: Customize**
- Modify generated content
- Change templates
- Add civilizations
- Adjust settings

**Week 4: Create**
- Build a complete unit
- Share with others
- Get feedback
- Contribute improvements

## Get Support

### Built-in Help
```bash
# AI Tutor - your primary resource
npm run tutor

# Command help
npm run bot:content -- --help
npm run bot:quiz -- --help
```

### Documentation
- All in the `docs/` folder
- Written for beginners
- Lots of examples

### Community
- Share your creations
- Learn from others
- Ask questions
- Contribute code

## You're Ready! 🚀

You now have everything you need to start creating amazing curriculum!

**First Task:** Generate a lesson about your favorite geometric topic!

```bash
npm run bot:content -- --civilization [pick one] --topic [your topic]
```

**Have fun learning and creating!** 🎓

---

**Questions?** Run `npm run tutor` and ask away!

**Stuck?** Check `docs/troubleshooting.md`

**Want to dive deep?** Read `docs/beginner-guide.md`
