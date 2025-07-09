from dotenv import load_dotenv
from base.json_operations import json_read
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
import os
from base.logfile import Logger

log=Logger().get_logger(__name__)

class signup(BasePage):
    load_dotenv()
    __private_SIGNUP_BUTTON=(By.XPATH, "//button[@class=' button--ph1--bc4--bw1--oc4--fc1 w-button']")
    __private_EMAIL_FIELD=(By.ID, "login-email")
    __private_CONTINUE_BUTTON=(By.CSS_SELECTOR, "button[class='ss-auth-primary-button--bc4--fc1 w-button']")
    __private_FIRST_FIELD=(By.NAME, "firstname")
    __private_LAST_FIELD=(By.NAME, "lastname")
    __private_phone_number=(By.ID,"phone")
    __private_SUBMIT=(By.CSS_SELECTOR, "input[value='Create Account']")
    __private_PASSWORD=(By.ID, "password")
    __private_CONFIRM_PASSWORD=(By.ID, "confirm_password")
    #custom fields
    __private_CUSTOM_FIELD=(By.CSS_SELECTOR, "input[class='display-flex ss-auth-input--bc3--fc2--oc2 font-size-16 w-input']")
    __private_DOB_FIELD=(By.CSS_SELECTOR, "input[class='display-flex ss-auth-input--bc3--fc2--oc2 font-size-16 w-input']")  #2times
    date=int(json_read("DATE"))
    __private_DATE=(By.XPATH, f"(//button[@class='rdp-button_reset rdp-button rdp-day'])[{date}]")
    __private_VIMA_consent=(By.CSS_SELECTOR,"input[class='w-checkbox-input tos-checkbox']")

    def click_signup(self):
        self.click(self.__private_SIGNUP_BUTTON)
    
    def enter_email(self, email):
        self.send_keys(self.__private_EMAIL_FIELD , email)
    
    def click_continuebutton(self):
        self.click(self.__private_CONTINUE_BUTTON)
        
    def enter_firstname(self, firstname):
        self.send_keys(self.__private_FIRST_FIELD, firstname)
    
    def enter_lastname(self, lastname):
        self.send_keys(self.__private_LAST_FIELD , lastname)
        
    def enter_phone_number(self, phone):
        if self.is_visible(self.__private_phone_number):
            self.send_keys(self.__private_phone_number, phone)
    
    def click_submit(self):
        self.click(self.__private_SUBMIT)
    
    def enter_password(self, password):
        self.send_keys(self.__private_PASSWORD, password)
    
    def enter_confirmpassword(self, confirepassword):
        self.send_keys(self.__private_CONFIRM_PASSWORD, confirepassword)
    
    def check_custom_field(self):
        try:    
            value=self.is_visible(self.__private_CUSTOM_FIELD)
            return(value)
        except:
            return False
    
    def click_dobfield(self):
        # log.info("clicked dob")
        self.click(self.__private_DOB_FIELD)
    
    def click_date(self):
        self.click(self.__private_DATE) 

    def click_vima_consent(self):
        if self.is_visible(self.__private_VIMA_consent):
            self.click(self.__private_VIMA_consent)