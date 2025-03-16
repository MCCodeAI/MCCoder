
# Axes = [18]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 18
posCommand.target = 99
# Reduced velocity to a more reasonable value
posCommand.profile.velocity = 100
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
# Adjusted jerk ratios to valid range
posCommand.profile.jerkAccRatio = 1.0
posCommand.profile.jerkDecRatio = 1.0
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(18)
