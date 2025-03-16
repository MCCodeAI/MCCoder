
# Axes = [2, 10]
# IOInputs = []
# IOOutputs = []

# Start an absolute position command for Axis 10 to move to position -1000 with a velocity of 600
posCommand = Motion_PosCommand()
posCommand.axis = 10
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = -1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 starts moving
Wmx3Lib_cm.motion.Wait(10)

# Set up a trigger to move Axis 10 to -500 with a velocity of 1000 when the remaining distance is 500
trigPosCommand = Motion_TriggerPosCommand()
trigPosCommand.axis = 10
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = -500
trigPosCommand.trigger.triggerType = TriggerType.RemainingDistance
trigPosCommand.trigger.triggerAxis = 10
trigPosCommand.trigger.triggerValue = 500

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 10 stops moving
Wmx3Lib_cm.motion.Wait(10)

# Set an event that triggers to start the movement of Axis 2 to -200 when Axis 10 moves to the position of 100
eventIN_Motion = CoreMotionEventInput()
eventOut_Motion = CoreMotionEventOutput()

# Set the event input for Axis 10 to equal 100
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Set the event output to move Axis 2 to -200
eventOut_Motion.type = CoreMotionEventOutputType.StartPos
eventOut_Motion.startPos.axis = 2
eventOut_Motion.startPos.profile.type = ProfileType.Trapezoidal
eventOut_Motion.startPos.profile.velocity = 1000
eventOut_Motion.startPos.profile.acc = 10000
eventOut_Motion.startPos.profile.dec = 10000
eventOut_Motion.startPos.target = -200

# Set the event ID and enable the event
eventID = 0
ret = Wmx3Lib_EventCtl.SetEvent_ID(eventIN_Motion, eventOut_Motion, eventID)
if ret != 0:
    print('SetEvent_ID error code is ' + str(ret))
    return

Wmx3Lib_EventCtl.EnableEvent(eventID, 1)

# Wait until Axis 2 stops moving
Wmx3Lib_cm.motion.Wait(2)

# Disable the event
Wmx3Lib_EventCtl.EnableEvent(eventID, 0)
