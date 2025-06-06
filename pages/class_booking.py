from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger()

class class_booking(BasePage):
    __private__home_page=(By.CSS_SELECTOR, "a[href='/home']")
    __private__service_type=(By.XPATH, "(//label[@class='w-checkbox form_main_checkbox-wrap--pb0-5']//span[@class='form_main_field-label-fs8-5 w-form-label'])[1]")
    __private_checkbox=(By.XPATH,"//input[@class='w-checkbox-input w-checkbox-input--inputType-custom form_main_button--bw1-oc2 filter-checkbox']")
    __private_filter_submit=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']")
    __private_attendee_proceed=(By.XPATH, "(//div[@class='fc3 booking-footer-button-text-left attendee-form-done button-text-medium-regular'])[1]")
    __private_addonpage=(By.XPATH,"//div[@class='add-on-section bc4_a bw1t bottom-120']")
    __private_credit_booking=(By.ID,"select-credit-label")

    def attendee_xpath(self,count):
        xpath=f"(//input[@name='attendees-id-list'])[{count}]"
        __private_attendee_select=(By.XPATH,xpath)
        return __private_attendee_select

    def book_button(self,i):
        xpath=f"(//a[@data-w-id='bd14a762-7e6e-a4d0-06b1-dd4b2b8fe0da'])[{i}]"
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

    def click_home(self):
        self.click(self.__private__home_page)

    def get_checkbox_text(self):
        service_type=self.get_text(self.__private__service_type)
        return service_type
    
    def click_checkbox(self):
        self.click(self.__private_checkbox)

    def click_filter_submit(self):
        self.click(self.__private_filter_submit)

    def click_book_button(self,i):
        self.click(self.book_button(i))

    def get_service_name(self)->str:
        text=self.get_text(self.__private__service_name)
        return text
    
    def click_schedule(self,i):
        self.click(self.schedules(i))

    def click_checkout_proceed(self):
        self.click(self.__private__proceed_button)

    def click_review_proceed(self):
        self.click(self.__priavte__proceed_review)
    
    def click_back_to_home(self):
        self.click(self.__private_HOME_BUTTON)

    def click_attendee_box(self,i):
        self.click(self.attendee_xpath(i))
    
    def click_attendee_proceed(self):
        self.click(self.__private_attendee_proceed)

    def visible_addon_page(self):
        try:
            op=self.is_visible(self.__private_addonpage)
            log.info("add on page check:"+str(op))   
            return op
        except Exception as e:
            return False
        
    def is_credit_booking(self)->str:
        try:
            text=self.get_text(self.__private_credit_booking)
            return text
        except Exception as e:
            return False