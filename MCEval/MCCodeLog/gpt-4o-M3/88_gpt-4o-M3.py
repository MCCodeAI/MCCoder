
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Initialize the WMX3 API and CoreMotion
from WMX3ApiPython import *
from time import sleep

def main():
    # Initialize the WMX3 API
    wmxlib = WMX3Api()
    wmxlib_cm = CoreMotion(wmxlib)
    wmxlib_comp = Compensation(wmxlib)

    # Create device
    ret = wmxlib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal)
    if ret != 0:
        print('CreateDevice error code is ' + str(ret) + ': ' + wmxlib.ErrorToString(ret))
        return

    # Start communication
    ret = wmxlib.StartCommunication(5000)  # Wait for up to 5 seconds
    if ret != 0:
        print('StartCommunication error code is ' + str(ret) + ': ' + wmxlib.ErrorToString(ret))
        wmxlib.CloseDevice()
        return

    # Set the positive direction BacklashCompensation for Axis 8
    backlashcomp = BacklashCompensationData()
    backlashcomp.enable = 1
    backlashcomp.offsetDirection = 1
    backlashcomp.backlashHigh = 11
    backlashcomp.backlashLow = 4
    backlashcomp.distanceHigh = 80
    backlashcomp.distanceLow = 30

    # Set the BacklashCompensation for Axis 8
    ret = wmxlib_comp.SetBacklashCompensation(8, backlashcomp)
    if ret != 0:
        print('SetBacklashCompensation error code is ' + str(ret) + ': ' + wmxlib_comp.ErrorToString(ret))
        return

    # Enable Backlash Compensation
    ret = wmxlib_comp.EnableBacklashCompensation(8)
    if ret != 0:
        print('EnableBacklashCompensation error code is ' + str(ret) + ': ' + wmxlib_comp.ErrorToString(ret))
        return

    # Create a command value of target as 122.6
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = 122.6
    posCommand.profile.velocity = 2000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position
    ret = wmxlib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + wmxlib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    wmxlib_cm.motion.Wait(8)

    # Disable Backlash Compensation
    ret = wmxlib_comp.DisableBacklashCompensation(8)
    if ret != 0:
        print('DisableBacklashCompensation error code is ' + str(ret) + ': ' + wmxlib_comp.ErrorToString(ret))
        return

    # Stop communication and close device
    wmxlib.StopCommunication()
    wmxlib.CloseDevice()

if __name__ == '__main__':
    main()
