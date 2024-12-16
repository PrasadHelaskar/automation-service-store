import os
import time
from Base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log = Logger().get_logger()
class stripepopup(BasePage):
    __private__heading_new=(By.XPATH,"//h2[@class='cc-heading']")
    __private__heading=(By.CSS_SELECTOR,"div[class='header-text _500 fc2 font-20']")
    __private__strip_pop_up=(By.XPATH,"//*[@id=\"radix-:r1as:\"]")
    __private__card_number_field=(By.NAME,"cardnumber") 
    __private__expiry_date_field=(By.NAME,"exp-date")
    __private__cvv_field=(By.NAME,"cvc")
    __private__zip_field=(By.NAME,"postal")
    __priavte__Confirm_button=(By.CSS_SELECTOR,"button[class='discount-button fc1 bc4 align-right _50 w-button']")
    __priavte__Confirm_button_new=(By.ID,"submitFinalReviewFormBtn")


    # def find_stripe_popup(self):
    #     time.sleep(10)
    #     element=self.find_element(self.__private__strip_pop_up)
    #     if element:
    #         return element
    #     else:
    #         return False

    def check_heading(self):
        try:
            value=self.is_visible(self.__private__heading_new)
            log.warning("Using new value: "+str(value))
            locator=(self.__private__heading_new) if value else (self.__private__heading)
            log.warning("locator is none? : "+str(locator is None))
            op=self.is_visible(locator)
            return op
        except:
            return False

    def enter_card_number(self):
        self.send_keys(self.__private__card_number_field , os.getenv("card_number"))

    def enter_expiry_date(self):
        self.send_keys(self.__private__expiry_date_field, os.getenv("expiry_date"))

    def enter_cvv_number(self):
        self.send_keys(self.__private__cvv_field, os.getenv("cvv_number"))

    def enter_zip_field(self):
        self.send_keys(self.__private__zip_field, os.getenv("zip_code"))

    def click_confirm(self):
        try:
            value=self.is_visible(self.__priavte__Confirm_button_new)
            log.warning("Using new value: "+str(value))
            locator=(self.__priavte__Confirm_button_new) if value else (self.__priavte__Confirm_button)
            log.warning("locator is none? : "+str(locator is None))
            self.click(locator)
        except:
            log.warning("Unable to locate both values")
