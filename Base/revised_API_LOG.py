import json
import time
import os
from dotenv import load_dotenv
from base.logfile import Logger
from tests.base_page import BasePage

log = Logger().get_logger()

class APILOG:
    def __init__(self, driver):
        load_dotenv()
        self.driver = driver

        try:
            # Enable network tracking using Chrome DevTools Protocol (CDP)
            self.driver.execute_cdp_cmd('Network.enable', {})
            self.driver.get(os.getenv("URL"))  # Navigate to the page
            log.info("In API LOG Constructor try block and network enabled %s",str(os.getenv("URL")))
            # Sleep to allow network requests to happen
            time.sleep(5)  # Adjust the time according to the network activity
            self.fetch_logs(driver)

        except Exception as e:
            log.exception("Error capturing network logs.", exc_info=e)

    def fetch_logs(self,driver):
        try:
            logs = self.driver.get_log('performance')
            for entry in logs:
                log_entry = json.loads(entry['message'])
                message = log_entry['message']
        
                if 'response' in message['params']:
                    response = message['params']['response']
                    
                    # Handle different MIME types
                    request_url = response["request"]["url"] if ("url" in response["request"]) else None
                    
                    response_status= response['status']

                    if request_url:
                        log.info(f"request Url: {request_url}")
                        if response_status == 200:
                            log.info(f"✅Status Code: {response_status}")
                        elif response_status == 404:
                            log.warning(f"❌Status Code: {response_status}")
                        elif response_status == 500:
                            log.error(f"❌Status Code: {response_status}")
                        else:
                            log.info(f"☑️Status Code: {response_status}")
                    else:
                        # log.info("No valid URL found.")   
                        pass

                    request_id = message['params'].get('requestId')
                    mime_type = response['mimeType']
                    
                    if request_id and request_url:
                        try:
                            response_body = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                            if mime_type == "application/json":
                                log.info(f"Response Body (JSON): {response_body.get('body', '')}")
                            elif mime_type == "text/html":
                                log.info(f"Response Body (HTML): {response_body.get('body', '')}")
                            elif mime_type == "Script":
                                log.info(f"Response Body (Script): {response_body.get('body', '')}")
                            # elif message['params']['type'] == "Document":
                            #     log.info(f"Server-rendered page URL: {response['url']}")    
                            elif message['params']['type'] == "XHR":
                                log.info(f"XHR API URL: {response['url']}")
                            # else:
                            #     log.info(f"Response Body (Other - {mime_type}): {response_body.get('body', '')}" or None)
                        except Exception as e:
                            print(f"Error retrieving response body: {e}")
                    else:
                        print("No valid requestId found.")    
        except Exception as e:
            log.exception("Error fetching logs.", exc_info=e)

