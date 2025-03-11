# from app_NaiveRAG_M1_eval import *
from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message
from time import *

def run():
 
    log_message("M3 Script execution starts")

    tp="""

Write Python code to execute an absolute triggered position command. Start an absolute position command for Axis 10 to move to position -1000 with a velocity of 600, when the remaining distance is 500, trigger Axis 10 to move to -300 with a velocity of 1000; Then set an event that triggers to start the movement of Axis 2 to -200 when Axis 10 moves to the position of 100;

"""

    re = on_message(143, tp) 

    log_message("M3 Script execution completed")
    

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")