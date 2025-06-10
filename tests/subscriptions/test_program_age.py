import time
import pytest
import random 
import sys
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.waiver_vima import waiver_vima_action
from base.custom_field import custom_fields_actions
from pages.classpack_bookings_elements import classpackbooking
# from base.discount import apply_discount
from tests.login import loginAction
from tests.add_on import add_on_test
from tests.test_add_family import add_family_checkout_flow


log = Logger().get_logger(__name__)
lg=loginAction()
iteration_count = 0

class Test_program_age():        
    @pytest.mark.order(4)
    def test_program_age(self, driver):
        """The Method for the program booking"""
        # driver.implicitly_wait(30)
        pb=classpackbooking(driver)
        
        if (iteration_count==0):
            lg.login_action(driver)
        
        log.info('Program booking Started')
        # filter the programs
        # pb.click_classpack_checkbox()
        # pb.click_apply()
        time.sleep(5)
        pb.click_program_page()
        time.sleep(2) 
        
        elements=pb.get_service_name()
        # log.info("sorted_dict: %s",elements)
        
        sorted_dict={
            index:{'id':index,'name':service.text,'element':service}
            for index,service in enumerate(elements,start=1)
            if 'age' in service.text.lower()
        }
        
        # log.info("sorted_dict: %s",sorted_dict)
        if not sorted_dict:
            raise ValueError("No service found containing 'age' in text.")
        selected = random.choice(list(sorted_dict.values()))
        selected_id = selected['id']

        log.info("Selected service with id: %d, name: %s", selected_id, selected['name'])

        pb.click_select_service(selected_id)      

        time.sleep(5)
        script="""return document.getElementsByName("cp-radio-button").length;"""
        recived_count=driver.execute_script(script)
        index=select_random().random_number(recived_count)
        log.info("Selected schedule index: %s",index)
        pb.click_start_date(index)

        pb.click_proceed()
        time.sleep(3)
        
        # add_family_checkout_flow(driver)
 
        script="""return document.getElementsByClassName("w-checkbox-input waitlist-checkbox").length;"""
        recived_count=driver.execute_script(script)
        attendee=select_random().random_number(recived_count)
        pb.click_attendee_box(attendee)
        log.info("Attendee selected index: %s",str(attendee))
        pb.click_attendee_proceed()
        time.sleep(2)
        
        age_model(driver)

        # log.info("Addons page visible="+str(driver.title or "None"))
        
        if(driver.title=="Addons"):
            add_on_test().add_on_page(driver)

        custom_fields_actions().custom_field_action(driver)

        waiver_vima_action().waiver_vima(driver)
        # apply_discount().test_discount(driver)
        lg.order_invoice_cookies(driver)
        time.sleep(10)
        pb.click_review_proceed()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        stripe_action().stripe_data_enty(driver)
        pb.click_home()
        lg.authenticate_cookie(driver)
        log.info("Tha Program booking Execution Completed \n")

def age_model(driver):
    """Used to dael with the ade restrictions model"""
    global iteration_count
    arm=classpackbooking(driver)

    time.sleep(5)
    if(arm.is_restriction_model_visible()):
        text=arm.get_restriction_head_message()
        log.info("Warning text: %s\n",text)
        time.sleep(2)
        arm.click_go_back()
        
        if (iteration_count<2):
            iteration_count +=1
            Test_program_age().test_program_age(driver)
        else:
            raise Exception("The maximum number of tries has been reached.")
    else:
        log.info("The attendee's age falls within the restricted range.")