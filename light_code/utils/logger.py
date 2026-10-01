# utils/logger.py

import logging

logging.basicConfig(
    format="%(levelname)s - File: %(filename)s, Func: %(funcName)s, Line: %(lineno)d - %(message)s",
    datefmt="%I:%M:%S %p",
    level=logging.DEBUG,
)


def setup_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


logger = setup_logger(__name__)
