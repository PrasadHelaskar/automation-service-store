import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from threading import Thread
from base.Screenshot import screenshot
from base.logfile import Logger
from base.api_interception import *

log=Logger().get_logger()

@pytest.fixture(autouse=True)
def log_on_failure(request):
    sco=screenshot(driver)
    yield
    item = request.node
    
    if item.rep_call.failed:
        sco.take_screenshot_fail(item.name)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="session")
def driver():
    global driver
    load_dotenv()
    is_lambda_test = os.getenv("IS_REMOTE", "0") == "1"
    api_interception_enable=os.getenv("NETWORK_INTERCEPTION", "0") == "1"
    
    if is_lambda_test:
        # LambdaTest setup
        username = os.getenv("USERNAME")
        access_key = os.getenv("ACCESS_KEY")
        remote_url = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"
        
        chrome_options = Options()
        chrome_options.set_capability("browserName", "Safari")
        chrome_options.set_capability("browserVersion", "18")
        chrome_options.set_capability("LT:Options", {
            "video": True,
            "platformName": "MacOS Sequoia",
            "resolution": "1024x768",
            "build": "Service_store",
            "project": "DEMO",
            "console": "error",
            "network": True,
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
            'browser': 'ALL',
            'performance': 'ALL'       
        }
        
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.binary_location = "/mnt/k/automation/Automation_scripts/chrome-linux64/chrome"
        chrome_options.binary_location = "/usr/bin/google-chrome"
        chrome_options.set_capability('goog:loggingPrefs', logging_prefs)
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # chrome_options.add_argument("--auto-open-devtools-for-tabs")
        # chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd('Network.enable', {})
        driver.execute_cdp_cmd("Debugger.setSkipAllPauses", {"skip": True})
        driver.execute_cdp_cmd("Page.setLifecycleEventsEnabled",{"enabled": True})
        driver.execute_cdp_cmd("Page.enable", {})
        driver.maximize_window()


        driver.implicitly_wait(30)
        
        if (api_interception_enable):
            log.info("API Interception Enabled")
            driver.execute_cdp_cmd("Fetch.enable", {
                "patterns": [{"urlPattern": "*", "resourceType": "XHR", "requestStage": "Request"}]
            })         
            
            intercepter().intreception_handler(driver)

    yield driver
    
    # Common teardown for both setups
    driver.get(os.getenv("LOGOUTURL"))
    time.sleep(5)
    driver.quit()


@pytest.fixture(autouse=True, scope="function")
def track_url_and_screenshot(driver, request):
    if os.getenv("RUNNING_SCREENSHOTS", "0") == "1":    
        sco = screenshot(driver)  # Initialize the screenshot object
        previous_url = driver.current_url  # Track the initial URL

        def monitor_url_change():
            nonlocal previous_url
            while True:
                current_url = driver.current_url

                if current_url != previous_url:
                    time.sleep(2)
                    sco.take_screenshot(request) 
                    previous_url = current_url
                    log.info(f"URL changed Captured screenshot for {current_url}")
                time.sleep(0.5)  # Poll every 0.5 seconds (adjust as needed)

        monitor_thread = Thread(target=monitor_url_change, daemon=True)
        monitor_thread.start()
        yield
        monitor_thread.join(timeout=1)
    else:
        yield