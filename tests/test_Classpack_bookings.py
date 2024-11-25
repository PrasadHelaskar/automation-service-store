import time
import pytest
from Base.logfile import Logger
from Base.stripe_popup import stripe_action
from pages.classpackbookings import classpackbooking
from tests.login import loginAction

log = Logger().get_logger()
lg=loginAction()

class Testclasspack_bookings():
    @pytest.mark.order(2)
    def test_classpackbooking_action(self, driver):
        lg.login_action(driver)
        cpb=classpackbooking(driver)
        print('classpack booking started')
        cpb.click_classpack_checkbox()
        cpb.click_apply()
        time.sleep(20)
        driver.execute_script("window.scrollBy(0, 300);")
        cpb.click_select_classpack()
        cpb.click_proceed()
        if (cpb.visible_attendee_moddel()):
            time.sleep(10)
            cpb.click_attendee_box()
            cpb.click_attendee_proceed()
        # need if condition for discount
        # cpb.enter_couponcode("DSCNT123")
        # cpb.click_applycoupon()
        cpb.click_waiver_box()
        cpb.click_review_proceed()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        stripe_action().stripe_data_enty(driver)
        cpb.click_home()
        lg.authenticate_cookie(driver)

        
    @pytest.mark.order(3)
    def test_program_action(self, driver):
        pb=classpackbooking(driver)
        print('Program booking Started')
        pb.click_classpack_checkbox()
        pb.click_apply()
        time.sleep(20)
        driver.execute_script("window.scrollBy(0, 300);")
        pb.click_select_program()
        pb.click_proceed()
        if (pb.visible_attendee_moddel()):
            time.sleep(10)
            pb.click_attendee_box()
            pb.click_attendee_proceed()
        # need if condition for discount
        # cpb.enter_couponcode("FIXRENEW")
        # cpb.click_applycoupon()
        pb.click_waiver_box()
        time.sleep(15)
        pb.click_review_proceed()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        stripe_action().stripe_data_enty(driver)
        pb.click_home()
        lg.authenticate_cookie(driver)
