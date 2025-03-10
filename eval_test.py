from app_NaiveRAG_M1_eval import *
# from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message
from time import *

def run():
 
    log_message("M3 Script execution starts")

    re = on_message(160, "Write Python code to move Axis 15 to the position -410 at a speed of 1000, starting Velocity of 0, and end Velocity of 0, using a para-curve profile.")

    log_message("M3 Script execution completed")
    

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")