
# Axes = [10, 12]
# Inputs = []
# Outputs = []

# Initialize motion command for Axis 10
posCommand_Axis10 = Motion_PosCommand()
posCommand_Axis10.axis = 10
posCommand_Axis10.profile.type = ProfileType.Trapezoidal
posCommand_Axis10.profile.velocity = 600
posCommand_Axis10.profile.acc = 10000
posCommand_Axis10.profile.dec = 10000
posCommand_Axis10.target = -800

# Start the motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos(posCommand_Axis10)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to complete its motion to -800
Wmx3Lib_cm.motion.Wait(10)

# Initialize triggered motion command for Axis 10
trigger = Trigger()
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 200

trigPosCommand_Axis10 = Motion_TriggerPosCommand()
trigPosCommand_Axis10.axis = 10
trigPosCommand_Axis10.profile.type = ProfileType.Trapezoidal
trigPosCommand_Axis10.profile.velocity = 1000
trigPosCommand_Axis10.profile.acc = 10000
trigPosCommand_Axis10.profile.dec = 10000
trigPosCommand_Axis10.target = 300
trigPosCommand_Axis10.trigger = trigger

# Start the triggered motion for Axis 10
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand_Axis10)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to reach position 100
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()
posEventID = 0

eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

eventOut_Motion.type = CoreMotionEventOutputType.StartSinglePos
eventOut_Motion.startSinglePos.axis = 12
eventOut_Motion.startSinglePos.type = ProfileType.Trapezoidal
eventOut_Motion.startSinglePos.target = -50
eventOut_Motion.startSinglePos.velocity = 1000
eventOut_Motion.startSinglePos.acc = 10000
eventOut_Motion.startSinglePos.dec = 10000

# Initialize EventControl
Wmx3Lib_EventCtl = EventControl(Wmx3Lib)

ret, Event_ID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, posEventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

Wmx3Lib_EventCtl.EnableEvent(posEventID, 1)

# Wait for Axis 10 to complete its motion
Wmx3Lib_cm.motion.Wait(10)

# Remove the event
ret = Wmx3Lib_EventCtl.RemoveEvent(posEventID)
if ret != 0:
    print('RemoveEvent error code is ' + str(ret) + ': ' + WMX3Log.ErrorToString(ret))
    return

# Wait for Axis 12 to complete its motion
Wmx3Lib_cm.motion.Wait(12)
