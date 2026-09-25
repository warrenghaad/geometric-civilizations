# URGENT: Obsidian Isolation Plan

**Created:** 2026-09-25  
**Purpose:** Stop all automated file movement and isolate Obsidian from git connections

---

## IMMEDIATE ACTIONS (Do These First)

### Step 1: Stop Obsidian Sync (On Your Mac)

```bash
# Kill any running Obsidian processes
pkill -f Obsidian

# Or on Mac, force quit from Activity Monitor
```

### Step 2: Disable obsidian-git Plugin

In each Obsidian vault:
1. Open Settings → Community Plugins
2. **Disable** "Obsidian Git" plugin
3. Do NOT delete - just disable

### Step 3: Stop Google Drive Sync (Temporarily)

```bash
# On Mac, quit Google Drive
osascript -e 'quit app "Google Drive"'
```

---

## IDENTIFIED CONNECTIONS IN GOOGLE DRIVE

### Primary Obsidian Locations

| Location | Type | Risk |
|----------|------|------|
| `Obsidian - Main Vault/` | Main vault folder | Contains .obsidian config |
| `Obsidian - Main Vault_archive.tar.gz` | **SAFE BACKUP** (4.3GB) | Already archived |
| `EUCLID_STUDIO/00_Reconciliation/` | Has `.git` + `.obsidian` | **HIGH RISK** - git + obsidian connected |
| `EUCLID_STUDIO/00_Reconciliation/hooks/` | Git hooks | May be automating pushes |

### obsidian-git Plugin Locations (Multiple Copies)

These folders contain the obsidian-git plugin which auto-syncs to git:

```
Multiple parent folders contain:
├── obsidian-git/
├── obsidian-kanban/
├── obsidian-tasks-plugin/
├── obsidian-excalidraw-plugin/
├── obsidian-importer/
├── obsidian-style-settings/
├── obsidian-textgenerator-plugin/
├── table-editor-obsidian/
├── templater-obsidian/
```

---

## SAFE ARCHIVING STEPS

### Option A: Create New Archive in Google Drive (Manual)

1. Go to Google Drive
2. Navigate to `EUCLID_STUDIO/00_Reconciliation/`
3. Right-click → Download (this creates a .zip)
4. Move the .zip to a new folder called `OBSIDIAN_QUARANTINE_2026-09-25`

### Option B: Isolate .git and .obsidian Folders

In Google Drive, create this structure:

```
OBSIDIAN_QUARANTINE_2026-09-25/
├── git_configs/           # Move all .git folders here
├── obsidian_configs/      # Move all .obsidian folders here
├── obsidian_plugins/      # Move all obsidian-* plugin folders here
└── README.txt             # Note: "Quarantined 2026-09-25 - do not reconnect without review"
```

### Option C: On Your Local Mac

```bash
# Create quarantine directory
mkdir -p ~/OBSIDIAN_QUARANTINE_2026-09-25

# Find and zip all .obsidian folders
find ~/Library/Mobile\ Documents/com~apple~CloudDocs -name ".obsidian" -type d 2>/dev/null | while read dir; do
    parent=$(dirname "$dir")
    name=$(basename "$parent")
    zip -r ~/OBSIDIAN_QUARANTINE_2026-09-25/"${name}_obsidian_config.zip" "$dir"
done

# Find and zip all .git folders in Drive-synced locations
find ~/Library/Mobile\ Documents/com~apple~CloudDocs -name ".git" -type d 2>/dev/null | while read dir; do
    parent=$(dirname "$dir")
    name=$(basename "$parent")
    zip -r ~/OBSIDIAN_QUARANTINE_2026-09-25/"${name}_git_config.zip" "$dir"
done
```

---

## SPECIFIC 00_Reconciliation ISOLATION

The `00_Reconciliation` folder is the most complex. It contains:

### What's Inside (from earlier scan)

```
00_Reconciliation/
├── .git/                  # GIT REPOSITORY - disconnect this
├── .obsidian/             # OBSIDIAN CONFIG - disconnect this
├── hooks/                 # POSSIBLY AUTOMATION - check these
├── 00_INBOX/
├── 01_CANON/
├── 02_SCHEMA/
├── 03_CONCEPTS/
├── 04_FLOWS/
├── 05_WORKSPACES/
├── 05_TEMPLATES/
├── 06_EVIDENCE/
├── 07_DATASETS/
├── 08_TRANSLATIONS/
├── 09_WORKFLOW/
├── 10_AUTOMATION/         # CHECK FOR SCRIPTS
├── 90_PATCHES/
├── 99_ARCHIVE/
├── scripts/               # CHECK FOR SCRIPTS
├── curriculum-data-instantiation/
├── META-UI-sandbox/
├── obsidian_euclid_template_pack/
├── ZIPS_obsidian <>vault system/
└── Cognition and MAGIC.md
```

### Isolation Steps for 00_Reconciliation

1. **Download entire folder** as .zip from Google Drive
2. **Move these subfolders** to quarantine:
   - `.git/`
   - `.obsidian/`
   - `hooks/`
   - `scripts/`
   - `10_AUTOMATION/`
3. **Keep the content folders** (01_CANON through 99_ARCHIVE) in place

---

## VERIFICATION CHECKLIST

After isolation, verify:

- [ ] Obsidian app is closed
- [ ] obsidian-git plugin is disabled in all vaults
- [ ] Google Drive sync is paused or `.git` folders are moved
- [ ] All `.obsidian` folders are archived/quarantined
- [ ] No cron jobs or scheduled tasks running sync scripts
- [ ] GitHub/GitLab webhooks are not triggering on these repos

---

## DO NOT DELETE

Do not delete any files yet. Just move them to quarantine locations until you understand what's causing the unwanted movement.

The existing archive (`Obsidian - Main Vault_archive.tar.gz` - 4.3GB) is a good safety net.

---

## NEXT STEPS

1. Complete the isolation above
2. Wait 24 hours to confirm no automated movement
3. Review what was in the quarantined folders
4. Decide what to reconnect (if anything)

---

*This document was created to help isolate Obsidian from git connections without losing any data.*
