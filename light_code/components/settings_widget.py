
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QFontComboBox, QHBoxLayout, QLabel, QPushButton, QSpinBox

from light_code.base_widgets.base_widget import BaseWidget
from light_code.settings import settings
from light_code.utils.logger import logger


class SettingsWidget(BaseWidget):
    settings_changed = pyqtSignal(str) 
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.main_layout.setContentsMargins(15,15,15,15)
        self.main_layout.setSpacing(10)

        # Buttons
        button_layout = QHBoxLayout()
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(settings.reset)
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save)
        
        button_layout.addStretch()
        button_layout.addWidget(self.reset_button)
        button_layout.addWidget(self.save_button)

        self.add(button_layout)
        
        # Window Settings
        ws_lbl = self._make_header("Window Settings")
        self.add(ws_lbl)

        w_font_family_lbl = self._make_subheader("Window Font Family")
        self.add(w_font_family_lbl)

        self.wf_combobox = QFontComboBox()
        self.wf_combobox.setCurrentFont(QFont(settings.get("window_font_family")))
        self.add(self.wf_combobox)

        w_font_size_lbl = self._make_subheader("Window Font Size")
        self.add(w_font_size_lbl)
        
        self.wf_spinbox = QSpinBox()
        self.wf_spinbox.setRange(8, 50)
        self.wf_spinbox.setSuffix(" px")
        self.wf_spinbox.setValue(settings.get("window_font_size"))
        self.add(self.wf_spinbox)
 
        # Editor settings
        es_lbl = self._make_header("Editor Settings")
        self.add(es_lbl)

        e_font_family_lbl = self._make_subheader("Editor Font Family")
        self.add(e_font_family_lbl)

        self.ef_combobox = QFontComboBox()
        self.ef_combobox.setCurrentFont(QFont(settings.get("editor_font_family")))
        self.add(self.ef_combobox)

        e_font_size_lbl = QLabel("Editor Font Size")
        e_font_size_lbl.setObjectName("settings_subheaders")
        self.add(e_font_size_lbl)

        self.ef_spinbox = QSpinBox()
        self.ef_spinbox.setRange(8, 50)
        self.ef_spinbox.setValue(settings.get("editor_font_size"))
        self.add(self.ef_spinbox)
        
        self.main_layout.addStretch()

    def _make_header(self, text: str):
        header = QLabel(text=text)
        header.setObjectName("settings_headers")
        return header

    def _make_subheader(self, text: str):
        sub_header = self._make_header(text=text)
        sub_header.setObjectName("settings_subheaders")
        return sub_header

    def save(self):
        settings.set("window_font_family", self.wf_combobox.currentFont().family())
        settings.set("window_font_size", self.wf_spinbox.value())
        settings.set("editor_font_family", self.ef_combobox.currentFont().family())
        settings.set("editor_font_size", self.ef_spinbox.value())
