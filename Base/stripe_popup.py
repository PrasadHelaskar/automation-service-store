import time
from Base.logfile import Logger
from pages.stripe_popup_ele import stripepopup
from selenium.webdriver.common.by import By


log = Logger().get_logger()

class stripe_action():
    def stripe_data_enty(self, driver):
        time.sleep(5)
        sp=stripepopup(driver)
        # log.warning("check_heading return :"+str(sp.check_heading()))
        if sp.check_heading():
            # try:
                time.sleep(10)
                try:    
                    value=driver.find_element(By.XPATH,"//*[@id=\"email-form-2\"]/div[1]/div/iframe").is_displayed()
                except:
                    value=False
                locator=(driver.find_element(By.XPATH,"//*[@id=\"email-form-2\"]/div[1]/div/iframe")) if value else (driver.find_element(By.XPATH,"//iframe[@title='Secure card payment input frame']"))
                log.info("Is locator valid: "+str(locator is not None))
                if locator:
                    driver.switch_to.frame(locator)
                    log.info("Switched")
                else:
                    log.error("Frame element not found, cannot switch")
                sp.enter_card_number()
                sp.enter_expiry_date()
                sp.enter_cvv_number()
                sp.enter_zip_field()
                driver.switch_to.default_content()
                log.info("Switched")
                sp.click_confirm()
            # except Exception as e:
            #     log.info("Card frame not found please check")
            #     log.info(f"Execption Details: {e}")

