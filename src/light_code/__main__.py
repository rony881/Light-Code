# src/light_code/__main__.py
import sys

from PyQt6.QtWidgets import QApplication
from ui.views.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
