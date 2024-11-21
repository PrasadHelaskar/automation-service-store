import os
import time
import logging

from tests.base_page import BasePage

logger = logging.getLogger(__name__)

class screenshot(BasePage):
        def take_screenshot(self, classname):
                screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
                if not os.path.exists(screenshot_dir):
                        os.makedirs(screenshot_dir)
                # logger.info('In the take screenshot method at line 12')
                timestamp = int(time.time())
                # logger.info(f'Timestamp: {timestamp}')
                screenshot_file = os.path.join(screenshot_dir, f"{classname}_{timestamp}.png")
                try:
                        self.driver.save_screenshot(screenshot_file)
                        # logger.info('Screenshot saved successfully.')
                        logger.info(f"Screenshot saved to: {screenshot_file}")
                except Exception as e:
                        logger.error(f"Failed to take screenshot: {str(e)}")    