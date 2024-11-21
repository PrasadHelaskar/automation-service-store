import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from Base.Screenshot import screenshot   

@pytest.fixture(autouse=True)
def log_on_failure(request):
    sco=screenshot(driver)
    yield
    item = request.node
    if item.rep_call.failed:
        sco.take_screenshot(item.name)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

@pytest.fixture(scope="session")
def driver():
    global driver
    load_dotenv()
    is_lambda_test = os.getenv("IS_REMOTE", "0") == "1"
    
    if is_lambda_test:
        # LambdaTest setup
        username = os.getenv("username")
        access_key = os.getenv("access_key")
        remote_url = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"
        
        chrome_options = Options()
        chrome_options.set_capability("browserName", "Safari")
        chrome_options.set_capability("browserVersion", "18")
        chrome_options.set_capability("LT:Options", {
            "video": True,
            "platformName": "MacOS Sequoia",
            "resolution": "1024x768",
            "project": "DEMO",
            "tunnel": True,
            "w3c": True,
            "plugin": "python-pytest"
        })
        
        driver = webdriver.Remote(
            command_executor=remote_url,
            options=chrome_options
        )
    else:
        # Local setup
        logging_prefs = {
            'browser': 'ALL',          # Log JavaScript errors/warnings
            'performance': 'ALL'       # Log network requests (using CDP)
        }
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/opt/google/chrome/google-chrome"
        chrome_options.set_capability('goog:loggingPrefs', logging_prefs)
        # chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd('Network.enable', {})
        driver.execute_cdp_cmd("Debugger.setSkipAllPauses", {"skip": True})
        driver.maximize_window()
    
    yield driver
    
    # Common teardown for both setups
    driver.get(os.getenv("logouturl"))
    time.sleep(10)
    driver.quit()
