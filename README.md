# Light Code

A lightweight, VS Code–inspired desktop code editor written in Python, built with PyQt6 and QScintilla.

Light Code pairs a fast, native-feeling editing surface with a dockable file explorer, a tabbed editing area, and slide-out side panels for Git, an AI agent, and a terminal — all wrapped in a dark, GitHub-style theme.

## ⚠️ Currently in Progress
This project is under active development and doesn't have many features yet. Most features are incomplete and it may crash. Feel free to contribute or report issues 🙂.

## 🚀 Current Features

- **Tabbed code editor** — QScintilla-powered editor with line numbers, auto-completion, a custom caret, and a dark colour scheme.
- **File explorer** — VS Code/Zed-style tree view for browsing and opening folders, with new file/folder actions
- **Dockable side panels** — toggleable left dock (Explorer / Git) and right dock (AI Agent / Terminal).
- **Run Python files** — Run the active python file in background (thinking for more language support)
- **Full menu bar** — File, Edit, View, Build, Settings, About, and Help menus with standard shortcuts (New, Open, Save, Rename, Undo/Redo, Cut/Copy/Paste, Find, Replace, Go to Line, Zoom, panel toggles, and more)

## 🛠️ Installation

### Requirements
- Python 3.10+
- [PyQt6](https://pypi.org/project/PyQt6/)
- [PyQt6-QScintilla](https://pypi.org/project/PyQt6-QScintilla/)

# Prerequisites
Install dependencies manually:
```bash
pip install PyQt6 PyQt6-QScintilla
```
or with `uv`:
```bash
uv sync
```

### Setup
Clone the repository and install the dependencies:

```bash
git clone https://github.com/rony881/Light-Code.git
cd Light-Code
```

Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
Run the application
```bash
python src/light_code
```

(equivalently, `cd` into `light_code/` and run `python __main__.py` or `python .`)


## 🤝 Contributing

Contributions are welcome!
