# Troubleshooting Guide

Common issues and solutions for the Geometric Civilizations system.

## Installation Issues

### "npm: command not found"
**Problem**: npm (Node Package Manager) is not installed or not in PATH.

**Solution**:
1. Install Node.js from https://nodejs.org
2. Restart your terminal
3. Verify with: `node --version` and `npm --version`

### "npm install" fails
**Problem**: Dependency installation errors.

**Solutions**:
- Clear npm cache: `npm cache clean --force`
- Delete node_modules: `rm -rf node_modules` (or `rmdir /s node_modules` on Windows)
- Run install again: `npm install`
- Check internet connection
- Try with administrator/sudo privileges if permission errors occur

### "EACCES" or permission errors
**Problem**: npm doesn't have permission to write files.

**Solution**:
- On Mac/Linux: Use a version manager like nvm instead of system Node.js
- Don't use sudo with npm (security risk)
- Fix npm permissions: https://docs.npmjs.com/resolving-eacces-permissions-errors

## Configuration Issues

### "Cannot find config.json"
**Problem**: Configuration file doesn't exist.

**Solution**:
```bash
# Copy the example configuration
cp config.example.json config.json

# Windows users:
copy config.example.json config.json

# Then edit config.json with your settings
```

### "API key invalid" or "Unauthorized"
**Problem**: OpenAI API key is incorrect or not set.

**Solution**:
1. Get an API key from https://platform.openai.com/api-keys
2. Open config.json
3. Find the line: `"apiKey": "YOUR_API_KEY_HERE"`
4. Replace with your actual key: `"apiKey": "sk-..."`
5. Make sure there are no extra spaces
6. Save the file

### "Unexpected token in JSON"
**Problem**: config.json has invalid JSON syntax.

**Solution**:
- Check for missing commas or quotes
- Use a JSON validator: https://jsonlint.com
- Compare with config.example.json
- Common mistakes:
  - Trailing commas: `"value",}` ❌ → `"value"}` ✓
  - Missing quotes: `{key: value}` ❌ → `{"key": "value"}` ✓
  - Single quotes: `{'key': 'value'}` ❌ → `{"key": "value"}` ✓

## Bot Issues

### "Bot is disabled in config.json"
**Problem**: The bot you're trying to use is turned off.

**Solution**:
Edit config.json and set `enabled` to `true`:
```json
{
  "bots": {
    "contentGenerator": {
      "enabled": true
    }
  }
}
```

### "Cannot find module"
**Problem**: Required dependencies aren't installed.

**Solution**:
```bash
npm install
```

### "Command not found: npm run bot:content"
**Problem**: Script doesn't exist or package.json is corrupted.

**Solution**:
1. Verify package.json exists
2. Check that scripts section is intact
3. Try running directly: `node bots/content-generator/index.js --help`

### Bot generates empty or error output
**Problem**: Bot encountered an error but didn't crash.

**Solution**:
1. Check your API key is valid
2. Verify internet connection
3. Look for error messages in output
4. Run with verbose logging (if available)
5. Check API rate limits and quota

## AI Tutor Issues

### Tutor won't start
**Problem**: Error when running `npm run tutor`.

**Solution**:
```bash
# Verify the file exists
ls tutor/tutor.js

# Try running directly
node tutor/tutor.js

# Check for syntax errors
node -c tutor/tutor.js
```

### Tutor starts but doesn't respond
**Problem**: Prompt appears but nothing happens.

**Solution**:
- Make sure you're typing and pressing Enter
- Check terminal is in focus
- Try typing 'help' and pressing Enter
- Restart the tutor: Ctrl+C then `npm run tutor`

## Output Issues

### "ENOENT: no such file or directory"
**Problem**: Trying to write to non-existent directory.

**Solution**:
- Directories are created automatically by bots
- If issue persists, manually create: `mkdir -p curriculum/ancient-egypt`
- Check file path doesn't have invalid characters

### "Permission denied" when writing files
**Problem**: No permission to write to output directory.

**Solution**:
- Check directory permissions
- Don't run in system directories
- Use a directory you own (like Documents)

### Output files are empty or corrupted
**Problem**: Files created but content is wrong.

**Solution**:
1. Delete the file
2. Run the bot again
3. Check for errors during generation
4. Verify config.json settings

## Runtime Errors

### "Maximum call stack size exceeded"
**Problem**: Infinite recursion or very deep function calls.

**Solution**:
- This is usually a bug in the code
- Restart Node.js
- Report the issue with steps to reproduce

### "Out of memory"
**Problem**: Process used too much RAM.

**Solution**:
- Close other applications
- Increase Node.js memory: `node --max-old-space-size=4096 script.js`
- Process smaller batches of data

### "TypeError: Cannot read property"
**Problem**: Trying to access property of undefined/null.

**Solution**:
- This is usually a bug or missing data
- Check your input arguments
- Verify config.json is complete
- Report with error details

## Path and Directory Issues

### "Working directory" confusion
**Problem**: Commands work from one directory but not another.

**Solution**:
Always run commands from the project root:
```bash
# Navigate to project
cd /path/to/geometric-civilizations

# Verify you're in the right place
ls package.json

# Now run commands
npm run tutor
```

### Relative vs Absolute Paths
**Problem**: File not found with relative paths.

**Understanding**:
- Relative path: `curriculum/lesson.json` (from current directory)
- Absolute path: `/home/user/project/curriculum/lesson.json` (full path)

**Solution**: Use relative paths from project root, or full absolute paths.

## Version Compatibility

### "Syntax error" or "Unexpected token"
**Problem**: Code uses features not in your Node.js version.

**Solution**:
1. Check Node.js version: `node --version`
2. Upgrade if below 14.0.0
3. Download from: https://nodejs.org

### npm version issues
**Problem**: npm commands don't work as expected.

**Solution**:
Update npm: `npm install -g npm@latest`

## Performance Issues

### Bots are slow
**Causes and Solutions**:
- **API latency**: AI calls take time (normal)
- **Slow internet**: Check connection speed
- **Large output**: Generating extensive content takes longer
- **Rate limiting**: API provider may throttle requests

### High CPU usage
**Causes and Solutions**:
- **Normal during generation**: AI processing is intensive
- **Stuck process**: Kill with Ctrl+C and restart
- **Memory leak**: Restart Node.js process

## Getting More Help

### Enable Verbose Output
Add debugging to see what's happening:
```javascript
// In bot files, add before operations
console.log('Debug: Current state:', variable);
```

### Check Logs
Look for error logs:
```bash
# Check for npm errors
cat npm-debug.log

# Check for Node.js errors  
# (location varies by system)
```

### Isolate the Problem
Test components individually:
```bash
# Test Node.js
node --version

# Test npm
npm --version

# Test file reading
node -e "console.log(require('fs').readFileSync('package.json', 'utf8'))"

# Test specific bot
node bots/content-generator/index.js --help
```

### Report an Issue
If you found a bug, report it with:
1. What you tried to do
2. What you expected to happen
3. What actually happened
4. Error messages (full text)
5. Your system (OS, Node.js version)
6. Steps to reproduce

### Ask the AI Tutor
Don't forget - the AI Tutor can help!
```bash
npm run tutor
# Then type: "I'm getting an error: [paste error]"
```

## Prevention Tips

### Regular Maintenance
```bash
# Update dependencies periodically
npm update

# Clear old files
rm -rf curriculum/generated/*

# Verify configuration
node -e "console.log(JSON.parse(require('fs').readFileSync('config.json')))"
```

### Backup Your Work
```bash
# Backup curriculum content
cp -r curriculum curriculum-backup-$(date +%Y%m%d)

# Backup configuration
cp config.json config.json.backup
```

### Best Practices
1. Always run `npm install` after pulling updates
2. Keep Node.js updated (but use LTS versions)
3. Don't commit config.json (contains API key)
4. Test commands with `--help` first
5. Read error messages completely
6. Start simple, add complexity gradually

## Still Stuck?

1. **Re-read documentation**: Often the answer is there
2. **Run AI Tutor**: `npm run tutor`
3. **Start fresh**: Clone the repository again
4. **Check examples**: Look in examples/ directory
5. **Community**: Check project issues on GitHub

Remember: Every error is a learning opportunity! 🎓
