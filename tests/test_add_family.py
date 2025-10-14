import time
import pytest
from faker import Faker
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from base.logfile import Logger
from base.random_select import select_random
from pages.addfamily_Client_elements import addfamily
from tests.login import loginAction


log=Logger().get_logger(__name__)

class Test_add_family():
    """Adding family memebrs from the client profile"""
    # @pytest.mark.skip(reason="Not required for full run")
    @pytest.mark.sign_up
    def test_add_family_client(self, driver):
        """Method to add the family member from the client profile"""
        af=addfamily(driver)
        loginAction().login_action(driver)
        time.sleep(10)
        count=5
        af.click_profile()
        af.click_profile_page()
        time.sleep(5)
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
            time.sleep(2)
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
            time.sleep(7)
            script = """return document.getElementsByClassName("product-listing bc3 bw1 width-100").length;"""
            i= driver.execute_script(script)
            log.info("element count: %s",str(i))
            time.sleep(5)
            div=af.scroll_div()
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",div)
            value=True if (af.get_added_name(i)==(fn+" "+ln)) else False
            log.info("Verification of the family addition Process for %s: %s",fn,value)
            end_time=time.time()
            log.info("Execution time: %s",str(end_time-start_time))

@staticmethod
def add_family_checkout_flow(driver):
    """Adding Famly members from the check out flow"""
    afck=addfamily(driver)
    start_time=time.time()

    if(afck.is_attendee_model_visible()):
        afck.click_add_family_btn_ck()
        fn=Faker().first_name()
        afck.type_first_name(fn)
        ln=Faker().last_name()
        afck.type_last_name(ln)

        # afck.click_dob()
        # time.sleep(5)
        # sr= select_random()
        # month_dropdown = driver.find_element(By.NAME, "months")
        # select_month = Select(month_dropdown)
        # month=sr.random_month()
        # select_month.select_by_visible_text(month)
        # year_dropdown = driver.find_element(By.NAME, "years")
        # select_year = Select(year_dropdown)
        # year=sr.random_year()
        # select_year.select_by_visible_text(str(year))
        # afck.click_date()
        # afck.click_dob()

        afck.type_dob_old(10)
        afck.type_dob_old(5)
        yr=select_random().random_year()
        afck.type_dob_old(yr)

        afck.click_submit()
        time.sleep(10)
        script="return document.getElementsByClassName('fc2 booking-content-list-text body-text-1-regular fc2 text-capitalize new-attendee-list-t').length;"
        i= driver.execute_script(script)
        log.info("element count: %s",str(i))
        time.sleep(2)
        div=afck.scroll_div_ck()
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;",div)

        # value=True if (afck.get_added_name_ck(i)==(fn+" "+ln)) else False
        log.info("Completed the family addition Process")

    end_time=time.time()
    log.info("Execution time: %s",str(end_time-start_time))