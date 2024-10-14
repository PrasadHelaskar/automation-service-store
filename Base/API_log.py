# import logging
# import json
# import os
# from dotenv import load_dotenv
# from selenium.webdriver.chrome.options import Options
# from Base.logfile import MyLogger


# MyLogger.setup()    
# logger = MyLogger.get_logger()

# class APILOG1:
#     def __init__(self, driver):
#         self.driver = driver
#         load_dotenv()
#         driver.get(os.getenv("url"))  
#         # try:
#         #     self.devtools = self.driver.devtools
#         # except AttributeError as e:
#         #     print(f"Error: {e}. Is the driver a WebDriver instance?")
#         logger.setLevel(logging.INFO)
#         handler = logging.StreamHandler()
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)

#         # chrome_options = Options() 
#         # chrome_options.add_experimental_option("w3c", False)
#         # driver = webdriver.Chrome(service=service, options=chrome_options)

#         try:
#             try:
#             # Enable network tracking using Chrome DevTools Protocol (CDP)
#                  self.driver.execute_cdp_cmd('Network.enable', {})
#             except Exception as e:
#                 logging.error(f"An error occurred during network logging: {e}")
#             def capture_response(event):
#                 response = event['response']
#                 resource_type = event['type']

#                 if resource_type == "XHR":
#                     request_id = event['requestId']
#                     url = response['url']
#                     status = response['status']
#                     response_body = self.driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})

#                     logger.info(f"XHR Request URL: {url}")
#                     logger.info(f"XHR Response Status: {status}")
#                     # Fetch the response body if needed
#                     if "body" in response_body:
#                         logger.info(f"XHR Response Body: {response_body['body']}")
#                     else:
#                         logger.warning("Response body is empty or not available.")
                
#                 elif response['mimeType'] == "application/json":
#                     logger.info(f"JSON URL: {response['url']}")
#                     logger.info(f"JSON Status Code: {response['status']}")

#                     try:
#                         response_body = driver.execute_cdp_cmd("Network.getResponseBody", {"requestId": event['requestId']})
#                         if "body" in response_body:
#                             body = response_body['body']
#                             logger.info(f"JSON Response Body: {body}")
#                         else:
#                             logger.warning("Response body is empty or not available.")
#                     except Exception as e:
#                         logger.warning("Error retrieving response body")
#                         logger.exception(e)
#                 else:
#                     logger.info("fishy Nothibg found !!!!")
#                 self.driver.execute_cdp_cmd.add_listener("Network.responseReceived", capture_response)
        

#         except Exception as e:
#             logger.exception("An error occurred during network logging.", exc_info=e)
