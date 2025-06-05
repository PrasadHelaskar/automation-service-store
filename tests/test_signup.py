import pytest
import time
import os
from faker import Faker
from dotenv import load_dotenv
from base.random_select import select_random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from base.revised_API_LOG import APILOG
from pages.signup import signup
from tests.login import loginAction

class Test_sign_up():
    # @pytest.mark.skip(reason="Not required for full run")
    @pytest.mark.sign_up
    @pytest.mark.order(1)
    def test_sign_up(self, driver):
        load_dotenv()
        # apilogger = APILOG(driver)
        driver.get(os.getenv('URL'))
        sg=signup(driver)
        faker=Faker('en_US')
        sg.click_signup()
        sg.enter_email(os.getenv('EMAIL'))
        sg.click_continuebutton()
        sg.enter_firstname(faker.first_name())
        sg.enter_lastname(faker.last_name())
        sg.enter_phone_number(faker.phone_number())
        
        sg.enter_password(os.getenv('PASSWORD'))
        sg.enter_confirmpassword(os.getenv('PASSWORD'))
        
        if (sg.check_custom_field()):
            sg.click_dobfield()
            time.sleep(5)
            sr= select_random()
            month_dropdown = driver.find_element(By.NAME, "months")
            select_month = Select(month_dropdown)
            month=sr.random_month()
            select_month.select_by_visible_text(month)
            year_dropdown = driver.find_element(By.NAME, "years")
            select_year = Select(year_dropdown)
            year=sr.random_year()
            select_year.select_by_visible_text(str(year))
            sg.click_date()
            sg.click_dobfield()
        sg.click_vima_consent()
        sg.click_submit()
        time.sleep(5)
        loginAction().Store_cookie(driver)