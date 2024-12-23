import time
import traceback
from selenium import webdriver
import pytest
from Base.logfile import Logger
from Base.stripe_popup import stripe_action
from pages.camp_booking import camp_booking
from tests.login import loginAction
from Base.random_select import select_random

log=Logger().get_logger()

class TestCamp_booking():
    @pytest.mark.order(6)
    def test_camp_booking(self, driver):
        driver.implicitly_wait(30)    
        cmp=camp_booking(driver)
        loginAction().login_action(driver)
        cmp.click_camp_page()
        time.sleep(5)
        script = """return document.getElementsByClassName('primary-button-card bc4 fc1').length;"""
        i= driver.execute_script(script)
        log.info("element count="+str(i))
        service_index=select_random().random_number(i)
        cmp.click_camp_selection(service_index)
        cmp.click_add_attendee()
        time.sleep(2)
        script = """return document.getElementsByClassName('w-checkbox-input waitlist-checkbox').length;"""
        i= driver.execute_script(script)
        log.info("element count="+str(i))
        attendee_count=select_random().random_number(i)
        log.info("selected attendee count="+str(attendee_count))

        for j in range (1, (attendee_count+1)):
            cmp.click_attendee(j)

        cmp.click_attendee_proceed()

        schedule_count=35
        for j in range(schedule_count, (schedule_count+5)):
            cmp.click_schedule(j)
            
        cmp.click_schedule_proceed()

        if cmp.visible_addon_page():
            cmp.click_addon_proceed()
            
        time.sleep(2)
        cmp.click_waiverbox()
        cmp.click_review_proceed()
        stripe_action().stripe_data_enty(driver)
        driver.execute_script("window.debugger = function() {};")
        cmp.click_home()
        loginAction().authenticate_cookie(driver)
        log.info("Camp booking Compleated")        
