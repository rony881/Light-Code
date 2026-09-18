# src/light_code/dialogs/__init__.py
from PyQt6.QtWidgets import QInputDialog


class NewFileDialog(QInputDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def get_file_name(self):
        return self.getText(self, "New File", "File Name:")

class RenameFileDialog(QInputDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def get_file_name(self):
        return self.getText(self, "Rename File", "New file name:")

class GoToLineDialog(QInputDialog):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def get_line_number(self, current_line: int, max_line: int):
        return self.getInt(
            self,
            "Go to Line",
            f"Line number (1 - {max_line}):",
            current_line,
            1,
            max_line,
        )