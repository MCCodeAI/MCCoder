
# Import necessary libraries
from WMX3ApiPython import *
from time import sleep

def main():
    # Initialize the WMX3 library
    wmx3_lib = WMX3Api()
    core_motion = CoreMotion(wmx3_lib)

    # Initialize the device
    ret = wmx3_lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret != 0:
        print('CreateDevice error:', wmx3_lib.ErrorToString(ret))
        return

    # Start communication
    ret = wmx3_lib.StartCommunication(INFINITE)
    if ret != 0:
        print('StartCommunication error:', wmx3_lib.ErrorToString(ret))
        return

    # Set servo on for Axis 0
    ret = core_motion.axisControl.SetServoOn(0, 1)
    if ret != 0:
        print('SetServoOn error:', core_motion.ErrorToString(ret))
        return

    # Define the position command
    pos_command = Motion_PosCommand()
    pos_command.profile.type = ProfileType.Trapezoidal
    pos_command.axis = 0
    pos_command.target = 180
    pos_command.profile.velocity = 1000
    pos_command.profile.acc = 10000
    pos_command.profile.dec = 10000

    # Start the absolute position command
    ret = core_motion.motion.StartPos(pos_command)
    if ret != 0:
        print('StartPos error:', core_motion.ErrorToString(ret))
        return

    # Wait for the motion to complete
    core_motion.motion.Wait(0)

    # Set servo off
    ret = core_motion.axisControl.SetServoOn(0, 0)
    if ret != 0:
        print('SetServoOff error:', core_motion.ErrorToString(ret))
        return

    # Stop communication
    ret = wmx3_lib.StopCommunication(INFINITE)
    if ret != 0:
        print('StopCommunication error:', wmx3_lib.ErrorToString(ret))
        return

    # Close the device
    ret = wmx3_lib.CloseDevice()
    if ret != 0:
        print('CloseDevice error:', wmx3_lib.ErrorToString(ret))
        return

    print('Operation completed successfully.')

if __name__ == '__main__':
    main()
