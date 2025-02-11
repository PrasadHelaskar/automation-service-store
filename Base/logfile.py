import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, base_log_dir="/mnt/k/automation/Automation_scripts/log", log_level=logging.INFO):
        today = datetime.now()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        date = today.strftime("%d")
        year_directory = os.path.join(base_log_dir, year)
        log_directory = os.path.join(year_directory, month)
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)
        log_file_path = os.path.join(log_directory, f"{date}.log")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_file_path)
            file_handler.setLevel(log_level)
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger


# Usage
# if __name__ == "__main__":
#     log = Logger().get_logger()

#     log.debug('This is a debug message')
#     log.info('This is an info message')
#     log.warning('This is a warning message')
#     log.error('This is an error message')
#     log.critical('This is a critical message')
