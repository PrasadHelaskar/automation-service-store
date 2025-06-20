import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log= Logger().get_logger(__name__)

class custom_fields(BasePage):
    __private__custome_field_page=(By.ID, "prebookingfields")
    __private__attendee=(By.XPATH,"//span[@class='text-capitalize']") 
    __private__all_custome_fields=(By.XPATH, "//form[@id='before-booking-extra-f']//input[@name and not(@type='hidden')]")
    __private__proceed=(By.ID,"sub-btn")
    __private__custom_field_div=(By.CSS_SELECTOR,"div[class='custom-mob']")
    
    def month_select(self,i):
        xpath=f"(//div[@class='xdsoft_label xdsoft_month'])[{i}]"
        __private__month_select=(By.XPATH,xpath)
        return __private__month_select
    
    def year_select(self,i):
        xpath=f"(//div[@class='xdsoft_label xdsoft_year'])[{i}]"
        __private__year_select=(By.XPATH,xpath)
        return __private__year_select
    
    def select_date(self,date,i):
        xpath=f"(//td[@data-date='{date}'])[{i}]"
        # log.info("xpath: %s",xpath)
        __private_selected_date=(By.XPATH,xpath)
        return __private_selected_date
    
    def select_month(self,month,i): 
        xpath=f"(//div[@data-value='{month}'])[{i}]"
        __private_selected_month=(By.XPATH,xpath)
        return __private_selected_month

    def select_year(self,year,i): 
        xpath=f"(//div[@data-value='{year}'])[{i}]"
        __private_selected_year=(By.XPATH,xpath)
        return __private_selected_year

    
    def is_visible_page(self):
        value=self.is_visible(self.__private__custome_field_page)
        return value
    
    def get_attendee_name(self): #multi-attendee
        name=self.get_text(self.__private__attendee)
        return name
    
    def get_all_custom_fields(self):
        elements=self.find_elements_wait_presence(self.__private__all_custome_fields)
        return elements
    
    def click_proceed(self):
        self.click(self.__private__proceed)
        time.sleep(2)
    
    def custom_field_div(self):
        element=self.find_element_wait(self.__private__custom_field_div)
        return element
    
    def date_selection(self,date,month,year,i):
        self.click(self.month_select(i))
        self.click_presence(self.select_month(month,i))
        time.sleep(1)
        self.click(self.year_select(i))
        self.click_presence(self.select_year(year,i))
        time.sleep(1)
        self.click(self.select_date(date,i))
    
    def click_attendee_name(self):
        self.click(self.__private__attendee)