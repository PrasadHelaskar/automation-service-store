import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver
import os

@pytest.fixture (scope="session")
def driver():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("url"))  
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.get(os.getenv("logouturl"))
    time.sleep(10)
    driver.quit()