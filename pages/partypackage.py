from base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log = Logger().get_logger()

class partypackage(BasePage):
    __private_party_page=(By.CSS_SELECTOR, "a[href^='/party']")
    
    def select_party(self,index):
        xpath=f"(//div[@class='ss-card--bc3--br2-bw1--oc5 '])[{index}]"
        __praivte_party_selection=(By.XPATH, xpath)
        return __praivte_party_selection
    
    __private_expand_button=(By.CSS_SELECTOR, "svg[class='cursor-pointer']")
    
    def select_package(self, index):
        xpath=f"(//div/..//div/..//div/..//a[@class='ss-primary-button--bc4--bw1--oc4--fc1 width-100 padding-8 bottom-20 w-button'])[{index}]"
        __private_package_selection=(By.XPATH, xpath)
        return __private_package_selection
    # for the if seen Emty state

    __private_Empty_state=(By.XPATH, "//div[@class='empty-state-text-holder']")
    __priavte_Next_schedule=(By.XPATH, "//button[@class='discount-button bc4 fc1 w-button']")
    
    def select_schedule(self, index):
        xpath=f"(//div[@class='schedule-top-bar-date-selector--bc3--bw1--fc2 slot width-196 centre '])[{index}]"
        __praivte_Schedule=(By.XPATH, xpath)
        return __praivte_Schedule
    
    __praivte_Select_proceed=(By.XPATH, "//div[@class='discount-button fc1 bc4 w-button']")
    __private_attendee_model=(By.CSS_SELECTOR, "div[class='gs-modal bc3']")
    
    def select_attendee(self,index):
        xpath= f"(//input[@class='w-checkbox-input attendee-checkbox'])[{index}]"
        __private_Attendee_select=(By.XPATH, xpath)
        return __private_Attendee_select
    
    __private_Attendee_Proceed=(By.XPATH, "//div[@class='discount-button bc4 align-right _50 w-button']")
    __private_addonpage=(By.XPATH,"//div[@class='add-on-section bc4_a bw1t bottom-120']") 
    __private_additional_attendee=(By.XPATH, "(//button[@class='add-section fc4 oc4 justify-centre'])[1]") 
    __private_Addon_Proceed=(By.XPATH, "//button[@class='discount-button fc1 bc4 w-button shrink']")
    __private_Waiver_Checkbox=(By.ID, "checkbox-3")
    __private_Review_Proceed_cardno=(By.CSS_SELECTOR,"div[class='stripeModal']")
    __private_Review_Proceed_card=(By.CSS_SELECTOR,"div[class='discount-button fc1 bc4 w-button one']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")

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
            log.info("Is Schedule not available today: %s",str(op))   
            return op
        except Exception as e:
            return False

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
