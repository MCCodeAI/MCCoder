
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# First event - Distance trigger for Axis 10
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 10
eventIN_Motion.distanceToTarget.distance = 200

eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 10
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 300
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Request unique event ID for first event
ret, posEventID1 = Wmx3Lib_EventCtl.RequestEventID()
if ret != 0:
    print('RequestEventID error code is ' + str(ret))
    return

ret = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID1)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(posEventID1, 1)

# Second event - Position trigger for Axis 12
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 80
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Request unique event ID for second event
ret, posEventID2 = Wmx3Lib_EventCtl.RequestEventID()
if ret != 0:
    print('RequestEventID error code is ' + str(ret))
    return

ret = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID2)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
Wmx3Lib_EventCtl.EnableEvent(posEventID2, 1)

sleep(0.01)

# Start initial position command for Axis 10 to 800
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = 800
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to finish its movement
Wmx3Lib_cm.motion.Wait(10)

# Disable and remove both events
Wmx3Lib_EventCtl.EnableEvent(posEventID1, 0)
Wmx3Lib_EventCtl.EnableEvent(posEventID2, 0)

ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID1)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret))
    return

ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID2)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret))
    return
