import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://sony.omnifyapp.com/")  
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.click_login()
    login_page.enter_username("prasad@getomnify.com")
    login_page.click_CONTINUE_BUTTON()
    login_page.enter_password("123123123")
    login_page.click_submit()
    time.sleep(10)
    
