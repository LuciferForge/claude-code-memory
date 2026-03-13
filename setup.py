#!/usr/bin/env python3
"""
claude-code-memory setup — creates a persistent memory system for Claude Code.

Usage:
    python3 setup.py                    # Interactive setup
    python3 setup.py --project /path    # Set up for specific project
    python3 setup.py --global-only      # Only set up global CLAUDE.md
"""

import argparse
import os
import shutil
import sys
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"
CLAUDE_HOME = Path.home() / ".claude"


def copy_template(src, dst, overwrite=False):
    """Copy a template file, skip if exists unless overwrite."""
    dst = Path(dst)
    if dst.exists() and not overwrite:
        print(f"  SKIP {dst} (already exists, use --force to overwrite)")
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"  CREATED {dst}")
    return True


def setup_global():
    """Set up global CLAUDE.md."""
    print("\n--- Global Setup ---")
    global_claude = CLAUDE_HOME / "CLAUDE.md"

    if global_claude.exists():
        print(f"  {global_claude} already exists.")
        print("  To use the template, back up your current file and run with --force")
    else:
        copy_template(TEMPLATES_DIR / "CLAUDE.md", global_claude)
        print("  Edit ~/.claude/CLAUDE.md to customize your instructions.")


def get_project_key(project_path):
    """Generate the Claude Code project key from a path."""
    # Claude Code uses the absolute path with / replaced by -
    # e.g., /Users/alice/myproject -> -Users-alice-myproject
    return str(project_path).replace("/", "-").replace("\\", "-")


def setup_project(project_path, force=False):
    """Set up memory system for a project."""
    project_path = Path(project_path).resolve()
    if not project_path.is_dir():
        print(f"Error: {project_path} is not a directory", file=sys.stderr)
        sys.exit(1)

    project_key = get_project_key(project_path)
    memory_dir = CLAUDE_HOME / "projects" / project_key / "memory"

    print(f"\n--- Project Setup: {project_path} ---")
    print(f"  Memory dir: {memory_dir}")

    # Project CLAUDE.md (in the project directory itself)
    project_claude = project_path / "CLAUDE.md"
    if not project_claude.exists():
        copy_template(TEMPLATES_DIR / "project-CLAUDE.md", project_claude, force)

    # MEMORY.md index
    copy_template(TEMPLATES_DIR / "MEMORY.md", memory_dir / "MEMORY.md", force)

    # Memory topic templates
    templates = ["user_profile.md", "feedback_style.md", "project_overview.md", "reference_links.md"]
    for t in templates:
        src = TEMPLATES_DIR / "memory" / t
        if src.exists():
            copy_template(src, memory_dir / t, force)

    print(f"\n  Memory system ready at {memory_dir}")
    print("  Start Claude Code in your project directory — it will auto-detect the memory.")


def main():
    parser = argparse.ArgumentParser(description="Set up Claude Code memory system")
    parser.add_argument("--project", default=".", help="Project directory (default: current)")
    parser.add_argument("--global-only", action="store_true", help="Only set up global CLAUDE.md")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    print("Claude Code Memory Setup")
    print("=" * 40)

    setup_global()

    if not args.global_only:
        setup_project(args.project, args.force)

    print("\nDone. Start a new Claude Code session to use your memory system.")


if __name__ == "__main__":
    main()
