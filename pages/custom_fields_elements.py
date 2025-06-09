import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log= Logger().get_logger()

class custom_fields(BasePage):
    __private__custome_field_page=(By.ID, "prebookingfields")
    __private__attendee=(By.XPATH,"//span[@class='text-capitalize']")
    __private__all_custome_fields=(By.XPATH, "//form[@id='before-booking-extra-f']//input[@name]")
    __private__proceed=(By.ID,"sub-btn")
    __private__custom_field_div=(By.CSS_SELECTOR,"div[class='custom-mob']")

    def is_visible_page(self):
        value=self.is_visible(self.__private__custome_field_page)
        return value
    
    def get_attendee_name(self):
        name=self.get_text(self.__private__attendee)
        return name
    
    def get_all_custom_fields(self):
        elements=self.find_elements_wait_presence(self.__private__all_custome_fields)
        return elements
    
    def click_proceed(self):
        self.click(self.__private__proceed)
        time.sleep(2)
    
    def custom_field_div(self):
        element=self.find_element_wait(self.__private__custom_field_div)
        return element
    


