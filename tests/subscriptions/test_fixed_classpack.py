import time
import pytest
import random
from base.logfile import Logger
from base.random_select import select_random
from base.stripe_popup import stripe_action
from base.waiver_vima import waiver_vima_action
from pages.classpackbookings import classpackbooking
# from base.discount import apply_discount
from tests.login import loginAction
from tests.add_on import add_on_test



log = Logger().get_logger()
lg=loginAction()

class Test_fixed_classpack():
    @pytest.mark.order(12)
    def test_fixed_classpack(self, driver):
        lg.login_action(driver)
        cpb=classpackbooking(driver)
        print('classpack booking started')
        
        # filter the classpacks
        # cpb.click_classpack_checkbox()
        # cpb.click_apply()

        cpb.click_classpack_page()
        time.sleep(2)

        elements=cpb.get_service_name()
        # log.info("sorted_dict: %s",elements)
        
        sorted_dict={
            index:{'id':index,'name':service.text,'element':service}
            for index,service in enumerate(elements,start=1)
            if 'fixed' in service.text.lower()
        }
        if not sorted_dict:
            raise ValueError("No service found containing 'fixed' in text.")
        # log.info("sorted_dict: %s",sorted_dict)
        selected = random.choice(list(sorted_dict.values()))
        selected_id = selected['id']

        log.info("Selected service with id: %d, name: %s", selected_id, selected['name'])

        cpb.click_select_service(selected_id)      
        cpb.click_proceed()

        if (cpb.visible_attendee_moddel()):
            time.sleep(2)
            script="""return document.getElementsByName('attendees-id-list').length"""
            recived_count=driver.execute_script(script)
            attendee=select_random().random_number(recived_count)
            cpb.click_attendee_box(attendee)
            log.info("Attendee selected index: %s",str(attendee))
            cpb.click_attendee_proceed()

        repeat_booking(driver)

        time.sleep(2)
        # log.info("Addons page visible="+str(driver.title or "None"))
        if(driver.title=="Addons"):
            add_on_test().add_on_page(driver)

        time.sleep(2)
        waiver_vima_action().waiver_vima(driver)
        # apply_discount().test_discount(driver)
        cpb.click_review_proceed()
        loginAction().order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        time.sleep(10)

        if(driver.title=="Classpacks"):
            cpb.click_credit_booking_class()
            cpb.click_confirm_booking()
            time.sleep(10)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        cpb.click_home()
        lg.authenticate_cookie(driver)

def repeat_booking(driver):
    """Used to handle the BOok again  model"""
    rb=classpackbooking(driver)
    if(rb.is_repeat_booking_visible()):
        log.info("The Buy Again model visible?: %s",str(rb.is_repeat_booking_visible()))
        rb.click_buy_again()