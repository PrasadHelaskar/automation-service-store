import time
import pytest
from Base.logfile import Logger
from pages.classpackbookings import classpackbooking
from tests.login import loginAction

log = Logger().get_logger()

class Testclasspack_bookings():
    @pytest.mark.order(2)
    def test_classpackbooking_action(self, driver):
        lg=loginAction()
        lg.login_action(driver)
        cpb=classpackbooking(driver)
        print('classpack booking started')
        cpb.click_classpack_checkbox()
        cpb.click_apply()
        time.sleep(20)
        driver.execute_script("window.scrollBy(0, 300);")
        cpb.click_select_classpack()
        cpb.click_proceed()
        # need if condition for discount
        cpb.enter_couponcode("DSCNT123")
        log.info("B4 Discount applied")
        cpb.click_applycoupon()
        log.info("After Discount applied")
        cpb.click_waiver_box()
        time.sleep(15)
        cpb.click_review_proceed()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        cpb.click_home()
        assert driver.title == "Expected Title", "Title does not match!"

        
    @pytest.mark.order(3)
    def test_program_action(self, driver):
        cpb=classpackbooking(driver)
        print('Program booking Started')
        cpb.click_classpack_checkbox()
        cpb.click_apply()
        time.sleep(20)
        driver.execute_script("window.scrollBy(0, 300);")
        cpb.click_select_program()
        cpb.click_proceed()
        # need if condition for discount
        cpb.enter_couponcode("FIXRENEW")
        cpb.click_applycoupon()
        cpb.click_waiver_box()
        time.sleep(15)
        cpb.click_review_proceed()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        cpb.click_home()
