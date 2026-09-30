# src/light_code/components/widgets/output_panel.py

import os

from PyQt6.QtWidgets import QFrame, QLineEdit, QPlainTextEdit, QLabel, QHBoxLayout, QPushButton
from light_code.base_widgets.base_widget import BaseWidget
from light_code.services.run_code_service import CodeRunner
from light_code.utils.logger import logger


class OutputPanel(BaseWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        logger.info("Initializing OutputPanel")
        self.setObjectName("output_panel")
        self.path = None

        self.code_runner = CodeRunner(self)
        self.code_runner.output_received.connect(self.show_output)
        self.code_runner.error_received.connect(self.show_error)
        
        self._setup_ui()

    def _setup_ui(self):
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
        self.cmd_input.returnPressed.connect(self.run_command)
        
        self.add(self.header_frame)
        self.add(self.output_view)
        self.add(self.cmd_input)

    def execute_file(self, file_path: str) -> None:
        self.clear_output()
        self.set_file_name(file_path)
        self.path = file_path
        self.code_runner.run(file_path)
        
    def show_output(self, text: str) -> None:
        self.output_view.insertPlainText(text)
        scrollbar = self.output_view.verticalScrollBar()
        if scrollbar is not None:
            scrollbar.setValue(scrollbar.maximum())

    def show_error(self, text: str) -> None:
        self.show_output(text)
     
    def clear_output(self) -> None:
        self.output_view.clear()

    def set_file_name(self, path: str) -> None:
        self.file_name_lbl.setText(os.path.basename(path))
        self.file_name_lbl.setToolTip(path)

    def on_run_finished(self, exit_code: int):
        self.show_output(
            f"\n[process finished with exit code {exit_code}]\n"
        )

    def run_command(self) -> None:
        command = self.cmd_input.text()
        self.cmd_input.clear()
        self.clear_output()
        self.code_runner.run_command(command)