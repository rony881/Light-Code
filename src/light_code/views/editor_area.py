# src/light_code/views/editor_area.py

from pathlib import Path

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMessageBox

from light_code.editor.editor import BaseEditor
from light_code.services.file_service import write_file
from light_code.base_widgets.tab_base import TabBase
from light_code.utils.logger import logger


class EditorArea(TabBase):
    """Editor area: tabbed code editors."""
    cursor_moved = pyqtSignal(int, int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("editor_panel")
        logger.info("Initializing EditorArea")

    def add_tab(self, tab_name: str, file_path: str, content: str) -> int | None:
        """this method used for open a tab"""
        logger.info(f"Adding tab: {tab_name}")
        if file_path in self.OPEN_TABS:
            tab = self.OPEN_TABS[file_path]
            index = self.indexOf(tab)
            self.setCurrentIndex(index)
            return

        tab = BaseEditor(file_path=file_path)
        tab.setText(content)
        tab.setModified(False)
        tab.modificationChanged.connect(
            lambda dirty, e=tab: self._update_tab_title(e, dirty)
        )
        tab.cursorPositionChanged.connect(
            lambda line, column, e=tab: self.cursor_position(e, line, column)
        )

        tab_index = self.addTab(tab, tab_name)

        self.OPEN_TABS[file_path] = tab
        self.setCurrentIndex(tab_index)

        return tab_index

    def cursor_position(self, editor, line: int, column: int) -> None:
        if editor is self.currentWidget():
            self.cursor_moved.emit(line + 1, column + 1)

    def _update_tab_title(self, editor, dirty: bool) -> None:
        index = self.indexOf(editor)
        if index != -1:
            name = Path(editor.file_path).name
            self.setTabText(index, f"* {name}" if dirty else name)

    def current_editor(self) -> BaseEditor | None:
        """Returns file path of current selected tab"""
        editor = self.currentWidget()
        if editor is None:
                return None
        if isinstance(editor, BaseEditor):
            return editor

    def rename_current_tab(self, new_name: str) -> None:
        """Rename the current tab to the given name."""
        widget = self.currentWidget()
        if widget is None:
            return
        index = self.currentIndex()
        self.setTabText(index, new_name)

    def close_tab_by_path(self, file_path: str) -> None:
        """Silently close and remove the tab for the given file path."""
        file_path = str(file_path)
        widget = self.OPEN_TABS.get(file_path)
        if widget is None:
            return

        index = self.indexOf(widget)
        if index == -1:
            return

        del self.OPEN_TABS[file_path]
        self.removeTab(index)
        widget.deleteLater()

    def ask_for_save(self, index: int) -> bool:
        """Ask the user to save changes about one tab.
        Returns True if the user chooses to save, False if the user canceled or saving failed.
        """
        editor = self.widget(index)
        if not isinstance(editor, BaseEditor) or not editor.file_path:
            return True
        if not editor.isModified():
            return True

        name = Path(editor.file_path).name
        choice = QMessageBox.question(
                self, "Unsaved Changes", f'Save changes to "{name}"?',
                QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard
                | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Save,
            )
        if choice == QMessageBox.StandardButton.Cancel:
            return False
        if choice == QMessageBox.StandardButton.Save:
            try:
                write_file(editor.file_path, editor.text())
            except OSError as e:
                QMessageBox.critical(self, "Save Failed", str(e))
                return False
            editor.setModified(False)
        return True

    def confirm_close_all(self) -> bool:
        for i in range(self.count()):
            self.setCurrentIndex(i)
            if not self.ask_for_save(i):
                return False
        return True

    def _remove_tab(self, index: int) -> None:
        """Remove the tab at the given index."""
        widget = self.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.removeTab(index)
        
    def on_close_tab(self, index: int) -> None:
        """Close the tab at the given index."""
        if self.ask_for_save(index):
            self._remove_tab(index)

    def undo(self):
        """Undo the last editing operation."""
        editor = self.current_editor()
        if editor is not None:
            editor.undo()

    def redo(self):
        """Redo the last editing operation."""
        editor = self.current_editor()
        if editor is not None:
            editor.redo()

    def cut(self):
        """cut the selected text"""
        editor = self.current_editor()
        if editor is not None:
            editor.cut()

    def copy(self):
        editor = self.current_editor()
        if editor is not None:
            editor.copy()

    def paste(self):
        editor = self.current_editor()
        if editor is not None:
            editor.paste()

    def zoom_in(self):
        editor = self.current_editor()
        if editor is not None:
            editor.zoomIn()

    def zoom_out(self):
        editor = self.current_editor()
        if editor is not None:
            editor.zoomOut()

    def go_to_line(self, line: int):
        """Move the cursor to the given line number."""
        editor = self.current_editor()
        if editor is None:
            return

        line_index = max(0, min(line - 1, editor.lines() - 1))
        editor.setCursorPosition(line_index, 0)
        editor.ensureLineVisible(line_index)
        editor.setFocus()

    def reset_zoom(self):
        """Reset editor zoom to the default level."""
        editor = self.current_editor()
        if editor is not None:
            editor.zoomTo(0)