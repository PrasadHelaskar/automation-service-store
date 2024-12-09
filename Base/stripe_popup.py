import time
from Base.logfile import Logger
from pages.stripe_popup_ele import stripepopup
from selenium.webdriver.common.by import By


log = Logger().get_logger()

class stripe_action():
    def stripe_data_enty(self, driver):
        time.sleep(10)
        sp=stripepopup(driver)
        if sp.check_heading():
            # try:
                time.sleep(10)
                frame_element = driver.find_element(By.XPATH,"//*[@id=\"email-form-2\"]/div[1]/div/iframe")
                log.warning(frame_element is not None)
                if frame_element:
                    driver.switch_to.frame(frame_element)
                else:
                    log.error("Frame element not found, cannot switch")
                sp.enter_card_number()
                sp.enter_expiry_date()
                sp.enter_cvv_number()
                sp.enter_zip_field()
                driver.switch_to.default_content()
                sp.click_confirm()
            # except Exception as e:
            #     log.info("Card frame not found please check")
            #     log.info(f"Execption Details: {e}")

