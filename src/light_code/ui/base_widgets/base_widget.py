from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLayout, QVBoxLayout, QWidget


class BaseWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setObjectName("base_widget")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

    def add(self, item):
        if isinstance(item, QLayout):
            self.main_layout.addLayout(item)
        elif isinstance(item, QWidget):
            self.main_layout.addWidget(item)
        else:
            raise TypeError(
                f"BaseWidget.add() expects a QWidget or QVBoxLayout, got {type(item).__name__}"
            )