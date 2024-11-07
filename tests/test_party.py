import time
import traceback
from selenium import webdriver
import pytest
from Base.logfile import Logger
from pages.partypackage import partypackage
from tests.login import loginAction

log = Logger().get_logger()

class Testparty_bookings():
    @pytest.mark.order(3)
    def test_party(self, driver):
        # try:
            pb=partypackage(driver)
            lg=loginAction()
            driver.implicitly_wait(30)
            lg.login_action(driver)
            pb.click_party_tab()
            time.sleep(10)
            pb.click_party_select()
            pb.click_expand()
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            pb.click_package()
            time.sleep(10)        
            # log.info(pb.text_empty_state())
            if pb.visible_empty_state():
                time.sleep(15)
                log.info('in if block')
                pb.click_next_schedule()
                time.sleep(5)
            pb.click_schedule_selection()
            pb.click_schedule_proceed()
            pb.click_attendee_seletion()
            time.sleep(5)
            pb.click_attendee_peoceed()
            time.sleep(5)
            pb.click_addon_proceed()
            pb.click_waiverbox()
            pb.click_review_proceed()
            driver.execute_script("window.debugger = function() {};")
            pb.click_home()
            # assert driver.title == "Expected", "Title does not match!"
            lg.authenticatte_cookie(driver)
        # except Exception as e:
        #     log.error("failed !!!")
        #     traceback.print_exc()
            # log.warn(traceback.format_exc())
