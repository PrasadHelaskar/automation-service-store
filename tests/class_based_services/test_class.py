import time
from base.logfile import Logger
from base.stripe_popup import stripe_action
from base.json_operations import (json_read,json_update)
from base.random_select import select_random
from base.waiver_vima import waiver_vima_action
from base.custom_field import custom_fields_actions
from pages.class_booking import class_booking
from tests.login import loginAction
from tests.add_on import add_on_test


log=Logger().get_logger()

class Test_class_booking_action():
    def test_class_booking_action(self,driver):
        """CLass Booking"""
        # driver.implicitly_wait(30)
        loginAction().login_action(driver)
        cb=class_booking(driver)
        
        cb.click_home()
        time.sleep(5)

        service_type=cb.get_checkbox_text()
        log.info("service_type: %s",service_type)

        if service_type.lower()=="classes":
            cb.click_checkbox()
            cb.click_filter_submit()
        
        else:
            raise Exception("Unable to locate the class in filters")
        
        time.sleep(5)
        
        script="return document.getElementsByClassName('primary-button-card bc4 fc1').length;"
        i= driver.execute_script(script)
        log.info("element count: %s",str(i))
        selected_service=select_random().random_number(i)
        cb.click_book_button(selected_service)

        log.info("Service name: %s",cb.get_service_name())
        
        schedule_count=int(json_read("CLASS_SCHEDULE_COUNT"))
        log.info("schedule count: %s",str(schedule_count))
        for j in range(schedule_count, (schedule_count+5)):
            cb.click_schedule(j)

        cb.click_checkout_proceed()

        time.sleep(3)
            
        # add_family_checkout_flow(driver)

        script="""return document.getElementsByClassName("w-checkbox-input waitlist-checkbox").length;"""
        recived_count=driver.execute_script(script)
        attendee=select_random().random_number(recived_count)
        log.info("seleccted attendee count: %s",attendee)

        for i in range(1, (attendee+1)):
            cb.click_attendee_box(i)

        cb.click_attendee_proceed()
    
        if cb.visible_addon_page():
            add_on_test().add_on_page(driver)

        custom_fields_actions().custom_field_action(driver)
        waiver_vima_action().waiver(driver)

        time.sleep(5)

        text=cb.is_credit_booking()
        if text=="Select Credits":
            raise Exception("Triggering credit booking causes the system to exit the normal booking flow.")
        
        cb.click_review_proceed()
        stripe_action().stripe_data_enty(driver)
        time.sleep(7)
        cb.click_back_to_home()
        loginAction().authenticate_cookie(driver)
        json_update("CLASS_SCHEDULE_COUNT",str(schedule_count+5))
        