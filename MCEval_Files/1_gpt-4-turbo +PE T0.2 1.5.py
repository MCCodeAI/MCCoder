
# Import necessary libraries
from WMX3ApiPython import *
from time import sleep

# Define constants
INFINITE = int(0xFFFFFFFF)

def main():
    # Initialize the WMX3 library
    Wmx3Lib = WMX3Api()
    print("WMX3 library initialized.")

    # Create a device
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret != 0:
        print('CreateDevice error:', Wmx3Lib.ErrorToString(ret))
        return

    # Set device name
    Wmx3Lib.SetDeviceName('WMX3initTest')
    print("Device name set.")

    # Start communication
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret != 0:
        print('StartCommunication error:', Wmx3Lib.ErrorToString(ret))
        return

    # Clear amplifier alarm and set servo on
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)
    ret = Wmx3Lib_cm.axisControl.ClearAmpAlarm(0)
    if ret != 0:
        print('ClearAmpAlarm error:', Wmx3Lib.ErrorToString(ret))
        return

    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
    if ret != 0:
        print('SetServoOn error:', Wmx3Lib.ErrorToString(ret))
        return

    # Sleep for stability
    sleep(0.1)

    # Start homing
    ret = Wmx3Lib_cm.home.StartHome(0)
    if ret != 0:
        print('StartHome error:', Wmx3Lib.ErrorToString(ret))
        return

    # Wait for homing to complete
    Wmx3Lib_cm.motion.Wait(0)

    # Move to absolute position
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 180
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error:', Wmx3Lib.ErrorToString(ret))
        return

    # Wait until the motion is complete
    Wmx3Lib_cm.motion.Wait(0)

    # Turn off the servo
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 0)
    if ret != 0:
        print('SetServoOff error:', Wmx3Lib.ErrorToString(ret))
        return

    # Stop communication and close device
    ret = Wmx3Lib.StopCommunication(INFINITE)
    if ret != 0:
        print('StopCommunication error:', Wmx3Lib.ErrorToString(ret))
        return

    ret = Wmx3Lib.CloseDevice()
    if ret != 0:
        print('CloseDevice error:', Wmx3Lib.ErrorToString(ret))
        return

    print("WMX3 device closed successfully.")

if __name__ == '__main__':
    main()
