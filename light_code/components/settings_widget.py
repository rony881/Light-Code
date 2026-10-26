

from PyQt6.QtWidgets import QLabel

from light_code.base_widgets.base_widget import BaseWidget


class SettingsWidget(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.main_layout.setContentsMargins(10,8,0,8)
        self.window_settings_lbl = QLabel("Window Settings", parent=self)
        self.window_settings_lbl.setObjectName("win_settings_lbl")
        self.add(self.window_settings_lbl)

        self.main_layout.addStretch()


