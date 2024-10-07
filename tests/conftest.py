import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver
import os
from Base.Screenshot import setUp,take_screenshot


@pytest.fixture(autouse=True)
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        item.instance.setUp()
        item.instance.take_screenshot()
        # if hasattr(item.instance, "take_screenshot"):
        #     item.instance.take_screenshot()
        # else:
        #     print("The class does not have a take_screenshot method")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture (scope="session")
def driver():
    load_dotenv()
    global driver 
    options = webdriver.ChromeOptions()
    options.add_argument("--auto-open-devtools-for-tabs") 
    driver = webdriver.Chrome(options=options)
# Access DevTools through the execute_cdp_cmd method
# Enable network tracking to monitor network activity
    driver.execute_cdp_cmd('Network.enable', {}) 
    # driver.get(os.getenv("url"))  
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.get(os.getenv("logouturl"))
    time.sleep(10)
    driver.quit()