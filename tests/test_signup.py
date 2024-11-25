import pytest
from Base.revised_API_LOG import APILOG
from pages.signup import signup
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import os
import time
import logging
from Base.random_select import select_random
from selenium.webdriver.support.ui import Select


logger = logging.getLogger(__name__)
class Testsign_up():
    @pytest.mark.order(1)
    def test_sign_up(self, driver):
        load_dotenv()
        sr=select_random()
        # apilogger = APILOG(driver)
        driver.get(os.getenv('url'))
        sg=signup(driver)
        sg.click_signup()
        sg.enter_email(os.getenv('email'))
        sg.click_continuebutton()
        sg.enter_firstname(sr.first_name())
        sg.enter_lastname(sr.last_name())
        sg.click_submit()
        sg.enter_password(os.getenv('password'))
        sg.enter_confirmpassword(os.getenv('password'))
        sg.click_submit()
        logger.info(str(sg.check_header))
        if (sg.check_header()):
            sg.click_dobfield()
            time.sleep(5)
            month_dropdown = driver.find_element(By.NAME, "months")
            select_month = Select(month_dropdown)
            month=sr.random_month()
            select_month.select_by_visible_text(month)
            year_dropdown = driver.find_element(By.NAME, "years")
            select_year = Select(year_dropdown)
            year=sr.rendom_year()
            select_year.select_by_visible_text(year)
            sg.click_date()
            sg.click_dobfield()
        sg.click_submit()
        time.sleep(20)