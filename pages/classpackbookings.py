from tests.base_page import BasePage
from selenium.webdriver.common.by import By

class classpackbooking(BasePage):
    __private_FILTER_CHECKBOX= (By.XPATH,"(//input[@type='checkbox'])[2]")
    __private_APPLY_BUTTON=(By.CSS_SELECTOR,"div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']") 
    __private_select_proceed= (By.ID, "classpack_proceed_btn")
    __private_classpack_page=(By.CSS_SELECTOR,"a[href='/classpacks?b=t']")
    __private_program_page=(By.CSS_SELECTOR,"a[href='/programs?b=t']")

    def select_service(self,i):
        xpath=f"(//a[@class='primary-button-card bc4 fc1'])[{i}]"
        __private_select_service=(By.XPATH,xpath)
        return __private_select_service
    
    __private_attendee_model=(By.CSS_SELECTOR, "h4[class='h5-regular modal-title ']")
    
    def attendee_xpath(self,count):
        xpath=f"(//input[@name='attendees-id-list'])[{count}]"
        __private_attendee_select=(By.XPATH,xpath)
        return __private_attendee_select
    
    __private_attendee_proceed=(By.XPATH, "//a[@class='booking-footer-button small w-inline-block w-clearfix next-btn-classpack-modal bc4']")
    __private_waiver_checkbox=(By.ID, "waiverCheckbox")
    __private_Review_Proceed_cardno=(By.CSS_SELECTOR,"div[class='stripeModal']")
    __private_Review_Proceed_card=(By.CSS_SELECTOR,"div[class='discount-button fc1 bc4 w-button one']")
    __private_COUPONCODE= (By.NAME,"couponcode")
    __private_COUPONCODE_APPLY= (By.ID, "couponApply")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")
    __private_Addon_proceed=(By.ID,"proceed-btn")

    __private_credit_booking_class=(By.NAME, "checkbox-13")
    __private_confirm_booking=(By.XPATH, "//button[@class='cta-sec-button pri bc4 fc1 w-button']")

    def click_classpack_page(self):
        self.click(self.__private_classpack_page)

    def click_program_page(self):
        self.click(self.__private_program_page) 

    def click_classpack_checkbox(self):
        self.click(self.__private_FILTER_CHECKBOX)

    def click_apply(self):
        self.click(self.__private_APPLY_BUTTON)
    
    def click_select_service(self,i):
        self.click(self.select_service(i))

    def click_proceed(self):
        self.click(self.__private_select_proceed)

    def click_waiver_box(self):
        self.click(self.__private_waiver_checkbox)

    def click_review_proceed(self):
        try:    
            value=self.is_visible(self.__private_Review_Proceed_cardno)
        except:
            value=False
        locator=(self.__private_Review_Proceed_cardno) if value else (self.__private_Review_Proceed_card)
        self.click(locator)
    
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
    
    def click_attendee_box(self,i):
        self.click(self.attendee_xpath(i))

    def click_attendee_proceed(self):
        self.click(self.__private_attendee_proceed)

    def click_addon_proceed(self):
        self.click(self.__private_Addon_proceed)

    def click_credit_booking_class(self):
        self.click(self.__private_credit_booking_class)

    def click_confirm_booking(self):
        self.click(self.__private_confirm_booking)