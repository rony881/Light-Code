from PyQt6.QtWidgets import QPushButton

from light_code.utils.logger import logger


class CustomButton(QPushButton):
    def __init__(self, text: str, parent=None):
        super().__init__(parent)
        logger.info("Initializing CustomButton")
        self.setObjectName("custom_button")
        self.setFixedSize(24, 24)
        self.setText(text)
        self.setStyleSheet(self._get_style())

    def _get_style(self) -> str:
        return """
        QPushButton#custom_button {
            background: #21262d;
            color: #c9d1d9;
            border: 1px solid #30363d;
            border-radius: 1px;
            padding: 0px;
            font-size: 13px;
        }

        QPushButton#custom_button:hover {
            background: #30363d;
            border-color: #8b949e;
        }

        QPushButton#custom_button:pressed {
            background: #21262d;
        }
        """
