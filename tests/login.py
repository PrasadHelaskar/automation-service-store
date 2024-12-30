import time
from Base.logfile import Logger
from Base.revised_API_LOG import APILOG
from pages.login_page import LoginPage
import pytest
from dotenv import load_dotenv
import os


log = Logger().get_logger()

static_cookie= None
cookies= None
class loginAction():
    @pytest.mark.order()
    def login_action(self,driver):
        load_dotenv()
        # apilog=APILOG(driver)
        driver.get(os.getenv("url"))
        login_page = LoginPage(driver)
        time.sleep(3)
        if login_page.login_button_visible():
            login_page.click_login()
            login_page.enter_username(os.getenv("email"))
            login_page.click_CONTINUE_BUTTON()
            login_page.enter_password(os.getenv("password"))
            login_page.click_submit()
            if login_page.is_visible_model():
                login_page.click_skip()
            self.Store_cookie(driver)

    def Store_cookie(self, driver):
        global static_cookie
        time.sleep(2)
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

    def check_cookies(self,driver):
        cookie_order_number = driver.get_cookie('order_number')
        cookie_invoice_number = driver.get_cookie('invoice_number')

        if cookie_order_number and cookie_invoice_number:
            log.info("cookie_order_number"+ cookie_order_number)
            log.info("cookie_invoice_number"+ cookie_invoice_number)
        else:
            log.warning("Cookie not found! \n cookie_order_number \n cookie_invoice_number")

    def get_all_cookies(self,driver):
        global cookies
        cookies=driver.get_cookies()

        for cookie in cookies:
            # log.info(str(cookie['name']) + ": " + str(cookie['value']))
            pass


    def set_all_cookies(self, driver):
        log.info(cookies)
        
        for cookie in cookies:
            # driver.add_cookie(cookie)
            # log.info("cookie added : "+str(cookie['name']))
            pass