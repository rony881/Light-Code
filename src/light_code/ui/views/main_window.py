# src/ui/views/main_window.py

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QSplitter,
    QMainWindow,
    QFileDialog,
    QInputDialog,
    QMessageBox
)
from PyQt6.QtGui import QIcon

from utils.logger import logger
from ui.views.left_dock import LeftDock
from ui.views.right_dock import RightDock
from ui.views.editor_area import EditorArea
from ui.base_widgets.base_widget import BaseWidget
from services.run_code_service import run_python_file
from ui.custom_widgets.custom_menubar import CustomMenuBar
from ui.custom_widgets.custom_statusbar import CustomStatusBar
from services.file_service import read_file, rename_file, write_file
from config import STYLE_SHEET_FILE, WINDOW_HEIGHT, WINDOW_LOGO, WINDOW_WIDTH


class MainWindow(QMainWindow):
    """
    Main application window containing MenuBar, Editor,
    Left Panel, Right Panel, Down Panel etc.
    """

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        logger.info("Initializing MainWindow")
        self.setWindowTitle("Light Code")
        self.setWindowIcon(QIcon(WINDOW_LOGO))
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(self.read_style_sheet())

        # ============= Menu Bar ===============
        self.menu_bar = CustomMenuBar(parent=self)
        self.setMenuBar(self.menu_bar)

        # ============= Central Widget ============
        self.central_widget = BaseWidget()
        self.setCentralWidget(self.central_widget)

        # ==================== Splitter =======================
        # This splitter container widget would contain 3 panels-
        # left,right and the contral panel.
        self.splitter_container = QSplitter(Qt.Orientation.Horizontal)
        self.central_widget.add(self.splitter_container)

        self.LEFT_PANEL_INDEX = 0
        self.RIGHT_PANEL_INDEX = -1

        # ============= Left Panel ==============
        self.left_panel = LeftDock(parent=self)
        self.splitter_container.addWidget(self.left_panel)
        self.left_panel.explorer_file_selected_conn(self.open_file_from_explorer)
        self.left_panel.file_explorer.set_new_file_btn_conn(self.new_file)
        
        # ============= Central Panel ==============
        self.central_panel = EditorArea(parent=self)
        self.splitter_container.addWidget(self.central_panel)

        # ============= Right Panel ==============
        self.right_panel = RightDock(parent=self)
        self.splitter_container.addWidget(self.right_panel)

        self.splitter_container.setSizes([260, 1000, 0])

        # ==================== Status Bar ======================
        self.status_bar = CustomStatusBar(self)
        self.setStatusBar(self.status_bar)

        self.status_bar.setLeftPanelToggleBtnConn(self.toggle_left_panel)
        self.status_bar.setRightPanelToggleBtnConn(self.toggle_right_panel)
        self.status_bar.setGitBtnConn(self.open_git_panel)
        self.status_bar.setExplorerBtnConn(self.open_explorer_panel)
        self.status_bar.setAgentBtnConn(self.open_agent_panel)
        self.status_bar.setTerminalBtnConn(self.open_terminal_panel)

    def open_file_from_explorer(self, file_path: str):
        logger.info(f"Opening file from explorer: {file_path}")

        try:
            content, name = read_file(file_path)
        except OSError as e:
            logger.error(f"Failed to open file: {e}")
            QMessageBox.critical(
                self,
                "Open File Failed",
                f"Failed to open file:\n{file_path}\n{e}"
            )
            return
        self.central_panel.add_tab(name, file_path, content)

    def _left_panel_width(self) -> int:
        return self.splitter_container.sizes()[0]

    def set_left_panel_visible(self, visible: bool):
        sizes = self.splitter_container.sizes()

        if visible:
            sizes[self.LEFT_PANEL_INDEX] = 260
        else:
            sizes[self.LEFT_PANEL_INDEX] = 0
        self.splitter_container.setSizes(sizes)

    def _right_panel_width(self):
        return self.splitter_container.sizes()[self.RIGHT_PANEL_INDEX]

    def set_right_panel_visible(self, visible: bool):
        sizes = self.splitter_container.sizes()

        if visible:
            sizes[self.RIGHT_PANEL_INDEX] = 260
        else:
            sizes[self.RIGHT_PANEL_INDEX] = 0
        self.splitter_container.setSizes(sizes)

    def _show_left_panel(self, name: str):
        logger.info(f"Opening {name} panel")
        self.left_panel.showPanel(name)
        if self._left_panel_width() < 5:
            self.set_left_panel_visible(True)
    
    def _show_right_panel(self, name: str):
        logger.info(f"Opening {name} panel")
        self.right_panel.showPanel(name)
        if self._right_panel_width() < 5:
            self.set_right_panel_visible(True)
    
    def open_git_panel(self):
        self._show_left_panel("git")

    def open_explorer_panel(self):
        self._show_left_panel("explorer")

    def open_agent_panel(self):
        self._show_right_panel("agent")

    def open_terminal_panel(self):
        self._show_right_panel("terminal")

    def read_style_sheet(self, styleSheetFile: str = STYLE_SHEET_FILE) -> str:
        style_sheet, _ = read_file(styleSheetFile)
        return style_sheet

    def open_existing_file(self, file_path: str | None = None):
        if not file_path:
            return
        content, file_name = read_file(file_path)
        self.central_panel.add_tab(file_name, file_path, content)

    def current_file_path(self) -> str | None:
        return self.central_panel.current_file_path()

    # File / Edit / View / Settings / About / Help methods unchanged below...

    # ─────────────────────────────────────────────
    # File
    # ─────────────────────────────────────────────

    def new_file(self):
        """Create a new file."""
        logger.info("Creating new file")

        file_name, ok = QInputDialog.getText(
            self,
            "New File",
            "File name:"
        )
        if not ok or not file_name:
            return

        self.left_panel.file_explorer.new_file(file_name)

    def open_file(self):
        """Ask the user to select a file and open it."""
        logger.info("Opening file...")
        file_path = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")[0]
        self.open_existing_file(file_path=file_path)

    def browse_folder(self):
        """Open a folder."""
        self.left_panel.file_explorer.browse_folder()

    def save_file(self):
        """Save the current file."""
        file_path = self.current_file_path()
        content = self.central_panel.current_content()

        write_file(file_path, content)

    def rename_file(self):
        """Rename the current file."""
        old_file_path = self.current_file_path()

        if not old_file_path:
            return

        new_file_name, ok = QInputDialog.getText(self, "Rename File", "New file name:")
        if ok and new_file_name:
            new_file_path = rename_file(old_file_path, new_file_name)
            self.central_panel.close_tab_by_path(old_file_path)
            self.open_existing_file(str(new_file_path))

    def close_tab(self):
        """Close the current editor tab."""
        index = self.central_panel.currentIndex()
        if index is not None:
            self.central_panel.on_close_tab(index)

    # ─────────────────────────────────────────────
    # Edit
    # ─────────────────────────────────────────────

    def undo(self):
        """Undo the last editing operation."""
        self.central_panel.undo()

    def redo(self):
        """Redo the last editing operation."""
        self.central_panel.redo()

    def cut(self):
        """Cut the selected text."""
        self.central_panel.cut()

    def copy(self):
        """Copy the selected text."""
        self.central_panel.copy()

    def paste(self):
        """Paste text from the clipboard."""
        self.central_panel.paste()

    def find_(self):
        """Open the find interface."""
        pass

    def replace(self):
        """Open the replace interface."""
        pass

    def go_to_line(self):
        """Go to a specific line."""
        pass

    # ─────────────────────────────────────────────
    # View
    # ─────────────────────────────────────────────

    def toggle_left_panel(self):
        logger.info("Toggling left panel")

        if self._left_panel_width() < 5:
            self.set_left_panel_visible(True)
        else:
            self.set_left_panel_visible(False)

    def toggle_right_panel(self):
        logger.info("Toggling right panel")

        if self._right_panel_width() < 5:
            self.set_right_panel_visible(True)
        else:
            self.set_right_panel_visible(False)

    def toggle_terminal(self):
        """Show or hide the terminal."""
        pass

    def toggle_minimap(self):
        """Show or hide the minimap."""
        pass

    def zoom_in(self):
        """Increase editor zoom."""
        pass

    def zoom_out(self):
        """Decrease editor zoom."""
        pass

    def reset_zoom(self):
        """Reset editor zoom to the default level."""
        pass

    # ─────────────────────────────────────────────
    # Build
    # ─────────────────────────────────────────────

    def run_file(self):
        """Run interpreted  language scripts"""
        file_path = self.current_file_path()
        run_python_file(file_path)

    # ─────────────────────────────────────────────
    # Settings
    # ─────────────────────────────────────────────

    def open_preferences(self):
        """Open editor preferences."""
        pass

    def open_shortcuts_editor(self):
        """Open keyboard shortcut settings."""
        pass

    def open_theme_settings(self):
        """Open theme settings."""
        pass

    # ─────────────────────────────────────────────
    # About
    # ─────────────────────────────────────────────

    def show_about_dialog(self):
        """Show the About dialog."""
        pass

    def check_for_updates(self):
        """Check for application updates."""
        pass

    # ─────────────────────────────────────────────
    # Help
    # ─────────────────────────────────────────────

    def open_docs(self):
        """Open the editor documentation."""
        pass

    def report_issue(self):
        """Open the issue reporting page."""
        pass