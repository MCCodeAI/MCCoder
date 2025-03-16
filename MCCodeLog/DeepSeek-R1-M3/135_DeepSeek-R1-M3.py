
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = []

from WMX3ApiPython import *
from time import *

INFINITE = int(0xFFFFFFFF)

def main():
    # Initialize WMX3 API
    wmxlib = WMX3Api()
    wmxlib_cm = CoreMotion(wmxlib)

    # Create device
    err = wmxlib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal, INFINITE)
    if err != 0:
        print('CreateDevice error code is ' + str(err) + ': ' + wmxlib.ErrorToString(err))
        return

    # Start communication
    err = wmxlib.StartCommunication(INFINITE)
    if err != 0:
        print('StartCommunication error code is ' + str(err) + ': ' + wmxlib.ErrorToString(err))
        return

    # Import motion parameters
    err = wmxlib_cm.config.ImportAndSetAll("C:\\Program Files\\SoftServo\\WMX3\\wmx_parameters.xml")
    if err != 0:
        print('ImportAndSetAll error code is ' + str(err) + ': ' + wmxlib_cm.ErrorToString(err))
        return

    # Set servo on for all axes
    for axis in [1, 2, 3]:
        err = wmxlib_cm.axisControl.SetServoOn(axis, 1)
        if err != 0:
            print(f'SetServoOn error for axis {axis}: ' + str(err) + ': ' + wmxlib_cm.ErrorToString(err))
            return

    # Wait for servo to be on
    for axis in [1, 2, 3]:
        while True:
            ret, status = wmxlib_cm.GetStatus()
            if status.GetAxesStatus(axis).servoOn:
                break
            sleep(0.1)

    # Create event for monitoring Axis 3 completion time
    event = wmxlib.CreateEvent()
    wmxlib.SetEventSource(event, EventSource.Axis3_CompletedTime)
    wmxlib.SetEventCondition(event, EventCondition.Equal, 300)  # 300ms

    # Define callback function
    def on_axis3_completion():
        # Move Axis 1 to position 300
        posCommand1 = Motion_PosCommand()
        posCommand1.profile.type = ProfileType.Trapezoidal
        posCommand1.axis = 1
        posCommand1.target = 300
        posCommand1.profile.velocity = 1000
        posCommand1.profile.acc = 10000
        posCommand1.profile.dec = 10000

        ret = wmxlib_cm.motion.StartPos(posCommand1)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + wmxlib_cm.ErrorToString(ret))
            return

        wmxlib_cm.motion.Wait(1)

        # Move Axis 2 and 3 to 2000
        posCommand2 = Motion_PosCommand()
        posCommand2.profile.type = ProfileType.Trapezoidal
        posCommand2.axis = 2
        posCommand2.target = 2000
        posCommand2.profile.velocity = 1000
        posCommand2.profile.acc = 10000
        posCommand2.profile.dec = 10000

        ret = wmxlib_cm.motion.StartPos(posCommand2)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + wmxlib_cm.ErrorToString(ret))
            return

        wmxlib_cm.motion.Wait(2)

        posCommand3 = Motion_PosCommand()
        posCommand3.profile.type = ProfileType.Trapezoidal
        posCommand3.axis = 3
        posCommand3.target = 2000
        posCommand3.profile.velocity = 1000
        posCommand3.profile.acc = 10000
        posCommand3.profile.dec = 10000

        ret = wmxlib_cm.motion.StartPos(posCommand3)
        if ret != 0:
            print('StartPos error code is ' + str(ret) + ': ' + wmxlib_cm.ErrorToString(ret))
            return

        wmxlib_cm.motion.Wait(3)

    # Set callback for the event
    wmxlib.SetEventCallback(event, on_axis3_completion)

    # Start monitoring
    wmxlib.StartEventMonitoring(event)

    # Move Axis 3 first
    posCommand3 = Motion_PosCommand()
    posCommand3.profile.type = ProfileType.Trapezoidal
    posCommand3.axis = 3
    posCommand3.target = 2000
    posCommand3.profile.velocity = 1000
    posCommand3.profile.acc = 10000
    posCommand3.profile.dec = 10000

    ret = wmxlib_cm.motion.StartPos(posCommand3)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + wmxlib_cm.ErrorToString(ret))
        return

    # Wait for Axis 3 to complete movement
    wmxlib_cm.motion.Wait(3)

    # Stop communication and close device
    err = wmxlib.StopCommunication(INFINITE)
    if err != 0:
        print('StopCommunication error code is ' + str(err) + ': ' + wmxlib.ErrorToString(err))

    err = wmxlib.CloseDevice()
    if err != 0:
        print('CloseDevice error code is ' + str(err) + ': ' + wmxlib.ErrorToString(err))

if __name__ == '__main__':
    main()
