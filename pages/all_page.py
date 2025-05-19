import json
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from base.logfile import Logger

log=Logger().get_logger()

class page_check(BasePage):
    __private__home=(By.CSS_SELECTOR,'a[href="/home"]')
    __private__subscriptions=(By.CSS_SELECTOR,'a[href="/subscriptions"]')
    __private__programs=(By.CSS_SELECTOR,'a[href="/programs"]')
    __private__classpacks=(By.CSS_SELECTOR,'a[href="/classpacks"]')
    __private__schedules=(By.CSS_SELECTOR,'a[href^="/schedules/"]')
    __private__products=(By.CSS_SELECTOR,'a[href="/products"]')
    __private__party=(By.CSS_SELECTOR,'a[href="/party"]')
    __private__camps=(By.CSS_SELECTOR,'a[href="/camps"]')
    __private__giftcards=(By.CSS_SELECTOR,'a[href="/gift-cards"]')


    def click_home(self):
        self.click(self.__private__home)

    def click_subscription(self):
        self.click(self.__private__subscriptions)

    def click_program(self):
        self.click(self.__private__programs)
    
    def click_classpacks(self):
        self.click(self.__private__classpacks)

    def click_schedules(self):
        self.click(self.__private__schedules)

    def click_products(self):
        self.click(self.__private__products)
 
    def click_party(self):
        self.click(self.__private__party)

    def click_camps(self):
        self.click(self.__private__camps)
    
    def click_giftcards(self):
        self.click(self.__private__giftcards)

    def get_attribute(self):
        
        element=self.driver.find_element(By.XPATH,"//script[@id='seo-nap-details']")
        json_data=element.get_attribute("innerHTML")
        formated_json=json.dumps(json.loads(json_data), indent=2)
        log.info("NAP schema json text: \n%s\n",formated_json)