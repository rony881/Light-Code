from PyQt6.QtCore import QSettings


class Settings(QSettings):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        # Application Settings
        self.window_width = self.value("window_width", 1080)
        self.window_height = self.value("window_height", 720)
        self.font_family = self.value("font", "JetBrains Mono")
        self.font_size = self.value("font_size", 12)
        self.last_directory = self.value("last_opened_project")
        
        # Editor Settings
        self.editor_font_family = self.value("editor_font_family", "JetBrains Mono")
        self.editor_font_size = self.value("editor_font_size", 15)
        self.show_line_numbers = self.value("show_line_numbers", True)
        
        