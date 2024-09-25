import time
from pages.login_page import LoginPage
import pytest

class Testlogin():

<<<<<<< HEAD
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username("")
    login_page.click_CONTINUE_BUTTON()
    login_page.enter_password("")
    login_page.click_submit()
    time.sleep(10)
    
=======
    def test_login(self, driver):
        login_page = LoginPage(driver)
        login_page.click_login()
        login_page.enter_username("your.email+fakedata11842@gmail.com")
        login_page.click_CONTINUE_BUTTON()
        login_page.enter_password("123123123")
        login_page.click_submit()
        time.sleep(10)
>>>>>>> a26c2a7 (basic classpack booking flow)
