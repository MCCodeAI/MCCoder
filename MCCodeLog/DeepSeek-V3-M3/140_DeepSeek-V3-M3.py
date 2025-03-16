
from WMX3ApiPython import *
from time import *

def main():
    print('starting application...')

    wmxlib = WMX3Api()
    wmxlib_cm = CoreMotion(wmxlib)
    err = 0

    err = wmxlib.CreateDevice('C:\\Program Files\\SoftServo\\WMX3\\', DeviceType.DeviceTypeNormal)
    if err != ErrorCode.PyNone:
        print('Failed CreateDevice %08x %s' % (err, WMX3Api.ErrorToString(err)))
        return 1

    err = wmxlib.StartCommunication(5000)  # Wait for up to 5 seconds for communication
    if err != ErrorCode.PyNone:
        print('Failed StartCommunication %08x %s' % (err, WMX3Api.ErrorToString(err)))
        wmxlib.CloseDevice()
        return 1

    err = wmxlib_cm.axisControl.SetServoOn(0, 1)  # Set axis 0 servo on
    if err != ErrorCode.PyNone:
        print('Failed to set servo on %08x %s' % (err, CoreMotion.ErrorToString(err)))
        wmxlib.StopCommunication()
        wmxlib.CloseDevice()
        return 1

    sleep(5)  # Wait five seconds before stopping communication

    # Set the input event to monitor if the DistanceToTarget of Axis 3's movement is 500
    eventIN_Motion = CoreMotionEventInput()
    eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
    eventIN_Motion.distanceToTarget.axis = 3
    eventIN_Motion.distanceToTarget.distance = 500
    eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

    # Move Axis 1 to the position -200 at a speed of 1000 when the event is triggered
    eventOut_Motion = CoreMotionEventOutput()
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 1
    eventOut_Motion.startSinglePos.target = -200
    eventOut_Motion.startSinglePos.profile.velocity = 1000
    eventOut_Motion.startSinglePos.profile.acc = 10000
    eventOut_Motion.startSinglePos.profile.dec = 10000

    # Set the event ID and enable the event
    eventID = 0
    ret, Event_ID = wmxlib_cm.eventCtl.SetEvent(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print('SetEvent error code is ' + str(ret))
        return
    wmxlib_cm.eventCtl.EnableEvent(eventID, 1)

    # Move Axis 3 to 1200
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 3
    posCommand.target = 1200
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = wmxlib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + wmxlib_cm.ErrorToString(ret))
        return

    # Wait until Axis 3 moves to the target position and stops
    wmxlib_cm.motion.Wait(3)

    # Remove the event after the motion is complete
    ret = wmxlib_cm.eventCtl.RemoveEvent(eventID)
    if ret != 0:
        print('RemoveEvent error code is ' + str(ret) + ': ' + wmxlib_cm.eventCtl.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
