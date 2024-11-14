import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver 
from os import environ
from Base.Screenshot import screenshot



@pytest.fixture(autouse=True)
def log_on_failure(request):
    sco=screenshot(driver)
    yield
    item = request.node
    if item.rep_call.failed:
        sco.take_screenshot(driver, item.name)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture (scope="session")
def driver(request):
    global driver 
    logging_prefs = {
        'browser': 'ALL',          # Log JavaScript errors/warnings
        'performance': 'ALL'       # Log network requests (using CDP)
    }
    browser = request.param
    desired_caps = {
        "single_test": 
        {
            "browserName": browser,
            "browserVersion": "130",
            "LT:Options": {
                "username": "developersgetomnify",
                "accessKey": "iURTRLu6LkS0JYvWjvHvUd98204bgdCvasF6EQ3LOLInXtSqeN",
                "video": True,
                "platformName": "Windows 10",
                "network": True,
                "build": "test",
                "project": "integration-lambda",
                "w3c": True,
                "plugin": "python-pytest"
            }
        }
    }
    desired_caps.update()
    test_name = request.param["platform"] + "_" + request.param["browserName"] + "_" + request.param["version"]
    build = environ.get('BUILD', "Sample PY Build Chrome")

    tunnel_id = environ.get('TUNNEL', False)
    username = environ.get('LT_USERNAME', None)
    access_key = environ.get('LT_ACCESS_KEY', None)

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/opt/google/chrome/google-chrome"
<<<<<<< Updated upstream
    option = {
        "platform": "Windows 10",
        "version": "latest",
        "name": test_name,
        "Build": build,
        "video": True,
        "visual": True,
        "network": True,
        "console": True
    }
    chrome_options.set_capability("LT:Options", option)
    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=chrome_options
    )
    load_dotenv()
=======
>>>>>>> Stashed changes
    # chrome_options.add_experimental_option("w3c", False) 
    # chrome_options.add_argument("--auto-open-devtools-for-tabs") 
    # chrome_options.add_argument('--headless')
    chrome_options.set_capability('goog:loggingPrefs', logging_prefs)
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd('Network.enable', {}) 
    driver.execute_cdp_cmd("Debugger.setSkipAllPauses", {"skip": True})
    # driver.get(os.getenv("url"))  
    driver.maximize_window()
    # driver.implicitly_wait(30)
    yield driver
    driver.get(os.getenv("logouturl"))
    time.sleep(10)
    driver.quit()

# @pytest.fixture(scope="session")
# def driver():
#     global driver
#     username="developersgetomnify"
#     access_key="iURTRLu6LkS0JYvWjvHvUd98204bgdCvasF6EQ3LOLInXtSqeN"
#     remote_url="http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    
#     chrome_options = Options()
#     chrome_options.set_capability("browserName", "Chrome")
#     chrome_options.set_capability("browserVersion", "latest")
#     chrome_options.set_capability("LT:Options", {
#         "video": True,
#         "platformName": "Windows 10",
#         "network": True,
#         "build": "test",
#         "project": "lambda integration",
#         "name": "test",
#         "selenium_version": "4.0.0",
#         "w3c": True
#     })

#     driver=webdriver.Remote(
#         command_executor=remote_url,
#         options=chrome_options
#     )

#     yield driver
#     driver.get(os.getenv("logouturl"))
#     time.sleep(10)
#     driver.quit()