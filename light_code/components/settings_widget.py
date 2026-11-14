
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QFontComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSpinBox
)

from light_code.base_widgets.base_widget import BaseWidget
from light_code.settings import settings
from light_code.utils.logger import logger


class SettingsWidget(BaseWidget):
    settings_changed = pyqtSignal(str) 
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowType.Window)
        self.setWindowTitle("Light Code Settings")
        self.resize(420, 500)
        
        self.setup_ui()
        self.update_display()
    
    def setup_ui(self):    
        self.main_layout.setContentsMargins(15,15,15,15)
        self.main_layout.setSpacing(10)

        # Buttons
        button_layout = QHBoxLayout()
        
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_settings)
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

        self.window_font_family = QFontComboBox()
        self.add(self.window_font_family)

        w_font_size_lbl = self._make_subheader("Window Font Size")
        self.add(w_font_size_lbl)
        
        self.window_font_size = QSpinBox()
        self.window_font_size.setRange(8, 50)
        self.window_font_size.setSuffix(" px")
        self.add(self.window_font_size)
 
        # Editor settings
        es_lbl = self._make_header("Editor Settings")
        self.add(es_lbl)

        e_font_family_lbl = self._make_subheader("Editor Font Family")
        self.add(e_font_family_lbl)

        self.editor_font_family = QFontComboBox()
        self.add(self.editor_font_family)

        e_font_size_lbl = QLabel("Editor Font Size")
        e_font_size_lbl.setObjectName("settings_subheaders")
        self.add(e_font_size_lbl)

        self.editor_font_size = QSpinBox()
        self.editor_font_size.setRange(8, 50)
        self.add(self.editor_font_size)
        
        self.main_layout.addStretch()

    def reset_settings(self):
        settings.reset()
        self.update_display()

    def update_display(self):
        self.window_font_family.setCurrentFont(QFont(settings.get("window_font_family")))
        self.window_font_size.setValue(settings.get("window_font_size"))
        self.editor_font_family.setCurrentFont(QFont(settings.get("editor_font_family")))
        self.editor_font_size.setValue(settings.get("editor_font_size"))

    def _make_header(self, text: str):
        header = QLabel(text=text)
        header.setObjectName("settings_headers")
        return header

    def _make_subheader(self, text: str):
        sub_header = self._make_header(text=text)
        sub_header.setObjectName("settings_subheaders")
        return sub_header

    def save(self):
        settings.set("window_font_family", self.window_font_family.currentFont().family())
        settings.set("window_font_size", self.window_font_size.value())
        settings.set("editor_font_family", self.editor_font_family.currentFont().family())
        settings.set("editor_font_size", self.editor_font_size.value())
        logger.info("Settings Saved")
