import time
import pytest
from base import random_select
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.waiver_vima import waiver_vima_action
from pages.classpackbookings import classpackbooking
from tests.login import loginAction
from base.discount import apply_discount
from tests.add_on import add_on_test


log = Logger().get_logger()
lg=loginAction()

class Test_classpack_bookings():
    # """This is for the subscription booking: Classpack/Program"""
    # @pytest.mark.order(3)
    # def test_classpackbooking_action(self, driver):
    # """This is for the classpack booking"""
    #     driver.implicitly_wait(30)        
    #     lg.login_action(driver)
    #     cpb=classpackbooking(driver)
    #     print('classpack booking started')
        
    #     # filter the classpacks
    #     # cpb.click_classpack_checkbox()
    #     # cpb.click_apply()
    #     cpb.click_classpack_page()
    #     time.sleep(2)

    #     script="""return document.getElementsByClassName('primary-button-card bc4 fc1').length;"""
    #     i=driver.execute_script(script)
    #     log.info("Total services available: "+str(i))

    #     if i in range(1,10):
    #         service_index=select_random().random_number(i)
    #     else:
    #         service_index=select_random().random_number(10)
        
    #     log.info("Service selected index: "+str(service_index))
    #     cpb.click_select_service(service_index)        
    #     cpb.click_proceed()

    #     if (cpb.visible_attendee_moddel()):
    #         time.sleep(2)
    #         script="""return document.getElementsByName('attendees-id-list').length"""
    #         recived_count=driver.execute_script(script)
    #         attendee=select_random().random_number(recived_count)
    #         cpb.click_attendee_box(attendee)
    #         log.info("Attendee selected index: "+str(attendee))
    #         cpb.click_attendee_proceed()
    #         self.repeat_booking(driver)

    #     # cpb.enter_couponcode("DSCNT123")
    #     # cpb.click_applycoupon()
    #     time.sleep(2)
    #     # log.info("Addons page visible="+str(driver.title or "None"))
    #     if(driver.title=="Addons"):
    #         add_on_test().add_on_page(driver)

    #     time.sleep(2)
    #     waiver_vima_action().waiver_vima(driver)
    #     apply_discount().test_discount(driver)
    #     cpb.click_review_proceed()
    #     loginAction().order_invoice_cookies(driver)
    #     stripe_action().stripe_data_enty(driver)
    #     time.sleep(10)

    #     if(driver.title=="Classpacks"):
    #         cpb.click_credit_booking_class()
    #         cpb.click_confirm_booking()
    #         time.sleep(10)

    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #     cpb.click_home()
    #     lg.authenticate_cookie(driver)
    #     log.info("Tha classpack booking Execution Completed")

        
    @pytest.mark.order(4)
    def test_program_action(self, driver):
        """The Method for the program booking"""
        driver.implicitly_wait(30)
        pb=classpackbooking(driver)
        lg.login_action(driver)
        print('Program booking Started')
        #  filter the programs
        # pb.click_classpack_checkbox()
        # pb.click_apply()
        time.sleep(5)
        pb.click_program_page()
        time.sleep(2) 

        script="""return document.getElementsByClassName('primary-button-card bc4 fc1').length;"""
        i=driver.execute_script(script)
        log.info("Total services available: %s",str(i))

        if i in range(1,10):
            service_index=select_random().random_number(i)
        else:
            service_index=select_random().random_number(10)

        log.info("Service selected index: %s",str(service_index))
        pb.click_select_service(service_index)
        pb.click_proceed()
        
        if (pb.visible_attendee_moddel()):
            time.sleep(2)
            script="""return document.getElementsByName('attendees-id-list').length"""
            recived_count=driver.execute_script(script)
            attendee=select_random().random_number(recived_count)
            pb.click_attendee_box(attendee)
            log.info("Attendee selected index: %s",str(attendee))
            pb.click_attendee_proceed()
            self.repeat_booking(driver)

        # cpb.enter_couponcode("FIXRENEW")
        # cpb.click_applycoupon()
        time.sleep(2)
        # log.info("Addons page visible="+str(driver.title or "None"))
        if(driver.title=="Addons"):
            add_on_test().add_on_page(driver)

        waiver_vima_action().waiver_vima(driver)
        apply_discount().test_discount(driver)
        pb.click_review_proceed()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        stripe_action().stripe_data_enty(driver)
        pb.click_home()
        lg.authenticate_cookie(driver)
        log.info("Tha Program booking Execution Completed")

    def repeat_booking(self,driver):
        """Used to handle the BOok again  model"""
        rb=classpackbooking(driver)
        if(rb.is_repeat_booking_visible()):
            log.info("The Buy Again model visible?: %s",str(rb.is_repeat_booking_visible()))
            rb.click_buy_again()