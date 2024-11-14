import time
from Base.logfile import Logger
from Base.revised_API_LOG import APILOG
from pages.login_page import LoginPage
import pytest
from dotenv import load_dotenv
import os


log = Logger().get_logger()

static_cookie= None
class loginAction():
    @pytest.mark.order(1)
    def login_action(self,driver):
        load_dotenv()
        # apilog=APILOG(driver)
        driver.get(os.getenv("url"))
        login_page = LoginPage(driver)
        login_page.click_login()
        login_page.enter_username(os.getenv("email"))
        login_page.click_CONTINUE_BUTTON()
        login_page.enter_password(os.getenv("password"))
        login_page.click_submit()
        time.sleep(10)
        self.Store_cookie(driver)

    def Store_cookie(self, driver):
        global static_cookie
        time.sleep(10)
        cookie = driver.get_cookie('omnify-token')
        # log.info(cookie)
        if cookie:
            static_cookie = cookie['value']
            static_cookie_name = cookie['name']
            log.info(f"Stored cookie name: {static_cookie_name}")
        else:
            log.warning("Cookie not found!")

    def authenticatte_cookie(self, driver):
        cookie = driver.get_cookie('omnify-token')
        if cookie:
            cookie = cookie['value']
            if(cookie['value']==static_cookie['value']):
                log.log("Cookie authenticated")        
        else:
            log.warning("Cookie not found! \n authenticated failed")
