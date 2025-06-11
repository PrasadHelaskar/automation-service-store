import time
import pytest
from base.logfile import Logger
from tests.login import loginAction
from pages.all_page_elements import page_check

log=Logger().get_logger(__name__)

class Test_all_pages():
    """ 
    To check the if all pages in service store are working 
    """
    pytest.mark.order(10)
    def test_page_check(self, driver):
        """ 
        To check the if all pages in service store are working as well as check the URL and NAP schema integration on pages 
        """
        ap=page_check(driver)
        loginAction().login_action(driver)
        
        pages=[
            ap.click_home,ap.click_subscription,ap.click_classpacks,ap.click_program,ap.click_schedules,ap.click_products,ap.click_party,ap.click_camps,ap.click_giftcards
            ]

        for methods in pages:
            log.info("Current method: %s",methods.__name__)
            methods()
            time.sleep(5)
            driver.refresh()
            url=ap.get_url()
            log.info("Current URL: %s",url)
            ap.get_attribute()