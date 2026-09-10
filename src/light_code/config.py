# src/light_code/config.py

from pathlib import Path

# ============================================================
# Project Paths
# ============================================================

# Project root:
# LiteCode/
# ├── src/
# │   └── light_code/
# │       └── config.py
# └── ...
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Python package root:
PACKAGE_ROOT = Path(__file__).resolve().parent

# Application resources
ASSETS_PATH = PACKAGE_ROOT / "assets"
ICONS_PATH = ASSETS_PATH / "icons"


# ============================================================
# Application Window Configuration
# ============================================================

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720

WINDOW_LOGO = str(ICONS_PATH / "app-logo.png")


# ============================================================
# Application Icons
# ============================================================

# File Explorer Button
EXPLORER_ICON = str(ICONS_PATH / "file-explorer-logo.svg")

# Git Button
GIT_ICON = str(ICONS_PATH / "git-logo.svg")

# Left Panel Button
LEFT_PANEL_ICON = str(ICONS_PATH / "left-panel-logo.svg")

# AI Agent Button
AI_AGENT_ICON = str(ICONS_PATH / "ai-agent-logo.svg")

# Right Panel Button
RIGHT_PANEL_ICON = str(ICONS_PATH / "right-panel-logo.svg")

# Output Panel Button
OUTPUT_ICON = str(ICONS_PATH / "output-logo.svg")

# File Plus Button
FILE_PLUS_ICON = str(ICONS_PATH / "file-plus-logo.svg")

# Folder Plus Button
FOLDER_PLUS_ICON = str(ICONS_PATH / "folder-plus-logo.svg")


# ============================================================
# Application Styles
# ============================================================

STYLE_SHEET_FILE = str(PACKAGE_ROOT / "ui" / "themes" / "style.qss")
