import time
import pytest
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from pages.trial_booking import trialkbooking
from tests.login import loginAction
from base.discount import apply_discount
from tests.add_on import add_on_test 
from base.waiver_vima import *

log = Logger().get_logger()

class Test_trialBooking():
    @pytest.mark.order(10)
    def test_trial(self,driver):
        driver.implicitly_wait(30)        
        loginAction().login_action(driver)
        tb=trialkbooking(driver)
        print('Trial booking started')

        tb.click_program_page()
        time.sleep(2)

        script="""return document.getElementsByClassName('secondary-button-card bw1 oc4 fc4').length;"""
        i=driver.execute_script(script)
        log.info("Total services available: "+str(i))
        service_index=select_random().random_number(i)
        log.info("Service selected index: "+str(service_index))
        tb.click_select_service(service_index)        
        tb.click_proceed()

        if (tb.visible_attendee_moddel()):
            time.sleep(2)
            script="""return document.getElementsByName('attendees-id-list').length"""
            recived_count=driver.execute_script(script)
            log.info("Attendee count: "+str(recived_count))
            attendee=select_random().random_number(recived_count)
            tb.click_attendee_box(attendee)
            log.info("Attendee selected index: "+str(attendee))
            tb.click_attendee_proceed()

        if (tb.visible_warning_model()):
            time.sleep(2)
            for i in range(3):    
                tb.click_cross_button()
                tb.click_proceed()
                log.info("Warning model closed for attendee index: "+str(attendee))
                attendee=select_random().random_number(recived_count)
                tb.click_attendee_box(attendee)
                log.info("Next attendee selected index: "+str(attendee))
                tb.click_attendee_proceed()
                if(tb.visible_warning_model()==False):
                    break
            if(tb.visible_warning_model()):
                assert False ,"Warning model not closed"

        time.sleep(2)

        if(driver.title=="Addons"):
            add_on_test().add_on_page(driver)

        time.sleep(2)
        waiver_vima_action().waiver_vima(driver)
        apply_discount().test_discount(driver)
        tb.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        tb.click_home()
        loginAction().authenticate_cookie(driver)