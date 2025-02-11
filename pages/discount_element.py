from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import *

log=Logger().get_logger()
class discount_elemnts(BasePage):
    __private_COUPONCODE= (By.NAME,"couponcode")
    __private_COUPONCODE_APPLY= (By.ID, "couponApply")
    __private_COUPONCODE_new= (By.NAME,"field-2")
    __private_COUPONCODE_APPLY_new= (By.XPATH, "(//button[@class='discount-button fc1 bc4 shrink w-button'])[1]")
    __private_review_page_div=(By.CSS_SELECTOR, "div[class='review-section']")
    __private_remove_discount_new=(By.CSS_SELECTOR,"svg[class='lucide lucide-trash2']")
    __private_remove_discount=(By.ID,"removeDiscount1")


    def enter_coupon_code(self,code):
        try:
            value=self.is_visible(self.__private_COUPONCODE_new)
            locator=(self.__private_COUPONCODE_new) if value else (self.__private_COUPONCODE)
            self.clear_element(locator)
            self.send_keys(locator,code)
        except Exception as e:
            log.error("Exception Occured > enter_coupon_code: "+ str(e))
    
    def click_coupon_apply(self):
        try:
            value=self.is_visible(self.__private_COUPONCODE_APPLY_new)
            locator=(self.__private_COUPONCODE_APPLY_new) if value else (self.__private_COUPONCODE_APPLY)
            self.click(locator)
        except Exception as e:
            log.error("Exception Occured > click_coupon_apply: "+ str(e))

    def visible_code_box(self):
        try:
            value=self.is_visible(self.__private_COUPONCODE)
            locator=(self.__private_COUPONCODE) if value else (self.__private_COUPONCODE_new)
            op=self.is_visible(locator)
            return op
        except:
            return False
        
    def scroll_div(self):
        try:
            element=self.find_element_wait(self.__private_review_page_div)
            return element
        except:
            return False
        
    def element_coupon_apply(self):
        try:
            value=self.is_visible(self.__private_COUPONCODE_APPLY_new)
            locator=(self.__private_COUPONCODE_APPLY_new) if value else (self.__private_COUPONCODE_APPLY)
            return self.find_element_wait(locator)
        except Exception as e:
            log.error("Exception Occured > element_coupon_apply: "+ str(e))

    def click_remove_discount(self):
        try:
            value=self.is_visible(self.__private_remove_discount)
            locator=(self.__private_remove_discount) if value else (self.__private_remove_discount_new)
            return self.click(locator)
        except Exception as e:
            log.error("Exception Occured in > click_remove_discount: "+ str(e))

    def is_visible_remove_discount(self):
        try:
            value=self.is_visible(self.__private_remove_discount)
            if value:
                return value
            else:
                value=self.is_visible(self.__private_remove_discount)
                if value:
                    return value
                else:
                    return False
            return False
        except Exception as e:
            log.error("Exception Occured in > click_remove_discount: "+ str(e))
