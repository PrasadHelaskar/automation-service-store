import time
from Base.logfile import Logger
from pages.add_on_element import add_on
from Base.random_select import select_random

log=Logger().get_logger()

class add_on_test():
    def add_on_page(self, driver):
        time.sleep(5)
        aop=add_on(driver)
        log.info("Add_on page flow")
        try:
            script_General_item="return document.querySelectorAll('#select_general_service').length;"
            recived_general_item=driver.execute_script(script_General_item)
            log.info("General item count="+str(recived_general_item))
            selected_count=select_random().random_number(recived_general_item)
            log.info("General_item selected_count: "+str(selected_count))
            for i in range(1, selected_count):
                try:
                    aop.click_general_item(i)
                    time.sleep(2)
                except:
                    log.info("General item not found")
                    break
        except Exception as e:
            log.error("No General item found to add")

        try:
            script_classpack="return document.querySelectorAll('#select_classpack').length;"
            recived_classpack=driver.execute_script(script_classpack)
            log.info("Classpack count="+str(recived_classpack))
            selected_count=select_random().random_number(recived_classpack)
            log.info("classpack selected_count: "+str(selected_count))
            for i in range(1, selected_count):
                try:
                    aop.click_classpack(i)
                    time.sleep(2)
                except:
                    log.info("Classpack not found")
                    break
        except Exception as e:
            log.error("No classpack found to add")


        aop.click_addon_proceed()