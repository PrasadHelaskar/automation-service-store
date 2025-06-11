from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger(__name__)

class MembershipBooking(BasePage):
    __private_subscriptions_page=(By.CSS_SELECTOR,"a[href^='/subscriptions']")
    __private__service_type=(By.XPATH, "(//label[@class='w-checkbox form_main_checkbox-wrap--pb0-5']//span[@class='form_main_field-label-fs8-5 w-form-label'])[2]")
    __private_checkbox=(By.XPATH,"(//input[@class='w-checkbox-input w-checkbox-input--inputType-custom form_main_button--bw1-oc2 filter-checkbox'])[2]")
    __private__filter_apply=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']") 
    
    def service_selection(self,i):
        xpath=f"(//div[@class='ss-card-details top-align'])[{i}]"
        __private_service_selection=(By.XPATH,xpath)

        return __private_service_selection
    
    __private_expand_pop_up=(By.CSS_SELECTOR,"svg[class='cursor-pointer']")
    __private_book_button=(By.CSS_SELECTOR,"a[class='primary-button-card bc4 fc1']")
    
    def membership_durations(self,i):
        xpath=f"(//li[@class='booking-content-list-item classes-list w-clearfix'])[{i}]"
        __private_membership_durations=(By.XPATH,xpath)

        return __private_membership_durations

    __private_checkout_proceed=(By.CSS_SELECTOR,"div[class='booking-footer-button-text-right move-next fc3 button-text-medium-regular']")

    __private_attendee_model=(By.CSS_SELECTOR, "h4[class='h5-regular modal-title ']")
    
    def attendee_xpath(self,count):
        xpath=f"(//input[@name='attendees-id-list'])[{count}]"
        __private_attendee_select=(By.XPATH,xpath)
        return __private_attendee_select
    
    __private_attendee_proceed=(By.XPATH, "(//div[@class='fc3 booking-footer-button-text-left attendee-form-done button-text-medium-regular'])[1]")
    __private_addonpage=(By.XPATH,"//div[@class='add-on-section bc4_a bw1t bottom-120']") 
    __priavte__proceed_review=(By.XPATH,"//span[@id='totalPriceHolder' and @class='fc3 confirm-text']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")

    #Action Methods
    def click_subscriptions_page(self):
        self.click(self.__private_subscriptions_page)

    def get_checkbox_text(self):
        service_type=self.get_text(self.__private__service_type)
        return service_type
    
    def click_checkbox(self):
        self.click(self.__private_checkbox)

    def click_apply_filter(self):
        self.click(self.__private__filter_apply)

    def click_service_selection(self,i):
        self.click(self.service_selection(i))

    def click_expand(self):
        self.click(self.__private_expand_pop_up)

    def click_book(self):
        self.click(self.__private_book_button)
    
    def click_membership_duration(self,i):
        self.click(self.membership_durations(i))

    def click_checkout_proceed(self):
        self.click(self.__private_checkout_proceed)

    def attendee_model_visible(self):
        seen=self.is_visible(self.__private_attendee_model)
        return seen

    def click_attendee_box(self,i):
        self.click(self.attendee_xpath(i))
    
    def click_attendee_proceed(self):
        self.click(self.__private_attendee_proceed)

    def addon_page_visible(self):
        op=self.is_visible(self.__private_addonpage)   
        return op
    
    def visible_addon_page(self):
        try:
            op=self.is_visible(self.__private_addonpage)
            log.info("add on page check:"+str(op))   
            return op
        except Exception as e:
            return False
        
    def click_review_proceed(self):
        self.click(self.__priavte__proceed_review)
    
    def click_back_to_home(self):
        self.click(self.__private_HOME_BUTTON)