import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger
from base.json_operations import json_read

log=Logger().get_logger()

class addfamily(BasePage):
    __private__profile=(By.XPATH, "(//div[@class='profile-wrapper'])[1]")
    __private__profile_page=(By.XPATH, "(//a[@class='profile-dropdown-list-holder'])[1]")
    __private_family_page=(By.XPATH, "(//a[@class='subtitle-2-medium profile-top-nav-links w-inline-block  d-flex '])[3]")
    __private_add_familt_btn=(By.CSS_SELECTOR, "div[class='ss-auth-primary-button--bc4--fc1 padding-new horizontal']")
    __private__firstname=(By.NAME, "firstname")
    __private__lastname=(By.NAME, "lastname")
    __private__DOB=(By.CSS_SELECTOR, "input[class='display-flex ss-auth-input--bc3--fc2--oc2 font-size-16 w-input']")
    __private__submit_button=(By.CSS_SELECTOR, "input[class='ss-auth-primary-button--bc4--fc1 padding-new left-32 exp w-button']")
    
    def added_member(self, i):
        xpath=f"(//div[@class='sub-text font-16 semi-bold fc2 lc1'])[{i}]"
        __private__added_name=(By.XPATH, xpath)
        return __private__added_name
    
    __private__back_to_home=(By.CSS_SELECTOR , "a[class='top-most-link w-inline-block']")

    date=int(json_read("DATE"))
    __private_DATE=(By.XPATH, f"(//button[@class='rdp-button_reset rdp-button rdp-day'])[{date}]")

    __private__family_div=(By.CSS_SELECTOR,"div[class='c-p-content-section width']")

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

    def type_dob(self):
        self.click(self.__private__DOB)

    def click_submit_button(self):
        self.click(self.__private__submit_button)
    
    def get_added_name(self, i):
        name=self.get_text(self.added_member(i))
        log.info(name)
        return name

    def click_back_button(self):
        self.click(self.__private__back_to_home)
    
    def scroll_div(self):
        element=self.find_element_wait(self.__private__family_div)
        return element
    
    def click_date(self):
        self.click(self.__private_DATE) 