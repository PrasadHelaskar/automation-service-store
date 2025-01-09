from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from Base.logfile import Logger

log=Logger().get_logger()

class cancelation_booking(BasePage):
    __private__profile=(By.XPATH, "(//div[@class='profile-wrapper'])[1]")
    __private__profile_page=(By.XPATH, "(//a[@class='profile-dropdown-list-holder'])[1]")
    __private_empty_div=(By.CSS_SELECTOR,"div[class='w-tab-content']")
    __priavte_family_dropdown=(By.ID, "w-dropdown-toggle-2")
    
    def femily_members(self,i):
        xpath=f"(//div[@class='d-flex schedule-dropdown'])[{i}]"
        __private_family_member=(By.XPATH,xpath)
        return __private_family_member

    def services_View_Details(self,i):
        xpath=f"(//a[@class='view-details-button schedule_details'])[{i}]"
        __private_selected_service=(By.XPATH,xpath)
        return __private_selected_service
    
    def service_card(self,i):
        xapth=f"(//ul[@class='w-list-unstyled'])[{i}]"
        __private_service_card=(By.XPATH,xapth)
        return __private_service_card
    
    __private_cancel_button=(By.ID,"cancelClassBtn")
    __private_cancel_everyone=(By.ID,"cancelForEveryoneButton")

    def cancelled_label(self,i):
        xpath=f"(//span[@class='label label-danger'])[{i}]"
        __private_cancelled_label=(By.XPATH,xpath)
        return __private_cancelled_label

    def is_visible_empty_state(self):
        self.is_visible(self.__private_empty_div)

    def click_profile(self):
        self.click(self.__private__profile)

    def click_profile_page(self):
        self.click(self.__private__profile_page)

    def click_drop_down(self):
        self.click(self.__priavte_family_dropdown)

    def click_familty_members(self,count):
        self.click(self.femily_members(count))

    def view_details(self,count):
        element=self.find_element_wait(self.services_View_Details(count))
        return element
    
    def view_card(self,count):
        element=self.find_element_wait(self.service_card(count))
        return element

    def click_view_details(self,count):
        self.click(self.services_View_Details(count))

    def click_cancel_button(self):
        self.click(self.__private_cancel_button)

    def click_cancel_everyone(self):
        self.click(self.__private_cancel_everyone)
    
    def is_visible_lable(self,i):
        self.is_visible(self.cancelled_label(i))
