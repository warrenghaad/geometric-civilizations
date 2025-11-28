# Get Started - 3 Simple Steps

## Step 1: Get New API Key

1. Go to: **https://console.anthropic.com/settings/keys**
2. Log in
3. Click **"Create Key"**
4. Copy the key (starts with `sk-ant-api03-...`)

---

## Step 2: Set the Key & Test It

```bash
# Set the key
export ANTHROPIC_API_KEY='paste-your-key-here'

# Test it works
cd ~/Documents/Obsidian\ -\ Main\ Vault/06_Tools_and_Tutors/AutoProcessor/
python3 test_api_key.py
```

**You should see:**
```
✓ API key found: sk-ant-api03-...
🧪 Testing API key...
✅ SUCCESS! Claude says: API key works!
🎉 Your API key is working correctly!
```

---

## Step 3: Start Auto-Processor

```bash
cd ~/Documents/Obsidian\ -\ Main\ Vault/06_Tools_and_Tutors/AutoProcessor/
python3 auto_processor.py
```

**It will show:**
```
🤖 CLAUDE AUTO-PROCESSOR
Watching: .../01_INPUT/PDFs_Unsorted
Database: .../02_DATABASE

📂 Drop PDFs/images into watched folder to process...
Press Ctrl+C to stop
```

---

## Step 4: Test with a File

1. Open Finder
2. Go to: `Documents/Obsidian - Main Vault/01_INPUT/PDFs_Unsorted/`
3. Drop ANY PDF about Mesopotamia artifacts/myths
4. Watch console output

**In ~30 seconds, check:**
- `02_DATABASE/Artifacts/` for new entry
- Entry will have:
  - ✅ **The Metaphor** (semiotic meaning)
  - ✅ **The Material Object** (physical description)
  - ✅ **The Geometric Element** (shape/pattern)
  - ✅ Auto-tagged with week, deity, section

---

## What Changed Based on Your Feedback

You said: *"I don't care about museum ids. The most important is the metaphor, the material object, the geometric element"*

**I updated the system to prioritize:**

1. **THE METAPHOR** (semiotic meaning)
   - What does the geometric element symbolize?
   - e.g., "Circle = Impartial justice reaching all equally"

2. **THE MATERIAL OBJECT** (physical description)
   - What is the artifact itself?
   - Physical characteristics

3. **THE GEOMETRIC ELEMENT** (shape/pattern)
   - Circle, triangle, square, etc.
   - Where/how it appears

**Museum IDs are still extracted but de-emphasized.**

---

## Queries Now Show What You Care About

Open: `00_SYSTEM/Lesson_Outlines_Index.md`

**Old query (focused on IDs):**
```
| Artifact | Museum ID | Museum | Date |
```

**New query (focused on meaning):**
```
| Material Object | Geometric Element | Metaphor/Meaning | Image Quality |
```

---

## If Test Fails

### "No API key found"
```bash
# Check if set
echo $ANTHROPIC_API_KEY

# If empty, set it again
export ANTHROPIC_API_KEY='your-key-here'
```

### "Authentication Error"
- Key is invalid or expired
- Get a new one from Anthropic console
- Make sure you copy the FULL key

### "Module not found"
```bash
pip3 install watchdog anthropic PyPDF2
```

---

## To Make Key Permanent

Add to `~/.zshrc`:
```bash
echo "export ANTHROPIC_API_KEY='your-key-here'" >> ~/.zshrc
source ~/.zshrc
```

Then it's set every time you open terminal.

---

## Ready?

1. Get key from: https://console.anthropic.com/settings/keys
2. Test: `python3 test_api_key.py`
3. Run: `python3 auto_processor.py`
4. Drop file and watch!

🚀 **Let's break that bottleneck!**
