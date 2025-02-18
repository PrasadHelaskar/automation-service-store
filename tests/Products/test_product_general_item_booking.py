import time
import pytest
from base.logfile import Logger
from base.stripe_popup import stripe_action
from pages.product_General_item_booking import productElements
from tests.login import loginAction
from base.random_select import select_random

log = Logger().get_logger()

class Testproduct_booking():
    @pytest.mark.order(7)
    def test_general_itam(self,driver):
        driver.implicitly_wait(30)
        pe=productElements(driver)
        loginAction().login_action(driver)
        pe.click_product_page()
        time.sleep(5)
        pe.click_GI_filter()
        pe.click_submit()
        pe.click_service()
        time.sleep(5)
        script = """return document.querySelectorAll('.add-section.fc4.oc4.justify-centre').length;"""
        i= driver.execute_script(script)
        log.info("element count="+str(i))
        count=select_random().random_number(i)
        log.info("Loop limit="+str(count))

        for j in range(count):
            try:
                pe.click_pricing_option()
                time.sleep(2)
            except Exception as e:
                log.info("the Count Exceeded Then Visible UI Elements")
                break
            
        pe.click_checkout_proceed()
        pe.click_waiver_checkbox()
        pe.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)
        pe.click_home()
        loginAction().authenticate_cookie(driver)
        