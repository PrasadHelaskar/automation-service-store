import time
import pytest
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.waiver_vima import waiver_vima_action
# from base.discount import apply_discount
from base.custom_field import custom_fields_actions
from pages.classpackbookings import classpackbooking
from tests.login import loginAction
from tests.add_on import add_on_test
from tests.test_add_family import add_family_checkout_flow


log = Logger().get_logger()
lg=loginAction()

class Test_program():        
    @pytest.mark.order(4)
    def test_program(self, driver):
        """The Method for the program booking"""
        driver.implicitly_wait(30)
        pb=classpackbooking(driver)
        lg.login_action(driver)
        for i in range(0,20):
            log.info('Program booking Started')
            # filter the programs
            # pb.click_classpack_checkbox()
            # pb.click_apply()
            time.sleep(5)
            pb.click_program_page()
            time.sleep(2) 

            script="""return document.getElementsByClassName('primary-button-card bc4 fc1').length;"""
            i=driver.execute_script(script)
            log.info("Total services available: %s",str(i))

            if i in range(1,20):
                service_index=select_random().random_number(i)
            else:
                service_index=select_random().random_number(10)

            pb.click_select_service(service_index)
            log.info("Service selected index: %s",str(service_index))

            time.sleep(5)
            script="""return document.getElementsByName("cp-radio-button").length;"""
            recived_count=driver.execute_script(script)
            index=select_random().random_number(recived_count)
            log.info("Selected schedule index: %s",index)
            pb.click_start_date(index)

            pb.click_proceed()
            time.sleep(3)
            
            # add_family_checkout_flow(driver)

            script="""return document.getElementsByClassName("w-checkbox-input waitlist-checkbox").length;"""
            recived_count=driver.execute_script(script)
            attendee=select_random().random_number(recived_count)
            pb.click_attendee_box(attendee)
            log.info("Attendee selected index: %s",str(attendee))
            pb.click_attendee_proceed()
            repeat_booking(driver)
            time.sleep(2)
        
            # log.info("Addons page visible="+str(driver.title or "None"))
            
            if(driver.title=="Addons"):
                add_on_test().add_on_page(driver)

            custom_fields_actions().custom_field_action(driver)
            
            waiver_vima_action().waiver_vima(driver)
            # apply_discount().test_discount(driver)
            lg.order_invoice_cookies(driver)
            time.sleep(10)
            pb.click_review_proceed()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            stripe_action().stripe_data_enty(driver)
            pb.click_home()
            lg.authenticate_cookie(driver)
            log.info("Tha Program booking Execution Completed \n")

def repeat_booking(driver):
    """Used to handle the BOok again  model"""
    rb=classpackbooking(driver)
    if(rb.is_repeat_booking_visible()):
        log.info("The Buy Again model visible?: %s",str(rb.is_repeat_booking_visible()))
        rb.click_buy_again()