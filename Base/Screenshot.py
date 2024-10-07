import os
import time
import logging

logger = logging.getLogger(__name__)

def setUp(self):
        self.screenshot_dir = os.path.join(os.getcwd(), "/mnt/k/automation/Automation_scripts/Screenshots")
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)  # Create directory if it doesn't exist

def take_screenshot(self):
        logger.info('in the take scrennshot methond')
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        print('timestamp: ',timestamp)
        screenshot_file = os.path.join(self.screenshot_dir, f"{timestamp}.png")
        self.driver.save_screenshot(screenshot_file)
        print(f"Screenshot saved to: {screenshot_file}")