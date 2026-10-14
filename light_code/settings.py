from pathlib import Path

from PyQt6.QtCore import QByteArray, QSettings
from PyQt6.QtGui import QFont


class Settings(QSettings):
    def __init__(self, parent=None):
        super().__init__("Rony", "Light Code", parent)

        self.default_font_family = "JetBrains Mono"
        self.default_font_size = 12

        # Window settings
        self.window_width = self.value("window_width", 1080, type=int)
        self.window_height = self.value("window_height", 720, type=int)
        self.splitter_state = self.value("splitter_state", QByteArray(),type=QByteArray)
        self.window_background = self.value(
            "window_background", "#0d1117"
        )

        self.window_font_family = QFont(
            self.value("window_font_family", self.default_font_family)
        )
        self.window_font_size = self.value(
            "window_font_size", self.default_font_size, type=int
        )

        self.last_directory = self.value(
            "last_directory", str(Path.home())
        )

        # Editor settings
        self.editor_font_family = QFont(
            self.value("editor_font_family", self.default_font_family)
        )
        self.editor_font_size = self.value(
            "editor_font_size", 15, type=int
        )

        self.show_line_numbers = self.value(
            "show_line_numbers", True, type=bool
        )

        self.editor_selection_background = self.value(
            "editor_selection_background", "#273747"
        )
        self.editor_selection_foreground = self.value(
            "editor_selection_foreground", "#f0f6fc"
        )


settings = Settings()