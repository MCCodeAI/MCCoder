
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

# This script sets an event to monitor when the RemainingDistance of Axis 0 reaches 1000.
# When triggered, it moves Axis 1 to 800 at speed 1000.
# In parallel, Axis 0 is commanded to move to position 2000.
#
# Note: After starting a motion command (such as Axis 0’s move), the code waits for that motion to complete.

from time import sleep

# Assume that the following objects and classes are available:
#   Wmx3Lib, Wmx3Lib_cm, Wmx3Lib_EventCtl, CoreMotionEventInput, CoreMotionEventOutput,
#   CoreMotionEventInputType, CoreMotionEventOutputType,
#   Motion_PosCommand, ProfileType, EventControl
#
# Also assume that error handling and logging functions are provided by the system.

def main():
    # Create event control objects
    eventCtl = EventControl(Wmx3Lib)
    eventIN_Motion = CoreMotionEventInput()
    eventOut_Motion = CoreMotionEventOutput()

    # Event ID
    eventID = 0

    # Set the event input to monitor RemainingDistance on Axis 0 equals 1000.
    eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingDistance
    eventIN_Motion.remainingDistance.axis = 0
    eventIN_Motion.remainingDistance.distance = 1000
    eventIN_Motion.remainingDistance.disableIdleAxisTrigger = 1

    # Set the event output to start a position command on Axis 1.
    # When the event is triggered, Axis 1 will move to target 800 at velocity 1000.
    eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
    eventOut_Motion.startSinglePos.axis = 1
    eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
    eventOut_Motion.startSinglePos.target = 800
    eventOut_Motion.startSinglePos.velocity = 1000
    eventOut_Motion.startSinglePos.acc = 10000
    eventOut_Motion.startSinglePos.dec = 10000

    # Register the event.
    ret, Event_ID = eventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
    if ret != 0:
        print('SetEvent_ID error code is ' + str(ret))
        return

    # Enable the event.
    eventCtl.EnableEvent(eventID, 1)
    sleep(0.01)  # Short delay to ensure the event setup takes effect

    # Now, command Axis 0 to move to position 2000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 2000
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute the absolute position command for Axis 0.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 0 completes its motion.
    Wmx3Lib_cm.motion.Wait(0)

    # At this point, while Axis 0 was moving, the event trigger should have started the motion of Axis 1.
    # Wait until Axis 1 completes its motion.
    Wmx3Lib_cm.motion.Wait(1)

    # Remove the event after both motions have completed.
    ret = eventCtl.RemoveEvent(eventID)
    if ret != 0:
        print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

if __name__ == "__main__":
    main()
