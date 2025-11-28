# Auto-Processor System - Quick Start Guide

**What This Does:** Automatically tags, summarizes, and organizes ALL your curriculum content

---

## Installation (One-Time Setup)

### Step 1: Install Python Packages
```bash
pip3 install watchdog anthropic PyPDF2
```

### Step 2: Set API Key
```bash
# Add to ~/.zshrc (permanent)
echo "export ANTHROPIC_API_KEY='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'" >> ~/.zshrc
source ~/.zshrc

# Or just for this session
export ANTHROPIC_API_KEY='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'
```

### Step 3: Make Executable
```bash
chmod +x ~/Documents/Obsidian\ -\ Main\ Vault/06_Tools_and_Tutors/AutoProcessor/auto_processor.py
```

---

## Daily Usage

### Start the Auto-Processor
	```bash
cd ~/Documents/Obsidian\ -\ Main\ Vault/06_Tools_and_Tutors/AutoProcessor/
python3 auto_processor.py
```

**It will watch:** `01_INPUT/PDFs_Unsorted/`

### Use It
1. Drop a PDF or image into `01_INPUT/PDFs_Unsorted/`
2. Wait ~10-30 seconds
3. Check `02_DATABASE/Artifacts/` or `02_DATABASE/Myths/` for new entries
4. Open `00_SYSTEM/Lesson_Outlines_Index.md` to see auto-populated content

### Stop It
Press `Ctrl+C`

---

## What Gets Auto-Tagged

Every file is analyzed for:

### Identification
- ✅ Content type (artifact, myth, STEM innovation)
- ✅ Artifact name & catalog number
- ✅ Museum & date
- ✅ Geometric elements
- ✅ Deities mentioned

### Curriculum Assignment
- ✅ Week number (1-16)
- ✅ Day A or Day B
- ✅ Section number
- ✅ Grade level (3, 4, or 5)

### Teaching Metadata
- ✅ Standards (CCSS Math, CCSS ELA, NCSS)
- ✅ Materials needed
- ✅ Difficulty level
- ✅ Prep time

### MAGIC Driver Vector
- ✅ M (Myth) percentage
- ✅ A (Art/Material) percentage
- ✅ G (Geometric) percentage
- ✅ I (Innovation) percentage
- ✅ C (Ceremonial) percentage

### AI-Generated Content
- ✅ Summary (2-3 sentences)
- ✅ Description
- ✅ Teaching notes
- ✅ Key quotes
- ✅ Cross-references

---

## Output Example

**Input:** `shamash_tablet_british_museum.pdf`

**Output:**
```
02_DATABASE/Artifacts/Tablet-of-Shamash-BM-91000_20251124_153022.md
```

**Contents:**
- Fully tagged YAML frontmatter
- Week 1 assignment
- Day A, Section 3
- Grades 3-5 differentiation
- Standards aligned
- Materials list
- Teaching notes
- Status: ready

**Appears automatically in:**
- `Lesson_Outlines_Index.md` (Week 1 queries)
- Searchable by tags
- Ready to use in lessons

---

## Troubleshooting

### "No API key" error
```bash
echo $ANTHROPIC_API_KEY
# Should show your key, not empty
```

### "No module named 'watchdog'" error
```bash
pip3 install watchdog anthropic PyPDF2
```

### File not processing
- Check it's a PDF or image (.png, .jpg)
- Check file size (< 50MB works best)
- Check console for error messages

### Wrong week assignment
- Claude guesses based on content
- Edit the `week_number:` field in created file
- Or add more context to source file

---

## Files Created

For each processed file, you get:

1. **Database Entry** - In `02_DATABASE/{Type}/`
   - Properly tagged
   - Auto-formatted
   - Ready to use

2. **Processing Report** - In `01_INPUT/_Processed_Archive/`
   - Shows what was extracted
   - Lists entries created
   - Useful for verification

3. **Archived Source** - In `01_INPUT/_Processed_Archive/{date}/`
   - Original file moved here
   - Organized by date
   - Easy to find later

---

## Next Steps

1. **Test it:** Drop a sample PDF and watch it work
2. **Verify tags:** Check the generated entry, edit if needed
3. **Bulk process:** Drop multiple files, let it run
4. **Build lessons:** Use `Lesson_Outlines_Index.md` to assemble lessons

---

## Advanced: Process Existing Content

To process all your existing PDFs:

```bash
# Copy files to watched folder
cp ~/path/to/your/pdfs/*.pdf ~/Documents/Obsidian\ -\ Main\ Vault/01_INPUT/PDFs_Unsorted/

# Auto-processor will detect and process each one
# Takes ~30 seconds per file
```

---

## Questions?

- Check: `AUTOMATED_CONTENT_PROCESSOR.md` for full documentation
- Check: `OmniTutor_enhanced.py` for conversational help
- Or just ask Claude Code (me!) for help

**This solves your 2-month bottleneck!**
