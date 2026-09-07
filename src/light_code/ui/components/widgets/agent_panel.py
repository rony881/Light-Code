# ui/components/widgets/agent_panel.py
from PyQt6.QtWidgets import QLabel

from light_code.ui.base_widgets.base_widget import BaseWidget
from light_code.utils.logger import logger


class AgentPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Initializing AgentPanel")
        self.setObjectName("agent_panel")
        label = QLabel("AGENT PANEL — COMING SOON")
        label.setObjectName("agent_panel_label")
        self.add(label)
