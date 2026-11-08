from PyQt6.QtGui import QFontDatabase

from light_code.config import JETBRAINS_MONO_REGULAR_FONT


def load_font():
    font = QFontDatabase.addApplicationFont(str(JETBRAINS_MONO_REGULAR_FONT))
    if font == -1:
        print("Failed to load font")
        return
    print("Font loaded successfully")