
# Import necessary libraries
from WMX3ApiPython import *
from time import sleep

# Define constants
INFINITE = int(0xFFFFFFFF)

def main():
    # Create an instance of the WMX3 API
    Wmx3Lib = WMX3Api()
    Wmx3Lib_cm = CoreMotion(Wmx3Lib)

    # Initialize the device
    ret = Wmx3Lib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3', DeviceType.DeviceTypeNormal, INFINITE)
    if ret != 0:
        print('CreateDevice error:', Wmx3Lib.ErrorToString(ret))
        return

    # Start communication
    ret = Wmx3Lib.StartCommunication(INFINITE)
    if ret != 0:
        print('StartCommunication error:', Wmx3Lib.ErrorToString(ret))
        return

    # Clear amplifier alarms and set servo on
    ret = Wmx3Lib_cm.axisControl.ClearAmpAlarm(0)
    sleep(0.1)
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 1)
    sleep(0.1)

    # Start homing
    ret = Wmx3Lib_cm.home.StartHome(0)
    if ret != 0:
        print('StartHome error:', Wmx3Lib.ErrorToString(ret))
        return

    # Wait for homing to complete
    Wmx3Lib_cm.motion.Wait(0)

    # Move to an absolute position
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

    # Turn off the servo and stop communication
    ret = Wmx3Lib_cm.axisControl.SetServoOn(0, 0)
    ret = Wmx3Lib.StopCommunication(INFINITE)
    ret = Wmx3Lib.CloseDevice()

    print('Motion completed and device closed.')

if __name__ == '__main__':
    main()
