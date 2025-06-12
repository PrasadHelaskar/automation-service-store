import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log= Logger().get_logger(__name__)

class custom_fields(BasePage):
    __private__custome_field_page=(By.ID, "prebookingfields")
    __private__attendee=(By.XPATH,"//span[@class='text-capitalize']") #multi-attendee
    __private__all_custome_fields=(By.XPATH, "//form[@id='before-booking-extra-f']//input[@name]")
    __private__proceed=(By.ID,"sub-btn")
    __private__custom_field_div=(By.CSS_SELECTOR,"div[class='custom-mob']")
    __private__month_select=(By.CSS_SELECTOR,"div[class='xdsoft_label xdsoft_month']") #multi-attendee
    __private__year_select=(By.CSS_SELECTOR,"div[class='xdsoft_label xdsoft_year']") #multi-attendee
    
    def select_date(self,date):
        css=f"td[data-date='{date}']"
        __private_selected_date=(By.CSS_SELECTOR,css)
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
    
    def date_selection(self,driver,date,month,year,i):
        self.click(self.__private__month_select)
        month=self.find_element_wait_presence(self.select_month(month,i))
        time.sleep(1)
        driver.execute_script("arguments[0].click();", month)
        self.click(self.__private__year_select)
        year=self.find_element_wait_presence(self.select_year(year,i))
        time.sleep(1)
        driver.execute_script("arguments[0].click();", year)
        self.click(self.select_date(date))
    
    def click_attendee_name(self):
        self.click(self.__private__attendee)