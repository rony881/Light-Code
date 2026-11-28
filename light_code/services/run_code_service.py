# services/run_code_service.py

import os
import sys

from PyQt6.QtCore import QObject, QProcess, pyqtSignal

from light_code.utils.logger import logger


class CodeRunner(QObject):
    """Runs a file as a subprocess and streams its output via signals.
    """

    output_received = pyqtSignal(str, int)
    error_received = pyqtSignal(str, int)
    finished = pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.process: QProcess | None = None
        self.python_executable = sys.executable

    def run(self, file_path: str) -> None:
        self.stop()

        logger.info(f"Running Python file: {file_path}")
        self.process = QProcess(self)
        self.process.setWorkingDirectory(os.path.dirname(file_path))
        self.process.readyReadStandardOutput.connect(self._on_stdout)
        self.process.readyReadStandardError.connect(self._on_stderr)
        self.process.finished.connect(self._on_finished)
        self.process.start(self.python_executable, ["-u", file_path])

    def stop(self) -> None:
        if self.process is not None and self.process.state() != QProcess.ProcessState.NotRunning:
            self.process.kill()
            self.process.waitForFinished(1000)

    def run_command(self, command: str, cwd: str | None = None) -> None:
        self.stop()
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self._on_stdout)
        self.process.readyReadStandardError.connect(self._on_stderr)
        self.process.finished.connect(self._on_finished)
        if cwd:
            self.process.setWorkingDirectory(cwd)
        self.process.start("sh", ["-c", command])

    def _on_stdout(self) -> None:
        data = bytes(self.process.readAllStandardOutput()).decode("utf-8", errors="replace")
        exit_code = self.process.exitCode()
        self.output_received.emit(data, exit_code)

    def _on_stderr(self) -> None:
        data = bytes(self.process.readAllStandardError()).decode("utf-8", errors="replace")
        exit_code = self.process.exitCode()
        self.error_received.emit(data, exit_code)

    def _on_finished(self, exit_code: int):
        self.finished.emit(exit_code)
        