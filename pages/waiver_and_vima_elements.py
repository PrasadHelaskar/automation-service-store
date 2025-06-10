import os
import time
from base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log=Logger().get_logger()

class waiver_vima(BasePage):
    __private_waiver_box=(By.XPATH, "(//div[@class='gs-modal bc3'])[1]")
    __private_waiver_vima_box=(By.XPATH, "(//div[@class='modal-content'])[1]")
    __private_accept_waiver=(By.ID, "agree-waiver-terms")
    __private_waiver_vima_accept=(By.ID,"agree-waiver-terms-and-proceed-to-vima")
    __private_vima_accept=(By.ID,"agree-vima-terms")
    __private_accept_waiver_new=(By.XPATH,"//button[@class='discount-button fc1 bc4 align-right _50 w-button']")
    __private_review_checkbox=(By.NAME, "checkbox-3")
    __private_review_checkbox_new=(By.ID,"waiverCheckbox")
    
    def check_waiver_box(self):
        # log.info("In check_waiver_box method")
        try:
            try:        
                value=self.is_visible(self.__private_waiver_box)
        
            except Exception:
                value=False
            
            locator=(self.__private_waiver_box) if value else (self.__private_waiver_vima_box)
            op=self.is_visible(locator)
            return op
        
        except Exception as e:
            log.warning(str(e))
            return False
        
    def click_accept_waiver(self):
        # log.info("In click_accept_waiver method") 
        try:    
            value=self.is_visible(self.__private_accept_waiver)
        
        except Exception:
            value=False
        
        locator=(self.__private_accept_waiver) if value else (self.__private_waiver_vima_accept)
        try:
            if (locator):
                self.click(locator)
        
        except Exception:
            self.click(self.__private_accept_waiver_new)
        
    def click_waiver(self):
        try:
            value=self.is_visible(self.__private_review_checkbox)
        
        except Exception:
            value=False

        locator=(self.__private_review_checkbox) if value else (self.__private_review_checkbox_new)
        
        self.click(locator)
    
    def click_vima_accept(self):
        self.click(self.__private_vima_accept)
    
    def get_waiver_button_text(self):
        # log.info("In get_waiver_button_text method")
        
        try:    
            value=self.is_visible(self.__private_accept_waiver)
            log.info("get_waiver_button_text > try block > %s",str(value))
        
        except Exception:
            value=False
        
        locator=(self.__private_accept_waiver) if value else (self.__private_waiver_vima_accept)
        
        try:
            text=self.get_text(locator)
            return text
        
        except Exception:
            text=self.get_text(self.__private_accept_waiver_new)
            return text