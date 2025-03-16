
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Define the position command for Axis 3 using the TimeAcc+AdvancedS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 3
posCommand.target = 10
posCommand.profile.velocity = 12000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 1.0  # Adjusted to a valid value
posCommand.profile.jerkDecRatio = 1.0  # Adjusted to a valid value
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)
