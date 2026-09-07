# ui/components/widgets/git_panel.py

from PyQt6.QtWidgets import QLabel

from light_code.ui.base_widgets.base_widget import BaseWidget
from light_code.utils.logger import logger


class GitPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing GitPanel")
        self.setObjectName("git_panel")
        label = QLabel("GIT PANEL — COMING SOON")
        label.setObjectName("git_panel_label")
        self.add(label)