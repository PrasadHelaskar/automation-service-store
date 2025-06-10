from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger(__name__)

class add_on(BasePage):
    def geneal_item_selection(self, i):
        xpath=f"(//a[@id='select_general_service'])[{i}]"
        __private_general_item=(By.XPATH, xpath)
        return __private_general_item
    
    def classpack_selection(self, i):
        xpath=f"(//a[@id='select_classpack'])[{i}]"
        __private_classpack=(By.XPATH, xpath)
        return __private_classpack
    
    __private_Addon_proceed=(By.ID,"proceed-btn")

    def click_general_item(self, i):
        # log.info("Clicking on general item")
        self.click(self.geneal_item_selection(i))

    def click_classpack(self, i):
        # log.info("Clicking on classpack")
        self.click(self.classpack_selection(i))

    def click_addon_proceed(self):
        self.click(self.__private_Addon_proceed)

    __private_mulit_option_box=(By.CSS_SELECTOR,"div[class='gs-modal bc3']")
    __private_close_box=(By.ID,"message-us-close")

    def visible_box(self):
        value=self.is_visible(self.__private_mulit_option_box)
        return value
    
    def click_close(self):
        self.click(self.__private_close_box)