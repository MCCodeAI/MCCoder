
# Axes = [1]
# IOInputs = []
# IOOutputs = []

# Execute an absolute triggered position command for Axis 1
posCommand = Motion_PosCommand()
triggerPosCommand = Motion_TriggerPosCommand()
trigger = Trigger()

# Execute normal motion command
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

# Execute trigger motion command
triggerPosCommand.axis = 1
triggerPosCommand.profile.type = ProfileType.Trapezoidal
triggerPosCommand.profile.velocity = 1000
triggerPosCommand.profile.acc = 10000
triggerPosCommand.profile.dec = 10000
triggerPosCommand.target = -66.6

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
