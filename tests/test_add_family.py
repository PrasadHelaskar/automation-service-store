import time
import pytest
from faker import Faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from base.logfile import Logger
from pages.addfamily_Client_profile import addfamily
from tests.login import loginAction
from base.random_select import select_random

log=Logger().get_logger()

class Test_add_family():
    # @pytest.mark.skip(reason="Not required for full run")
    @pytest.mark.sign_up
    @pytest.mark.order(2)
    def test_add_family_client(self, driver):
        """Method to add the family member from the client profile"""
        loginAction().login_action(driver)
        time.sleep(5)
        count=2
        af=addfamily(driver)
        af.click_profile()
        af.click_profile_page()
        af.click_family()
        for i in range (count):
            time.sleep(5)
            start_time=time.time()
            af.click_add_family_btn()
            fn=Faker().first_name()
            af.type_first_name(fn)
            ln=Faker().last_name()
            af.type_last_name(ln)
            
            af.type_dob()
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
            af.click_date()
            af.type_dob()

            af.click_submit_button()
            time.sleep(10)
            script = """return document.getElementsByClassName("product-listing bc3 bw1 width-100").length;"""
            i= driver.execute_script(script)
            log.info("element count: %s",str(i))
            time.sleep(2)
            div=af.scroll_div()
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",div)
            value=True if (af.get_added_name(i)==(fn+" "+ln)) else False
            log.info("Completed the family addition Process")
            end_time=time.time()
            log.info("Execution time: %s",str(end_time-start_time))
            # if value:
            #     af.click_back_button()
            #     log.info("Back to home with adding the family member")
            # else:
            #     log.info("failed in adding the family member")


        