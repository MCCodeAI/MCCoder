
# Axes = [1]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
trigger = Trigger()

# Start an absolute position command for Axis 1 to move to 66.6 with a velocity of 600
posCommand.axis = 1
posCommand.target = 66.6
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set trigger for Axis 1 to move to -66.6 with a velocity of 1000 when the remaining distance is 6.6
triggerPosCommand = Motion_TriggerPosCommand()
triggerPosCommand.axis = 1
triggerPosCommand.target = -66.6
triggerPosCommand.profile.type = ProfileType.Trapezoidal
triggerPosCommand.profile.velocity = 1000
triggerPosCommand.profile.acc = 10000
triggerPosCommand.profile.dec = 10000

trigger.triggerAxis = 1
trigger.triggerType = TriggerType.RemainingDistance
trigger.triggerValue = 6.6
triggerPosCommand.trigger = trigger

ret = Wmx3Lib_cm.motion.StartPos_Trigger(triggerPosCommand)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(1)
