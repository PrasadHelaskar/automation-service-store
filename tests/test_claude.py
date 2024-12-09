from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

class LoginAutomation:
    def __init__(self, url, username, password):
        """
        Initialize the login automation
        
        :param url: Login page URL
        :param username: User's username
        :param password: User's password
        """
        # Setup Chrome WebDriver (ensure you have chromedriver installed)
        self.driver = webdriver.Chrome()
        self.url = url
        self.username = username
        self.password = password
        
    def navigate_to_login_page(self):
        """
        Navigate to the login page
        """
        try:
            self.driver.get(self.url)
            print("Successfully navigated to login page")
        except Exception as e:
            print(f"Error navigating to login page: {e}")
            return False
        return True
    
    def login(self):
        """
        Perform login operation
        
        :return: True if login successful, False otherwise
        """
        try:
            # Wait for username field (adjust selector as needed)
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.send_keys(self.username)
            
            # Wait for password field (adjust selector as needed)
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys(self.password)
            
            # Wait for login button (adjust selector as needed)
            login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
            login_button.click()
            
            # Wait for login confirmation (adjust based on expected post-login element)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "dashboard"))
            )
            
            print("Login successful!")
            return True
        
        except TimeoutException:
            print("Timeout: Could not find login elements")
            return False
        
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            return False
        
        except Exception as e:
            print(f"Unexpected login error: {e}")
            return False
    
    def validate_login(self):
        """
        Validate login by checking for key post-login elements
        
        :return: True if login validation successful, False otherwise
        """
        try:
            # Add specific validation checks for your application
            # Examples:
            # - Check for dashboard element
            # - Verify welcome message
            # - Check URL changed
            current_url = self.driver.current_url
            if "dashboard" in current_url.lower():
                print("Login validation successful")
                return True
            else:
                print("Login validation failed")
                return False
        
        except Exception as e:
            print(f"Login validation error: {e}")
            return False
    
    def take_screenshot(self, filename="login_screenshot.png"):
        """
        Take a screenshot for debugging
        
        :param filename: Name of screenshot file
        """
        try:
            self.driver.save_screenshot(filename)
            print(f"Screenshot saved: {filename}")
        except Exception as e:
            print(f"Error taking screenshot: {e}")
    
    def run_login_test(self):
        """
        Complete login test workflow
        """
        try:
            # Navigate to login page
            if not self.navigate_to_login_page():
                return False
            
            # Perform login
            login_result = self.login()
            
            # Validate login
            validation_result = self.validate_login() if login_result else False
            
            return validation_result
        
        except Exception as e:
            print(f"Unexpected error in login test: {e}")
            return False
        
        finally:
            # Always close the browser
            self.driver.quit()
    
    @staticmethod
    def run_test_suite():
        """
        Run multiple login test scenarios
        """
        # Test valid login
        valid_login = LoginAutomation(
            url="https://urbantribetest.omnifyapp.com/login",
            username="your_valid_username",
            password="your_valid_password"
        )
        print("Valid Login Test:")
        valid_result = valid_login.run_login_test()
        
        # Test invalid login (optional)
        invalid_login = LoginAutomation(
            url="https://urbantribetest.omnifyapp.com/login",
            username="invalid_username",
            password="wrong_password"
        )
        print("\nInvalid Login Test:")
        invalid_result = invalid_login.run_login_test()

# Run the test suite
if __name__ == "__main__":
    LoginAutomation.run_test_suite()