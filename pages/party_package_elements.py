from base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log = Logger().get_logger(__name__)

class partypackage(BasePage):
    __private_party_page=(By.CSS_SELECTOR, "a[href^='/party']")
    
    def select_party(self,index):
        xpath=f"(//div[@class='ss-card-details top-align'])[{index}]"
        __praivte_party_selection=(By.XPATH, xpath)
        return __praivte_party_selection
    
    __private_expand_button=(By.CSS_SELECTOR, "svg[class='cursor-pointer']")
    
    def select_package(self, index):
        xpath=f"(//div/..//div/..//div/..//a[@class='ss-primary-button--bc4--bw1--oc4--fc1 width-100 padding-8 bottom-20 w-button'])[{index}]"
        __private_package_selection=(By.XPATH, xpath)
        return __private_package_selection
    
    __private_monthSelection=(By.XPATH,"(//button[@class='schedule-top-bar-date-selector--bc3--bw1--fc2 slot width-196 left-align schedule-top-bar-date-selector--bc3--bw1--fc2 slot width-196 left-align'])[1]")

    def selectedMonth(self, index):
        xpath=f"(//button[contains(@class, 'rdp-button') and contains(@class, 'custom-month-picker-button') and not(@disabled)])[{index}]"
        __private_selectedMonth=(By.XPATH,xpath)
        return __private_selectedMonth

    __private_dateSelection=(By.XPATH,"(//button[@class='schedule-top-bar-date-selector--bc3--bw1--fc2 slot width-196 left-align schedule-top-bar-date-selector--bc3--bw1--fc2 slot width-196 left-align'])[2]")

    def selectedDate(self, index):
        xpath=f"(//button[@name='day'])[{index}]"
        __private_selectedDate=(By.XPATH,xpath)
        return __private_selectedDate

    # for the if seen Emty state
    __private_Empty_state=(By.XPATH, "//div[@class='empty-state-text-holder']")
    __priavte_Next_schedule=(By.CSS_SELECTOR, "a[class='discount-button bc4 fc1 w-button']")
    
    def select_schedule(self, index):
        xpath=f"(//div[@class='slot-selection-header padding-t-b-16 bw1 radius-4 padding-16 '])[{index}]"
        __praivte_Schedule=(By.XPATH, xpath)
        return __praivte_Schedule
    
    __praivte_Select_proceed=(By.CSS_SELECTOR, "div[class='discount-button bc4 fc1 w-button']")
    __private_attendee_model=(By.CSS_SELECTOR, "div[class='gs-modal bc3']")
    
    def select_attendee(self,index):
        xpath= f"(//input[@class='w-checkbox-input attendee-checkbox'])[{index}]"
        __private_Attendee_select=(By.XPATH, xpath)
        return __private_Attendee_select
    
    __private_Attendee_Proceed=(By.XPATH, "//div[@class='discount-button bc4 align-right _50 w-button']")
    __private_addonpage=(By.XPATH,"//div[@class='add-on-section bc4_a bw1t bottom-120']") 
    __private_additional_attendee=(By.XPATH, "(//button[@class='add-section fc4 oc4 justify-centre'])[1]") 
    __private_Addon_Proceed=(By.XPATH, "//div[@class='review-cta-section  justify-left bc3 space-between']/button")
    __private_Waiver_Checkbox=(By.ID, "checkbox-3")
    __private_Review_Proceed_cardno=(By.CSS_SELECTOR,"div[class='stripeModal']")
    __private_Review_Proceed_card=(By.CSS_SELECTOR,"div[class='discount-button fc1 bc4 w-button one']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")
    
    #Actions Methods

    def click_party_tab(self):
        self.click(self.__private_party_page)

    def click_party_select(self,index):
        self.click(self.select_party(index))

    def click_expand(self):
        self.click(self.__private_expand_button)
    
    def click_package(self,index):
        self.click(self.select_package(index))

    def visible_empty_state(self):
        try:
            op=self.is_visible(self.__private_Empty_state)
            log.info("Is Schedule available in month?:%s",str(not(op)))
            return op
        except Exception as e:
            return False

    def click_monthSelection(self):
        self.click(self.__private_monthSelection)

    def click_selectedMonth(self,index):
        self.click(self.selectedMonth(index))

    def click_dateSelection(self):
        self.click(self.__private_dateSelection)

    def click_selectedDate(self,index):
        self.click(self.selectedDate(index))

    def text_empty_state(self):
        self.get_text(self.__private_Empty_state)
        
    def click_next_schedule(self):
        self.click(self.__priavte_Next_schedule)

    def click_schedule_selection(self, index):
        self.click(self.select_schedule(index))

    def click_schedule_proceed(self):
        self.click(self.__praivte_Select_proceed)

    def visible_attendee_model(self):
        try:
            op=self.is_visible(self.__private_attendee_model)
            return op
        except:
            return False

    def click_attendee_seletion(self, index):
        self.click(self.select_attendee(index))

    def click_attendee_proceed(self):
        self.click(self.__private_Attendee_Proceed)

    def click_additiona_attendee(self):
        self.click(self.__private_additional_attendee)

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
        log.info("click_review_proceed > "+str(value))
        locator=(self.__private_Review_Proceed_cardno) if value else (self.__private_Review_Proceed_card)
        self.click(locator)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)
