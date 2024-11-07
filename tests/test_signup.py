import pytest
from Base.revised_API_LOG import APILOG
from pages.signup import signup
from dotenv import load_dotenv
import os
import time
import logging
from Base.random_select import select_random


logger = logging.getLogger(__name__)
@pytest.mark.parametrize('driver',['chrome'])
class Testsign_up():
    @pytest.mark.order(1)
    def test_sign_up(self, driver):
        load_dotenv()
        sr=select_random()
        apilogger = APILOG(driver)
        sg=signup(driver)
        sg.click_signup()
        sg.enter_email(os.getenv('email'))
        sg.click_continuebutton()
        sg.enter_firstname(sr.first_name())
        sg.enter_lastname(sr.last_name())
        sg.click_submit()
        sg.enetr_password(os.getenv('password'))
        sg.enetr_confirmpassword(os.getenv('password'))
        sg.click_submit()
        logger.info(str(sg.check_header))
        if (sg.check_header()):
            sg.click_dobfield()
            sg.click_date()
            sg.click_dobfield()
        sg.click_submit()
        time.sleep(60)