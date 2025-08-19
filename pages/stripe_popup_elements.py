import os
from base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log = Logger().get_logger(__name__)
class stripepopup(BasePage):
    __private__heading_new=(By.XPATH,"//div[@class='credit-debit-header cc-heading']")
    __private__heading=(By.CSS_SELECTOR,"div[class='ss-modal-header--fc2 padding-16 gs bc3']")
    __private__strip_pop_up=(By.XPATH,"//*[@id=\"radix-:r1as:\"]")
    __private__card_number_field=(By.NAME,"cardnumber") 
    __private__expiry_date_field=(By.NAME,"exp-date")
    __private__cvv_field=(By.NAME,"cvc")
    __private__zip_field=(By.NAME,"postal")
    __private__Confirm_button=(By.CSS_SELECTOR,"button[class='discount-button fc1 bc4 align-right w-button']")
    __private__Confirm_button_new=(By.CSS_SELECTOR,"button[id='submitFinalReviewFormBtn']")
    __private__payable=(By.ID, "totalPriceHolder")
    __private__payable_new=(By.XPATH, "")


    # def find_stripe_popup(self):
    #     time.sleep(10)
    #     element=self.find_element(self.__private__strip_pop_up)
    #     if element:
    #         return element
    #     else:
    #         return False

    def check_heading(self):
        # log.info("Check Heading Method")
        try:
            value=self.is_visible(self.__private__heading_new)
            # log.warning("Using new value: "+str(value))
            locator=(self.__private__heading_new) if value else (self.__private__heading)
            # log.warning("locator is none? : %s",str(locator is None))
            op=self.is_visible(locator)
            return op
        
        except Exception as e:
            log.info("Check Heading Method Exception: %s",e)
            return False

    def enter_card_number(self):
        self.send_keys(self.__private__card_number_field , os.getenv("CARD_NUMBER"))

    def enter_expiry_date(self):
        self.send_keys(self.__private__expiry_date_field, os.getenv("EXPIRY_DATE"))

    def enter_cvv_number(self):
        self.send_keys(self.__private__cvv_field, os.getenv("CVV_NUMBER"))

    def enter_zip_field(self):
        self.send_keys(self.__private__zip_field, os.getenv("ZIP_CODE"))

    def click_confirm(self):
        # log.info("Click Confirm Method")
        try:
            value=self.is_visible(self.__private__Confirm_button_new)
            locator=(self.__private__Confirm_button_new) if value else (self.__private__Confirm_button)
            # log.warning("Using new value: %s",str(value))
            self.click(locator)
        
        except Exception as e:
            log.warning("Unable to locate both values: %s",e)

    def get_payable(self):
        # log.info("Get Payable Method")
        try:
            value=self.is_visible(self.__private__payable_new)
            log.warning("Using new value: %s",str(value))
            locator=(self.__private__payable_new) if value else (self.__private__payable)
            payable=self.get_text(locator)
            log.info("Total payable for Service: %s",payable)
        
        except Exception as e:
            log.warning("Unable to locate both values: %s",e)