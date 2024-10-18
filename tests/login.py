import time
from pages.login_page import LoginPage
import pytest
from dotenv import load_dotenv
import os

class loginAction():
    @pytest.mark.order(1)
    def login_action(self,driver):
        load_dotenv()
        login_page = LoginPage(driver)
        login_page.click_login()
        login_page.enter_username(os.getenv("email"))
        login_page.click_CONTINUE_BUTTON()
        login_page.enter_password(os.getenv("password"))
        login_page.click_submit()
        time.sleep(10)