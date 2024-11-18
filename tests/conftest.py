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


# @pytest.fixture (scope="session")
# def driver():
#     global driver
#     logging_prefs = {
#         'browser': 'ALL',          # Log JavaScript errors/warnings
#         'performance': 'ALL'       # Log network requests (using CDP)
#     }
#     load_dotenv()
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = "/opt/google/chrome/google-chrome"
#     # chrome_options.add_experimental_option("w3c", False) 
#     # chrome_options.add_argument("--auto-open-devtools-for-tabs") 
#     # chrome_options.add_argument('--headless')
#     chrome_options.set_capability('goog:loggingPrefs', logging_prefs)
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.execute_cdp_cmd('Network.enable', {}) 
#     driver.execute_cdp_cmd("Debugger.setSkipAllPauses", {"skip": True})
#     # driver.get(os.getenv("url"))  
#     driver.maximize_window()
#     # driver.implicitly_wait(30)
#     yield driver
#     driver.get(os.getenv("logouturl"))
#     time.sleep(10)
#     driver.quit()

# # lambda test fixture 
@pytest.fixture(scope="session")
def driver():
    global driver
    username="developersgetomnify"
    access_key="iURTRLu6LkS0JYvWjvHvUd98204bgdCvasF6EQ3LOLInXtSqeN"
    remote_url="http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    
    chrome_options = Options()
    chrome_options.set_capability("browserName", "Chrome")
    chrome_options.set_capability("browserVersion", "latest")
    chrome_options.set_capability("LT:Options", {
        "video": True,
        "platformName": "Windows 10",
        "network": True,
        "build": "test",
        "project": "lambda integration",
        "name": "test",
        "selenium_version": "4.0.0",
        "w3c": True
    })

    driver=webdriver.Remote(
        command_executor=remote_url,
        options=chrome_options
    )

    yield driver
    driver.get(os.getenv("logouturl"))
    time.sleep(10)
    driver.quit()