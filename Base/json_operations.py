import json
from base.logfile import Logger


log=Logger().get_logger()
__private_json_path="data.json"

def json_read(key):
    """For reading the json file"""
    with open (__private_json_path, 'r', encoding='utf-8') as json_file:
        data= json.load(json_file)
        # log.info("Request Data: \n"+str(data[key]))
        return data[key] 


def json_update(key,value):
    """For updaing the json file"""
    with open(__private_json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        data[key] = value

    with open(__private_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

        log.info("Updated data: %s",str(data[key]))


def json_read_array():
    """For reading the json array key"""
    with open(__private_json_path, 'r', encoding='utf-8') as json_file:
        data=json.load(json_file)
        cookies=data.get("COOKIES")
        return cookies