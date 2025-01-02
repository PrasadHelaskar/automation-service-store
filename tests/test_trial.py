import time
import pytest
from Base.logfile import Logger
from Base.random_select import select_random
from Base.stripe_popup import stripe_action
from pages.trial_booking import trialkbooking
from tests.login import loginAction
from Base.discount import apply_discount

log = Logger().get_logger()

class TesttrialBooking():
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
            assert False, "Warning model is visible"

        time.sleep(2)

        if(driver.title=="Addons"):
            tb.click_addon_proceed()

        time.sleep(2)
        apply_discount().test_discount(driver)
        tb.click_waiver_box()
        tb.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        tb.click_home()
        loginAction().authenticate_cookie(driver)