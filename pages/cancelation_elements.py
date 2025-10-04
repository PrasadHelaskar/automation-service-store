import time
from tests.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import * 
from selenium.webdriver.support.ui import Select
from base.logfile import Logger
from base.random_select import select_random


log=Logger().get_logger(__name__)

class cancelation_booking(BasePage):
    __private_profile=(By.XPATH, "(//div[@class='profile-wrapper'])[1]")
    __private_profilePage=(By.XPATH, "(//a[@class='profile-dropdown-list-holder'])[1]")
    __private_emptyState=(By.XPATH, "(//div[@class='sub-text fc2'])[2]")
    __private_subscriptionsPage=(By.XPATH, "(//a[@href='/profile/my-subscriptions?type=classpack'])[1]")

    def cancelationsButtonIndex(self,index) ->tuple:
        xpath=f"(//div[@class='trial-tag red strech relative'])[{index}]"
        __private_cancelationButton=(By.XPATH, xpath)
        
        return __private_cancelationButton

    def cancelationPolicySelection(self,index)->tuple:
        xpath=f"(//input[@type='radio'])[{index}]"
        __private_lastRedioButton=(By.XPATH, xpath)

        return __private_lastRedioButton
    
    __private_datepicker=(By.CSS_SELECTOR, "div[class='cancellation-option-details']")

    __private_confirem_cancelation=(By.XPATH, "//button[text()='Confirm']")

    __private_page_title=(By.CSS_SELECTOR,"h1[class='ss-heading semi-bold fc2 bottom-32']")
    
    # Action Methods 
    def click_profile(self):
        self.click(self.__private_profile)

    def click_profile_page(self):
        self.click(self.__private_profilePage)

    def clickSubscriptionsPage(self):
        self.click(self.__private_subscriptionsPage)

    def getTextForEmptySubscriptionPage(self)-> bool:
        try:
            text=self.get_text(self.__private_emptyState)
            requiredText="You don’t have any Subscriptions"
            
            if requiredText.lower() in text.lower():
                return True
        except TimeoutException:
            log.warning("Timeout Exception") 
            return False
    
    def clickCancelationButton(self,index):
        self.click(self.cancelationsButtonIndex(index))

    def clickCancelationPolicySelection(self,index):
        self.click(self.cancelationPolicySelection(index))
        # log.info("Index: %s",index)
        if index==3:
            self.datePickerActions()

    def datePickerActions(self):
        if self.is_visible(self.__private_datepicker):
            time.sleep(5)
            self.click(self.__private_datepicker)
            month_dropdown = self.driver.find_element(By.NAME, "months")
            select_month = Select(month_dropdown)
            select_month.select_by_visible_text("December")
            year_dropdown = self.driver.find_element(By.NAME, "years")
            select_year = Select(year_dropdown)
            select_year.select_by_visible_text(str(2025))
            self.driver.find_element(By.XPATH, "(//button[@name='day'])[20]").click()
            self.click(self.__private_datepicker)
            # date=self.get_attribute(self.__private_datepicker,"value")
            # log.info("Selected Date: %s",date)

    def confiremCancelation(self):
        self.click(self.__private_confirem_cancelation)

    def pageTitleAssertion(self)-> str:
        title=self.get_text(self.__private_page_title)

        return title