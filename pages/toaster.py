from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger()

class toaster_message_elements(BasePage):
    __private_toaster=(By.CSS_SELECTOR, "div[class='Toastify__toast Toastify__toast-theme--light Toastify__toast--error Toastify__toast--close-on-click']")
    __private_invalid_gift_card_text=(By.XPATH,"//div[@class='Toastify__toast-body']//div[2]")


    def is_toaster_visible(self):
        value=self.is_visible(self.__private_toaster)
        log.info("Is Toaster Visible? > "+str(value))
        if value:
            return value 
        else:
            return False
        
    def get_toaster_text(self):
        text=self.get_text(self.__private_invalid_gift_card_text)
        if  (text):
            log.info("Toaster text > "+str(text))
            return text
        else:
            return None