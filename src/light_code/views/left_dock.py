from PyQt6.QtWidgets import QStackedWidget

from light_code.base_widgets.base_widget import BaseWidget
from light_code.base_widgets.panel_base import PanelBase
from light_code.components.widgets.file_explorer_panel import FileExplorer
from light_code.components.widgets.git_panel import GitPanel
from light_code.utils.logger import logger


class LeftDock(PanelBase):
    """Sidebar file explorer panel."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        logger.info("Initializing LeftDock")
        self.setObjectName("leftPanel")

        self.file_explorer = FileExplorer(parent=self)
        self.add_panel("explorer", self.file_explorer)
        self.git_panel = GitPanel()
        self.add_panel("git", self.git_panel)

    def explorer_file_selected_conn(self, conn):
        self.file_explorer.file_selected.connect(conn)
