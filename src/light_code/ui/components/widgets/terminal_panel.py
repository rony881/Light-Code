# ui/components/widgets/git_panel.py

from PyQt6.QtWidgets import QLabel

from light_code.ui.base_widgets.base_widget import BaseWidget
from light_code.utils.logger import logger


class TerminalPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing TerminalPanel")
        self.setObjectName("terminal_panel")
        label = QLabel("TERMINAL PANEL — COMING SOON")
        label.setObjectName("terminal_panel_label")
        self.add(label)
