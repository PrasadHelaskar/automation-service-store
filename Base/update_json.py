from Base.logfile import Logger
import json


log=Logger().get_logger()
__private_json_path="data.json" 

def json_read(key):
    with open (__private_json_path, 'r') as json_file:
        data= json.load(json_file)
        log.info("Request Data: \n"+str(data[key]))
        return data[key] 


def json_update(key,value):

    with open(__private_json_path, 'r') as json_file:
        data = json.load(json_file)

        data[key] = value

    with open(__private_json_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

        log.info("Updateed data: \n"+str(data))

