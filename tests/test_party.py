import time
import traceback
from selenium import webdriver
import pytest
from Base.logfile import Logger
from Base.stripe_popup import stripe_action
from pages.partypackage import partypackage
from tests.login import loginAction

log = Logger().get_logger()

class Testparty_bookings():
    @pytest.mark.order(2)
    def test_party(self, driver):
        # try:
            pb=partypackage(driver)
            lg=loginAction()
            lg.login_action(driver)
            pb.click_party_tab()
            time.sleep(5)
            pb.click_party_select()
            pb.click_expand()
            time.sleep(10)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            pb.click_package()        
            if pb.visible_empty_state():
                log.info('in if block')
                pb.click_next_schedule()
            pb.click_schedule_selection()
            pb.click_schedule_proceed()
            pb.click_attendee_seletion()
            pb.click_attendee_proceed()
            if pb.visible_addon_page():
                pb.click_addon_proceed()
            pb.click_waiverbox()
            pb.click_review_proceed()
            stripe_action().stripe_data_enty(driver)
            # driver.execute_script("window.debugger = function() {};")
            time.sleep(30)
            pb.click_home()
            lg.authenticate_cookie(driver)
            log.info("Praty booking Compleated")
        # except Exception as e:
        #     log.error("failed !!!")
        #     traceback.print_exc()
            # log.warn(traceback.format_exc())
