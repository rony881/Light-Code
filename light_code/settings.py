from pathlib import Path

from PyQt6.QtCore import QByteArray, QObject, QSettings, pyqtSignal

from light_code.utils.logger import logger


DEFAULTS = {
    # Default font settings
    "default_font_family": "JetBrains Mono",
    "default_font_size": 12,

    # Window settings
    "window_width": 1080,
    "window_height": 720,
    "splitter_state": QByteArray(),
    "window_background": "#0d1117",
    "window_font_family": "JetBrains Mono",
    "window_font_size": 12,
    "last_folder_path": str(Path.home()),

    # Editor settings
    "editor_font_family": "JetBrains Mono",
    "editor_font_size": 15,
    "show_line_numbers": True,
    "editor_selection_background": "#273747",
    "editor_selection_foreground": "#f0f6fc",
}

class Settings(QObject):
    setting_changed = pyqtSignal(str, object)

    def __init__(self) -> None:
        super().__init__()
        self.qs = QSettings("Rony", "Light Code")

    def get(self, key):
        default = DEFAULTS[key]
        return self.qs.value(key, default, type=type(default))

    def set(self, key, value):
        if self.get(key) == value:
            return
        self.qs.setValue(key,value)
        self.setting_changed.emit(key, value)

    def set_to_default(self, key):
        self.set(key, DEFAULTS[key])

    def reset(self):
        for key in DEFAULTS:
            self.set_to_default(key)
        logger.info("Application settings Reset")

settings = Settings()
