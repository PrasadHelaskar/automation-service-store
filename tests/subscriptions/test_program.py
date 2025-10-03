import sys
import time
import json
from datetime import datetime, timedelta
import pytest
from selenium.webdriver.common.by import By
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.waiver_vima import waiver_vima_action
# from base.discount import apply_discount
from base.custom_field import custom_fields_actions
from pages.classpack_bookings_elements import classpackbooking
from tests.login import loginAction
from tests.add_on import add_on_test
from tests.test_add_family import add_family_checkout_flow


log = Logger().get_logger(__name__)
lg=loginAction()
selectedAttendees=[]

class Test_program():        
    @pytest.mark.order(4)
    def test_program(self, driver):
        """The Method for the program booking"""
        pb=classpackbooking(driver)
        driver.implicitly_wait(10)
        lg.login_action(driver)
        for i in range(0,1):
            log.info('Program booking Started')
            # filter the programs
            # pb.click_classpack_checkbox()
            # pb.click_apply()
            pb.click_program_page()
            time.sleep(5)

            script="""return document.getElementsByClassName('primary-button-card bc4 fc1').length;"""
            service_count=driver.execute_script(script)
            log.info("Total services available: %s",service_count)

            if service_count in range(1,10):
                service_index=select_random().random_number(service_count)
            else:
                service_index=select_random().random_number(5)

            pb.click_select_service(1)
            log.info("Service selected index: %s",str(service_index))

            time.sleep(2)
            script="""return document.getElementsByName("cp-radio-button").length;"""
            received_count=driver.execute_script(script)
            index=select_random().random_number(received_count)
            log.info("Selected schedule index: %s",index)
            pb.click_start_date(index)

            pb.click_proceed()
            time.sleep(5)
            # add_family_checkout_flow(driver)

            # add_family_checkout_flow(driver)
            script="""return document.getElementsByClassName("w-checkbox-input waitlist-checkbox").length;"""
            received_count=driver.execute_script(script)
            attendee=select_random().random_number(received_count)
            log.info("Selected Attendees Arrey:%s",selectedAttendees)
            
            if attendee not in selectedAttendees:
                pb.click_attendee_box(attendee)
                log.info("Attendee selected index: %s",str(attendee))
                pb.click_attendee_proceed()
                selectedAttendees.append(attendee)
            else:
                log.info("Repeat Booking Attendee selected index: %s",str(attendee))
                pb.click_attendee_box(attendee)
                pb.click_attendee_proceed()
                time.sleep(2)
            
            repeat_booking(driver)
            time.sleep(2)
            
            if(driver.title=="Addons"):
                # log.info("Addons page visible="+str(driver.title or "None"))
                add_on_test().add_on_page(driver)
                
            custom_fields_actions().custom_field_action(driver)
            
            waiver_vima_action().waiver_vima(driver)
            # apply_discount().test_discount(driver)
            lg.order_invoice_cookies(driver)

            # date aiteration method
            # dateAlteration(driver)

            pb.click_review_proceed()
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            stripe_action().stripe_data_enty(driver)
            time.sleep(20)
            pb.click_home()
            lg.authenticate_cookie(driver)
            log.info("Tha Program booking Execution Completed \n")

def repeat_booking(driver):
    """Used to handle the BOok again  model"""
    rb=classpackbooking(driver)
    if(rb.is_repeat_booking_visible()):
        log.info("The Buy Again model visible?: %s",str(rb.is_repeat_booking_visible()))
        rb.click_buy_again()
        Test_program().test_program(driver)
        sys.exit()

def dateAlteration(driver):
    
    start_date_str = "20 Sep 2025"
    start_date = datetime.strptime(start_date_str, "%d %b %Y")
    end_date = start_date + timedelta(weeks=4)
    end_date_str = end_date.strftime("%d %b %Y")

    # Start date
    hidden_date_start = driver.find_element(By.NAME, "start_date")
    driver.execute_script("arguments[0].value = arguments[1];", hidden_date_start, start_date_str)
    log.info("Start Date: %s",start_date_str)
    
    # End date
    hidden_date_end = driver.find_element(By.ID, "end_date")
    driver.execute_script("arguments[0].value = arguments[1];", hidden_date_end, end_date_str)
    log.info("End Date: %s",end_date_str)

    # Update hidden input JSON
    hidden_input = driver.find_element(By.NAME, "classpacks")
    json_str = hidden_input.get_attribute("value")
    data = json.loads(json_str)
    data[0]["classpack_start_date"] = start_date_str
    new_json_str = json.dumps(data)
    driver.execute_script("arguments[0].value = arguments[1];", hidden_input, new_json_str)