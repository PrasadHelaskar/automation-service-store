from Base.logfile import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

log = Logger().get_logger()

class partypackage(BasePage):
    __private_party_page=(By.CSS_SELECTOR, "a[href='/party?b=t']")
    party=1
    __praivte_party_selection=(By.XPATH, f"(//button[@class='card-header-alignment'])[{party}]")
    __private_expand_button=(By.CSS_SELECTOR, "svg[class='cursor-pointer']")
    package=1
    __private_package_selection=(By.XPATH, f"//div/..//div/..//div/..//a[@class='ss-primary-button--bc4--bw1--oc4--fc1 width-100 padding-8 bottom-20 w-button'][{package}]")
    # for the if seen Emty state
    __private_Empty_state={By.XPATH, "//div[@class='sub-text font-14 fc2 opacity_70']"}
    __priavte_Next_schedule={By.XPATH, "//button[@class='discount-button bc4 fc1 w-button']"}
    schedule=1
    __praivte_Schedule={By.XPATH, f"(//div[@class='select-time-holder'])[{schedule}]"}
    __praivte_Select_proceed={By.XPATH, "//div[@class='discount-button fc1 bc4 w-button']"}
    attendee=1
    __private_Attendee_select={By.XPATH, f"(//input[@id='checkbox-3'])[{attendee}]"}
    __private_Attendee_Proceed={By.XPATH, "//div/..//div[@class='discount-button bc4 align-right _50 w-button']"}
    __private_Addon_Proceed={By.XPATH, "//button[@class='discount-button fc1 bc4 w-button shrink']"}
    __private_Waiver_Checkbox={By.XPATH, "//input[@class='w-checkbox-input tos-checkbox']"}
    __private_Review_Proceed={By.XPATH, "//div[@class='discount-button fc1 bc4 w-button one']"}
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")

    def click_party_tab(self):
        self.click(self.__private_party_page)

    def click_party_select(self):
        self.click(self.__praivte_party_selection)

    def click_expand(self):
        self.click(self.__private_expand_button)
    
    def click_package(self):
        self.click(self.__private_package_selection)

    def visible_empty_state(self):
        op=self.is_visible(self.__private_Empty_state)
        # log.info(str(op))
        return op

    def text_empty_state(self):
        self.get_text(self.__private_Empty_state)
        
    def click_next_schedule(self):
        self.click(self.__priavte_Next_schedule)

    def click_schedule_selection(self):
        self.click(self.__praivte_Schedule)

    def click_schedule_proceed(self):
        self.click(self.__praivte_Select_proceed)

    def click_attendee_seletion(self):
        self.click(self.__private_Attendee_select)

    def click_attendee_peoceed(self):
        self.click(self.__private_Attendee_Proceed)

    def click_addon_proceed(self):
        self.click(self.__private_Addon_Proceed)

    def click_waiverbox(self):
        self.click(self.__private_Waiver_Checkbox)

    def click_review_proceed(self):
        self.click(self.__private_Review_Proceed)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)