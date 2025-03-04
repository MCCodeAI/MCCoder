# Import necessary libraries
from WMX3ApiPython import *
from time import sleep

# Constants
INFINITE = int(0xFFFFFFFF)

def initialize_wmx3():
    # Create and configure the WMX3 device
    wmx3 = WMX3Api()
    wmx3.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    wmx3.SetDeviceName('WMX3initTest')
    wmx3.StartCommunication(INFINITE)
    
    # Clear alarms and set servo on
    wmx3.axisControl.ClearAmpAlarm(0)
    wmx3.axisControl.SetServoOn(0, 1)
    sleep(0.1)  # Sleep is necessary between setting servo on and homing
    
    # Start homing
    wmx3.home.StartHome(0)
    wmx3.motion.Wait(0)  # Wait for homing to complete
    
    return wmx3

def move_to_position(wmx3, position, velocity):
    # Set up position command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = position
    posCommand.profile.velocity = velocity
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    # Execute the move command
    wmx3.motion.StartPos(posCommand)
    wmx3.motion.Wait(0)  # Wait for the move to complete

def close_wmx3(wmx3):
    # Turn off the servo and stop communication
    wmx3.axisControl.SetServoOn(0, 0)
    wmx3.StopCommunication(INFINITE)
    wmx3.CloseDevice()

def main():
    wmx3 = initialize_wmx3()
    move_to_position(wmx3, 180, 1000)
    close_wmx3(wmx3)
    print("Operation completed successfully.")

if __name__ == "__main__":
    main()
