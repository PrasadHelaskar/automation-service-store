from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from Base.logfile import Logger

log=Logger().get_logger()

class camp_booking(BasePage):
    __private_camp_page=(By.CSS_SELECTOR ,"a[href='/camps?b=t']")
    def service_select(self, service):
        xpath=f"(//a[@class='primary-button-card bc4 fc1'])[{service}]"
        __private_camp_selection=(By.XPATH, xpath)
        return __private_camp_selection
    
    __private_add_attendee=(By.ID, "addCampAttendeeBtn")
    def select_attendee(self , i):
        xpath=f"(//div[@class='checkbox w-checkbox'])[{i}]"
        __private_attendee_select=(By.XPATH, xpath)
        return __private_attendee_select
    
    __private_attendee_proced=(By.XPATH, "(//div[@class='fc3 booking-footer-button-text-left attendee-form-done button-text-medium-regular'])[1]")
    def select_schedule(self, i):
        xpath=f"(//input[@class='w-checkbox-input class-schedule-check'])[{i}]"
        __private_schedule_select=(By.XPATH, xpath)
        return __private_schedule_select
    
    __private_schedule_proceed=(By.ID,"class_go_next_btn")
    __private_addonpage=(By.XPATH,"//div[@class='add-on-section bc4_a bw1t bottom-120']")
    __private_Addon_Proceed=(By.XPATH, "//button[@class='discount-button bc4 shrink w-button']")
    __private_Waiver_Checkbox=(By.ID, "waiverCheckbox")
    __private_Review_Proceed_cardno=(By.ID, "submitFinalReviewFormBtn")
    __private_Review_Proceed_card=(By.CSS_SELECTOR,"div[class='fc3 booking-footer-button-text-right body-text-2-medium']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")


    def click_camp_page(self):
        self.click(self.__private_camp_page)

    def click_camp_selection(self, service_index):
        self.click(self.service_select(service_index))

    def click_add_attendee(self):
        self.click(self.__private_add_attendee)

    def click_attendee(self,i):
        self.click(self.select_attendee(i))

    def click_attendee_proceed(self):
        self.click(self.__private_attendee_proced)

    def click_schedule(self,i):
        try:
            self.click(self.select_schedule(i))
        except:
            log.error("Schedule is not available")

    def click_schedule_proceed(self):
        self.click(self.__private_schedule_proceed)

    def visible_addon_page(self):
        try:
            op=self.is_visible(self.__private_addonpage)
            log.info("add on page check:"+str(op))   
            return op
        except:
            return False

    def click_addon_proceed(self):
        self.click(self.__private_Addon_Proceed)

    def click_waiverbox(self):
        self.click(self.__private_Waiver_Checkbox)

    def click_review_proceed(self):
        try:    
            value=self.is_visible(self.__private_Review_Proceed_cardno)
        except:
            value=False
        locator=(self.__private_Review_Proceed_cardno) if value else (self.__private_Review_Proceed_card)
        self.click(locator)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)
