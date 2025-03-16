
# Axes = [0, 1]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Let the system assign an available event ID
posEventID = -1  # Use -1 to request an unused event ID

# Set the event input to monitor RemainingDistance of Axis 0
eventIN_Motion.inputFunction = CoreMotionEventInputType.RemainingDistance
eventIN_Motion.remainingDistance.axis = 0
eventIN_Motion.remainingDistance.distance = 1000
eventIN_Motion.remainingDistance.disableIdleAxisTrigger = 1

# Set the event output to move Axis 1 and Axis 0
eventOut_Motion.type = CoreMotionEventOutputType.StartMultiplePos
eventOut_Motion.startMultiplePos.axisCount = 2
eventOut_Motion.startMultiplePos.SetAxis(0, 1)
eventOut_Motion.startMultiplePos.SetAxis(1, 0)
eventOut_Motion.startMultiplePos.SetType(0, ProfileType.Trapezoidal)
eventOut_Motion.startMultiplePos.SetType(1, ProfileType.Trapezoidal)
eventOut_Motion.startMultiplePos.SetVelocity(0, 1000)
eventOut_Motion.startMultiplePos.SetVelocity(1, 1000)
eventOut_Motion.startMultiplePos.SetAcc(0, 10000)
eventOut_Motion.startMultiplePos.SetAcc(1, 10000)
eventOut_Motion.startMultiplePos.SetDec(0, 10000)
eventOut_Motion.startMultiplePos.SetDec(1, 10000)
eventOut_Motion.startMultiplePos.SetTarget(0, 800)
eventOut_Motion.startMultiplePos.SetTarget(1, 2000)

# Set and enable the event
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
posEventID = Event_ID  # Use the assigned event ID
Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Start the initial motion for Axis 0
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 0
posCommand.target = 2000
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for both axes to complete their movements
axisSel = AxisSelection()
axisSel.axisCount = 2
axisSel.SetAxis(0, 0)
axisSel.SetAxis(1, 1)
ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
if ret != 0:
    print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
