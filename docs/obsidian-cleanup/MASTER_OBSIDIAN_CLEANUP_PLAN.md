# Master Obsidian Cleanup Plan: Start to Finish

**Date:** 2026-09-25  
**Estimated Time:** 2-4 hours active work + 24 hour verification period  
**Goal:** Stop all automated file movement, isolate Obsidian from git/cloud, establish clean working environment

---

## TABLE OF CONTENTS

1. [Pre-Work Assessment](#phase-1-pre-work-assessment)
2. [Emergency Stop](#phase-2-emergency-stop)
3. [Full System Inventory](#phase-3-full-system-inventory)
4. [Create Safe Backups](#phase-4-create-safe-backups)
5. [Disable Sync Mechanisms](#phase-5-disable-sync-mechanisms)
6. [Remove Indexing Data](#phase-6-remove-indexing-data)
7. [Fix Cloud Storage](#phase-7-fix-cloud-storage)
8. [Fix Claude Desktop](#phase-8-fix-claude-desktop)
9. [Verification Period](#phase-9-verification-period)
10. [Safe Restoration](#phase-10-safe-restoration)
11. [New Workflow Setup](#phase-11-new-workflow-setup)
12. [Ongoing Maintenance](#phase-12-ongoing-maintenance)

---

## PHASE 1: PRE-WORK ASSESSMENT

**Time:** 10 minutes  
**Goal:** Understand what you're dealing with before making changes

### 1.1 Check what's currently running
```bash
# See all Obsidian-related processes
ps aux | grep -i obsidian

# See all sync processes
ps aux | grep -i "google\|icloud\|dropbox"

# See any git processes
ps aux | grep -i git
```

### 1.2 Check disk space
```bash
# Make sure you have room for backups
df -h ~
```
You need at least 10GB free for safe archiving.

### 1.3 Note your current state
Write down:
- [ ] How many Obsidian vaults do you have?
- [ ] Which cloud services are active? (Google Drive / iCloud / Dropbox)
- [ ] What projects are you actively working on?
- [ ] When did the file movement problem start?

---

## PHASE 2: EMERGENCY STOP

**Time:** 5 minutes  
**Goal:** Stop all automated processes immediately

### 2.1 Quit Obsidian
```bash
# Force quit all Obsidian processes
pkill -9 -f Obsidian
```
**Verify:** Open Activity Monitor, search "Obsidian" - should show nothing.

### 2.2 Pause Google Drive
1. Click Google Drive icon in menu bar (top right of screen)
2. Click gear icon → Pause syncing
3. **Verify:** Icon should show paused state

### 2.3 Pause iCloud Drive
```bash
# Pause iCloud sync temporarily
killall bird
```
Or: System Settings → Apple ID → iCloud → iCloud Drive → Turn OFF

### 2.4 Pause Dropbox (if using)
1. Click Dropbox icon in menu bar
2. Click profile icon → Pause syncing

### 2.5 Confirm all sync is stopped
```bash
# Should return nothing
ps aux | grep -i "google\|icloud\|dropbox\|obsidian"
```

---

## PHASE 3: FULL SYSTEM INVENTORY

**Time:** 15-20 minutes  
**Goal:** Find everything Obsidian-related on your system

### 3.1 Create inventory directory
```bash
mkdir -p ~/OBSIDIAN_INVENTORY_2026-09-25
cd ~/OBSIDIAN_INVENTORY_2026-09-25
```

### 3.2 Find all Obsidian vaults (.obsidian folders)
```bash
find ~ -name ".obsidian" -type d 2>/dev/null > vaults.txt
echo "Found $(wc -l < vaults.txt) vaults"
cat vaults.txt
```

### 3.3 Find all Smart Environment indexes
```bash
find ~ -name ".smart-env" -type d 2>/dev/null > smart_env.txt
echo "Found $(wc -l < smart_env.txt) .smart-env folders"
cat smart_env.txt
```

### 3.4 Find all obsidian-git plugins
```bash
find ~ -type d -name "obsidian-git" 2>/dev/null > obsidian_git.txt
echo "Found $(wc -l < obsidian_git.txt) obsidian-git plugins"
cat obsidian_git.txt
```

### 3.5 Find all folders with "obsidian" in name
```bash
find ~ -type d -iname "*obsidian*" 2>/dev/null > obsidian_folders.txt
echo "Found $(wc -l < obsidian_folders.txt) obsidian-named folders"
cat obsidian_folders.txt
```

### 3.6 Find .git folders in cloud locations
```bash
# iCloud
find ~/Library/Mobile\ Documents -name ".git" -type d 2>/dev/null > git_in_icloud.txt

# Google Drive
find ~/Library/CloudStorage -name ".git" -type d 2>/dev/null > git_in_gdrive.txt

# Combine
cat git_in_icloud.txt git_in_gdrive.txt > git_in_cloud.txt
echo "Found $(wc -l < git_in_cloud.txt) .git folders in cloud storage"
cat git_in_cloud.txt
```

### 3.7 Find reconcile scripts
```bash
find ~ -name "reconcile*.py" -o -name "*reconcile*.sh" 2>/dev/null > reconcile_scripts.txt
echo "Found $(wc -l < reconcile_scripts.txt) reconcile scripts"
cat reconcile_scripts.txt
```

### 3.8 Check Claude Desktop config
```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json > claude_config.txt
cat claude_config.txt
```

### 3.9 Review the inventory
```bash
echo "=== INVENTORY SUMMARY ==="
echo "Vaults: $(wc -l < vaults.txt)"
echo "Smart-env: $(wc -l < smart_env.txt)"
echo "Obsidian-git: $(wc -l < obsidian_git.txt)"
echo "Obsidian folders: $(wc -l < obsidian_folders.txt)"
echo "Git in cloud: $(wc -l < git_in_cloud.txt)"
echo "Reconcile scripts: $(wc -l < reconcile_scripts.txt)"
```

---

## PHASE 4: CREATE SAFE BACKUPS

**Time:** 30-60 minutes (depends on vault sizes)  
**Goal:** Archive everything before making destructive changes

### 4.1 Create quarantine directory
```bash
mkdir -p ~/OBSIDIAN_QUARANTINE_2026-09-25
cd ~/OBSIDIAN_QUARANTINE_2026-09-25
```

### 4.2 Archive main Obsidian vault
```bash
# This may take a while for large vaults
echo "Archiving main vault..."
zip -r "main-vault-backup.zip" "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault" -x "*.smart-env/*"

echo "Archiving .smart-env separately..."
zip -r "main-vault-smart-env.zip" "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.smart-env"
```

### 4.3 Archive each additional vault
For each vault found in `vaults.txt`:
```bash
# Example pattern - repeat for each vault
VAULT_PATH="/path/to/vault"
VAULT_NAME=$(basename "$VAULT_PATH")
zip -r "${VAULT_NAME}-backup.zip" "$VAULT_PATH"
```

### 4.4 Archive all obsidian-git configs
```bash
while read -r gitpath; do
    name=$(echo "$gitpath" | tr '/' '_')
    zip -r "obsidian-git-${name}.zip" "$gitpath"
done < ~/OBSIDIAN_INVENTORY_2026-09-25/obsidian_git.txt
```

### 4.5 Archive .git folders from cloud
```bash
while read -r gitpath; do
    name=$(echo "$gitpath" | tr '/' '_')
    zip -r "cloud-git-${name}.zip" "$gitpath"
done < ~/OBSIDIAN_INVENTORY_2026-09-25/git_in_cloud.txt
```

### 4.6 Verify backups
```bash
ls -lh ~/OBSIDIAN_QUARANTINE_2026-09-25/
# Should see multiple .zip files
```

### 4.7 Copy inventory files
```bash
cp ~/OBSIDIAN_INVENTORY_2026-09-25/*.txt ~/OBSIDIAN_QUARANTINE_2026-09-25/
```

---

## PHASE 5: DISABLE SYNC MECHANISMS

**Time:** 15 minutes  
**Goal:** Disable all plugins that sync Obsidian to git

### 5.1 Disable obsidian-git in each vault
For each vault, rename the plugin folder:
```bash
# Read each vault from inventory
while read -r vaultpath; do
    PLUGIN_PATH="${vaultpath}/plugins/obsidian-git"
    if [ -d "$PLUGIN_PATH" ]; then
        echo "Disabling obsidian-git in: $vaultpath"
        mv "$PLUGIN_PATH" "${PLUGIN_PATH}-DISABLED"
    fi
done < ~/OBSIDIAN_INVENTORY_2026-09-25/vaults.txt
```

### 5.2 Disable Smart Connections
```bash
while read -r vaultpath; do
    PLUGIN_PATH="${vaultpath}/plugins/smart-connections"
    if [ -d "$PLUGIN_PATH" ]; then
        echo "Disabling smart-connections in: $vaultpath"
        mv "$PLUGIN_PATH" "${PLUGIN_PATH}-DISABLED"
    fi
done < ~/OBSIDIAN_INVENTORY_2026-09-25/vaults.txt
```

### 5.3 Disable any other AI/indexing plugins
```bash
# Common ones to disable
PLUGINS_TO_DISABLE=(
    "smart-connections"
    "smart-environment"
    "obsidian-git"
    "obsidian-github-sync"
    "remotely-save"
    "obsidian-livesync"
)

while read -r vaultpath; do
    for plugin in "${PLUGINS_TO_DISABLE[@]}"; do
        PLUGIN_PATH="${vaultpath}/plugins/${plugin}"
        if [ -d "$PLUGIN_PATH" ]; then
            echo "Disabling ${plugin} in: $vaultpath"
            mv "$PLUGIN_PATH" "${PLUGIN_PATH}-DISABLED"
        fi
    done
done < ~/OBSIDIAN_INVENTORY_2026-09-25/vaults.txt
```

---

## PHASE 6: REMOVE INDEXING DATA

**Time:** 10 minutes  
**Goal:** Delete the .smart-env folders that index your entire system

### 6.1 Confirm backups exist
```bash
ls ~/OBSIDIAN_QUARANTINE_2026-09-25/*smart-env*
# Should show your backup files
```

### 6.2 Remove .smart-env folders
```bash
while read -r smartenv; do
    echo "Removing: $smartenv"
    rm -rf "$smartenv"
done < ~/OBSIDIAN_INVENTORY_2026-09-25/smart_env.txt
```

### 6.3 Verify removal
```bash
find ~ -name ".smart-env" -type d 2>/dev/null
# Should return nothing
```

---

## PHASE 7: FIX CLOUD STORAGE

**Time:** 15-20 minutes  
**Goal:** Remove .git folders from cloud-synced locations

### 7.1 Review what will be removed
```bash
cat ~/OBSIDIAN_INVENTORY_2026-09-25/git_in_cloud.txt
```

### 7.2 Confirm backups exist
```bash
ls ~/OBSIDIAN_QUARANTINE_2026-09-25/cloud-git-*
```

### 7.3 Remove .git from iCloud
```bash
while read -r gitpath; do
    if [[ "$gitpath" == *"Mobile Documents"* ]]; then
        echo "Removing from iCloud: $gitpath"
        rm -rf "$gitpath"
    fi
done < ~/OBSIDIAN_INVENTORY_2026-09-25/git_in_cloud.txt
```

### 7.4 Remove .git from Google Drive
```bash
while read -r gitpath; do
    if [[ "$gitpath" == *"CloudStorage"* ]]; then
        echo "Removing from Google Drive: $gitpath"
        rm -rf "$gitpath"
    fi
done < ~/OBSIDIAN_INVENTORY_2026-09-25/git_in_cloud.txt
```

### 7.5 Verify removal
```bash
find ~/Library/Mobile\ Documents -name ".git" -type d 2>/dev/null
find ~/Library/CloudStorage -name ".git" -type d 2>/dev/null
# Both should return nothing
```

---

## PHASE 8: FIX CLAUDE DESKTOP

**Time:** 5 minutes  
**Goal:** Configure Claude Desktop to use safe project folders only

### 8.1 Backup current config
```bash
cp ~/Library/Application\ Support/Claude/claude_desktop_config.json \
   ~/OBSIDIAN_QUARANTINE_2026-09-25/claude_config_backup.json
```

### 8.2 Create clean config
```bash
cat > ~/Library/Application\ Support/Claude/claude_desktop_config.json << 'EOF'
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/warrenghaad/Documents/geometric-civilizations"
      ]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    }
  }
}
EOF
```

### 8.3 Verify config
```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
# Should show clean config with NO Obsidian paths
```

### 8.4 Restart Claude Desktop
```bash
osascript -e 'quit app "Claude"'
sleep 3
open -a Claude
```

### 8.5 Verify in Claude Desktop
Open Claude Desktop and check:
- [ ] No "Obsidian Vault" in environment selector
- [ ] Only "Cloud" and expected environments shown

---

## PHASE 9: VERIFICATION PERIOD

**Time:** 24 hours (passive monitoring)  
**Goal:** Confirm no automated file movement is occurring

### 9.1 Create monitoring script
```bash
cat > ~/Desktop/monitor_changes.sh << 'EOF'
#!/bin/bash
echo "=== File Change Monitor ==="
echo "Started at: $(date)"
echo "Checking for obsidian-related changes every hour..."

while true; do
    echo ""
    echo "=== $(date) ==="
    
    # Check for recently modified obsidian files
    echo "Recently modified obsidian files:"
    find ~ -iname "*obsidian*" -type f -mmin -60 2>/dev/null | head -20
    
    # Check for new .git folders in cloud
    echo "Git in cloud:"
    find ~/Library/Mobile\ Documents ~/Library/CloudStorage -name ".git" -type d 2>/dev/null
    
    # Check for new .smart-env
    echo "Smart-env folders:"
    find ~ -name ".smart-env" -type d 2>/dev/null
    
    sleep 3600  # Check every hour
done
EOF
chmod +x ~/Desktop/monitor_changes.sh
```

### 9.2 Run monitoring
```bash
# In a terminal window, leave this running
~/Desktop/monitor_changes.sh
```

### 9.3 After 24 hours, check results
- [ ] No new .git folders appeared in cloud storage
- [ ] No new .smart-env folders appeared
- [ ] No unexpected file modifications
- [ ] Claude Desktop working normally without Obsidian environment

---

## PHASE 10: SAFE RESTORATION

**Time:** 30+ minutes (as needed)  
**Goal:** Carefully restore only what you need

### 10.1 Decide what to keep
Review your vaults and decide:
- [ ] Which vaults do you actually use?
- [ ] Do you need the indexed data (.smart-env)?
- [ ] Do you need git versioning for notes?

### 10.2 Re-enable cloud sync (carefully)
1. Start Google Drive sync
2. Start iCloud sync
3. **Do NOT sync any folder containing .obsidian**

### 10.3 Open Obsidian (carefully)
1. Open Obsidian
2. If prompted about Safe Mode, choose **Safe Mode**
3. Go to Settings → Community Plugins
4. Verify dangerous plugins are NOT installed:
   - [ ] obsidian-git - should NOT be there
   - [ ] smart-connections - should NOT be there
5. Enable only safe plugins you need

### 10.4 If you need git for notes
Use a **separate** workflow:
```bash
# Manual git from command line
cd "/path/to/vault"
git init
git add .
git commit -m "Manual backup"
```
**Do NOT use obsidian-git plugin.**

---

## PHASE 11: NEW WORKFLOW SETUP

**Time:** Variable  
**Goal:** Establish safe working practices

### 11.1 Project organization rules

| Type | Location | Cloud Sync | Git |
|------|----------|------------|-----|
| Code projects | `~/Documents/` or `~/Projects/` | NO | YES (local) |
| Obsidian vaults | `~/Obsidian Vaults/` | Optional (without .git) | NO |
| Cloud documents | Google Drive / iCloud | YES | NO |
| Claude Desktop access | Project folders only | N/A | N/A |

### 11.2 Never do these again
- [ ] Never put .git inside cloud-synced folders
- [ ] Never point Claude Desktop at Obsidian vaults
- [ ] Never use obsidian-git with cloud-synced vaults
- [ ] Never use Smart Connections to index project folders

### 11.3 Safe Obsidian setup
If you want to use Obsidian for notes:
1. Keep vaults LOCAL (not in cloud sync)
2. Use manual git backups (not obsidian-git)
3. Disable AI indexing plugins
4. Keep vaults separate from code projects

### 11.4 Safe Claude Desktop setup
Only point to:
- Project folders (`~/Documents/project-name/`)
- Folders without `.obsidian`
- Folders not synced to cloud

---

## PHASE 12: ONGOING MAINTENANCE

**Time:** 5 minutes monthly  
**Goal:** Prevent recurrence

### 12.1 Monthly check
Run this monthly:
```bash
# Check for .git in cloud
find ~/Library/Mobile\ Documents ~/Library/CloudStorage -name ".git" -type d 2>/dev/null

# Check for .smart-env
find ~ -name ".smart-env" -type d 2>/dev/null

# Check Claude Desktop config
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json | grep -i obsidian
```

### 12.2 Before installing Obsidian plugins
Ask:
- Does it sync to external services?
- Does it index files outside the vault?
- Does it use git?

If yes to any → **Do not install** or configure very carefully.

### 12.3 Backup schedule
- Weekly: Manual backup of Obsidian vaults
- Monthly: Review and clean up inventory
- Quarterly: Full audit of what's in cloud storage

---

## QUICK REFERENCE: Commands Summary

### Emergency Stop
```bash
pkill -9 -f Obsidian
killall bird
# Pause Google Drive from menu bar
```

### Find Everything
```bash
find ~ -name ".obsidian" -type d 2>/dev/null
find ~ -name ".smart-env" -type d 2>/dev/null
find ~ -type d -name "obsidian-git" 2>/dev/null
```

### Check Claude Config
```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### Restart Claude Desktop
```bash
osascript -e 'quit app "Claude"' && sleep 2 && open -a Claude
```

---

## TROUBLESHOOTING

### Problem: Files still moving after cleanup
1. Check for running sync processes: `ps aux | grep -i sync`
2. Check for cron jobs: `crontab -l`
3. Check for Launch Agents: `ls ~/Library/LaunchAgents/`
4. Look for any remaining .git in cloud

### Problem: Claude Desktop still shows Obsidian environment
1. Quit Claude Desktop completely
2. Delete config: `rm ~/Library/Application\ Support/Claude/claude_desktop_config.json`
3. Restart Claude Desktop (will create fresh config)

### Problem: Obsidian won't open after cleanup
1. Open in Safe Mode: Hold Shift while opening Obsidian
2. Disable all plugins
3. Re-enable one at a time

### Problem: Lost data after cleanup
1. Check quarantine folder: `ls ~/OBSIDIAN_QUARANTINE_2026-09-25/`
2. Unzip relevant backup: `unzip backup-file.zip -d ~/Recovery/`
3. Check existing backup: `Obsidian - Main Vault_archive.tar.gz (4.3GB)`

---

## FINAL CHECKLIST

Before considering this complete, verify:

- [ ] Obsidian closed and all sync plugins disabled
- [ ] Google Drive / iCloud running but NOT syncing .obsidian or .git
- [ ] No .smart-env folders exist
- [ ] No .git folders in cloud storage
- [ ] Claude Desktop config points only to project folders
- [ ] Claude Desktop shows no "Obsidian Vault" environment
- [ ] 24-hour monitoring shows no file movement
- [ ] All backups safely stored in quarantine folder
- [ ] You understand what caused the problem
- [ ] You have a plan to avoid recurrence

---

**Congratulations!** If all boxes are checked, your system is clean.

---

*Master Plan Created: 2026-09-25*  
*Location: geometric-civilizations/MASTER_OBSIDIAN_CLEANUP_PLAN.md*
