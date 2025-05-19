import os
import time
import logging
import inspect

from tests.base_page import BasePage

logger = logging.getLogger(__name__)

class screenshot(BasePage):
        def take_screenshot_fail(self, classname):
                screenshot_dir = os.path.join(os.getcwd(), "On_Fail_Screenshots")
                
                if not os.path.exists(screenshot_dir):
                        os.makedirs(screenshot_dir)
                timestamp = int(time.time())
                screenshot_file = os.path.join(screenshot_dir, f"{classname}_{timestamp}.png")
                
                try:
                        self.driver.save_screenshot(screenshot_file)
                        logger.info(f"Screenshot saved to: {screenshot_file}")
                
                except Exception as e:
                        logger.error(f"Failed to take screenshot: {str(e)}")    

        def take_screenshot(self,request):
                screenshot_dir = os.path.join(os.getcwd(), "Screenshots")
                
                if not os.path.exists(screenshot_dir):
                        os.makedirs(screenshot_dir)
                screenshot_name = os.path.join(screenshot_dir, f"{request.node.name}_url_change_{int(time.time())}.png")
                
                try:
                        self.driver.save_screenshot(screenshot_name)
                
                except Exception as e:
                        logger.error(f"Failed to take screenshot: {str(e)}")    
        
        def take_screenshot_direct(self):
                screenshot_dir = os.path.join(os.getcwd(), "requested_Screenshots")
                
                if not os.path.exists(screenshot_dir):
                        os.makedirs(screenshot_dir)

                caller = inspect.stack()[1].function
                screenshot_name = os.path.join(
                        screenshot_dir, f"{caller}_{int(time.time())}.png"
                )

                try:
                        self.driver.save_screenshot(screenshot_name)
                        logger.info(f"Screenshot saved to {screenshot_name}")
                
                except Exception as e:
                        logger.error(f"Failed to take screenshot: {str(e)}")