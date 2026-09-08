# services/run_code_service.py

import sys

from PyQt6.QtCore import QObject, QProcess, pyqtSignal

from light_code.utils.logger import logger


class CodeRunner(QObject):
    """Runs a file as a subprocess and streams its output via signals.

    Must be constructed with a long-lived parent (e.g. MainWindow) — Qt's
    parent/child ownership is what keeps the underlying QProcess alive,
    not just holding a Python reference to it.
    """

    output_received = pyqtSignal(str)
    error_received = pyqtSignal(str)
    finished = pyqtSignal(int)

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.process: QProcess | None = None

    def run_python_file(self, file_path: str) -> None:
        self.stop()

        logger.info(f"Running Python file: {file_path}")
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self._on_stdout)
        self.process.readyReadStandardError.connect(self._on_stderr)
        self.process.finished.connect(self._on_finished)
        self.process.start(sys.executable, ["-u", file_path])

    def stop(self) -> None:
        if self.process is not None and self.process.state() != QProcess.ProcessState.NotRunning:
            self.process.kill()
            self.process.waitForFinished(1000)

    def _on_stdout(self) -> None:
        data = bytes(self.process.readAllStandardOutput()).decode("utf-8", errors="replace")
        self.output_received.emit(data)

    def _on_stderr(self) -> None:
        data = bytes(self.process.readAllStandardError()).decode("utf-8", errors="replace")
        self.error_received.emit(data)

    def _on_finished(self, code: int, _status) -> None:
        logger.info(f"Process finished with exit code {code}")
        self.finished.emit(code)
