# src/light_code/components/widgets/output_panel.py

import os

from PyQt6.QtWidgets import QFrame, QLineEdit, QPlainTextEdit, QLabel, QHBoxLayout, QPushButton
from light_code.base_widgets.base_widget import BaseWidget
from light_code.utils.logger import logger


class OutputPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing OutputPanel")
        self.setObjectName("output_panel")

        self.header_frame = QFrame(self)
        self.header_frame.setObjectName("header_frame")
        self.header_frame.setMaximumHeight(30)
        
        self.hdr_frame_layout = QHBoxLayout(self.header_frame)
        self.hdr_frame_layout.setSpacing(0)
        self.hdr_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.file_name_lbl = QLabel(self.header_frame)
        self.file_name_lbl.setObjectName("file_name_lbl")
        self.hdr_frame_layout.addWidget(self.file_name_lbl)
        self.hdr_frame_layout.addStretch()

        self.clear_btn = QPushButton(parent=self, text="clear")
        self.clear_btn.clicked.connect(self.clear_output)
        self.hdr_frame_layout.addWidget(self.clear_btn)

        self.output_view = QPlainTextEdit(self)
        self.output_view.setObjectName("output_view")
        self.output_view.setReadOnly(True)

        self.cmd_input = QLineEdit(self)
        self.cmd_input.setObjectName("cmd_input")
        self.cmd_input.setPlaceholderText("Type a command...")
        
        self.add(self.header_frame)
        self.add(self.output_view)
        self.add(self.cmd_input)

    def show_output(self, text: str) -> None:
        self.output_view.insertPlainText(text)
        scrollbar = self.output_view.verticalScrollBar()
        if scrollbar is not None:
            scrollbar.setValue(scrollbar.maximum())

    def set_path(self, path: str) -> None:
        self.file_name_lbl.setText(os.path.basename(path))
        self.file_name_lbl.setToolTip(path)

    def show_error(self, text: str) -> None:
        self.show_output(text)

    def clear_output(self) -> None:
        self.output_view.clear()
