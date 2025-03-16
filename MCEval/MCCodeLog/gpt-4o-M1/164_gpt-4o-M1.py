
# Axes = [10, 12]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Start an absolute position command for Axis 10 to move to position 800 with a velocity of 600
posCommand.axis = 10
posCommand.target = 800
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000  # Assuming a default acceleration
posCommand.profile.dec = 10000  # Assuming a default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Trigger Axis 10 to move to 300 with a velocity of 1000 when the distance to target is 200
trigPosCommand.axis = 10
trigPosCommand.target = 300
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000  # Assuming a default acceleration
trigPosCommand.profile.dec = 10000  # Assuming a default deceleration

trigger.triggerAxis = 10
trigger.triggerType = TriggerType.DistanceToTarget
trigger.triggerValue = 200
trigPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set an event that triggers to start the movement of Axis 12 to 80 when Axis 10 moves to the position of 400
eventIN_Motion = CoreMotionEventInput()
eventIN_Motion.inputFunction = CoreMotionEventInputType.EqualPos
eventIN_Motion.equalPos.axis = 10
eventIN_Motion.equalPos.pos = 400

posCommand.axis = 12
posCommand.target = 80
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 500  # Assuming a default velocity
posCommand.profile.acc = 10000  # Assuming a default acceleration
posCommand.profile.dec = 10000  # Assuming a default deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 12 to complete the motion
Wmx3Lib_cm.motion.Wait(12)
