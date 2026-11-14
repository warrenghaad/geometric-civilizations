# Verification & Reconciliation Protocol

**Purpose:** Don't assume cleanup worked. Verify each step independently.

---

## VERIFICATION PHILOSOPHY

Every cleanup step must be **verified by a separate check**, not by the success of the command itself.

| Bad | Good |
|-----|------|
| "I ran `rm -rf .smart-env`" ✗ | "I ran `find ~ -name .smart-env` and got 0 results" ✓ |
| "I disabled the plugin" ✗ | "I checked the plugins folder and obsidian-git is renamed" ✓ |
| "I fixed the config" ✗ | "I ran `cat` on the config and verified no obsidian paths" ✓ |

---

## PHASE-BY-PHASE VERIFICATION

### VERIFY: Phase 2 (Emergency Stop)

**Check 1: Obsidian not running**
```bash
# MUST return nothing
ps aux | grep -i "[O]bsidian"
```
**Expected:** Empty output  
**If fails:** Run `pkill -9 -f Obsidian` again

**Check 2: Cloud sync paused**
```bash
# MUST return nothing
ps aux | grep -i "[g]oogle\|[b]ird\|[d]ropbox"
```
**Expected:** Empty or only system processes  
**If fails:** Manually pause from menu bar

---

### VERIFY: Phase 3 (Inventory)

**Check 1: Inventory files exist**
```bash
ls -la ~/OBSIDIAN_INVENTORY_*/
```
**Expected:** See vaults.txt, smart_env.txt, etc.  
**If fails:** Re-run inventory commands

**Check 2: Inventory files have content**
```bash
wc -l ~/OBSIDIAN_INVENTORY_*/*.txt
```
**Expected:** Non-zero line counts  
**If fails:** Paths may be wrong, re-run find commands

---

### VERIFY: Phase 4 (Backups)

**Check 1: Quarantine folder exists**
```bash
ls -la ~/LOCAL_OBSIDIAN_QUARANTINE/ 2>/dev/null || ls -la /Users/warrenghaad/LOCAL_OBSIDIAN_QUARANTINE/
```
**Expected:** Folder exists with .zip files  
**If fails:** Create folder and re-run backups

**Check 2: Backup files have size**
```bash
du -sh ~/LOCAL_OBSIDIAN_QUARANTINE/*.zip
```
**Expected:** Each file has non-zero size  
**If fails:** Re-run zip commands

**Check 3: Backups are valid**
```bash
# Test one backup
unzip -t ~/LOCAL_OBSIDIAN_QUARANTINE/main-vault-backup.zip | tail -5
```
**Expected:** "No errors detected"  
**If fails:** Re-create corrupted backup

---

### VERIFY: Phase 5 (Disable Sync)

**Check 1: obsidian-git disabled in ALL vaults**
```bash
# Should return 0 or only show -DISABLED folders
find ~ -type d -name "obsidian-git" 2>/dev/null | grep -v DISABLED
```
**Expected:** Empty output  
**If fails:** Rename remaining obsidian-git folders

**Check 2: Smart Connections disabled in ALL vaults**
```bash
find ~ -type d -name "smart-connections" 2>/dev/null | grep -v DISABLED
```
**Expected:** Empty output  
**If fails:** Rename remaining folders

---

### VERIFY: Phase 6 (Remove Indexing)

**Check 1: No .smart-env folders exist**
```bash
find ~ -name ".smart-env" -type d 2>/dev/null
```
**Expected:** Empty output  
**If fails:** Remove remaining .smart-env folders

**Check 2: Double-check cloud locations**
```bash
find ~/Library/Mobile\ Documents ~/Library/CloudStorage -name ".smart-env" -type d 2>/dev/null
```
**Expected:** Empty output  
**If fails:** Remove from cloud locations

---

### VERIFY: Phase 7 (Cloud Storage)

**Check 1: No .git in iCloud**
```bash
find ~/Library/Mobile\ Documents -name ".git" -type d 2>/dev/null
```
**Expected:** Empty output  
**If fails:** Remove remaining .git folders

**Check 2: No .git in Google Drive**
```bash
find ~/Library/CloudStorage -name ".git" -type d 2>/dev/null
```
**Expected:** Empty output  
**If fails:** Remove remaining .git folders

**Check 3: No .obsidian in cloud with .git siblings**
```bash
# Check for the dangerous combination
for obs in $(find ~/Library/Mobile\ Documents ~/Library/CloudStorage -name ".obsidian" -type d 2>/dev/null); do
    parent=$(dirname "$obs")
    if [ -d "$parent/.git" ]; then
        echo "DANGER: $parent has both .obsidian and .git"
    fi
done
```
**Expected:** No output  
**If fails:** Remove .git from those locations

---

### VERIFY: Phase 8 (Claude Desktop)

**Check 1: Config file exists and is valid JSON**
```bash
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json | python3 -m json.tool > /dev/null && echo "Valid JSON"
```
**Expected:** "Valid JSON"  
**If fails:** Re-create config file

**Check 2: No obsidian paths in config**
```bash
grep -i obsidian ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
**Expected:** Empty output (no matches)  
**If fails:** Edit config to remove obsidian paths

**Check 3: Config points to safe paths**
```bash
grep -o '"/.*/[^"]*"' ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
**Expected:** Only project folders, no vault folders  
**If fails:** Update paths in config

**Check 4: Claude Desktop actually restarted**
```bash
# Should show Claude process started recently
ps aux | grep -i "[C]laude" | grep -v grep
```
**Expected:** Claude process running  
**If fails:** Open Claude Desktop manually

---

### VERIFY: Phase 9 (24-Hour Check)

**Check 1: No new .smart-env appeared**
```bash
find ~ -name ".smart-env" -type d -mtime -1 2>/dev/null
```
**Expected:** Empty output  
**If fails:** Something recreated it - investigate

**Check 2: No new .git in cloud**
```bash
find ~/Library/Mobile\ Documents ~/Library/CloudStorage -name ".git" -type d -mtime -1 2>/dev/null
```
**Expected:** Empty output  
**If fails:** Something recreated it - investigate

**Check 3: No obsidian file changes in last 24h**
```bash
find ~ -iname "*obsidian*" -type f -mtime -1 2>/dev/null | wc -l
```
**Expected:** 0 or very low number (only your manual changes)  
**If fails:** Something is still syncing - investigate

---

## FULL RECONCILIATION SCRIPT

Run this AFTER completing all phases:

```bash
#!/bin/bash
# FULL VERIFICATION SCRIPT
# Save as: ~/verify_cleanup.sh
# Run with: bash ~/verify_cleanup.sh

echo "========================================"
echo "OBSIDIAN CLEANUP VERIFICATION"
echo "========================================"
FAILURES=0

# Check 1: Obsidian not running
echo -n "1. Obsidian not running: "
if ps aux | grep -i "[O]bsidian" > /dev/null; then
    echo "FAIL - Obsidian is running"
    ((FAILURES++))
else
    echo "PASS"
fi

# Check 2: No .smart-env folders
echo -n "2. No .smart-env folders: "
COUNT=$(find ~ -name ".smart-env" -type d 2>/dev/null | wc -l)
if [ "$COUNT" -gt 0 ]; then
    echo "FAIL - Found $COUNT .smart-env folders"
    ((FAILURES++))
else
    echo "PASS"
fi

# Check 3: obsidian-git disabled
echo -n "3. obsidian-git disabled: "
COUNT=$(find ~ -type d -name "obsidian-git" 2>/dev/null | grep -v DISABLED | wc -l)
if [ "$COUNT" -gt 0 ]; then
    echo "FAIL - Found $COUNT active obsidian-git plugins"
    ((FAILURES++))
else
    echo "PASS"
fi

# Check 4: No .git in iCloud
echo -n "4. No .git in iCloud: "
COUNT=$(find ~/Library/Mobile\ Documents -name ".git" -type d 2>/dev/null | wc -l)
if [ "$COUNT" -gt 0 ]; then
    echo "FAIL - Found $COUNT .git folders in iCloud"
    ((FAILURES++))
else
    echo "PASS"
fi

# Check 5: No .git in Google Drive
echo -n "5. No .git in Google Drive: "
COUNT=$(find ~/Library/CloudStorage -name ".git" -type d 2>/dev/null | wc -l)
if [ "$COUNT" -gt 0 ]; then
    echo "FAIL - Found $COUNT .git folders in Google Drive"
    ((FAILURES++))
else
    echo "PASS"
fi

# Check 6: Claude config clean
echo -n "6. Claude config has no obsidian: "
if grep -qi obsidian ~/Library/Application\ Support/Claude/claude_desktop_config.json 2>/dev/null; then
    echo "FAIL - Config contains obsidian paths"
    ((FAILURES++))
else
    echo "PASS"
fi

# Check 7: Backups exist
echo -n "7. Backups exist: "
if ls ~/LOCAL_OBSIDIAN_QUARANTINE/*.zip 2>/dev/null | head -1 > /dev/null; then
    echo "PASS"
else
    echo "FAIL - No backup files found"
    ((FAILURES++))
fi

# Check 8: No dangerous .obsidian + .git combinations
echo -n "8. No .obsidian + .git combos in cloud: "
DANGER=0
for obs in $(find ~/Library/Mobile\ Documents ~/Library/CloudStorage -name ".obsidian" -type d 2>/dev/null); do
    parent=$(dirname "$obs")
    if [ -d "$parent/.git" ]; then
        ((DANGER++))
    fi
done
if [ "$DANGER" -gt 0 ]; then
    echo "FAIL - Found $DANGER dangerous combinations"
    ((FAILURES++))
else
    echo "PASS"
fi

echo "========================================"
if [ "$FAILURES" -eq 0 ]; then
    echo "ALL CHECKS PASSED"
    echo "Cleanup verified successful."
else
    echo "FAILURES: $FAILURES"
    echo "Review failed checks and re-run cleanup steps."
fi
echo "========================================"
```

---

## AGENT VERIFICATION PROTOCOL

When an agent claims cleanup is complete, require these responses:

### Question 1: Proof of Removal
**Ask:** "Show me the output of `find ~ -name '.smart-env' -type d`"  
**Required answer:** Empty output or "0 results"  
**Not acceptable:** "I removed them" / "Done" / "Completed"

### Question 2: Proof of Backup
**Ask:** "Show me `ls -la` of the quarantine folder"  
**Required answer:** List of .zip files with sizes  
**Not acceptable:** "Backups created" / "Archived"

### Question 3: Proof of Config Fix
**Ask:** "Show me the contents of claude_desktop_config.json"  
**Required answer:** Actual JSON with no obsidian paths  
**Not acceptable:** "Config updated" / "Fixed"

### Question 4: Proof of No Recurrence
**Ask:** "Show me files modified in the last hour with obsidian in the name"  
**Required answer:** Empty or only files you intentionally touched  
**Not acceptable:** "No changes" / "Stable"

---

## RECONCILIATION CHECKLIST

Before declaring success, verify:

| Step | Verification Command | Expected Result | Actual Result | Pass? |
|------|---------------------|-----------------|---------------|-------|
| Obsidian stopped | `ps aux \| grep -i obsidian` | Nothing | | |
| .smart-env removed | `find ~ -name .smart-env` | Nothing | | |
| obsidian-git disabled | `find ~ -name obsidian-git \| grep -v DISABLED` | Nothing | | |
| .git removed from iCloud | `find ~/Library/Mobile\ Documents -name .git` | Nothing | | |
| .git removed from GDrive | `find ~/Library/CloudStorage -name .git` | Nothing | | |
| Claude config clean | `grep -i obsidian [config]` | Nothing | | |
| Backups exist | `ls ~/LOCAL_OBSIDIAN_QUARANTINE/*.zip` | Files listed | | |
| 24h no changes | `find ~ -iname "*obsidian*" -mtime -1` | Nothing/minimal | | |

---

## IF VERIFICATION FAILS

### Failure: .smart-env still exists
1. Check what process created it: `ls -la [path]/.smart-env`
2. Look at modification time: recently = still syncing
3. Kill Obsidian again: `pkill -9 -f Obsidian`
4. Remove again: `rm -rf [path]/.smart-env`
5. Re-verify

### Failure: .git in cloud
1. Check if backup exists in quarantine
2. If not, backup first: `zip -r backup.zip [path]/.git`
3. Remove: `rm -rf [path]/.git`
4. Re-verify

### Failure: Plugin not disabled
1. Manually rename: `mv [path]/obsidian-git [path]/obsidian-git-DISABLED`
2. Re-verify

### Failure: Claude config wrong
1. Delete config: `rm ~/Library/Application\ Support/Claude/claude_desktop_config.json`
2. Recreate clean config
3. Restart Claude Desktop
4. Re-verify

### Failure: Files still changing
1. Something is recreating files
2. Check for running processes: `ps aux | grep -i obsidian\|sync\|git`
3. Check for cron jobs: `crontab -l`
4. Check for launch agents: `ls ~/Library/LaunchAgents/`
5. Kill/disable the source
6. Re-verify after 1 hour

---

*Verification Protocol Created: 2026-09-25*
