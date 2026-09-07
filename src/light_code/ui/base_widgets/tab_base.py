# src/light_code/ui/base_widgets/tab_base.py

from PyQt6.QtWidgets import QTabWidget


class TabBase(QTabWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self._config()

        self.OPEN_TABS = {}

        # when user request for closing the tab this code
        # connects to close tab method
        self.tabCloseRequested.connect(self.on_close_tab)

    def _config(self):
        self.setObjectName("tab_widget")
        # This makes the tabs closable
        self.setTabsClosable(True)
        # This make the tabs movable
        self.setMovable(True)

    def on_close_tab(self, index):
        """Override this method to implement tab closing logic."""
        raise NotImplementedError
