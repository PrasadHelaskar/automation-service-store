from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger()

class class_booking(BasePage):
    __private__home_page=(By.CSS_SELECTOR, "a[href='/home']")
    __private__service_type=(By.XPATH, "//label[@class='w-checkbox form_main_checkbox-wrap--pb0-5']//span[@class='form_main_field-label-fs8-5 w-form-label']")
    __private_checkbox=(By.XPATH,"//input[@class='w-checkbox-input w-checkbox-input--inputType-custom form_main_button--bw1-oc2 filter-checkbox']")
    __private_filter_submit=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']")

    def book_button(self,i):
        xpath=f"(//a[@data-w-id='bd14a762-7e6e-a4d0-06b1-dd4b2b8fe0da'])({i})"
        __private_book_button=(By.XPATH,xpath)
        return __private_book_button
    
    __private__service_name=(By.CSS_SELECTOR,"div[class='fc2 class-title']")

    def schedules(self,i):
        xpath=f"(//input[@class='w-checkbox-input class-schedule-check'])[{i}]"
        __private_schedule_checkbox=(By.XPATH,xpath)
        return __private_schedule_checkbox
    
    __private__proceed_button=(By.ID,"class_go_next_btn")
    __priavte__proceed_review=(By.XPATH,"//span[@id='totalPriceHolder' and @class='fc3 confirm-text']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")

    