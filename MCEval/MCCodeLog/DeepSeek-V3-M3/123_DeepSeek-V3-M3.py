
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

# Initialize the EventControl object
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

# Set the event input to monitor if the RemainingDistance of Axis 0's movement is 1000
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingDistance
eventIN_Motion.remainingDistance.axis = 0
eventIN_Motion.remainingDistance.distance = 1000
eventIN_Motion.remainingDistance.disableIdleAxisTrigger = 1

# Set the event output to move Axis 1 to the position 800 at a speed of 1000
eventOut_Motion = CoreMotionEventOutput()
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 1
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 800
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set the event ID to a different value (e.g., 1)
posEventID = 1

# Set input events, output events, and event addresses
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the event
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Move Axis 0 to 2000
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(0)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
