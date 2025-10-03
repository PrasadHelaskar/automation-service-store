import time
from dotenv import load_dotenv
import pytest
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from threading import Thread
from base.Screenshot import screenshot
from base.logfile import Logger
from base.api_interception import *
from base.mitmproxy_addons import SaveXHRRequests

log=Logger().get_logger(__name__)

@pytest.fixture(autouse=True)
def log_on_failure(request,driver):
    
    """
    Logs detailed information and captures a screenshot when a test fails.

    Args:
        request (Fixture): The pytest request object, providing context for the test.

    This function is typically used as a pytest hook to capture logs and screenshots automatically
    whenever a test case fails, aiding in debugging and test analysis.
    """
    
    sco=screenshot(driver)
    yield
    item = request.node
    
    if item.rep_call.failed:
        sco.take_screenshot_fail(item.name)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):

    """
    Pytest hook to capture the result of each test execution and trigger log collection on failure.

    Args:
        item (TestCase): The test case item being executed.
        call (CallInfo): Object representing the test execution outcome.

    Returns:
        TestReport: A report object containing the test result.

    This function works in tandem with log_on_failure to ensure logs and screenshots are captured
    only when a test fails.
    """

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def driver():

    """
    Provides a Selenium WebDriver instance configured for test execution.

    Returns:
        WebDriver: A configured Selenium WebDriver instance.

    The driver is pre-configured to handle common settings for test automation and should be properly
    closed after use to prevent resource leaks.
    """

    load_dotenv()
    is_lambda_test = os.getenv("IS_REMOTE", "0") == "1"
    api_interception_enable=os.getenv("NETWORK_INTERCEPTION", "0") == "1"
    mitmporxy_enable=os.getenv("ENABLE_MITMPROXY","0")== "1"
    cert_path = "/home/prasad/.mitmproxy/mitmproxy-ca-cert.pem"
    
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
        
        driver = webdriver.Remote( # pylint: disable=redefined-outer-name
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
        chrome_options.add_argument("--force-device-scale-factor=0.8")
        # chrome_options.add_argument("--auto-open-devtools-for-tabs")
        # chrome_options.add_argument("--headless")

        if (mitmporxy_enable):
            log.info("MITMPROXY Enabled")
            chrome_options.add_argument("--proxy-server=http://localhost:8080")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument(f"--cert-authority={cert_path}") 
            SaveXHRRequests()
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_cdp_cmd('Network.enable', {})
        driver.execute_cdp_cmd("Debugger.setSkipAllPauses", {"skip": True})
        driver.execute_cdp_cmd("Page.setLifecycleEventsEnabled",{"enabled": True})
        driver.execute_cdp_cmd("Page.enable", {})
        driver.maximize_window()
        
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

    """
    Tracks the current URL and captures a screenshot of the page for test analysis.

    Args:
        driver (WebDriver): The Selenium WebDriver instance controlling the browser.
        request (Fixture): The pytest request object for context.

    This function is useful for debugging by providing a visual and contextual representation of the
    browser state when a test is executed.
    """

    if os.getenv("RUNNING_SCREENSHOTS", "0") == "1":    
        sco = screenshot(driver)  # Initialize the screenshot object
        previous_url = driver.current_url  # Track the initial URL

        def monitor_url_change():
    
            """
            Monitors URL changes in the active Selenium WebDriver session.

            Returns:
                bool: True if the URL changes successfully, False otherwise.

            This function is useful for tests that depend on URL transitions, allowing for robust verification
            of page navigations.
            """
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