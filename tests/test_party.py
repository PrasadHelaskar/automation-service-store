import time
from selenium import webdriver
import pytest
from Base.logfile import Logger
from pages.partypackage import partypackage
from tests.login import loginAction

log = Logger().get_logger()

class Testparty_bookings():
    @pytest.mark.order(3)
    def test_party(self, driver):
        driver.implicitly_wait(10)
        pb=partypackage(driver)
        lg=loginAction()
        lg.login_action(driver)
        pb.click_party_tab()
        pb.click_party_select()
        pb.click_expand()
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        pb.click_package()
        # log.info(pb.text_empty_state())
        if(pb.visible_empty_state):
            log.info("in if block")
            time.sleep(10)
            pb.click_next_schedule()
        pb.click_schedule_selection()
        pb.click_scheduel_proceed()
        pb.click_attendee_seletion()
        time.sleep(10)
        pb.click_attendee_peoceed()
        pb.click_addon_proceed()
        pb.click_waiverbox()
        pb.click_review_proceed()
        pb.click_home()
        assert driver.title == "Expected", "Title does not match!"