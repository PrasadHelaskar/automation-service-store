import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, base_log_dir="/mnt/k/automation/Automation_scripts/log", log_level=logging.INFO):
        # Get today's date
        today = datetime.now()
        month = today.strftime("%m")
        date = today.strftime("%d")

        # Define log directory path (by month)
        log_directory = os.path.join(base_log_dir, month)

        # Create directory if it doesn't exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        # Define log file path (by date)
        log_file_path = os.path.join(log_directory, f"{date}.log")

        # Set up logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        
        # Create file handler to log to the dynamically generated log file
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(log_level)
        
        # Create console handler to log to console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)
        
        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add the handlers to the logger
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
