from Base.logfile import Logger
from tests.base_page import BasePage
from selenium.webdriver.common.by import By

log = Logger().get_logger()

class giftcardbooking(BasePage):
    __private__gift_card_page=(By.CSS_SELECTOR, "a[href='/gift-cards?b=t']")
    giftcadt_number=2
    __private__select_gift_card=(By.XPATH , f"(//a[@class='primary-button-card bc4 fc1'])[{giftcadt_number}]")
    def amount_select(self, count):
            log.info("amount select option: "+str(count))
            selector=f"(//div[@class='schedule-top-bar-date-selector--bc3--bw1--fc2 slot pading-18 semi-bold '])[{count}]"
            __private__select_amount_custom=(By.XPATH, selector)
            return __private__select_amount_custom
    
    __private_enter_amount=(By.ID, "customAmount")
    __private_enter_recipient_name=(By.CSS_SELECTOR, "input[placeholder='Enter recipient’s name']")
    __private_enter_recipient_email=(By.CSS_SELECTOR, "input[placeholder='Enter recipient’s email']")
    __private_giftcard_checkout=(By.CSS_SELECTOR, "button[class='discount-button fc1 bc4 w-button step1']")
    __private_review_checkbox=(By.NAME, "checkbox-3")
    __private_Review_Proceed_cardno=(By.CSS_SELECTOR,"div[class='stripeModal']")
    __private_Review_Proceed_card=(By.CSS_SELECTOR,"div[class='discount-button fc1 bc4 w-button one']")
    __private_HOME_BUTTON= (By.LINK_TEXT, "BOOK ANOTHER") 

    def click_gift_card_page(self):
        self.click(self.__private__gift_card_page)
    
    def click_select_gift_card(self):
        self.click(self.__private__select_gift_card)

    def click_select_amount_type(self, count):
        self.click(self.amount_select(count))

    def enter_amount(self, amount):
        self.send_keys(self.__private_enter_amount, amount)

    def enter_name(self, name):
        self.send_keys(self.__private_enter_recipient_name, name)

    def enter_email(self, email):
        self.send_keys(self.__private_enter_recipient_email, email)

    def click_checkout_proceed(self):
        self.click(self.__private_giftcard_checkout)

    def click_waiverbox(self):
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

    