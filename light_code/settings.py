from pathlib import Path

from PyQt6.QtCore import QSettings
from PyQt6.QtGui import QFont


class Settings(QSettings):
    def __init__(self, parent = None):
        super().__init__(parent)
        # Default Settings
        self.default_font_family = "JetBrains Mono"
        self.default_font_size = 12
        
        # Window settings
        # window size
        self.window_width = self.value("window_width", 1080)
        self.window_height = self.value("window_height", 720)
        # window color settings
        self.window_background = self.value("window_background", "#0d1117")
        # window fonts
        self.window_font_family = QFont(self.value("window_font_family", self.default_font_family))
        self.window_font_size = self.value("window_font_size", self.default_font_size)
        self.last_directory = self.value("last_directory", str(Path.home()))
        
        # Editor Settings
        self.editor_font_family = QFont(self.value("editor_font_family", self.default_font_family))
        self.editor_font_size = self.value("editor_font_size", 15)
        self.show_line_numbers = self.value("show_line_numbers", True)
        self.editor_selection_background = self.value("editor_selection_background", "#273747")
        self.editor_selection_foreground = self.value("editor_selection_background", "#f0f6fc")

settings = Settings()