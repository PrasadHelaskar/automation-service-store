from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    __private_LOGIN=(By.XPATH,"(//button[@class='secondary-button--fc4--bw1 w-button'])[1]")
    __private_CONTINUE_BUTTON=(By.CSS_SELECTOR,"button[type='submit']")
    __private_USERNAME_FIELD = (By.ID, "login-email")
    __private_PASSWORD_FIELD = (By.ID, "login-password")
    __private_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='ss-auth-primary-button--bc4--fc1 w-button']")

    def enter_username(self, username):
        self.send_keys(self.__private_USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.__private_PASSWORD_FIELD, password)

    def click_submit(self):
        self.click(self.__private_LOGIN_BUTTON)

    def click_login(self):
        self.click(self.__private_LOGIN)

    def click_CONTINUE_BUTTON(self):
        self.click(self.__private_CONTINUE_BUTTON)
