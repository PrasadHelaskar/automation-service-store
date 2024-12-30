import time
import pytest
from Base.logfile import Logger
from Base.stripe_popup import stripe_action
from pages.product_digital_product import digitalproductelement
from tests.login import loginAction
from Base.random_select import select_random

log = Logger().get_logger()

class Testproduct_booking():
    @pytest.mark.order(9)
    def test_digital_product(self,driver):
        driver.implicitly_wait(30)
        pd=digitalproductelement(driver)
        loginAction().login_action(driver)
        pd.click_product_page()
        time.sleep(10)
        pd.click_PD_filter()
        pd.click_submit()
        pd.click_service()
        time.sleep(5)
        script = """return document.querySelectorAll('.add-section.fc4.oc4.justify-centre').length;"""
        i= driver.execute_script(script)
        log.info("element count="+str(i))
        count=select_random().random_number(i)
        log.info("Loop limit="+str(count))

        for j in range(count):
            try:
                pd.click_pricing_option()
                time.sleep(2)
            except:
                log.info("the Count Exceeded Then Visible UI Elements")
                break
            
        pd.click_checkout_proceed()
        pd.click_waiver_checkbox()
        pd.click_review_proceed()
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)
        pd.click_home()
        loginAction().authenticate_cookie(driver)