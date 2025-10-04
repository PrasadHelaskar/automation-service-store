import time
import pytest
from base.logfile import Logger
from pages.cancelation_elements import cancelation_booking
from tests.login import loginAction
from base.random_select import select_random

log=Logger().get_logger(__name__)

class Test_service_cancelation():
    @pytest.mark.order(11)
    def test_cancelation(self, driver):
        loginAction().login_action(driver)
        cb=cancelation_booking(driver)
        random=select_random()
        cb.click_profile()
        cb.click_profile_page()
        cb.clickSubscriptionsPage()
        time.sleep(5)
        if not cb.getTextForEmptySubscriptionPage():
            script="return document.getElementsByClassName('trial-tag red strech relative').length"
            index_service=driver.execute_script(script)
            serviec_index_cancelations=random.random_number(index_service)
            log.info("Primary Service Index For Cancelations:%s",serviec_index_cancelations)
            cb.clickCancelationButton(serviec_index_cancelations)

            script="return document.querySelectorAll(\"input[type='radio']\").length"
            index=driver.execute_script(script)
            cancelation_index=random.random_number(index)
            log.info("Index For Cancelations Option:%s",cancelation_index)
            cb.clickCancelationPolicySelection(cancelation_index)

            cb.confiremCancelation()
            time.sleep(10)
            if cb.pageTitleAssertion().lower()=="Subscriptions".lower():
                log.info("Cancelation Completed")
            else:
                log.info("API took more time then expected")