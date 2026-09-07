from PyQt6.QtWidgets import QStackedWidget

from light_code.ui.base_widgets.base_widget import BaseWidget
from light_code.ui.components.widgets.agent_panel import AgentPanel
from light_code.ui.components.widgets.terminal_panel import TerminalPanel
from light_code.utils.logger import logger


class RightDock(BaseWidget):
    """Right-hand agent/assistant panel."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Initializing RightDock")
        self.setObjectName("rightPanel")
        self.setMinimumWidth(0)
        self.setMaximumWidth(600)

        self.stack = QStackedWidget()
        self.add(self.stack)

        self.agent_panel = AgentPanel()
        self.stack.addWidget(self.agent_panel)

        self.terminal_panel = TerminalPanel()
        self.stack.addWidget(self.terminal_panel)

        self._panels = {
            "agent": 0,
            "terminal": 1,
        }

    def get_panel_index(self, panel_name: str) -> int:
        return self._panels[panel_name]

    def showPanel(self, panel_name: str):
        index = self.get_panel_index(panel_name)
        self.stack.setCurrentIndex(index)
