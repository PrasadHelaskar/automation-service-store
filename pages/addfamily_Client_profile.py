import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger
from base.json_operations import json_read

log=Logger().get_logger()

class addfamily(BasePage):
    """Service Store cilent profile"""
    __private__profile=(By.XPATH, "(//div[@class='profile-wrapper'])[1]")
    __private__profile_page=(By.XPATH, "(//a[@class='profile-dropdown-list-holder'])[1]")
    __private_family_page=(By.XPATH, "(//a[@class='subtitle-2-medium profile-top-nav-links w-inline-block  d-flex '])[2]")
    __private_add_family_btn=(By.CSS_SELECTOR, "div[class='ss-auth-primary-button--bc4--fc1 padding-new horizontal']")
    __private__firstname=(By.NAME, "firstname")
    __private__lastname=(By.NAME, "lastname")
    __private__DOB_old=(By.CSS_SELECTOR, "input[class='alt-changes cs-modal-form-field w-input custom-field-input']")
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
        self.click(self.__private_add_family_btn)

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

    def type_dob_old(self, dob):
        self.send_keys(self.__private__DOB_old, dob)

    """Service Store check out flow"""

    __private__attendee_model=(By.CSS_SELECTOR,"h4[class='h5-regular modal-title ']")
    __private_add_familt_btn_ck=(By.ID, "addfamilymember")
    __private_dob_ck=(By.ID , "dateTextWrapper")
    __private_add_family_submit=(By.ID, "submitFamilyAddForm")
    __private_scroll_div_ck=(By.CSS_SELECTOR, "div[class='modal-body bcbg']")

    def added_fam(self,i):
        xpath=f"(//div[@class='fc2 booking-content-list-text body-text-1-regular fc2 text-capitalize new-attendee-list-t'])[{i}]"
        __private_added_fam_xpath=(By.XPATH, xpath)
        return __private_added_fam_xpath
    
    def is_attendee_model_visible(self):
        value=self.is_visible(self.__private__attendee_model)
        return value
    
    def click_add_family_btn_ck(self):
        self.click(self.__private_add_familt_btn_ck)
    
    # took the first name and last name from the client profile methods  

    def click_dob(self):
        self.click(self.__private_dob_ck)

    def click_submit(self):
        self.click(self.__private_add_family_submit)

    def scroll_div_ck(self):
        element=self.find_element_wait(self.__private_scroll_div_ck)
        return element
    
    def get_added_name_ck(self, i):
        name=self.get_text(self.added_fam(i))
        log.info(name)
        return name