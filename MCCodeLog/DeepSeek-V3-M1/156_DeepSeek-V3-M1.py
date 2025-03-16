
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

# Execute an absolute triggered position command for Axis 10
posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()

# Start an absolute position command for Axis 10 to move to position -800 with a velocity of 600
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

# Set up a trigger for Axis 10 to move to 300 with a velocity of 1000 when the distance to target is 200
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.axis = 10
trigPosCommand.target = 300
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000

trigger = Trigger()
trigger.triggerAxis = 10
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerValue = 200
trigPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 10 to stop moving
Wmx3Lib_cm.motion.Wait(10)

# Set an event that triggers to start the movement of Axis 12 to -50 when Axis 10 moves to the position of 100
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 100

# Execute an absolute position command for Axis 12 to move to -50
posCommand.axis = 12
posCommand.target = -50
posCommand.profile.velocity = 500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to stop moving
Wmx3Lib_cm.motion.Wait(12)
