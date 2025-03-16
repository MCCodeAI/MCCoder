
# Axes = [1]
# Inputs = []
# Outputs = []

posCommand = Motion_PosCommand()
trigPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Start an absolute position command for Axis 1 to move to 66.6 with a velocity of 600
posCommand.axis = 1
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = 66.6

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set trigger for Axis 1 to move to -66.6 with a velocity of 1000 when the remaining distance is 6.6
trigPosCommand.axis = 1
trigPosCommand.profile.type = ProfileType.Trapezoidal
trigPosCommand.profile.velocity = 1000
trigPosCommand.profile.acc = 10000
trigPosCommand.profile.dec = 10000
trigPosCommand.target = -66.6

trigger.triggerAxis = 1
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 6.6
trigPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(1)
