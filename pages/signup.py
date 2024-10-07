from dotenv import load_dotenv
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import os

class signup(BasePage):
    load_dotenv()
    __private_SIGNUP_BUTTON=(By.CSS_SELECTOR, "button[class='button--ph1--bc4--bw1--oc4--fc1 w-button']")
    __private_EMAIL_FIELD=(By.NAME, "email")
    __private_CONTINUE_BUTTON=(By.CSS_SELECTOR, "button[class='ss-auth-primary-button--bc4--fc1 w-button']")
    __private_FIRST_FIELD=(By.NAME, "firstname")
    __private_LAST_FIELD=(By.NAME, "lastname")
    __private_SUBMIT=(By.CSS_SELECTOR, "input[value='Submit']") #3times
    __private_PASSWORD=(By.ID, "password")
    __private_CONFIRM_PASSWORD=(By.ID, "confirm_password")
    #custom fields
    __private_HEADER=(By.XPATH, "//div[@class='ss-auth-stepper-item ']")
    __private_DOB_FIELD=(By.CSS_SELECTOR, "input[class='display-flex ss-auth-input--bc3--fc2--oc2 font-size-16 w-input']")  #2times
    i=os.getenv("date")
    __private_DATE=(By.XPATH, f"(//button[@class='rdp-button_reset rdp-button rdp-day'])[{i}]")

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
        
    def click_submit(self):
        self.click(self.__private_SUBMIT)
    
    def enetr_password(self, password):
        self.send_keys(self.__private_PASSWORD, password)
    
    def enetr_confirmpassword(self, confirepassword):
        self.send_keys(self.__private_CONFIRM_PASSWORD, confirepassword)
    
    def check_header(self):
        value=self.is_visible(self.__private_HEADER)
        print(value)
        return(value)
    
    def click_dobfield(self):
        self.click(self.__private_DOB_FIELD)
    
    def click_date(self):
        self.click(self.__private_DATE)