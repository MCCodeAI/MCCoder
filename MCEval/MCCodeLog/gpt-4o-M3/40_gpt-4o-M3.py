
# Axes = [0]
# Inputs = []
# Outputs = []

# Define the motion command for Axis 0
posCommand = Motion_PosCommand()
posCommand.axis = 0
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.profile.velocity = 600
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.target = -66.6

# Start the absolute position command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Define the trigger motion command for Axis 0
trigPos = Motion_TriggerPosCommand()
trigPos.axis = 0
trigPos.profile.type = ProfileType.Trapezoidal
trigPos.profile.velocity = 1000
trigPos.profile.acc = 10000
trigPos.profile.dec = 10000
trigPos.target = 66.6
trigPos.trigger.triggerType = TriggerType.RemainingTime
trigPos.trigger.triggerAxis = 0
trigPos.trigger.triggerValue = 100  # 100 ms remaining time

# Start the trigger motion command
ret = Wmx3Lib_cm.motion.StartPos_Trigger(trigPos)
if ret != 0:
    print('StartPos_Trigger error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(0)
