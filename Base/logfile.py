import logging
from datetime import datetime
import os

class MyLogger:
    logger = logging.getLogger(__name__)
    
    @staticmethod
    def setup():
        try:
            # Get today's date
            today = datetime.now()
            month = today.strftime("%m")
            date = today.strftime("%d")
            
            # Define log directory path
            log_directory = os.path.join("/mnt/k/automation/Automation_scripts/log", month)  # Change this path as needed
            
            # Create directory if it doesn't exist
            if not os.path.exists(log_directory):
                os.makedirs(log_directory)
            
            # Define log file path
            log_file_path = os.path.join(log_directory, f"{date}.log")
            
            # Set up file handler
            file_handler = logging.FileHandler(log_file_path, mode='a')
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

            # Check if a file handler already exists
            if not any(isinstance(handler, logging.FileHandler) for handler in MyLogger.logger.handlers):
                MyLogger.logger.addHandler(file_handler)

            MyLogger.logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of logs

        except Exception as e:
            MyLogger.logger.error("Failed to set up logger", exc_info=e)

    @staticmethod
    def get_logger():
        return MyLogger.logger
