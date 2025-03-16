
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID for the first trigger
posEventID_1 = 0

# Set the event input for Axis 10 to move to position 400
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Set the event output to move Axis 12 to position 80
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 80
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and event addresses for the first trigger
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID_1)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the first event
Wmx3Lib_EventCtl.EnableEvent(posEventID_1, 1)

# Start an absolute position command for Axis 10 to move to position 800 with a velocity of 600
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

# Wait for Axis 10 to start moving
sleep(0.01)

# Event ID for the second trigger
posEventID_2 = 1

# Set the event input for Axis 10 when the distance to target is 200
eventIN_Motion.inputFunction = CoreMotionEventInputType.DistanceToTarget
eventIN_Motion.distanceToTarget.axis = 10
eventIN_Motion.distanceToTarget.distance = 200
eventIN_Motion.distanceToTarget.disableIdleAxisTrigger = 1

# Set the event output to move Axis 10 to position 300 with a velocity of 1000
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 10
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 300
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and event addresses for the second trigger
ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID_2)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

# Enable the second event
Wmx3Lib_EventCtl.EnableEvent(posEventID_2, 1)

# Wait for Axis 10 to complete the motion
Wmx3Lib_cm.motion.Wait(10)

# Remove the first event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID_1)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return

# Remove the second event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID_2)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return
