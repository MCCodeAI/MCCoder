# from app_NaiveRAG_M1_eval import *
from app_MCCoder_M3_eval import *
from userlib.user_logger import log_message
from time import *

def run():
 
    log_message("M3 Script execution starts")

    tp="""
Write Python code to set the input event to monitor if the DistanceToTarget of Axis 3's movement is 500，then move Axis 1 to the position -200 at a speed of 1000. Move Axis 3 to 1200; 


"""

    re = on_message(140, tp) 

    log_message("M3 Script execution completed")
    

# When running as a standalone script
if __name__ == "__main__":
    pass
    print(__name__)
    run()


    # on_message("Write a python code to move Axis 0 to the position 102 at starting Velocity of 10000,and end Velocity of 2000, using a ConstantDec profile.")