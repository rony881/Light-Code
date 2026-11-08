# src/light_code/__main__.py
import sys

from PyQt6.QtGui import QFontDatabase
from PyQt6.QtWidgets import QApplication

from light_code.config import JETBRAINS_MONO_REGULAR_FONT
from light_code.views.main_window import MainWindow

def load_font():
    font = QFontDatabase.addApplicationFont(str(JETBRAINS_MONO_REGULAR_FONT))
    if font == -1:
        print("Failed to load font")
        return
    print("Font loaded successfully")

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Rony")
    app.setApplicationName("Light Code")
    load_font()
    main_window = MainWindow()
    main_window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
