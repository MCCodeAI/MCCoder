
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

import time

def main():
    # Create the event control objects and event IO objects.
    Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
    eventIN_Motion = CoreMotionEventInput()
    eventOut_Motion = CoreMotionEventOutput()

    # Use event ID 0.
    eventID = 0

    #------------------------------------------------------------------------------
    # Set the input event:
    #   Monitor if the RemainingTime of Axis 2's movement is 1000ms.
    #------------------------------------------------------------------------------
    eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
    eventIN_Motion.remainingTime.axis = 2
    eventIN_Motion.remainingTime.timeMilliseconds = 1000
    eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

    #------------------------------------------------------------------------------
    # Set the event output:
    #   When the above condition is met, move:
    #       Axis 1 to target position 500 at a speed of 1000,
    #       Axis 2 to target position 2000 (using the same speed here).
    #   We use a multi-axis absolute position command.
    #------------------------------------------------------------------------------
    eventOut_Motion.type = CoreMotionEventOutputType.StartMultiplePos
    eventOut_Motion.startMultiplePos.axisCount = 2

    # Map the commands:
    #   For command index 0: Axis 1
    #   For command index 1: Axis 2
    eventOut_Motion.startMultiplePos.SetAxis(0, 1)
    eventOut_Motion.startMultiplePos.SetAxis(1, 2)

    # Configure Axis 1
    eventOut_Motion.startMultiplePos.SetType(0, ProfileType.Trapezoidal)
    eventOut_Motion.startMultiplePos.SetVelocity(0, 1000)
    eventOut_Motion.startMultiplePos.SetAcc(0, 10000)
    eventOut_Motion.startMultiplePos.SetDec(0, 10000)
    eventOut_Motion.startMultiplePos.SetTarget(0, 500)

    # Configure Axis 2
    eventOut_Motion.startMultiplePos.SetType(1, ProfileType.Trapezoidal)
    eventOut_Motion.startMultiplePos.SetVelocity(1, 1000)  # Using 1000 as default speed.
    eventOut_Motion.startMultiplePos.SetAcc(1, 10000)
    eventOut_Motion.startMultiplePos.SetDec(1, 10000)
    eventOut_Motion.startMultiplePos.SetTarget(1, 2000)

    #------------------------------------------------------------------------------
    # Set the event with the API.
    #------------------------------------------------------------------------------
    ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print('SetEvent_ID error code:', ret)
        return

    # Enable the event.
    Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

    #------------------------------------------------------------------------------
    # Start an initial motion on Axis 2 so that its movement is active.
    # This motion must be long enough so that at some point its remaining time becomes 1000ms,
    # thereby triggering the event which will command both Axis 1 and Axis 2.
    #------------------------------------------------------------------------------
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 2
    # Set a target farther than 2000 to ensure that the event condition is met before
    # the motion completes.
    posCommand.target = 3000
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code for Axis 2:', ret)
        return

    # Wait until Axis 2 has moved far enough that the event input condition may be reached.
    # Do not insert waiting during the multi-axis motion trigger;
    # instead, wait after the motion command completes.
    Wmx3Lib_cm.motion.Wait(2)

    #------------------------------------------------------------------------------
    # Wait until both Axis 1 and Axis 2 stop moving after the event-triggered motion.
    #------------------------------------------------------------------------------
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 1)
    axisSel.SetAxis(1, 2)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code:', ret)
        return

    #------------------------------------------------------------------------------
    # Remove the event after the triggered motions are complete.
    #------------------------------------------------------------------------------
    ret = Wmx3Lib_EventCtl.RemoveEvent(eventID)
    if ret != 0:
        print('RemoveEvent error code:', ret)
        return

if __name__ == '__main__':
    main()
