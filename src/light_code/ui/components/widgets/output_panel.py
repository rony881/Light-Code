# ui/components/widgets/output_panel.py

from PyQt6.QtWidgets import QPlainTextEdit

from light_code.ui.base_widgets.base_widget import BaseWidget
from light_code.utils.logger import logger


class OutputPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing OutputPanel")
        self.setObjectName("output_panel")

        self.output_view = QPlainTextEdit(self)
        self.output_view.setObjectName("output_panel")
        self.output_view.setReadOnly(True)
        self.add(self.output_view)

    def show_output(self, text: str) -> None:
        self.output_view.insertPlainText(text)
        scrollbar = self.output_view.verticalScrollBar()
        if scrollbar is not None:
            scrollbar.setValue(scrollbar.maximum())

    def show_error(self, text: str) -> None:
        self.show_output(text)

    def clear_output(self) -> None:
        self.output_view.clear()
