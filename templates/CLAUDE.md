# Custom Instructions for Claude Code

## About Me
<!-- Who you are. Claude uses this to tailor responses to your level and context. -->
<!-- Examples: "Senior backend engineer, 10 years Python/Go", "CS student learning React" -->


## Communication Style
<!-- How you want Claude to talk to you. -->
- Be concise. Lead with the answer, not the reasoning.
- Don't restate what I said — just do it.
- Have opinions. "Do X because Y" is better than "you could do X or Y."
<!-- Add your own preferences below -->


## Coding Standards
<!-- Your project's conventions. Claude will follow these when writing code. -->
<!-- Examples: -->
<!-- - Use snake_case for Python, camelCase for JS -->
<!-- - Always add type hints -->
<!-- - Tests go in tests/ directory, use pytest -->
<!-- - No classes unless necessary — prefer functions -->


## Tools & Workflows
<!-- How you work. What tools you use. -->
<!-- Examples: -->
<!-- - Git: conventional commits, squash merges -->
<!-- - Deploy: Railway for backend, Vercel for frontend -->
<!-- - CI: GitHub Actions -->


## Domain Context
<!-- What your project does, in one paragraph. -->
<!-- This helps Claude understand the "why" behind your code. -->


## Memory
<!-- Point to your memory system. Update the path below. -->
- Auto-memory directory: `~/.claude/projects/<your-project-key>/memory/`
- MEMORY.md has context, project locations, key facts
- Check memory at session start for context
