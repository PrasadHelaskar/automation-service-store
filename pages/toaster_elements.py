from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger()

class toaster_message_elements(BasePage):
    __private_toaster=(By.CSS_SELECTOR, "div[class='Toastify__toast Toastify__toast-theme--light Toastify__toast--error Toastify__toast--close-on-click']")
    __private_toaster_old=(By.CSS_SELECTOR, "div[class='toast-message']")
    __private_invalid_gift_card_text=(By.XPATH,"//div[@class='Toastify__toast-body']//div[2]")


    def is_toaster_visible(self):
        """Method for checking toster Visibility"""
        value=self.is_visible(self.__private_toaster)
        value_old=self.is_visible(self.__private_toaster_old)
        log.info("Is Toaster Visible? > %s",str(value))
        if value or value_old:
            return True
        
        return False
        
    def get_toaster_text(self):
        """Text for gift card validation"""
        text=self.get_text(self.__private_invalid_gift_card_text)
        if(text):
            log.info("Toaster text > %s",str(text))
            return text
        
        return None