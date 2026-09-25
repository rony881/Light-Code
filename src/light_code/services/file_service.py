# services/file_service.py

from dataclasses import dataclass
from os import path
from pathlib import Path

from light_code.utils.logger import logger


class UnsupportedFileError(Exception):
    """File can't or shouldn't be opened in the editor."""

@dataclass
class FileContent:
    text: str
    type: str

MAX_TEXT_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

def read_file(file_path) -> FileContent:
    logger.info(f"Reading file: {file_path}")
    file_path = Path(file_path)

    if not file_path.is_file():
        raise UnsupportedFileError("Not a regular file.")

    with file_path.open("rb") as f:
        head = f.read(8192)
    if b"\x00" in head:
        raise UnsupportedFileError(
            "Cannot open.Looks like a binery file (video, image, archive, etc.)."
        )
        
    file_size = file_path.stat().st_size
    if file_size > MAX_TEXT_FILE_SIZE:
        raise UnsupportedFileError(
            "Cannot open file."
            f"File is too large ({file_size / 1024 / 1024:.1f} MB, "
            f"limit is {MAX_TEXT_FILE_SIZE // 1024 // 1024} MB)."
        )
    text = file_path.read_text(encoding="utf-8-sig")
    return FileContent(text=text, type=file_path.suffix)

    
def write_file(file_path, content):
    """Writes content to a file."""
    file_path = Path(file_path)
    try:
        logger.info(f"Writing file: {file_path}")
        file_path.write_text(content, encoding="utf-8", newline="")
    except Exception as e:
        logger.error(f"Error writing file: {e}")
        raise
    else:
        logger.info(f"Successfully wrote file: {file_path}")


def rename_file(old_file_path, new_file_name):
    """
    Renames a file.
    Returns:
        Path: The new file path.
    """
    old_file_path = Path(old_file_path)
    new_file_name = Path(new_file_name)

    if new_file_name.suffix:
        new_file_path = old_file_path.parent / new_file_name.name
    else:
        new_file_path = old_file_path.parent / (
            new_file_name.name + old_file_path.suffix
        )

    try:
        logger.info(f"Renaming file: {old_file_path} to {new_file_path}")
        old_file_path.rename(new_file_path)
    except Exception as e:
        logger.error(f"Error renaming file: {e}")
        raise
    else:
        logger.info(f"Successfully renamed file: {old_file_path} to {new_file_path}")
        return new_file_path
