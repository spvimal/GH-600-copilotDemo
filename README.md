# Repository Health Check App

## Project purpose

This project is a beginner-friendly Python app that helps you quickly review whether a repository looks well organized and ready to share.

It checks for three commonly used project basics:

- a README.md file
- a tests folder
- a requirements.txt file

These files make a project easier for others to understand, set up, and test.

## Why this project is useful

A repository is easier to use when it includes:

- clear project instructions
- a place for tests
- dependency information for running the project

This app gives a simple report so beginners can learn what a healthy repository should contain.

## Setup instructions

1. Open a terminal in the project folder.
2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

On Windows:

```bash
.venv\Scripts\activate
```

4. Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the app in the current folder:

```bash
python app.py
```

Check a different repository path:

```bash
python app.py C:/path/to/your/project
```

## Run the tests

```bash
python -m pytest -q
```

## Example output

```text
========================================
Repository Health Check
========================================
Checking: C:\path\to\project

Good signs:
✅ README.md found
✅ tests folder found
✅ requirements.txt found

Overall status: Healthy
========================================
```

## Beginner note

The app prints simple checkmarks and warnings so it is easy to understand, even if you are new to Python or project setup.
