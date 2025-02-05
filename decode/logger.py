import logging
import sys
from typing import Optional

PROJECT = "decode"


class Logger:
    _instance: Optional["Logger"] = None
    _logger: Optional[logging.Logger] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._setup_logger()
        return cls._instance

    @classmethod
    def _setup_logger(cls):
        cls._logger = logging.getLogger(PROJECT)
        cls._logger.setLevel(logging.INFO)

        # Create console handler with formatting
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        cls._logger.addHandler(console_handler)

    @property
    def logger(self) -> logging.Logger:
        if self._logger is None:
            self._setup_logger()
        return self._logger


logger = Logger().logger
