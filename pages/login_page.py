from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    LOGIN=(By.XPATH,"(//button[@class='secondary-button--fc4--bw1 w-button'])[1]")
    CONTINUE_BUTTON=(By.CSS_SELECTOR,"button[type='submit']")
    USERNAME_FIELD = (By.ID, "login-email")
    PASSWORD_FIELD = (By.ID, "login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[class='ss-auth-primary-button--bc4--fc1 w-button']")

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_submit(self):
        self.click(self.LOGIN_BUTTON)

    def click_login(self):
        self.click(self.LOGIN)

    def click_CONTINUE_BUTTON(self):
        self.click(self.CONTINUE_BUTTON)
