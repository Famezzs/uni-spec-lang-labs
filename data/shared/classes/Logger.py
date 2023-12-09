__all__ = ['Logger']
import logging
from datetime import datetime


class Logger:
    """
    A class for logging messages to a file.

    This class provides functionality to log warning messages to a specified file. 
    The logging configuration is set up during initialization.

    Attributes:
        logs_file_path (str): The path of the file where logs will be saved.

    Methods:
        log_warning(message: str): Logs a warning message with a timestamp.
    """

    def __init__(self, logs_file_path):
        """
        Initializes the Logger with a specified file path for logging.

        Args:
            logs_file_path (str): The path of the file where logs will be saved.
        """
        self.logs_file_path = logs_file_path
        logging.basicConfig(filename=self.logs_file_path, encoding='utf-8', level=logging.WARNING)

    @staticmethod
    def log_warning(message: str):
        """
        Logs a warning message to the file, including a timestamp.

        Args:
            message (str): The warning message to be logged.
        """
        logging.warning(f"[{datetime.now()}]: {message}")
