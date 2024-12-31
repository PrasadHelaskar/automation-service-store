from tests.base_page import BasePage
from selenium.webdriver.common.by import By


class discount_elemnts(BasePage):
    __private_COUPONCODE= (By.NAME,"couponcode")
    __private_COUPONCODE_APPLY= (By.ID, "couponApply")
    
    def enter_coupon_code(self,code):
        self.send_keys(self.__private_COUPONCODE,code)
    
    def click_coupon_apply(self):
        self.click(self.__private_COUPONCODE_APPLY)

    def visible_code_box(self):
        try:
            self.is_visible(self.__private_COUPONCODE)
            return True
        except:
            return False