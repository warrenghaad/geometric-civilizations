# Geometric Civilizations - Obsidian Vault

This repository is configured as an Obsidian vault for managing the Geometric Civilizations curriculum materials.

## Dual Vault Setup: Local + Remote

This vault is designed to work seamlessly both locally and remotely through Git synchronization.

### Local Vault
- Open this repository folder directly in Obsidian on your computer
- All your notes, configurations, and settings are stored here
- Make edits, create new notes, and organize your curriculum materials

### Remote Vault (via Git)
- The vault is version-controlled using Git
- Push your changes to GitHub to keep a remote backup
- Pull changes from GitHub to sync across multiple devices
- Collaborate with others by sharing the repository

## What's Synced vs. What's Local

### Synced to Git (Shared Across Devices)
- `.obsidian/app.json` - Application settings
- `.obsidian/appearance.json` - Theme and appearance preferences
- `.obsidian/core-plugins.json` - Core plugin configurations
- `.obsidian/community-plugins.json` - Community plugin list
- `.obsidian/hotkeys.json` - Keyboard shortcuts
- All your markdown notes and curriculum content
- Scripts and automation tools

### Local Only (Not Synced)
- `.obsidian/workspace.json` - Current tab layout and open files
- `.obsidian/workspace-mobile.json` - Mobile workspace layout
- `.obsidian/cache` - Cache directory
- `.DS_Store` - macOS system files

This separation ensures that your personal workspace layout stays local while sharing vault configuration and content with others or across your devices.

## Getting Started

1. **Install Obsidian**: Download from [obsidian.md](https://obsidian.md)

2. **Open this vault**:
   - Click "Open folder as vault"
   - Navigate to this repository folder
   - Select it to open

3. **Start working**:
   - Browse the curriculum materials
   - Create new notes
   - Link concepts together

4. **Sync your changes**:
   ```bash
   git add .
   git commit -m "Your descriptive message"
   git push
   ```

5. **Pull changes from remote**:
   ```bash
   git pull
   ```

## Curriculum Content

This vault contains materials for the **Geometric Civilizations** curriculum:

- **MESOPOTAMIAN_CURRICULUM_MAPPING_FOR_PERPLEXITY.md**: Comprehensive curriculum guide
- **CURRICULUM_SYSTEM_ORGANIZED/**: Organized curriculum pipelines
  - `01_ETEXTBOOK_PIPELINE/`: E-textbook generation system
  - `02_VISUAL_ASSETS_PIPELINE/`: Visual assets processing

## Automation Scripts

- **script_cross_reference.py**: Python script cross-reference system
- **shell_script_manager.sh**: Shell script management utilities

## Tips for Using This Vault

1. **Use Git for Version Control**: Regular commits help track changes to your curriculum
2. **Branch for Experiments**: Create Git branches to try new curriculum structures
3. **Link Your Notes**: Use `[[wikilinks]]` to connect related concepts
4. **Tag Your Content**: Use `#tags` to categorize and find content
5. **Use Search**: Obsidian's search is powerful - use it to find information quickly

## Troubleshooting

### Workspace Not Syncing
This is intentional! Your workspace layout (open tabs, sidebar state) is kept local so each device can have its own layout.

### Merge Conflicts
If you edit the vault on multiple devices:
1. Always `git pull` before making changes
2. Commit and push frequently
3. If conflicts occur, resolve them in your text editor and commit

### Missing Plugins
If community plugins don't load:
1. Check `.obsidian/community-plugins.json`
2. Ensure plugins are installed in `.obsidian/plugins/`
3. Some plugins may need manual installation

## Contributing

When contributing to this curriculum:
1. Create a feature branch
2. Make your changes
3. Test in Obsidian
4. Commit with clear messages
5. Push and create a pull request

---

**Happy note-taking and curriculum building!**
