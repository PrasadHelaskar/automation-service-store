import time
import json
from base.logfile import Logger
from pages.discount_element import discount_elemnts
from pages.toaster import * 
from base.db import Omnify_connect
from base.random_select import select_random
from base.json_operations import *
from pages.discount_element import discount_elemnts
from pages.toaster import * 


log=Logger().get_logger()

class apply_discount():
    def fetch_discount(self):
        """Used for the fetching the data from the DB"""
        business_id=json_read("BUSINESS_ID")
        try:
            data=Omnify_connect().fetch_data(f"""select name,code from discounts 
                                                    where business_id=f"{business_id}" 
                                                        and isDeleted=0 
                                                        and isDisabled=0 
                                                        and isExpired=0 
                                                        and is_refund_discount=0 
                                                        and discount_for not in ("gift_cards","camps") 
                                                        and is_renewal_discount=0 
                                                        and expiry is not null;""")
            # log.info(f"Fetched data: {data}")
            if data:
                coupon_codes=[code for code in data]
                return coupon_codes
            
            else:
                log.error("No data fetched")
        
        except Exception as e:
            log.error("An error occurred > fetch_discount: %s",str(e))
            return False
        
    def test_discount(self,driver):
        """Execution of discount apply"""
        try:
            discount=discount_elemnts(driver)
            coupon_codes=apply_discount().fetch_discount()
            # log.info("is coupon_codes empty? >"+str(coupon_codes is not None))
            json_data=[
                {
                    "Name":coupon_code[0], 
                    "Code":coupon_code[1]
                } 
                for coupon_code in coupon_codes
            ]
            couponcode_output=json.dumps(json_data, indent=2)
            log.info(f"Fetched coupon codes:\n{couponcode_output}")
            self.remove_discount(driver)
           
            if coupon_codes:
                
                if discount.visible_code_box():
                    index=len(coupon_codes)
    
                    for i in range(1, 3):
                        start_time=time.time()
                        div=discount.scroll_div()
                        selected_index=select_random().random_number((index-1))
                        discount.enter_coupon_code(coupon_codes[selected_index][1])
                        scroll_script="""const div = arguments[0];
                                        const apply_button = arguments[1];
                                        div.scrollTop = apply_button.offsetTop - div.offsetTop;"""
                        driver.execute_script(scroll_script,div,discount.element_coupon_apply())
                        discount.click_coupon_apply()
                        time.sleep(2)
                    
                        self.remove_discount(driver)  
                        if not (discount.visible_code_box()):
                            log.info(f"Discount code {coupon_codes[selected_index][0]} applied successfully")  
                            break           
                    
                        else:
                            # gift card invalid check pop-up                    
                            if(toaster_message_elements(driver).is_toaster_visible()):
                                message=toaster_message_elements(driver).get_toaster_text()
                    
                                if message:
                                    if "Gift Card" in message:
                                        break
                    
                                    else:
                                        continue
                            log.error(f"Discount code {coupon_codes[selected_index][0]} not applied")
                        
                        end_time=time.time()
                        log.info("Execution time: %s",str(end_time-start_time))
                
                else:
                    log.error("Discount Box is not visible")
                
            else:
                log.error("No coupon code fetched")
                
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",discount.scroll_div())
        
        except Exception as e:
            log.error("An error occurred > test_discount: %s",str(e))
            return 
        
    remove_count=0
    def remove_discount(self,driver):                        
        discount=discount_elemnts(driver)
        if(self.remove_count<=2):
            discount.click_remove_discount()
            self.remove_count+=1
            log.info("The Removed Count: "+str(self.remove_count))
        else:
            pass