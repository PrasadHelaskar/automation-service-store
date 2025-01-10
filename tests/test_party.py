import time
import pytest
from Base.logfile import Logger
from Base.stripe_popup import stripe_action
from pages.partypackage import partypackage
from tests.login import loginAction
from Base.random_select import select_random

log = Logger().get_logger()

class Test_party_bookings():
    @pytest.mark.order(5)
    def test_party(self, driver):
        # try:
            driver.implicitly_wait(30)
            pb=partypackage(driver)
            lg=loginAction()
            lg.login_action(driver)
            pb.click_party_tab()
            time.sleep(5)

            script="return document.getElementsByClassName('primary-button-card bc4 fc1').length"
            service_count=driver.execute_script(script)
            selected_service_index=select_random().random_number(service_count)
            pb.click_party_select(selected_service_index)
            pb.click_expand()
            time.sleep(5)
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            script="document.getElementsByClassName('ss-primary-button--bc4--bw1--oc4--fc1 width-100 padding-8 bottom-20 w-button').length"
            package_count=driver.execute_script(script)
            selected_package_index=select_random().random_number(package_count)
            pb.click_package(selected_package_index)
            time.sleep(5)    

            if pb.visible_empty_state():
                log.info('in if block')
                pb.click_next_schedule()

            script="return document.getElementsByClassName('schedule-top-bar-date-selector--bc3--bw1--fc2 slot width-196 centre ').length"
            schedule_count=driver.execute_script(script)
            selected_schedule_index=select_random().random_number(schedule_count)
            pb.click_schedule_selection(selected_schedule_index)

            pb.click_schedule_proceed()
            
            pb.click_attendee_seletion()
            pb.click_attendee_proceed()

            if pb.visible_addon_page():
                script="""return document.getElementsByClassName('add-section fc4 oc4 justify-centre').length"""
                count=driver.execute_script(script)
                log.info(f"recived count="+str(count))
                pb.click_additiona_attendee()
                pb.click_addon_proceed()
                
            pb.click_waiverbox()
            log.info("In review page: ")
            lg.get_all_cookies(driver)
            pb.click_review_proceed()
            loginAction().order_invoice_cookies(driver)
            stripe_action().stripe_data_enty(driver)
            driver.execute_script("window.debugger = function() {};")
            pb.click_home()
            lg.authenticate_cookie(driver)
            log.info("Praty booking Compleated")
        # except Exception as e:
        #     log.error("failed !!!")
        #     traceback.print_exc()
            # log.warn(traceback.format_exc())
