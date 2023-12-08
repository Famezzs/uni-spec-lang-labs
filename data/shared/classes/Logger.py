import logging

class Logger:
    def __init__(self, logs_file_path):
        self.logs_file_path = logs_file_path
        logging.basicConfig(filename=self.logs_file_path, encoding='utf-8', level=logging.WARNING)

    def log_warning(self, message: str):
        from datetime import datetime
        logging.warning(f"[{datetime.now()}]: {message}")