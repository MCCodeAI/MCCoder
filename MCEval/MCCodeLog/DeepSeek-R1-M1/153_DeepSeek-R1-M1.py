
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

Wmx3Lib_EventCtl = EventControl(Wmx3Lib)
eventIN_Motion = CoreMotionEventInput()
eventOUT_Motion = CoreMotionEventOutput()

# First motion command for Axis 10
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = -800
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Triggered motion command for Axis 10
trigPos = Motion_TriggerPosCommand()
trigger = Trigger()

trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerAxis = 10
trigger.triggerValue = 400

trigPos.axis = 10
trigPos.target = 300
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Event configuration for Axis 12
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

eventOUT_Motion.type = CoreMotionEventOutputType.StartPos
eventOUT_Motion.startPos.axis = 12
eventOUT_Motion.startPos.target = -50
eventOUT_Motion.startPos.profile.type = ProfileType.Trapezoidal
eventOUT_Motion.startPos.profile.velocity = 500
eventOUT_Motion.startPos.profile.acc = 5000
eventOUT_Motion.startPos.profile.dec = 5000

ret, eventID = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOUT_Motion, 0)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret) + ': ' + Wmx3Lib_EventCtl.ErrorToString(ret))
    return

Wmx3Lib_EventCtl.EnableEvent(0, 1)

# Wait for Axis 12 to complete its motion
Wmx3Lib_cm.motion.Wait(12)
