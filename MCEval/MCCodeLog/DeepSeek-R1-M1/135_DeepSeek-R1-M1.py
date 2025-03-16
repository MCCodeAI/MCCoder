
# Axes = [1, 2, 3]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID
posEventID = 0

# Set the event input to monitor CompletedTime of Axis 3
eventIN_Motion.inputFunction = CoreMotionEventInputType.CompletedTime
eventIN_Motion.completedTime.axis = 3
eventIN_Motion.completedTime.timeMilliseconds = 300
eventIN_Motion.completedTime.disableIdleAxisTrigger = 1

# Set up the output event to move Axis 1, 2, and 3
eventOut_Motion.type = CoreMotionEventOutputType.LinearIntplPos
eventOut_Motion.linearIntplPos.axisCount = 3
eventOut_Motion.linearIntplPos.SetAxis(0, 1)
eventOut_Motion.linearIntplPos.SetAxis(1, 2)
eventOut_Motion.linearIntplPos.SetAxis(2, 3)
eventOut_Motion.linearIntplPos.type = ProfileType.Trapezoidal
eventOut_Motion.linearIntplPos.velocity = 1000
eventOut_Motion.linearIntplPos.acc = 10000
eventOut_Motion.linearIntplPos.dec = 10000
eventOut_Motion.linearIntplPos.SetTarget(0, 300)  # Axis 1 target
eventOut_Motion.linearIntplPos.SetTarget(1, 2000) # Axis 2 target
eventOut_Motion.linearIntplPos.SetTarget(2, 2000) # Axis 3 target

# Set up the event
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Start the initial motion for Axis 3
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 3 to complete its motion
Wmx3Lib_cm.motion.Wait(3)

# Wait for all axes to complete their motions
axisSel = AxisSelection()
axisSel.axisCount = 3
axisSel.SetAxis(0, 1)
axisSel.SetAxis(1, 2)
axisSel.SetAxis(2, 3)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
