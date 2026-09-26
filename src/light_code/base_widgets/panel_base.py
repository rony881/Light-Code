from PyQt6.QtWidgets import QStackedWidget
from light_code.base_widgets.base_widget import BaseWidget


class PanelBase(BaseWidget):
    def __init__(self, parent=None, max_width=600):
        super().__init__(parent)
        self.setMinimumWidth(0)
        self.setMaximumWidth(max_width)
        self._stack = QStackedWidget()
        self._panels = {}
        self.add(self._stack)

    def add_panel(self, name: str, widget) -> None:
        self._panels[name] = widget
        self._stack.addWidget(widget)

    def show_panel(self, name: str) -> None:
        self._stack.setCurrentWidget(self._panels[name])