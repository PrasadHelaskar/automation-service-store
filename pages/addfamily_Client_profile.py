import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from Base.logfile import Logger

log=Logger().get_logger()

class addfamily(BasePage):
    __private__profile=(By.XPATH, "(//div[@class='profile-wrapper'])[1]")
    __private__profile_page=(By.XPATH, "(//a[@class='profile-dropdown-list-holder'])[1]")
    __private_family_page=(By.XPATH, "(//a[@class='subtitle-2-medium profile-top-nav-links w-inline-block  d-flex '])[3]")
    __private_add_familt_btn=(By.CSS_SELECTOR, "div[style='text-align: center;']")
    __private__firstname=(By.ID, "firstname")
    __private__lastname=(By.ID, "lastname")
    __private__DOB=(By.CSS_SELECTOR, "input[class='alt-changes cs-modal-form-field w-input custom-field-input']")
    __private__submit_button=(By.CSS_SELECTOR, "button[form='add-family-form']")
    def added_member(self, i):
        xpath=f"(//div[@class='body-text-1-medium family-details-textblock1'])[{i}]"
        __private__added_name=(By.XPATH, xpath)
        return __private__added_name
    
    __private__back_to_home=(By.CSS_SELECTOR , "a[class='top-most-link w-inline-block']")

    def click_profile(self):
        self.click(self.__private__profile)

    def click_profile_page(self):
        self.click(self.__private__profile_page)
    
    def click_family(self):
        self.click(self.__private_family_page)

    def click_add_family_btn(self):
        self.click(self.__private_add_familt_btn)

    def type_first_name(self, name):
        self.send_keys(self.__private__firstname, name)
    
    def type_last_name(self, name):
        self.send_keys(self.__private__lastname, name)

    def type_dob(self, dob):
        self.send_keys(self.__private__DOB, dob)

    def click_submit_button(self):
        self.click(self.__private__submit_button)
    
    def get_added_name(self, i):
        name=self.get_text(self.added_member(i))
        log.info(name)
        return name

    def click_back_button(self):
        self.click(self.__private__back_to_home)

    __private__family_div=(By.CSS_SELECTOR,"div[class='profile-details']")
    
    def scroll_div(self):
        element=self.find_element_wait(self.__private__family_div)
        return element