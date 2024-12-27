from dotenv import load_dotenv,set_key
from Base.logfile import Logger

load_dotenv()
log=Logger().get_logger()

def update_env(key,value):
    set_key(".env",key,value)
    log.info(f"Updated {key}")