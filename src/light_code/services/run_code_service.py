# services/run_code_service.py

import sys

from PyQt6.QtCore import QProcess

from light_code.utils.logger import logger


def run_python_file(file_path: str) -> QProcess:
    logger.info(f"Running Python file: {file_path}")
    process = QProcess()

    process.readyReadStandardOutput.connect(
        lambda: print(
            bytes(process.readAllStandardOutput()).decode("utf-8", errors="replace"),
            end="",
        )
    )
    process.readyReadStandardError.connect(
        lambda: print(
            bytes(process.readAllStandardError()).decode("utf-8", errors="replace"),
            end="",
            file=sys.stderr,
        )
    )
    process.finished.connect(
        lambda code, _status: print(f"\n[process finished with exit code {code}]")
    )

    process.start(sys.executable, ["-u", file_path])
    return process
