# Complete Obsidian Isolation Plan

**Date:** 2026-09-25  
**Problem:** Obsidian vault with Smart Connections plugin is indexing your entire project ecosystem, and obsidian-git is syncing these indexes across your file system, causing unwanted file movement.

---

## PHASE 1: STOP ALL SYNC (Do This NOW)

### 1.1 Kill Obsidian
```bash
pkill -f Obsidian
```
Or: Cmd+Q Obsidian, then check Activity Monitor to confirm it's gone.

### 1.2 Pause Google Drive
Click Google Drive icon in menu bar → Settings → Pause syncing

### 1.3 Pause iCloud (Optional but recommended)
System Settings → Apple ID → iCloud → iCloud Drive → Turn off temporarily

---

## PHASE 2: LOCATE ALL OBSIDIAN COMPONENTS

### 2.1 Find all .obsidian folders (active vaults)
```bash
find ~ -name ".obsidian" -type d 2>/dev/null > ~/Desktop/obsidian_vaults.txt
cat ~/Desktop/obsidian_vaults.txt
```

### 2.2 Find all .smart-env folders (AI indexing)
```bash
find ~ -name ".smart-env" -type d 2>/dev/null > ~/Desktop/smart_env_folders.txt
cat ~/Desktop/smart_env_folders.txt
```

### 2.3 Find all obsidian-git plugin folders
```bash
find ~ -type d -name "obsidian-git" 2>/dev/null > ~/Desktop/obsidian_git_plugins.txt
cat ~/Desktop/obsidian_git_plugins.txt
```

### 2.4 Find all .git folders inside cloud-synced locations
```bash
find ~/Library/Mobile\ Documents -name ".git" -type d 2>/dev/null > ~/Desktop/git_in_icloud.txt
find ~/Library/CloudStorage -name ".git" -type d 2>/dev/null > ~/Desktop/git_in_cloud.txt
cat ~/Desktop/git_in_icloud.txt
cat ~/Desktop/git_in_cloud.txt
```

---

## PHASE 3: CREATE QUARANTINE ZONE

### 3.1 Create quarantine directory
```bash
mkdir -p ~/OBSIDIAN_QUARANTINE_2026-09-25
cd ~/OBSIDIAN_QUARANTINE_2026-09-25
```

### 3.2 Archive the main vault
```bash
# This preserves everything without deleting
zip -r "Obsidian-Main-Vault-FULL.zip" "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault"
```

### 3.3 Archive all .smart-env folders
```bash
# Run this for each .smart-env folder found in step 2.2
# Example:
zip -r "smart-env-main-vault.zip" "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.smart-env"
```

### 3.4 Archive obsidian-git configs
```bash
# For each obsidian-git folder found
zip -r "obsidian-git-configs.zip" [path-to-obsidian-git-folder]
```

---

## PHASE 4: DISABLE DANGEROUS COMPONENTS

### 4.1 Remove .smart-env folders (AFTER archiving)
```bash
# For each .smart-env folder found:
rm -rf "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.smart-env"
```

### 4.2 Disable obsidian-git in each vault
For each vault, rename the plugin folder:
```bash
# Example for main vault:
mv "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.obsidian/plugins/obsidian-git" \
   "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.obsidian/plugins/obsidian-git-DISABLED"
```

### 4.3 Disable Smart Connections
```bash
# Example:
mv "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.obsidian/plugins/smart-connections" \
   "/Users/warrenghaad/Obsidian Vaults/Obsidian - Main Vault/.obsidian/plugins/smart-connections-DISABLED"
```

---

## PHASE 5: FIX GIT IN CLOUD LOCATIONS

### 5.1 Remove .git from cloud-synced folders
For each .git folder found in iCloud/Google Drive (from step 2.4):
```bash
# Archive first
zip -r ~/OBSIDIAN_QUARANTINE_2026-09-25/git-folder-[name].zip [path-to-.git]

# Then remove
rm -rf [path-to-.git]
```

**WARNING:** Only remove .git from CLOUD-SYNCED locations, not from your actual development repos in ~/Documents or ~/Projects.

---

## PHASE 6: FIX CLAUDE DESKTOP CONFIG

### 6.1 Check current config
```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

### 6.2 Replace with clean config
```bash
# Option A: Use the example from geometric-civilizations
cp ~/Documents/geometric-civilizations/claude_desktop_config.example.json \
   ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Option B: Create minimal config manually
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

### 6.3 Restart Claude Desktop
```bash
osascript -e 'quit app "Claude"'
sleep 2
open -a Claude
```

---

## PHASE 7: VERIFICATION

### 7.1 Wait 24 hours
Do not open Obsidian. Do not re-enable cloud sync yet.

### 7.2 Check for file movement
```bash
# Look for recently modified files
find ~ -type f -mmin -60 2>/dev/null | grep -i obsidian
```

### 7.3 Verify Claude Desktop
Open Claude Desktop - confirm "Obsidian Vault" environment is gone.

---

## PHASE 8: SAFE RE-ENABLE (After 24 hours)

### 8.1 Re-enable Google Drive
But keep these folders OUT of sync:
- Any folder containing `.obsidian`
- Any folder containing `.git`
- The quarantine folder

### 8.2 Open Obsidian (carefully)
1. Open Obsidian
2. Immediately go to Settings → Community Plugins
3. Verify obsidian-git is NOT in the list
4. Verify Smart Connections is NOT in the list
5. Close Settings

### 8.3 If you need git versioning for notes
Use a SEPARATE tool (like Git command line) manually, not obsidian-git.
Keep the repo LOCAL, not in cloud-synced folders.

---

## KNOWN PROBLEM LOCATIONS (from your search)

### High-Risk Folders Found:
| Location | Issue |
|----------|-------|
| `Obsidian Vaults/Obsidian - Main Vault/` | Main vault with .smart-env indexing everything |
| `EUCLID_STUDIO/00_Reconciliation/` | Has BOTH .obsidian AND .git |
| Multiple `obsidian-canon-reconciler` folders | Duplicated many times |
| Multiple `obsidian_euclid_template_pack` versions | v2, v3, v4, v5 scattered |
| `GIT<>OBSIDIAN VAULT` folder | Explicit git-obsidian connection |
| `ZIPS_obsidian <>vault system` | May contain more connections |

### Files Indexed by .smart-env (partial list):
- mesopotamia-backend
- geometric-civilizations  
- StudioOS_Music_Local
- Curriculum_Codex
- Harmony-Tutor
- And thousands more

---

## DO NOT

- **DO NOT** delete anything without archiving first
- **DO NOT** re-enable obsidian-git without understanding why files moved
- **DO NOT** point Claude Desktop at any folder containing `.obsidian`
- **DO NOT** put git repos inside cloud-synced folders

---

## RECOVERY

If something goes wrong, your archives are in:
```
~/OBSIDIAN_QUARANTINE_2026-09-25/
```

Existing backup:
```
Obsidian - Main Vault_archive.tar.gz (4.3GB)
```

---

## SUMMARY

The root cause is:
1. **Smart Connections** indexed your entire project ecosystem
2. **obsidian-git** synced those indexes to git
3. **Google Drive** synced those git changes across devices
4. **Claude Desktop** was pointed at an Obsidian vault, making it worse

The fix is:
1. Stop all sync
2. Archive everything
3. Remove the indexing (.smart-env) and sync (obsidian-git) components
4. Fix Claude Desktop config
5. Never put .obsidian and .git together in cloud-synced folders

---

*Document created: 2026-09-25*
*Location: geometric-civilizations/OBSIDIAN_COMPLETE_ISOLATION_PLAN.md*
