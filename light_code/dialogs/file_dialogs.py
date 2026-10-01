
from PyQt6.QtWidgets import QInputDialog, QMessageBox


_BAD_CHARS = set('<>:"/\\|?*c')

def ask_file_name(parent, title: str, label: str, text: str = "") -> str | None:
    while True:
        name, ok = QInputDialog.getText(
            parent,
            title,
            label,
            text=text,
        )
        if not ok:
            return None
        error = validate_file_name(name)
        if error:
            QMessageBox.warning(
                parent,
                title,
                error,
            )
            text = name
            continue
        return name.strip()

def validate_file_name(file_name: str) -> str | None:
    file_name = file_name.strip()
    if not file_name or file_name in [".", ".."]:
        return "File name cannot be empty or a dot"
    if any(c in _BAD_CHARS for c in file_name):
        return "A file name cannot contain any of : " + ", ".join(_BAD_CHARS)
    if file_name.endswith((".", " ")):
        return "A file name cannot end with a dot or space"
    if file_name.startswith((".", " ")):
        return "A file name cannot start with a dot or space"
    
    return None


def ask_number(parent, title: str, label: str, value: int=None, min: int=0, max: int=100) -> int | None:
    while True:
        num, ok = QInputDialog.getInt(
            parent,
            title,
            label,
            value=value,
            min=min,
            max=max,
        )
        if not ok:
            return None
        if num < 0:
            QMessageBox.warning(
                parent,
                title,
                "Number must be greater than or equal to 0",
            )
            continue
        if num is not None:
            return num
        