import sys
import pprint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.logfile import Logger

log = Logger().get_logger()
class BasePage:
    def __init__(self, driver):
        """
        Initializes the base page object with a WebDriver instance and sets a default wait time.

        Parameters:
            driver (WebDriver): Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def find_element_wait(self, locator):
        """
        Waits until the element located by the given locator is visible and returns it.

        Parameters:
            locator (tuple): Locator strategy and locator value, e.g., (By.ID, "element_id").

        Returns:
            WebElement: The visible web element found.
        """
        op = self.wait.until(EC.visibility_of_element_located(locator))
        return op

    def click(self, locator):
        """
        Waits for visibility of the element and clicks on it.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        element = self.find_element_wait(locator)
        element.click()

    def send_keys(self, locator, text):
        """
        Waits for the element, clears it, and sends the specified text.

        Parameters:
            locator (tuple): Locator strategy and locator value.
            text (str): Text to input into the element.
        """
        element = self.find_element_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Retrieves the visible text of the located element.

        Parameters:
            locator (tuple): Locator strategy and locator value.

        Returns:
            str: Text content of the element.
        """
        element = self.find_element_wait(locator)
        element_text = element.text
        return element_text

    def is_visible(self, locator):
        """
        Checks whether the element located by the given locator is visible.

        Parameters:
            locator (tuple): Locator strategy and locator value.

        Returns:
            str or bool: "True"/"False" string if found, otherwise False if an exception occurs.
        """
        try:
            element = self.find_element_wait(locator)
            op = element.is_displayed()
            return str(op)
        except Exception:
            return False

    def clear_element(self, locator):
        """
        Waits for the element and clears its content.

        Parameters:
            locator (tuple): Locator strategy and locator value.
        """
        element = self.find_element_wait(locator)
        element.clear()


    def DD(self, data):
        """
        Debug utility method to pretty-print the provided data and exit the program.

        Parameters:
            data (Any): The data structure to be pretty-printed (e.g., dict, list).

        This method is typically used during development or debugging to inspect
        the structure and content of complex data by halting further execution.
        """
        pprint.pprint(data)
        sys.exit()

    def get_url(self):
        """
        Retrieves the current URL of the active browser window.

        Returns:
            str: The current URL loaded in the browser.
        """
        url = self.driver.current_url
        return url