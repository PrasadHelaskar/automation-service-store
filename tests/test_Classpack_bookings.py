import time
from selenium import webdriver
import pytest
from tests.conftest import driver
# from tests.test_login import Testlogin 
from pages.classpackbookings import classpackbooking 


class Testclasspack_bookings():

    def test_classpackbooking_action(self, driver):
        cpb=classpackbooking(driver)
        cpb.click_classpack_checkbox()
        cpb.click_apply()
        cpb.click_select_classpack()
        cpb.click_proceed()
        cpb.enter_couponcode("CP2309")
        cpb.click_applycoupon()
        cpb.click_waiver_box()
        time.sleep(15)
        cpb.click_review_proceed()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

