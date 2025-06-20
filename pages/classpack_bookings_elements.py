from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log = Logger().get_logger(__name__)
class classpackbooking(BasePage):
    __private_FILTER_CHECKBOX= (By.XPATH,"(//input[@type='checkbox'])[2]")
    __private_APPLY_BUTTON=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']") 
    __private_select_proceed= (By.ID, "classpack_proceed_btn")
    __private_classpack_page=(By.CSS_SELECTOR,"a[href^='/classpacks']")
    __private_program_page=(By.CSS_SELECTOR,"a[href^='/programs']")
    __private_select_service_name=(By.XPATH,"//div[@class='ss-card-title--fc2--lc2 font-18']")

    def select_service(self,i):
        xpath=f"(//a[@class='primary-button-card bc4 fc1'])[{i}]"
        __private_select_service=(By.XPATH,xpath)
        return __private_select_service

    def select_service_name(self,i):
        xpath=f"(//div[@class='ss-card-title--fc2--lc2 font-18'])[{i}]"
        __private_select_service_name=(By.XPATH,xpath)
        return __private_select_service_name
    
    def select_start_date(self,i):
        xpath=f"(//input[@name='cp-radio-button'])[{i}]"
        __private_select_start_date=(By.XPATH,xpath)
        return __private_select_start_date
    
    __private_attendee_model=(By.CSS_SELECTOR, "h4[class='h5-regular modal-title ']")
    
    def attendee_xpath(self,count):
        xpath=f"(//input[@name='attendees-id-list'])[{count}]"
        __private_attendee_select=(By.XPATH,xpath)
        return __private_attendee_select
    
    __private_attendee_proceed=(By.XPATH, "//a[@class='booking-footer-button small w-inline-block w-clearfix next-btn-classpack-modal bc4']")
    __private_waiver_checkbox=(By.ID, "waiverCheckbox")
    __private_Review_Proceed_cardno=(By.ID,"submitFinalReviewFormBtn")
    __private_Review_Proceed_card=(By.ID,"submitFinalReviewFormBtn")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")
    
    # repeat booking model locatores
    __repeat_booking_model=(By.CSS_SELECTOR, "div[class='modal-wrapper']")
    __repeat_booking_model_confirm=(By.ID,"re-buy-classpack")

    # Credit booking page locatores
    __private_credit_booking_class=(By.NAME, "checkbox-13")
    __private_confirm_booking=(By.XPATH, "//button[@class='cta-sec-button pri bc4 fc1 w-button']")
    __private_skip_button=(By.ID,"skipButton")
    __private_client_profile_back=(By.CSS_SELECTOR,"div[class='back-text normal cursor-pointer']")

    # age restriction model locators
    __private_restriction_model=(By.XPATH, "(//div[@class='conflict-modal booking-restriction-modal'])[3]")
    __private_age_restriction_message=(By.ID, "warning-title")
    __private_redirect_home=(By.CSS_SELECTOR,"a[href='/']")

    def click_classpack_page(self):
        self.click(self.__private_classpack_page)

    def click_program_page(self):
        self.click(self.__private_program_page) 

    def click_classpack_checkbox(self):
        self.click(self.__private_FILTER_CHECKBOX)

    def click_apply(self):
        self.click(self.__private_APPLY_BUTTON)
    
    def click_select_service(self,i):
        name=self.get_text(self.select_service_name(i))
        log.info("Service Name: %s",name)
        self.click(self.select_service(i))

    def click_start_date(self,i):
        self.click(self.select_start_date(i))

    def click_proceed(self):
        self.click(self.__private_select_proceed)

    def click_waiver_box(self):
        self.click(self.__private_waiver_checkbox)

    def click_review_proceed(self):
        try:    
            value=self.is_visible(self.__private_Review_Proceed_cardno)
        except Exception as e:
            log.error("Exception occurred: %s",e)
            value=False
        
        locator=(self.__private_Review_Proceed_cardno) if value else (self.__private_Review_Proceed_card)
        self.click(locator)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)

    def visible_attendee_model(self):
        try:
            op=self.is_visible(self.__private_attendee_model)
            return op
        except Exception as e:
            log.error("Exception occurred: %s",e)
            return False
    
    def click_attendee_box(self,i):
        self.click(self.attendee_xpath(i))

    def click_attendee_proceed(self):
        self.click(self.__private_attendee_proceed)

    def click_credit_booking_class(self):
        if self.is_visible(self.__private_credit_booking_class):
            self.click(self.__private_credit_booking_class)
            return True
        else:
            log.info("Success page loaded, but no schedules were found to display.")
            return False

    def click_confirm_booking(self):
        self.click(self.__private_confirm_booking)

    def click_skip_button(self):
        self.click(self.__private_skip_button)

    def click_back_client_profile(self):
        self.click(self.__private_client_profile_back)

    def is_repeat_booking_visible(self):
        try:
            value=self.is_visible(self.__repeat_booking_model)
            return value
        except Exception as e:
            log.error("Exception occurred: %s",e)
            return False

    def click_buy_again(self):
        self.click(self.__repeat_booking_model_confirm)

    def get_service_name(self):
        try:
            elements=self.find_elements_wait(self.__private_select_service_name)
        
            return elements

        except Exception as e:
            log.error("Exception occurred: %s",e)

    def is_restriction_model_visible(self):
        value=self.is_visible(self.__private_restriction_model)
        return value
    
    def get_restriction_head_message(self):
        text=self.get_text(self.__private_age_restriction_message)
        return text
    
    def click_go_back(self):
        self.click(self.__private_redirect_home)