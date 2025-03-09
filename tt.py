from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message

def run():
    # result = on_chat_start()
    log_message("M3 Script execution starts")
    on_message("Write a python code to move Axis 0 to the position 102")
    log_message("M3 Script execution completed")

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")