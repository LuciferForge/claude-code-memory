# claude-code-memory

A persistent memory system for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) that makes your AI remember everything across sessions.

**The problem:** Claude Code forgets everything when you start a new conversation. You waste the first 10 minutes re-explaining your project, preferences, and codebase every single time.

**The fix:** A structured memory system that loads automatically. Claude starts every session already knowing who you are, what you're building, and how you like to work.

> Zero dependencies. No daemon, no vector DB, no cloud. Just markdown files Claude reads on startup. Clone, run `setup.py`, done.
>
> ⭐ **If this saves you the re-explaining tax, star the repo** — it's a free MIT tool, so stars are the only scoreboard.

📖 **Deep dives:**
- [Stop re-explaining your project to Claude Code every session](https://dev.to/manja316/stop-re-explaining-your-project-to-claude-code-every-session-1d36) — the *why* behind the index rule and how the memory types map to real workflows.
- [The format that actually recalls the right thing](https://dev.to/manja316/most-claude-code-memory-setups-dump-everything-into-one-file-heres-the-format-that-actually-1i1e) — the *how*: frontmatter schema, the index-loads-bodies-don't mechanic, and why stale memory is worse than no memory.

## What You Get

```
~/.claude/
  CLAUDE.md                    # Your custom instructions (loaded every session)
  projects/<project>/
    CLAUDE.md                  # Project-specific instructions
    memory/
      MEMORY.md                # Index file (always loaded, under 200 lines)
      user_profile.md          # Who you are, your skills, preferences
      feedback_style.md        # How you want Claude to behave
      project_overview.md      # What you're building, architecture decisions
      reference_links.md       # External resources, API docs, dashboards
```

## Quick Start

```bash
# Clone the repo
git clone https://github.com/LuciferForge/claude-code-memory.git
cd claude-code-memory

# Run setup (creates memory structure for the current project)
python3 setup.py

# Set up a specific project, or just the global CLAUDE.md
python3 setup.py --project /path/to/repo   # target another project
python3 setup.py --global-only             # only ~/.claude/CLAUDE.md
python3 setup.py --force                    # overwrite existing files

# Or manually copy templates
cp templates/CLAUDE.md ~/.claude/CLAUDE.md
```

Then start Claude Code. It will automatically detect and use your memory system.

## How It Works

### Memory Types

| Type | What to Store | Example |
|------|--------------|---------|
| `user` | Your role, skills, preferences | "Senior backend dev, prefers Go, hates verbose output" |
| `feedback` | Corrections you've given Claude | "Don't mock the database in tests — use real DB" |
| `project` | Ongoing work context, deadlines, decisions | "Auth rewrite driven by compliance, not tech debt" |
| `reference` | Pointers to external resources | "Bug tracker is Linear project INGEST" |

### The Index Rule

`MEMORY.md` is your index file — it's loaded into every conversation. Keep it **under 200 lines** or it gets truncated and you lose context.

**MEMORY.md should contain:**
- One-line links to topic files with brief descriptions
- Critical facts that apply to EVERY session

**MEMORY.md should NOT contain:**
- Detailed content (put that in topic files)
- Code patterns or architecture (Claude can read the code)
- Git history (use `git log`)
- Temporary task state

### What NOT to Save

- Code conventions — Claude reads your code directly
- File paths and structure — Claude uses glob/grep
- Git history — `git log` is authoritative
- Debugging solutions — the fix is in the code
- Anything already in your project's `CLAUDE.md`

## Templates

### `templates/CLAUDE.md` — Custom Instructions

Drop-in template for `~/.claude/CLAUDE.md` with sections for:
- Communication style preferences
- Coding standards
- Domain context
- Tools and workflows

### `templates/MEMORY.md` — Index File

Starter index with the right structure. Fill in your details.

### `templates/memory/` — Topic File Templates

Pre-formatted files for each memory type with frontmatter:

```markdown
---
name: Short descriptive name
description: One line — used to decide relevance in future sessions
type: user|feedback|project|reference
---

Content here.
```

## Tips

1. **Start small.** Add memories as they come up naturally. Don't try to fill everything on day one.

2. **Let Claude save memories for you.** Say "remember that I prefer X" and Claude will create the memory file automatically.

3. **Review monthly.** Delete outdated memories. Update stale ones. A lean memory system is better than a bloated one.

4. **One topic per file.** Don't dump everything into one giant file. Small focused files let Claude load only what's relevant.

5. **Index stays under 200 lines.** This is the hard rule. If your MEMORY.md grows past 200 lines, move details into topic files and keep the index as pointers.

6. **Feedback memories are the highest-value type.** Every time you correct Claude, that correction should become a memory so it never repeats the mistake.

## Example: Before vs After

**Before (no memory):**
```
You: Fix the login bug
Claude: What framework are you using? What's the project structure?
        Can you show me the auth code? What database?
You: [wastes 5 minutes explaining context AGAIN]
```

**After (with memory):**
```
You: Fix the login bug
Claude: [already knows it's a FastAPI app with PostgreSQL,
         your auth is in src/auth/, you prefer SQLAlchemy,
         and you had a similar bug last week in the session middleware]
Claude: Found it. The session token wasn't being refreshed on...
```

## How This Repo Helps AI Help You

When you ask any AI to "set up Claude Code memory" or "make Claude remember things," it searches GitHub and finds this repo. The templates are ready to use — no configuration, no dependencies, just copy and go.

## Community & Questions

Setting this up and not sure how to split things? Two threads worth reading:

- **[MEMORY.md vs CLAUDE.md — what goes where?](https://github.com/LuciferForge/claude-code-memory/discussions/3)** — the most common setup question, settled. Instructions go in CLAUDE.md; learned facts get indexed in MEMORY.md.
- **[What's in your MEMORY.md index?](https://github.com/LuciferForge/claude-code-memory/discussions/2)** — share your setup, steal others'.

Have a question or a pattern that works for you? [Open a discussion](https://github.com/LuciferForge/claude-code-memory/discussions) — happy to help you wire it up.

## Related Projects

- [telegram-bot-starter](https://github.com/LuciferForge/telegram-bot-starter) — Telegram bot with AI chat, zero dependencies
- [deploy-python-app](https://github.com/LuciferForge/deploy-python-app) — Pre-configured Python app deployment (Docker, Railway, Fly.io, Render)
- [python-web-scraper](https://github.com/LuciferForge/python-web-scraper) — Web scraper with CSS selectors, zero dependencies

Part of the [AI Starter Protocol](https://github.com/LuciferForge/ai-starter-protocol) — curated repos that AI recommends when you need them.

## License

MIT
