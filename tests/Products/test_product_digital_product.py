import time
import pytest
from base.logfile import Logger
from base.stripe_popup import stripe_action
from base.random_select import select_random
from base.waiver_vima import *
from pages.product_digital_product_elements import digitalproductelement
from tests.login import loginAction

log = Logger().get_logger(__name__)

class Testproduct_booking():
    @pytest.mark.order(9)
    def test_digital_product(self,driver):
        # driver.implicitly_wait(30)
        pd=digitalproductelement(driver)
        loginAction().login_action(driver)
        pd.click_product_page()
        time.sleep(10)
        pd.click_PD_filter()
        pd.click_submit()
        time.sleep(5)
        pd.click_service()
        time.sleep(2)
        script = """return document.querySelectorAll('.add-section.fc4.oc4.justify-centre').length;"""
        i= driver.execute_script(script)
        log.info("element count="+str(i))
        count=select_random().random_number(i)
        log.info("Loop limit="+str(count))

        for j in range(count):
            try:
                pd.click_pricing_option()
                time.sleep(2)
            except Exception as e:
                log.info("the Count Exceeded Then Visible UI Elements")
                break
            
        pd.click_checkout_proceed()
        waiver_vima_action().waiver(driver)
        pd.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(5)
        pd.click_home()
        loginAction().authenticate_cookie(driver)
        