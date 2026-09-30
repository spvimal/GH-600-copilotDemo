#!/usr/bin/env python3
"""A simple repository health checker for beginners.

This script looks at a folder and checks for common signs of a healthy
Git repository, such as:
- a .git folder
- a README file
- Python files in the project
- a clean Git working tree

Run it like this:
    python repo_health_check.py
    python repo_health_check.py C:/path/to/your/project
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def print_banner() -> None:
    print("=" * 48)
    print("Repository Health Check")
    print("=" * 48)
    print("This tool gives a quick overview of your project health.")
    print()


def find_python_files(project_path: Path) -> list[Path]:
    """Return Python files in the project, ignoring virtual environments."""
    python_files = []
    for item in project_path.rglob("*.py"):
        parts = item.parts
        if ".venv" in parts or "venv" in parts or "__pycache__" in parts:
            continue
        python_files.append(item)
    return python_files


def check_git_status(project_path: Path) -> tuple[bool, str]:
    """Return (is_clean, details)."""
    git_status = subprocess.run(
        ["git", "-C", str(project_path), "status", "--short"],
        capture_output=True,
        text=True,
        check=False,
    )

    if git_status.returncode != 0:
        return False, "Git status could not be checked."

    output = git_status.stdout.strip()
    if not output:
        return True, "Git working tree is clean."

    lines = output.splitlines()[:5]
    preview = "\n".join(lines)
    return False, f"There are uncommitted changes:\n{preview}"


def check_repository(project_path: Path) -> tuple[list[str], list[str]]:
    """Return (good_checks, warnings)."""
    good_checks: list[str] = []
    warnings: list[str] = []

    if project_path.exists():
        good_checks.append("Project folder exists.")
    else:
        warnings.append("The folder does not exist.")

    if (project_path / ".git").exists():
        good_checks.append("Git repository found.")
    else:
        warnings.append("No .git folder found. This may not be a Git repo.")

    if (project_path / "README.md").exists():
        good_checks.append("README.md is present.")
    else:
        warnings.append("README.md is missing.")

    python_files = find_python_files(project_path)
    if python_files:
        good_checks.append(f"Found {len(python_files)} Python file(s).")
    else:
        warnings.append("No Python files were found.")

    if project_path.is_dir():
        git_ok, git_message = check_git_status(project_path)
        if git_ok:
            good_checks.append(git_message)
        else:
            warnings.append(git_message)

    return good_checks, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a repository for common beginner-friendly health signs."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repository to check. Default is current folder.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_path = Path(args.path).expanduser().resolve()

    print_banner()
    print(f"Checking: {project_path}")
    print()

    if not project_path.exists():
        print("This folder does not exist.")
        print("Please choose a real project folder and try again.")
        return 1

    good_checks, warnings = check_repository(project_path)

    print("Good signs:")
    if good_checks:
        for item in good_checks:
            print(f"  ✅ {item}")
    else:
        print("  No positive checks found.")

    print()
    print("Things to improve:")
    if warnings:
        for item in warnings:
            print(f"  ⚠️  {item}")
    else:
        print("  Everything looks good so far!")

    print()
    if warnings:
        print("Overall status: Needs attention")
        return 1

    print("Overall status: Healthy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
