import time
from Base.logfile import Logger
from pages.waiver_and_vima_elements import waiver_vima

log=Logger().get_logger()

class waiver_vima_action():
    def waiver(self, driver):
        waiver=waiver_vima(driver)
        time.sleep(2)
        try:
            if(waiver.check_waiver_box()):
                log.info("The enforced waiver is enabled")
                waiver.click_accept_waiver()

            else:
                waiver.check_waiver_box()
        except Exception as e:
            log.warning("Exception: "+str(e))


    def vima_action(self,driver):
        vima=waiver_vima(driver)
        time.sleep(2) 