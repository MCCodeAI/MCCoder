
# Axes = [1, 2]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID = 0

# Set the event input to monitor the RemainingTime of Axis 2's movement.
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingTime
eventIN_Motion.remainingTime.axis = 2
eventIN_Motion.remainingTime.timeMilliseconds = 1000
eventIN_Motion.remainingTime.disableIdleAxisTrigger = 1

# Set the event output to move Axis 1 to position 500 at a speed of 1000.
eventOut_Motion.type = CoreMotionEventOutputType.StartPos
eventOut_Motion.startPos.axis = 1
eventOut_Motion.startPos.profile.type = ProfileType.Trapezoidal
eventOut_Motion.startPos.profile.velocity = 1000
eventOut_Motion.startPos.profile.acc = 10000
eventOut_Motion.startPos.profile.dec = 10000
eventOut_Motion.startPos.target = 500

# Set input events, output events, and event addresses.
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# EnableEvent
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Start an absolute position command of Axis 2 to position 2000 with 1000 velocity.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 2
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(2)

# Wait for the motion to complete. Start a blocking wait command, returning only when Axis 1 and Axis 2 become idle.
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 2)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# RemoveEvent
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
