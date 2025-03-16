
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Use a fixed event ID instead of requesting a new one
posEventID = 0

# Set the event input to monitor RemainingTime of Axis 2
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
eventIN_Motion.remainingTime.axis = 2
eventIN_Motion.remainingTime.timeMilliseconds = 1000
eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

# Set the event output to start a multi-axis absolute position command
eventOut_Motion.type = CoreMotionEventOutputType.StartMultiplePos
eventOut_Motion.startMultiplePos.axisCount = 2
eventOut_Motion.startMultiplePos.SetAxis(0, 1)
eventOut_Motion.startMultiplePos.SetAxis(1, 2)
eventOut_Motion.startMultiplePos.SetType(0, ProfileType.Trapezoidal)
eventOut_Motion.startMultiplePos.SetType(1, ProfileType.Trapezoidal)
eventOut_Motion.startMultiplePos.SetVelocity(0, 1000)
eventOut_Motion.startMultiplePos.SetVelocity(1, 1000)
eventOut_Motion.startMultiplePos.SetAcc(0, 10000)
eventOut_Motion.startMultiplePos.SetAcc(1, 10000)
eventOut_Motion.startMultiplePos.SetDec(0, 10000)
eventOut_Motion.startMultiplePos.SetDec(1, 10000)
eventOut_Motion.startMultiplePos.SetTarget(0, 500)
eventOut_Motion.startMultiplePos.SetTarget(1, 2000)

# Set and enable the event
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Start the initial motion for Axis 2
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 3000  # A position that will take longer than 1000ms to reach
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the initial motion to complete
Wmx3Lib_cm.motion.Wait(2)

# Wait for the event-triggered motion to complete
Wmx3Lib_cm.motion.Wait(1)
Wmx3Lib_cm.motion.Wait(2)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
