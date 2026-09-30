"""Beginner-friendly repository health checker.

This app checks whether a project includes the basic files that make a
repository easier to understand and use:
- README.md
- tests folder
- requirements.txt
"""

from __future__ import annotations

import argparse
from pathlib import Path


REQUIRED_ITEMS = (
    ("README.md", "README.md"),
    ("tests folder", "tests"),
    ("requirements.txt", "requirements.txt"),
)


def check_repository(path):
    """Return the names of found and missing project health items."""
    repo = Path(path)
    found = []
    missing = []

    for label, item_name in REQUIRED_ITEMS:
        item = repo / item_name
        if item.exists():
            found.append(label)
        else:
            missing.append(label)

    return found, missing


def print_health_report(path):
    """Print a beginner-friendly repository health report."""
    repo = Path(path).resolve()
    found, missing = check_repository(repo)

    print("=" * 40)
    print("Repository Health Check")
    print("=" * 40)
    print(f"Checking: {repo}\n")

    if found:
        print("Good signs:")
        for item in found:
            print(f"✅ {item} found")

    if missing:
        print("\nNeeds attention:")
        for item in missing:
            print(f"⚠️  {item} missing")

    if not missing:
        print("\nOverall status: Healthy")
    else:
        print("\nOverall status: Needs improvement")

    print("=" * 40)
    return 0 if not missing else 1


def main():
    """Run the app from the command line."""
    parser = argparse.ArgumentParser(
        description="Check whether a repository has a README, tests folder, and requirements.txt."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repository you want to check (default: current folder).",
    )
    args = parser.parse_args()

    return print_health_report(args.path)


if __name__ == "__main__":
    raise SystemExit(main())
