import time
import os
import pytest
from dotenv import load_dotenv
from base.logfile import Logger
from base.revised_API_LOG import APILOG
from base.json_operations import json_read_array
from pages.login_page_elements import LoginPage


log = Logger().get_logger(__name__)

static_cookie= None
class loginAction():
    @pytest.mark.order()
    def login_action(self,driver):
        load_dotenv()
        # apilog=APILOG(driver)
        driver.get(os.getenv("URL"))
        login_page = LoginPage(driver)
        sttime=time.time()
        login_page.page_wait()
        if login_page.login_button_visible():
            login_page.click_login()
            login_page.enter_username(os.getenv("EMAIL"))
            login_page.click_CONTINUE_BUTTON()
            login_page.enter_password(os.getenv("PASSWORD"))
            login_page.click_submit()
            if login_page.is_visible_model():
                login_page.click_skip()
            self.Store_cookie(driver)
        entime=time.time()
        log.info("Required time: %s",(entime-sttime))

    def Store_cookie(self, driver):
        global static_cookie
        cookie = driver.get_cookie('omnify-token')
        # log.info(cookie)

        if cookie:
            static_cookie = cookie['value']
            static_cookie_name = cookie['name']
            log.info(f"Stored cookie name: {static_cookie_name}")
        else:
            log.warning("Cookie not found!")

    def authenticate_cookie(self, driver):
        cookie = driver.get_cookie('omnify-token')

        if cookie:
            cookie_value = cookie['value']
            if(cookie_value==static_cookie):
                log.info("Cookie authenticated")        
        else:
            log.warning("Cookie not found! \n authenticated failed")

    def order_invoice_cookies(self,driver):
        cookies=json_read_array()

        for cookie_name in cookies:
            cookie=driver.get_cookie(cookie_name)
            if cookie:
                log.info(f"{cookie_name}: %s",str(cookie['value']))
            else:
                log.error("Cookie not found!: %s",cookie_name)

    def get_all_cookies(self,driver):
        cookies=driver.get_cookies()

        for cookie in cookies:
            log.info(str(cookie['name']) , ": " , str(cookie['value']))
        