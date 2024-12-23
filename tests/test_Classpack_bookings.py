import time
import pytest
from Base.logfile import Logger
from Base.random_select import select_random
from Base.stripe_popup import stripe_action
from pages.classpackbookings import classpackbooking
from tests.login import loginAction


log = Logger().get_logger()
lg=loginAction()

class Testclasspack_bookings():
    @pytest.mark.order(3)
    def test_classpackbooking_action(self, driver):
        driver.implicitly_wait(30)        
        lg.login_action(driver)
        cpb=classpackbooking(driver)
        print('classpack booking started')
        cpb.click_classpack_checkbox()
        cpb.click_apply()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 300);")
        cpb.click_select_classpack()
        cpb.click_proceed()
        if (cpb.visible_attendee_moddel()):
            time.sleep(2)
            script="""return document.getElementsByName('attendees-id-list').length"""
            recived_count=driver.execute_script(script)
            attendee=select_random().random_number(recived_count)
            cpb.click_attendee_box(attendee)
            cpb.click_attendee_proceed()
        # cpb.enter_couponcode("DSCNT123")
        # cpb.click_applycoupon()
        if(driver.title=="Addons"):
            cpb.click_addon_proceed()
        cpb.click_waiver_box()
        cpb.click_review_proceed()
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)
        cpb.click_credit_booking_class()
        cpb.click_confirm_booking()
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        cpb.click_home()
        lg.authenticate_cookie(driver)

        
    @pytest.mark.order(4)
    def test_program_action(self, driver):
        driver.implicitly_wait(30)
        pb=classpackbooking(driver)
        lg.login_action(driver)
        print('Program booking Started')
        pb.click_classpack_checkbox()
        pb.click_apply()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 300);")
        pb.click_select_program()
        pb.click_proceed()
        if (pb.visible_attendee_moddel()):
            time.sleep(2)
            script="""return document.getElementsByName('attendees-id-list').length"""
            recived_count=driver.execute_script(script)
            attendee=select_random().random_number(recived_count)
            pb.click_attendee_box(attendee)
            pb.click_attendee_proceed()
        # cpb.enter_couponcode("FIXRENEW")
        # cpb.click_applycoupon()
        if(driver.title=="Addons"):
            pb.click_addon_proceed()
        pb.click_waiver_box()
        pb.click_review_proceed()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        stripe_action().stripe_data_enty(driver)
        pb.click_home()
        lg.authenticate_cookie(driver)