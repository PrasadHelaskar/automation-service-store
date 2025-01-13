import os
import time
from Base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log=Logger().get_logger()

class waiver_vima(BasePage):
    __private_waiver_box=(By.XPATH, "(//div[@class='gs-modal bc3'])[1]")
    __private_accept_waiver=(By.CSS_SELECTOR, "button[class='discount-button fc1 bc4 align-right _50 w-button']")
    __private_review_checkbox=(By.NAME, "checkbox-3")

    def check_waiver_box(self):
        try:
            op=self.is_visible(self.__private_waiver_box)
            return op
        except Exception as e:
            log.warning(str(e))
            return False
        
    def click_accept_waiver(self):
        self.click(self.__private_accept_waiver)
    
    def click_waiver(self):
        self.click(self.__private_review_checkbox)
