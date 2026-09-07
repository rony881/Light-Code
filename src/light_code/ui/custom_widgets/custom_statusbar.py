from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QStatusBar, QWidget

from light_code.config import (
    AI_AGENT_ICON,
    EXPLORER_ICON,
    GIT_ICON,
    LEFT_PANEL_ICON,
    RIGHT_PANEL_ICON,
    TERMINAL_ICON,
)
from light_code.ui.custom_widgets.custom_button import CustomButton
from light_code.utils.logger import logger

BUTTON_STYLE = """
QPushButton {
    background: transparent;
    color: #8b949e;
    border: none;
    border-radius: 3px;
    padding: 0px 6px;
    font-size: 12px;
}
QPushButton:hover {
    background: #30363d;
    color: #e6edf3;
}
QPushButton:pressed {
    background: #21262d;
    color: #e6edf3;
}
"""

LABEL_STYLE = """
color: #8b949e;
font-size: 12px;
padding: 0px 4px;
"""

STATUS_MESSAGE_STYLE = """
color: #c9d1d9;
font-size: 12px;
padding: 0px 4px;
"""


class CustomStatusBar(QStatusBar):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing CustomStatusBar")
        self.setFixedHeight(30)
        self.setSizeGripEnabled(False)
        self.setObjectName("status_bar")

        self.container_widget = QWidget()
        self.h_layout = QHBoxLayout(self.container_widget)
        self.h_layout.setContentsMargins(4, 0, 4, 0)
        self.h_layout.setSpacing(10)

        # Left panel buttons
        self.left_panel_toggle_btn = CustomButton("")
        self.left_panel_toggle_btn.setIcon(QIcon(LEFT_PANEL_ICON))
        self.left_panel_toggle_btn.setToolTip("Toggle Left Panel")
        self.left_panel_toggle_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.left_panel_toggle_btn)

        self.explorer_btn = CustomButton("")
        self.explorer_btn.setIcon(QIcon(EXPLORER_ICON))
        self.explorer_btn.setToolTip("Explorer")
        self.explorer_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.explorer_btn)

        self.git_btn = CustomButton("")
        self.git_btn.setIcon(QIcon(GIT_ICON))
        self.git_btn.setToolTip("Git Panel")
        self.git_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.git_btn)

        self.h_layout.addSpacing(8)

        # Status message
        self.status_message_label = QLabel("Ready")
        self.status_message_label.setStyleSheet(STATUS_MESSAGE_STYLE)
        self.h_layout.addWidget(self.status_message_label)

        self.h_layout.addStretch()

        # Status information
        self.language_label = self._create_label("Plain Text", "Language Mode")
        self.h_layout.addWidget(self.language_label)

        self.indent_label = self._create_label("Spaces: 4", "Indentation")
        self.h_layout.addWidget(self.indent_label)

        self.encoding_label = self._create_label("UTF-8", "Encoding")
        self.h_layout.addWidget(self.encoding_label)

        self.cursor_label = self._create_label("Ln 1, Col 1", "Cursor Position")
        self.h_layout.addWidget(self.cursor_label)

        self.h_layout.addSpacing(8)

        # Right panel buttons
        self.agent_btn = CustomButton("")
        self.agent_btn.setIcon(QIcon(AI_AGENT_ICON))
        self.agent_btn.setToolTip("AI Agent")
        self.agent_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.agent_btn)

        self.terminal_btn = CustomButton("")
        self.terminal_btn.setIcon(QIcon(TERMINAL_ICON))
        self.terminal_btn.setToolTip("Terminal")
        self.terminal_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.terminal_btn)

        self.right_panel_btn = CustomButton("")
        self.right_panel_btn.setIcon(QIcon(RIGHT_PANEL_ICON))
        self.right_panel_btn.setToolTip("Right Panel")
        self.right_panel_btn.setStyleSheet(BUTTON_STYLE)
        self.h_layout.addWidget(self.right_panel_btn)

        self.addWidget(self.container_widget, 1)

    @staticmethod
    def _create_label(text: str, tooltip: str) -> QLabel:
        label = QLabel(text)
        label.setToolTip(tooltip)
        label.setStyleSheet(LABEL_STYLE)
        return label

    def setLeftPanelToggleBtnConn(self, func):
        self.left_panel_toggle_btn.clicked.connect(func)

    def setRightPanelToggleBtnConn(self, func):
        self.right_panel_btn.clicked.connect(func)

    def setExplorerBtnConn(self, func):
        self.explorer_btn.clicked.connect(func)

    def setGitBtnConn(self, func):
        self.git_btn.clicked.connect(func)

    def setAgentBtnConn(self, func):
        self.agent_btn.clicked.connect(func)

    def setTerminalBtnConn(self, func):
        self.terminal_btn.clicked.connect(func)

    def set_status_message(self, message: str) -> None:
        self.status_message_label.setText(message)

    def set_cursor_position(self, line: int, column: int) -> None:
        self.cursor_label.setText(f"Ln {line}, Col {column}")

    def set_language(self, language: str) -> None:
        self.language_label.setText(language)

    def set_encoding(self, encoding: str) -> None:
        self.encoding_label.setText(encoding)

    def set_indentation(self, text: str) -> None:
        self.indent_label.setText(text)
