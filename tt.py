from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message

def run():
    # result = on_chat_start()
    log_message("M3 Script execution starts")
    on_message("Write a python code to move axis 6 to 10k901 with s profile type")
    log_message("M3 Script execution completed")

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()