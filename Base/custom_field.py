import time
from base.logfile import Logger
from base.random_select import select_random
from pages.custom_fields_elements import custom_fields
from pages.addfamily_Client_elements import addfamily

log= Logger().get_logger()

class custom_fields_actions():
    def custom_field_action(self,driver):
        afck=addfamily(driver)
        cf=custom_fields(driver)
        sr=select_random()
        time.sleep(2)
        if cf.is_visible_page():
            name=cf.get_attendee_name()
            log.info("Name: %s",name)
            recived_elements=cf.get_all_custom_fields()

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
                        month=sr.random_number(11)
                        year=sr.random_number(1990,2024)
                        cf.date_selection(driver,date,month,year)
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