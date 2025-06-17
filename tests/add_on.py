import time
from base.logfile import Logger
from pages.add_on_element import add_on
from base.random_select import select_random
from base.Screenshot import screenshot

log=Logger().get_logger(__name__)

class add_on_test():
    def add_on_page(self, driver):
        time.sleep(5)
        aop=add_on(driver)
        screenshot(driver).take_screenshot_direct()
        log.info("Add_on page flow")
        try:
            script_general_item="return document.querySelectorAll('#select_general_service').length;"
            recived_general_item=driver.execute_script(script_general_item)
            log.info("General item count: %s",str(recived_general_item))
            selected_count=select_random().random_number(recived_general_item)
            log.info("General_item selected_count: %s",str(selected_count))
            for i in range(1, selected_count):
                try:
                    aop.click_general_item(i)
                    time.sleep(2)
                    if(aop.visible_box()):
                        aop.click_close()
                except Exception as e:
                    log.info("General item not found > %s",e)
                    break
        except Exception as e:
            log.error("No General item found to add > %s",e)

        try:
            script_classpack="return document.querySelectorAll('#select_classpack').length;"
            recived_classpack=driver.execute_script(script_classpack)
            log.info("Classpack count: %s",str(recived_classpack))
            selected_count=select_random().random_number(recived_classpack)
            log.info("classpack selected_count: %s",str(selected_count))
            for i in range(1, selected_count+1):
                try:
                    aop.click_classpack(i)
                    time.sleep(2)
                except Exception as e:
                    log.info("Classpack not found > %s",e)
                    break
        except Exception as e:
            log.error("No classpack found to add > %s",e)


        aop.click_addon_proceed()