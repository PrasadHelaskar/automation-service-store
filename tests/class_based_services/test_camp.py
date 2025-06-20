import os
import time
import traceback
import pytest
from base.logfile import Logger
from base.stripe_popup import stripe_action
from base.random_select import select_random
from base.discount import apply_discount
from base.json_operations import *
from base.waiver_vima import *
from base.custom_field import custom_fields_actions
from pages.camp_booking_elements import camp_booking
from tests.login import loginAction
from tests.add_on import add_on_test

log=Logger().get_logger(__name__)

class Test_Camp_booking():
    @pytest.mark.order(6)
    def test_camp_booking(self, driver):
        # driver.implicitly_wait(30)    
        cmp=camp_booking(driver)
        loginAction().login_action(driver)
        cmp.click_camp_page()
        time.sleep(5)
        script = "return document.getElementsByClassName('primary-button-card bc4 fc1').length;"
        i= driver.execute_script(script)
        log.info("Service Index Count: %s",str(i))
        service_index=select_random().random_number(i)
        cmp.click_camp_selection(service_index)
        
        cmp.click_add_attendee()
        time.sleep(2)
        script = "return document.getElementsByClassName('w-checkbox-input waitlist-checkbox').length;"
        i= driver.execute_script(script)
        log.info("Attendee Count: %s",str(i))
        attendee_count=select_random().random_number(i)
        log.info("Selected Attendee Count: %s",str(attendee_count))

        for j in range (1, (attendee_count+1)):
            cmp.click_attendee(j)

        cmp.click_attendee_proceed()

        schedule_count=int(json_read("CAMP_SCHEDULE_COUNT"))
        log.info("Schedule Count: %s",str(schedule_count))
        for j in range(schedule_count, (schedule_count+2)):
            cmp.click_schedule(j)

        cmp.click_schedule_proceed()

        if cmp.visible_addon_page():
            add_on_test().add_on_page(driver)
            
        custom_fields_actions().custom_field_action(driver)
        waiver_vima_action().waiver(driver)
        # apply_discount().test_discount(driver)
        cmp.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(7)
        driver.execute_script("window.debugger = function() {};")
        cmp.click_home()
        loginAction().authenticate_cookie(driver)
        json_update("CAMP_SCHEDULE_COUNT",str(schedule_count+2))
        log.info("Camp booking Compleated")        
