import time
from Base.logfile import Logger
from pages.discount_element import discount_elemnts
from Base.db import Omnify_connect

log=Logger().get_logger()
class apply_discount():
    def fetch_discount(self):
        try:
            data=Omnify_connect().fetch_data("""select code from discounts 
                                                where 
                                                    business_id="25877" and 
                                                    isDeleted=0 and 
                                                    isDisabled=0 and 
                                                    isExpired=0 and 
                                                    discount_for not in ("gift_cards", "camps");""")
            # log.info(f"Fetched data: {data}")
            if data:
                coupon_codes=[code[0] for code in data]
                return coupon_codes
            else:
                log.error("No data fetched")
                return False
        
        except Exception as e:
            log.error(f"An error occurred: {e}")
            return False
        
    def test_discount(self,driver):
        discount=discount_elemnts(driver)
        coupon_codes=apply_discount().fetch_discount()
        log.info(f"Fetched coupon codes: {coupon_codes}")
        if coupon_codes:

            for code in coupon_codes:
                discount.enter_coupon_code(code)
                discount.click_coupon_apply()
                time.sleep(2)
            
                if discount.visible_code_box():
                    log.info(f"Discount code {code} applied successfully")
                    break
        
                else:
                    log.error(f"Discount code {code} not applied")
        
        else:
            log.error("No coupon code fetched")