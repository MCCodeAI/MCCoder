from app_NaiveRAG_M1_eval import *
from userlib.user_logger import log_message

def run():
    result = on_chat_start()
    on_message("Write a python code to move axis 0 to 444")
    log_message("Script execution completed")

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()