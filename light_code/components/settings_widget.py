
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QFontComboBox, QLabel, QSpinBox

from light_code.base_widgets.base_widget import BaseWidget


class SettingsWidget(BaseWidget):
    settings_changed = pyqtSignal(str) 
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.main_layout.setContentsMargins(15,15,15,15)
        self.main_layout.setSpacing(10)

        # Window Settings
        ws_lbl = QLabel("Window Settings", parent=self)
        ws_lbl.setObjectName("win_settings_lbl")
        
        self.add(ws_lbl)

        w_font_family = QLabel("Window Font Family")
        self.add(w_font_family)
        wf_combobox = QFontComboBox()
        self.add(wf_combobox)

        w_font_size = QLabel("Window Font Size")
        self.add(w_font_size)
        wf_spinbox = QSpinBox()
        wf_spinbox.setRange(8,50)
        wf_spinbox.setSuffix(" px")
        self.add(wf_spinbox)

        self.main_layout.addStretch()


