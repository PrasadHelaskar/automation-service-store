from base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By


log = Logger().get_logger()

class productElements(BasePage):
    '''the ELemnets for the General item booking flow'''
    __private_product_page=(By.CSS_SELECTOR, "a[href='/products']")
    __private_general_item_checkbox=(By.XPATH, "(//input[@type='checkbox'])[1]")
    __private_Submit_button=(By.CSS_SELECTOR, "div[class='button--ph1--bc4--bw1--oc4--fc1 max-width w-button apply']")
    def service_number(self,i):
        __private_select_service=(By.XPATH , f"(//a[@class='primary-button-card bc4 fc1'])[{i}]")
        return __private_select_service
    
    def pricing_option(self,i):
        '''Selection of the pricing option'''
        __private_pricing_option=(By.XPATH ,f"(//button[@class='add-section fc4 oc4 justify-centre'])[{i}]")
        return __private_pricing_option

    
    __private_proceed_button_checkout=(By.CSS_SELECTOR, "button[class='discount-button fc1 bc4 w-button step1']")
    __private_review_checkbox=(By.NAME, "checkbox-3")
    __private_Review_Proceed_cardno=(By.CSS_SELECTOR,"div[class='stripeModal']")
    __private_Review_Proceed_card=(By.CSS_SELECTOR,"div[class='discount-button fc1 bc4 w-button one']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER")
    
    def plus_button(self):
        i=1
        xpath=f"(//div[@class='fc4 display-flex margin-top-0 w-embed'])[{i}]"
        __plus_button=(By.XPATH,xpath)
        return __plus_button

    def click_product_page(self):
        self.click(self.__private_product_page)

    def click_GI_filter(self):
        self.click(self.__private_general_item_checkbox)

    def click_submit(self):
        self.click(self.__private_Submit_button)

    def click_service(self,i):
        self.click(self.service_number(i))

    def click_pricing_option(self):
        self.click(self.pricing_option(1))

    def click_checkout_proceed(self):
        self.click(self.__private_proceed_button_checkout)

    def click_waiver_checkbox(self):
        self.click(self.__private_review_checkbox)

    def click_review_proceed(self):
        try:    
            value=self.is_visible(self.__private_Review_Proceed_cardno)
        except:
            value=False
        log.info(value)
        locator=(self.__private_Review_Proceed_cardno) if value else (self.__private_Review_Proceed_card)
        self.click(locator)

    def click_home(self):
        self.click(self.__private_HOME_BUTTON)

    def click_plus_button(self):
        self.click(self.plus_button())