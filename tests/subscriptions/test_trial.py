import time
import pytest
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.discount import apply_discount
from base.waiver_vima import *
from base.custom_field import custom_fields_actions
from pages.trial_booking_elements import trialkbooking
from tests.add_on import add_on_test
from tests.login import loginAction

log = Logger().get_logger(__name__)

class Test_trialBooking():
    @pytest.mark.order(10)
    def test_trial(self,driver):
        # driver.implicitly_wait(30)
        loginAction().login_action(driver)
        tb=trialkbooking(driver)
        print('Trial booking started')

        tb.click_program_page()
        time.sleep(5)

        script="""return document.getElementsByClassName('secondary-button-card bw1 oc4 fc4').length;"""
        i=driver.execute_script(script)
        log.info("Total services available: %s",str(i))
        service_index=select_random().random_number(i)
        log.info("Service selected index: %s",str(service_index))
        tb.click_select_service(2)
        tb.click_proceed()

        if (tb.visible_attendee_model()):
            time.sleep(2)
            script="""return document.getElementsByName('attendees-id-list').length"""
            received_count=driver.execute_script(script)
            log.info("Attendee count: %s",str(received_count))
            attendee=select_random().random_number(received_count)
            tb.click_attendee_box(attendee)
            log.info("Attendee selected index: %s",str(attendee))
            tb.click_attendee_proceed()

        if (tb.visible_warning_model()):
            time.sleep(2)
            for i in range(5):   
                tb.click_cross_button()
                tb.click_proceed()
                log.info("Warning model closed for attendee index: %s",str(attendee))
                attendee=select_random().random_number(received_count)
                tb.click_attendee_box(attendee)
                log.info("Next attendee selected index: %s",str(attendee))
                tb.click_attendee_proceed()
                if(tb.visible_warning_model() is False):
                    break
            if(tb.visible_warning_model()):
                assert False ,"Warning model not closed"

        time.sleep(2)

        if(driver.title=="Addons"):
            add_on_test().add_on_page(driver)

        custom_fields_actions().custom_field_action(driver)

        time.sleep(2)
        waiver_vima_action().waiver_vima(driver)
        # apply_discount().test_discount(driver)
        time.sleep(2)
        tb.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        tb.click_home()
        loginAction().authenticate_cookie(driver)