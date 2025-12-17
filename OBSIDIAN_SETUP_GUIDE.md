# Obsidian Vault Setup - Quick Start Guide

## ✅ What Has Been Set Up

Your repository is now configured as a dual Obsidian vault that works both locally and remotely!

### 📁 Obsidian Configuration Created

The `.obsidian` directory has been set up with:

1. **app.json** - Core application settings
   - Auto-update links when files are renamed
   - New files created in current folder
   - Markdown features enabled

2. **appearance.json** - Visual preferences
   - Default theme: Moonstone
   - Font size: 16px

3. **core-plugins.json** - Essential plugins enabled
   - File explorer, search, graph view
   - Backlinks, outgoing links
   - Command palette, word count

4. **hotkeys.json** - Keyboard shortcuts (empty, customize as needed)

5. **workspace.json** - Your personal workspace layout
   - ⚠️ This file is LOCAL ONLY (not synced to Git)
   - Opens with the Mesopotamian curriculum file

### 🔄 Git Configuration

The `.gitignore` file ensures proper sync behavior:

**Synced to Remote:**
- ✅ Vault configuration files (app.json, appearance.json, etc.)
- ✅ All markdown notes and curriculum content
- ✅ Scripts and automation tools

**Kept Local Only:**
- ❌ workspace.json (your personal layout)
- ❌ workspace-mobile.json
- ❌ .obsidian/cache
- ❌ .DS_Store files

## 🚀 How to Use Your Vault

### First Time Setup

1. Install Obsidian from https://obsidian.md
2. Open Obsidian
3. Click "Open folder as vault"
4. Navigate to this repository folder
5. Click "Open"

### Daily Workflow

**Making Changes:**
```bash
# 1. Open Obsidian and edit your notes
# 2. Save your work (Obsidian auto-saves)
# 3. Commit and push to remote
git add .
git commit -m "Updated curriculum notes"
git push
```

**Syncing from Remote:**
```bash
# Pull latest changes
git pull

# Obsidian will automatically reload the vault
```

### Working on Multiple Devices

1. **Device A (e.g., Desktop):**
   - Make changes in Obsidian
   - Commit and push to Git

2. **Device B (e.g., Laptop):**
   - Pull changes from Git
   - Obsidian updates automatically
   - Your personal workspace layout stays unique to this device

## 📝 Current Content

Your vault includes:

- **MESOPOTAMIAN_CURRICULUM_MAPPING_FOR_PERPLEXITY.md** - Main curriculum document
- **CURRICULUM_SYSTEM_ORGANIZED/** - Organized curriculum pipelines
- Python scripts for automation
- Shell scripts for management

## 🎯 Next Steps

1. ✅ **Open the vault in Obsidian** to verify everything works
2. ✅ **Create your first link** - Try linking to MESOPOTAMIAN_CURRICULUM_MAPPING_FOR_PERPLEXITY.md using `[[MESOPOTAMIAN_CURRICULUM_MAPPING_FOR_PERPLEXITY]]`
3. ✅ **Add tags** - Organize content with tags like #mesopotamia #geometry #curriculum
4. ✅ **Explore the graph view** - See connections between notes
5. ✅ **Customize your workspace** - Arrange tabs and sidebars to your liking (these won't sync!)

## 🔧 Troubleshooting

**Q: Why aren't my tabs syncing between devices?**  
A: This is intentional! Workspace layout is personal to each device.

**Q: I see merge conflicts in .obsidian files**  
A: Most .obsidian files are synced. Resolve conflicts in a text editor, keeping the JSON valid.

**Q: Can I add community plugins?**  
A: Yes! Install them in Obsidian, and they'll be added to community-plugins.json automatically.

## 📚 Resources

- [Obsidian Help](https://help.obsidian.md/)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- This vault's main README.md for detailed information

---

**You're all set! Open Obsidian and start building your curriculum vault! 🎉**
