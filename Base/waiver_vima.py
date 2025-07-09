import time
from base.logfile import Logger
from pages.waiver_and_vima_elements import waiver_vima

log=Logger().get_logger(__name__)

class waiver_vima_action():
    def waiver_vima(self, driver):
        waiver=waiver_vima(driver)
        time.sleep(2)
        try:
            if(waiver.check_waiver_box()):
                log.info("The enforced waiver is enabled")
                # button_text=waiver.get_waiver_button_text()
                waiver.click_accept_waiver()
                if (waiver.check_waiver_box()):
                    log.info("The enforced VIMA is enabled")
                    waiver.click_vima_accept()

            else:
                waiver.click_waiver()
        
        except Exception as e:
            log.info("\nThe checkbox might be hidden")
            log.warning("Exception: ",exc_info=True)

    def waiver(self, driver):
        waiver=waiver_vima(driver)
        time.sleep(2)
        try:
            if(waiver.check_waiver_box()):
                log.info("The enforced waiver is enabled")
                # button_text=waiver.get_waiver_button_text()
                waiver.click_accept_waiver()
            else:
                waiver.click_waiver()
        
        except Exception as e:
            log.info("\n The checkbox might be hidden")
            log.warning("Exception: ",exc_info=True)
