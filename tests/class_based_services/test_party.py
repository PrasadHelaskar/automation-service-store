import time
import traceback
import pytest
from base.logfile import Logger
from base.stripe_popup import stripe_action
from base.random_select import select_random
from base.discount import apply_discount
from base.waiver_vima import *
from pages.party_package_elements import partypackage
from tests.login import loginAction

log = Logger().get_logger(__name__)

class Test_party_bookings():
    @pytest.mark.order(5)
    def test_party(self, driver):
        # driver.implicitly_wait(30)
        pb=partypackage(driver)
        sr=select_random()
        lg=loginAction()
        lg.login_action(driver)
        pb.click_party_tab()
        time.sleep(5)

        script="return document.getElementsByClassName('primary-button-card bc4 fc1').length"
        service_count=driver.execute_script(script)
        selected_service_index=sr.random_number(service_count)
        log.info("Selected Service Index: %s",str(selected_service_index))
        pb.click_party_select(selected_service_index)
        pb.click_expand()
        time.sleep(5)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        script="return document.getElementsByClassName('ss-primary-button--bc4--bw1--oc4--fc1 width-100 padding-8 bottom-20 w-button').length"
        package_count=driver.execute_script(script)
        
        
        selected_package_index=sr.random_number(package_count)
        log.info("Selected Package Index: %s",str(selected_package_index))
        pb.click_package(selected_package_index)
        time.sleep(5)    

        pb.click_monthSelection()
        script="return (Array.from(document.querySelectorAll('button.rdp-button.custom-month-picker-button')).filter(btn => !btn.disabled)).length"
        monthCount=driver.execute_script(script)
        selectedMonthIndex=sr.random_number(2,monthCount)
        pb.click_selectedMonth(selectedMonthIndex)

        # pb.click_dateSelection()
        # script="return document.getElementsByClassName('rdp-button_reset rdp-button rdp-day').length"
        # dateCount=driver.execute_script(script)
        # selectedDateIndex=sr.random_number(dateCount)
        # pb.click_selectedDate(selectedDateIndex)

        if pb.visible_empty_state():
            # log.info('test_party > Empty State > If block')
            pb.click_next_schedule()
        
        time.sleep(10)
        script="return document.getElementsByClassName('slot-selection-header padding-t-b-16 bw1 radius-4 padding-16 ').length"
        schedule_count=driver.execute_script(script)
        selected_schedule_index=sr.random_number(schedule_count)
        log.info("Selected Schedule Index: %s",str(selected_schedule_index))
        pb.click_schedule_selection(selected_schedule_index)

        pb.click_schedule_proceed()

        if (pb.visible_attendee_model()):
            time.sleep(5)            
            script="return document.getElementsByClassName('w-checkbox-input attendee-checkbox').length"
            attendee_count=driver.execute_script(script)
            selected_attendee=sr.random_number(attendee_count)
            log.info("Selected Attendee: %s",str(selected_attendee))
            
            try:
                for i in range(selected_attendee,(selected_attendee+2)):
                    pb.click_attendee_seletion(i)
            except Exception as e:
                log.info("Attendee Index is more the available count")

            pb.click_attendee_proceed()

        if pb.visible_addon_page():
            script="""return document.getElementsByClassName('add-section fc4 oc4 justify-centre').length"""
            count=driver.execute_script(script)
            log.info("Recived Count: %s",str(count))
            for i in range(1,(count+1)):
                time.sleep(5)
                pb.click_additiona_attendee()
                if i==3:
                    pass
            pb.click_addon_proceed()
        
        waiver_vima_action().waiver(driver)
        # apply_discount().test_discount(driver)
        # lg.get_all_cookies(driver)
        pb.click_review_proceed()
        lg.order_invoice_cookies(driver)
        stripe_action().stripe_data_enty(driver)
        pb.click_home()
        lg.authenticate_cookie(driver)
        log.info("Praty booking Compleated")