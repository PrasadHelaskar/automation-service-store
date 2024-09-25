import pytest
from selenium import webdriver


@pytest.fixture (scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://sony.omnifyapp.com/")  
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()