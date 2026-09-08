# src/light_code/ui/dialogs/__init__.py
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