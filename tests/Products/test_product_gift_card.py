import time
import pytest
from base.logfile import Logger
from base.stripe_popup import stripe_action
from pages.product_gift_card_booking_elements import giftcardbooking
from tests.login import loginAction
from base.random_select import select_random
from base.waiver_vima import *

log = Logger().get_logger(__name__)

class Test_gift_card():
    @pytest.mark.order(8)
    def test_gift_card(self, driver):
        # driver.implicitly_wait(30)
        gc=giftcardbooking(driver)
        loginAction().login_action(driver)
        gc.click_gift_card_page()
        time.sleep(5)
        gc.click_select_gift_card()
        time.sleep(10)
        script = """return document.getElementsByClassName('schedule-top-bar-date-selector--bc3--bw1--fc2 slot pading-18 semi-bold ').length;"""
        count=driver.execute_script(script)
        log.info("Recived element count: %s",str(count))
        gc.click_select_amount_type(count)

        if(gc.enter_amount_visible()):
            gc.enter_amount("2")

        gc.enter_name(select_random().first_name())
        gc.enter_email("prasad+giftcard@getomnify.com")
        gc.click_checkout_proceed()
        time.sleep(2)
        # waiver_vima_action().waiver(driver)
        gc.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(5)
        gc.click_home()
        loginAction().authenticate_cookie(driver)