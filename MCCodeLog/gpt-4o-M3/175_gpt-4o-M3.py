
# Axes = [10, 12]
# Inputs = []
# Outputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Event ID for Axis 12 movement
posEventID_12 = 0

# Set the event input for Axis 10 to move to position 400
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

# Start an absolute position command for Axis 12 to move to position 80
eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = 80
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Set input events, output events, and event addresses for Axis 12
ret, Event_ID_12 = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID_12)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return
# EnableEvent for Axis 12
Wmx3Lib_EventCtl.EnableEvent(posEventID_12, 1)

# Start an absolute position command for Axis 10 to move to position 800 with a velocity of 600
posCommand_10 = Motion_PosCommand()
posCommand_10.profile.type = ProfileType.Trapezoidal
posCommand_10.axis = 10
posCommand_10.target = 800
posCommand_10.profile.velocity = 600
posCommand_10.profile.acc = 10000
posCommand_10.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand_10)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach the target position and stop
Wmx3Lib_cm.motion.Wait(10)

# Set trigger for Axis 10 to move to 300 with a velocity of 1000 when the distance to target is 200
trigPosCommand_10 = Motion_TriggerPosCommand()
trigPosCommand_10.axis = 10
trigPosCommand_10.profile.type = ProfileType.Trapezoidal
trigPosCommand_10.profile.velocity = 1000
trigPosCommand_10.profile.acc = 10000
trigPosCommand_10.profile.dec = 10000
trigPosCommand_10.target = 300
trigPosCommand_10.trigger.triggerType = TriggerType.DistanceToTarget
trigPosCommand_10.trigger.triggerAxis = 10
trigPosCommand_10.trigger.triggerValue = 200

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand_10)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to complete the triggered motion and stop
Wmx3Lib_cm.motion.Wait(10)

# Remove events
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID_12)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return
