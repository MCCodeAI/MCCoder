
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

# Set up an event that monitors if the RemainingTime of Axis 2's movement is 1000ms.
# When the event triggers, move Axis 1 to the position 500 at a speed of 1000.

# Create the event control and the event input/output objects.
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use event ID 0.
posEventID = 0

# Configure the event input to trigger when the remaining time
# for Axis 2's motion equals 1000 milliseconds.
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
eventIN_Motion.remainingTime.axis = 2
eventIN_Motion.remainingTime.timeMilliseconds = 1000
eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

# Configure the event output to start a single absolute position command on Axis 1.
# Move Axis 1 to position 500 with a velocity of 1000.
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 1
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 500
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set the event using the specified event input, output, and event ID.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print("SetEvent_ID error code is " + str(ret))
    return

# Enable the event.
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Start the motion for Axis 2: move Axis 2 to the position 2000.
# Note: We do not wait for the event trigger in the middle of the continuous move.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 2 completes its motion.
Wmx3Lib_cm.motion.Wait(2)

# At this point the event should have triggered the motion on Axis 1.
# Now wait until Axis 1 completes its motion.
Wmx3Lib_cm.motion.Wait(1)

# Remove the event once it has been executed.
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print("RemoveEvent error code is " + str(ret))
    return
