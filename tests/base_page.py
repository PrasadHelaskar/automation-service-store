from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Base.logfile import Logger

log = Logger().get_logger()
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find_element_wait(self,locator):
        op=self.wait.until(EC.visibility_of_element_located(locator))
        return op

    def click(self, locator):
        element = self.find_element_wait(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element= self.find_element_wait(locator)
        element_text=element.text
        # log.info(element_text)
        return element_text

    def is_visible(self, locator):
        try:
            element=self.find_element_wait(locator)
            op=element.is_displayed()
            # log.info(f"Base page > is_visible > {op}")
            return str(op)
        except:
            return False
    
    def clear_element(self, locator):
        element=self.find_element_wait(locator)
        element.clear()