# components/top_bar.py

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout

from light_code.base_widgets.base_widget import BaseWidget
from light_code.components.button import Button
from light_code.components.menubar import MenuBar
from light_code.utils.logger import logger

BUTTON_STYLE = """
QPushButton {
    background: transparent;
    color: #8b949e;
    border: none;
    border-radius: 4px;
    padding: 0px;
    font-size: 14px;
}
QPushButton:hover {
    background: #21262d;
    color: #e6edf3;
}
QPushButton:pressed {
    background: #1D2733;
    color: #58a6ff;
}
"""


class TopBar(BaseWidget):
    """Thin bar across the top of the window."""

    HEIGHT = 34

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Initializing TopBar")
        self.setObjectName("top_bar")
        self.setFixedHeight(self.HEIGHT)

        self.h_layout = QHBoxLayout()
        self.h_layout.setContentsMargins(6, 0, 8, 0)
        self.h_layout.setSpacing(4)
        self.add(self.h_layout)

        # Menu Bar
        self.menu_bar = MenuBar(parent=parent)
        self.menu_bar.setNativeMenuBar(False)
        self.h_layout.addWidget(self.menu_bar, 0, Qt.AlignmentFlag.AlignVCenter)

        self.h_layout.addStretch(1)

        # Quick Actions
        self.add_button("▶", "Run")
        self.add_button("⚙", "Settings")
        self.add_button("⋮", "More")

    def add_button(self, text: str, tooltip: str = "", handler=None) -> Button:
        button = Button(text)
        button.setFixedSize(28, 24)
        button.setToolTip(tooltip)
        button.setStyleSheet(BUTTON_STYLE)
        if handler:
            button.clicked.connect(handler)
        self.h_layout.addWidget(button, 0, Qt.AlignmentFlag.AlignVCenter)
        return button