from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Base.logfile import Logger

log = Logger().get_logger()
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element= self.find_element(locator)
        element_text=str(element.text)
        log.info(element_text)
        return element_text

    def is_visible(self, locator):
        element=self.find_element(locator)
        op=element.is_displayed
        log.info(op)
        return(op)