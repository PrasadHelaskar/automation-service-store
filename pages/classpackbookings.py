from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class classpackbooking(BasePage):
    __private_FILTER_CHECKBOX= (By.XPATH,"(//input[@type='checkbox'])[2]")
    __private_APPLY_BUTTON=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']") 
    __private_select_proceed= (By.ID, "classpack_proceed_btn")
    i=6
    __private_classpack_select= (By.XPATH, f"(//div[@class='ss-card-primary-button--fc4 '])[{i}]")
    j=3
    __private_program_select= (By.XPATH, f"(//div[@class='ss-card-primary-button--fc4 '])[{j}]")
    __private_waiver_checkbox=(By.ID, "waiverCheckbox")
    __private_review_proceed =(By.XPATH, "(//span[@id='totalPriceHolder'])[2]")
    __private_COUPONCODE= (By.NAME, "couponcode")
    __private_COUPONCODE_APPLY= (By.ID, "couponApply")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")

    def click_classpack_checkbox(self):
        self.click(self.__private_FILTER_CHECKBOX)

    def click_apply(self):
        self.click(self.__private_APPLY_BUTTON)
    
    def click_select_classpack(self):
        self.click(self.__private_classpack_select)

    def click_select_program(self):
        self.click(self.__private_program_select)

    def click_proceed(self):
        self.click(self.__private_select_proceed)

    def click_waiver_box(self):
        self.click(self.__private_waiver_checkbox)

    def click_review_proceed(self):
        self.click(self.__private_review_proceed) 
    
    def enter_couponcode(self, code):
        self.send_keys(self.__private_COUPONCODE , code)

    def click_applycoupon(self):
        self.click(self.__private_COUPONCODE_APPLY)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)