import os
import time
import pytest
from Base.logfile import Logger
from pages.cancelation_element import cancelation_booking
from tests.login import loginAction
from Base.random_select import select_random

log=Logger().get_logger()

class Test_service_cancelation():
    @pytest.mark.order(11)
    def test_cancelation(self, driver):
        loginAction().login_action(driver)
        cb=cancelation_booking(driver)
        cb.click_profile()
        cb.click_profile_page()
        for i in range(1,5):
            time.sleep(15)
            if (cb.is_visible_empty_state()):
                log.info(f"Iteration Count: "+str(i))
                cb.click_drop_down()
                script="return document.getElementsByClassName('d-flex schedule-dropdown').length;"
                reviced_count=driver.excute_script(script)
                select_attendee=select_random().random_number(reviced_count)
                cb.click_familty_members(select_attendee)
                if(cb.is_visible_empty_state()==False):
                    log.info("Schedules are seen for: "+str(select_attendee))
                    break
        if(cb.is_visible_empty_state()):
            assert False, "Selected 5 attendees doesn't have schedule so try again"
        
        script="return document.getElementsByClassName('view-details-button schedule_details').length;"
        reviced_count=driver.execute_script(script)
        seleted_service=select_random().random_number(reviced_count)

        script_label="return document.getElementsByClassName('label label-danger').length"
        recived_lebel_count=driver.execute_script(script_label)
        log.info("Recived Lebel Count:"+str(recived_lebel_count))

        service=cb.view_details(seleted_service)
        service_name=str(service.get_attribute("data-service_name"))
        log.info(f"Selected Service Name"+service_name)
        service_type=str(service.get_attribute("data-service_type"))
        log.info("Selected Service typr"+service_type)
        cb.click_view_details(seleted_service)  

        cb.click_cancel_everyone()
        time.sleep(5)

        recived_lebel_count_update=driver.execute_script(script_label)
        log.info("Recived Lebel Count Update:"+str(recived_lebel_count_update))

        if(recived_lebel_count!=recived_lebel_count_update):
            service=cb.view_card(seleted_service)
            save_folder = "cancelled_screenshots"
            os.makedirs(save_folder, exist_ok=True) 
            save_path = os.path.join(save_folder, "Cancelled_element.png")
            service.screenshot(save_path)
            log.info("Cancelation Successful and Cancelled_element.png this is service card screenshot")
        else:
            log.error("Cancelation Faild")
            assert False