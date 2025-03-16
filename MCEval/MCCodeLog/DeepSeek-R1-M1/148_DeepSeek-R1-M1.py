
# Axes = [7]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 7
posCommand.target = 99
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)
