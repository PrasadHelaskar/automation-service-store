from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from Base.logfile import Logger

log=Logger().get_logger()
class LoginPage(BasePage):
    __private_LOGIN=(By.XPATH,"(//button[@class=' secondary-button--fc4--bw1 w-button'])[1]")
    __private_CONTINUE_BUTTON=(By.CSS_SELECTOR,"button[type='submit']")
    __private_USERNAME_FIELD = (By.ID, "login-email")
    __private_PASSWORD_FIELD = (By.ID, "login-password")
    __private_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='ss-auth-primary-button--bc4--fc1 w-button']")
    __private_card_model=(By.ID, "radix-:r0:")
    __private_skip_button=(By.CSS_SELECTOR, "button[class='ss-auth-label--fc2 centre']")

    def enter_username(self, username):
        self.send_keys(self.__private_USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.__private_PASSWORD_FIELD, password)

    def click_submit(self):
        self.click(self.__private_LOGIN_BUTTON)

    def click_login(self):
        self.click(self.__private_LOGIN)

    def login_button_visible(self):
        try:
            op=self.is_visible(self.__private_LOGIN)
            return op
        except:
            log.info("User is already logged in")
            return False

    def click_CONTINUE_BUTTON(self):
        self.click(self.__private_CONTINUE_BUTTON)

    def is_visible_model(self):
        try:
            op=self.is_visible(self.__private_card_model)
            return op
        except:
            return False
    
    def click_skip(self):
        self.click(self.__private_skip_button)
    