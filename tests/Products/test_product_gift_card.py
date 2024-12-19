import time
import pytest
from Base.logfile import Logger
from Base.stripe_popup import stripe_action
from pages.product_gift_card_booking import giftcardbooking
from tests.login import loginAction
from Base.random_select import select_random

log = Logger().get_logger()

class Testgift_booking():
    @pytest.mark.order(8)
    def test_gift_crad(self, driver):
        gc=giftcardbooking(driver)
        loginAction().login_action(driver)
        gc.click_gift_card_page()
        time.sleep(5)
        gc.click_select_gift_card()
        time.sleep(10)
        script = """return document.getElementsByClassName('schedule-top-bar-date-selector--bc3--bw1--fc2 slot pading-18 semi-bold ').length;"""
        count=driver.execute_script(script)
        log.info("Recived element count: "+str(count))
        gc.click_select_amount_type(count)
        gc.enter_amount("45")
        gc.enter_name(select_random().first_name())
        gc.enter_email("prasad+giftcard@getomnify.com")
        gc.click_checkout_proceed()
        gc.click_waiverbox()
        gc.click_review_proceed()
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)
        gc.click_home()
        loginAction().authenticate_cookie(driver)