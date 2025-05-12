import time
import pytest
from selenium.webdriver.support.ui import Select
from base.logfile import Logger
from tests.login import loginAction
from pages.all_page import page_check

log=Logger().get_logger()

class Test_all_pages():
    pytest.mark.order(10)
    def test_page_check(self, driver):
        ap=page_check(driver)
        loginAction().login_action(driver)
        
        ap.click_home()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_sunscription()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_classpacks()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_program()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_schedules()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_products()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_party()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_camps()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)

        ap.click_giftcards()
        time.sleep(5)
        url=ap.get_url()
        log.info("Current URL: %s",url)
        
