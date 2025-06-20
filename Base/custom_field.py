import time
from base.logfile import Logger
from base.random_select import select_random
from pages.custom_fields_elements import custom_fields

log= Logger().get_logger(__name__)

class custom_fields_actions():
    def custom_field_action(self,driver):
        cf=custom_fields(driver)
        sr=select_random()
        cf.page_wait()
        if cf.is_visible_page():
            recived_elements=cf.get_all_custom_fields()
            name=cf.get_attendee_name()
            
            for index,elem in enumerate(recived_elements, start=1):
                if not elem.is_displayed():
                    continue
                

                input_type=elem.get_attribute("type")
                is_date=elem.get_attribute("id")
                # log.info("Custom field: %s, Type: %s",index,input_type)

                scroll_script="arguments[0].scrollIntoView({block: 'center'});"
                driver.execute_script(scroll_script,elem)
                
                if input_type=="text":
                    if is_date=="dateTextWrapper":
                        elem.click()
                        date=sr.random_number(28)
                        month=7
                        year=sr.random_year()
                        cf.date_selection(date,month,year,index)
                        cf.click_attendee_name()
                    else:
                        elem.clear()
                        elem.send_keys(name)

                elif input_type=="number":
                    elem.clear()
                    elem.send_keys(sr.random_number(100))
                
                elif input_type=="checkbox":
                    if not elem.is_selected():
                        elem.click()
                        
            cf.click_proceed()