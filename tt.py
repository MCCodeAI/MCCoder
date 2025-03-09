from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message

def run():
    # result = on_chat_start()
    log_message("M3 Script execution starts")
    on_message("Write a python code to move Axis 10 to the position 1110 at a speed of 1000 , acceleration of 10000,deceleration of 10000,jerkAccRatio of 0.5,jerkDecRatio of 0.5,starting Velocity of 0,and end Velocity of 0, using a JerkRatioFixedVelocityT profile.")
    log_message("M3 Script execution completed")

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")