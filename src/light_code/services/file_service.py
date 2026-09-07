# services/file_service.py

from pathlib import Path

from light_code.utils.logger import logger


def read_file(file_path):
    """
    Reads the content of a file and returns it along with the file name.
    """
    try:
        logger.info(f"Reading file: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise
    else:
        logger.info(f"Successfully read file: {file_path}")
        file_name = Path(file_path).name
        return content, file_name

def write_file(file_path, content):
    """
    Writes content to a file.
    """
    try:
        logger.info(f"Writing file: {file_path}")
        with open(file_path, 'w', encoding='utf-8', newline="") as file:
            file.write(content)
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
