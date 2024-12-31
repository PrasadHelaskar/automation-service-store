import time
from Base.logfile import Logger
from pages.discount_element import discount_elemnts
from Base.db import Omnify_connect
from Base.random_select import select_random

log=Logger().get_logger()
class apply_discount():
    def fetch_discount(self):
        try:
            data=Omnify_connect().fetch_data("""select name,code from discounts 
                                                where 
                                                    business_id="25877" and 
                                                    isDeleted=0 and 
                                                    isDisabled=0 and 
                                                    isExpired=0 and 
                                                    discount_for not in ("gift_cards", "camps");""")
            # log.info(f"Fetched data: {data}")
            if data:
                coupon_codes=[code for code in data]
                return coupon_codes
            else:
                log.error("No data fetched")
        
        except Exception as e:
            log.error(f"An error occurred: {e}")
            return False
        
    def test_discount(self,driver):
        discount=discount_elemnts(driver)
        coupon_codes=apply_discount().fetch_discount()
        
        log.info(f"Fetched coupon codes: {coupon_codes}")
        if coupon_codes:
            if discount.visible_code_box():
                index=len(coupon_codes)
                for i in range(1, index):
                    selected_index=select_random().random_number((index-1))
                    discount.enter_coupon_code(coupon_codes[selected_index][1])
                    discount.click_coupon_apply()
                    time.sleep(5)
                
                    if not (discount.visible_code_box()):
                        log.info(f"Discount code {coupon_codes[selected_index][0]} applied successfully")
                        break           
                    else:
                        log.error(f"Discount code {coupon_codes[selected_index][0]} not applied")
            else:
                log.error("Discount Box is not visible")
            
        else:
            log.error("No coupon code fetched")