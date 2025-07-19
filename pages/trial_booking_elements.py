from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger(__name__)

class trialkbooking(BasePage):
    __private_program_page=(By.CSS_SELECTOR,"a[href^='/programs']")
    def select_service(self,i):
        xpath=f"(//a[@class='secondary-button-card bw1 oc4 fc4'])[{i}]"
        __private_select_service=(By.XPATH,xpath)
        return __private_select_service
    
    __private_select_proceed= (By.ID, "classpack_proceed_btn")
    __private_attendee_model=(By.CSS_SELECTOR, "div[class='cs-modal-hero-section select-family-members bc3']")
    
    def attendee_xpath(self,count):
        xpath=f"(//input[@name='attendees-id-list'])[{count}]"
        __private_attendee_select=(By.XPATH,xpath)
        return __private_attendee_select
    
    __private_attendee_proceed=(By.XPATH, "//a[@class='booking-footer-button small w-inline-block w-clearfix next-btn-classpack-modal bc4']")
    __priavte_cross_button=(By.ID,"close_age_modal")
    __private_Addon_proceed=(By.ID,"proceed-btn")
    __private_waiver_checkbox=(By.ID, "waiverCheckbox")
    __private_Review_Proceed_cardno=(By.XPATH,"//span[@id='totalPriceHolder' and @class='fc3 confirm-text']")
    __private_Review_Proceed_card=(By.ID,"submitFinalReviewFormBtn")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")

    #Warning model
    __private_warning_model=(By.XPATH,"(//div[@class='conflict-modal booking-restriction-modal'])[3]")

    def click_program_page(self):
        self.click(self.__private_program_page) 

    def click_select_service(self,i):
        self.click(self.select_service(i))

    def click_proceed(self):
        self.click(self.__private_select_proceed)
    
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

    def click_cross_button(self):
        self.click(self.__priavte_cross_button)

    def click_addon_proceed(self):
        self.click(self.__private_Addon_proceed)

    def visible_warning_model(self):
        try:
            op=self.is_visible(self.__private_warning_model)
            return op
        except:
            return False

    def click_waiver_box(self):
        self.click(self.__private_waiver_checkbox)

    def click_review_proceed(self):
        try:    
            value=self.is_visible(self.__private_Review_Proceed_cardno)
        except:
            value=False
        
        # log.info("click_review_proceed value: %s",value)
        locator=(self.__private_Review_Proceed_cardno) if value else (self.__private_Review_Proceed_card)
        # log.info("click_review_proceed locator: %s",locator)
        self.click(locator)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)
