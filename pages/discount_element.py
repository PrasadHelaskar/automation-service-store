from tests.base_page import BasePage
from selenium.webdriver.common.by import By


class discount_elemnts(BasePage):
    __private_COUPONCODE= (By.NAME,"couponcode")
    __private_COUPONCODE_APPLY= (By.ID, "couponApply")
    __private_COUPONCODE_new= (By.NAME,"field-2")
    __private_COUPONCODE_APPLY_new= (By.XPATH, "(//button[@class='discount-button fc1 bc4 shrink w-button'])[1]")

    def enter_coupon_code(self,code):
        try:
            value=self.is_visible(self.__private_COUPONCODE_new)
            locator=(self.__private_COUPONCODE_new) if value else (self.__private_COUPONCODE)
            self.clear_element(locator)
            self.send_keys(locator,code)
        except Exception as e:
            pass
    
    def click_coupon_apply(self):
        try:
            value=self.is_visible(self.__private_COUPONCODE_APPLY_new)
            locator=(self.__private_COUPONCODE_APPLY_new) if value else (self.__private_COUPONCODE_APPLY)
            self.click(locator)
        except Exception as e:
            pass

    def visible_code_box(self):
        try:
            value=self.is_visible(self.__private_COUPONCODE_new)
            locator=(self.__private_COUPONCODE_new) if value else (self.__private_COUPONCODE)
            op=self.is_visible(locator)
            return op
        except:
            return False