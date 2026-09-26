
from light_code.base_widgets.panel_base import PanelBase
from light_code.components.widgets.agent_panel import AgentPanel
from light_code.components.widgets.output_panel import OutputPanel
from light_code.utils.logger import logger


class RightDock(PanelBase):
    """Right-hand agent/assistant panel."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Initializing RightDock")
        self.setObjectName("rightPanel")

        self.agent_panel = AgentPanel()
        self.add_panel("agent", self.agent_panel)

        self.output_panel = OutputPanel()
        self.add_panel("output", self.output_panel)
