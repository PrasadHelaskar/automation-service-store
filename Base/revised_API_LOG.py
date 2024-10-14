from selenium import webdriver
import logging
import json
import os
from dotenv import load_dotenv
from Base.logfile import Logger
import time

log = Logger().get_logger()

class APILOG:
    def __init__(self, driver):
        self.driver = driver
        load_dotenv()

        # Logger setup
        # log.setLevel(logging.INFO)
        # handler = logging.StreamHandler()
        # file_handler = logging.FileHandler('api_log.log')  # Log to a file
        # formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # handler.setFormatter(formatter)
        # file_handler.setFormatter(formatter)
        # log.addHandler(handler)
        # log.addHandler(file_handler)

        try:
            # Enable network tracking using Chrome DevTools Protocol (CDP)
            self.driver.execute_cdp_cmd('Network.enable', {})
            self.driver.get(os.getenv("url"))  # Navigate to the page

            # Sleep to allow network requests to happen
            time.sleep(5)  # Adjust the time according to the network activity
            self.fetch_logs()

        except Exception as e:
            log.exception("Error capturing network logs.", exc_info=e)

    def fetch_logs(self):
        try:
            logs = self.driver.get_log('performance')
            for entry in logs:
                log_entry = json.loads(entry['message'])
                message = log_entry['message']
                if 'response' in message['params']:
                    response = message['params']['response']
                
                        # Log details for any response
                    log.info(f"Response URL: {response['url']}")
                    log.info(f"Status Code: {response['status']}")
                    
                    # Handle different MIME types
                    mime_type = response['mimeType']
                    request_id = message['params']['requestId']
                    
                    response_body = self.driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': request_id})
                    
                    if mime_type == "application/json":
                        log.info(f"Response Body (JSON): {response_body.get('body', '')}")
                    # elif mime_type == "text/html":
                    #     log.info(f"Response Body (HTML): {response_body.get('body', '')}")
                    elif mime_type == "Script":
                        log.info(f"Response Body (Script): {response_body.get('body', '')}")
                    # else:
                    #     log.info(f"Response Body (Other - {mime_type}): {response_body.get('body', '')}")
                    elif message['params']['type'] == "Document":
                        log.info(f"Server-rendered page URL: {response['url']}")
                        
                    elif message['params']['type'] == "XHR":
                        log.info(f"XHR API URL: {response['url']}")
                else:
                    log.error(f"No 'response' found in {message['params']}")

        except Exception as e:
            log.exception("Error fetching logs.", exc_info=e)

