from tests.base_page import BasePage
from selenium.webdriver.common.by import By

class classpackbooking(BasePage):
    __private_FILTER_CHECKBOX= (By.XPATH,"(//input[@type='checkbox'])[2]")
    __private_APPLY_BUTTON=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']") 
    __private_select_proceed= (By.ID, "classpack_proceed_btn")
    i=1
    __private_classpack_select= (By.XPATH, f"(//a[@class='primary-button-card bc4 fc1'])[{i}]")
    j=3
    __private_program_select= (By.XPATH, f"(//a[@class='primary-button-card bc4 fc1'])[{j}]")
    __private_attendee_model=(By.CSS_SELECTOR, "h4[class='h5-regular modal-title ']")
    attendee=2
    __private_attendee_select=(By.XPATH, f"(//input[@name='attendees-id-list'])[{attendee}]")
    __private_attendee_proceed=(By.XPATH, "(//div[@class='fc3 booking-footer-button-text-left attendee-form-done button-text-medium-regular'])[2]")
    __private_waiver_checkbox=(By.ID, "waiverCheckbox")
    __private_review_proceed =(By.XPATH, "(//span[@id='totalPriceHolder'])[2]")
    __private_COUPONCODE= (By.NAME,"couponcode")
    __private_COUPONCODE_APPLY= (By.ID, "couponApply")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")
    __private_Addon_proceed=(By.ID,"proceed-btn")

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
    
    def enter_couponcode(self,code):
        self.send_keys(self.__private_COUPONCODE,code)

    def click_applycoupon(self):
        self.click(self.__private_COUPONCODE_APPLY)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)

    def visible_attendee_moddel(self):
        try:
            op=self.is_visible(self.__private_attendee_model)
            return op
        except:
            return False
    
    def click_attendee_box(self):
        self.click(self.__private_attendee_select)

    def click_attendee_proceed(self):
        self.click(self.__private_attendee_proceed)

    def click_addon_proceed(self):
        self.click(self.__private_Addon_proceed)