import json
from base.logfile import *

log=Logger().get_logger()

class intercepter():
    api_interception_enable=os.getenv("NETWORK_INTERCEPTION", "0") == "1"
    # driver=webdriver.Chrome()
    def intreception_handler(self,driver):
         
         while True:
                log.info("Intreception Handler")
                events=driver.execute_cdp_cmd("Fetch.requestPaused", {})
                for event in events:
                    self.update_intercepted_request(event,driver)

    def update_intercepted_request(self,event,driver):

        request_url=event['request']['url']
        log.info("Requst URL: "+str())

        if "Nonsession.json" in request_url:
            payload=json.load(event['request']['postData'])
            log.info("Recived Payload: \n"+str(payload))

            # updating the payload

            payload[""]= "" # "key"="value"
            log.info("Update Payload: \n"+str(payload))

            # updating the headers

            header=event["request"]["headers"]
            header["Interception_purpose"]="Testing"

            driver.execute_cdp_cmd("Fetch.continueRequest",{
                                                                "requestId": event['requestId'],
                                                                "headers": event["request"]["headers"],
                                                                "postdata": payload
                                                            })
        else:
            driver.execute_cdp_cmd("Fetch.continueRequest",{
                                                                "requestId": event['requestId']
                                                            })

