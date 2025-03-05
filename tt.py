from app_LongContext_M2_eval import *
from userlib.user_logger import log_message

def run():
    # result = on_chat_start()
    log_message("M2 Script execution starts")
    on_message("Write a python code to move axis 6 to 4444")
    log_message("M2 Script execution completed")

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()