
# Axes = [18]
# IOInputs = []
# IOOutputs = []

# Move Axis 18 to the position 99 at a speed of 100000 using a TimeAccJerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 18
posCommand.target = 99
posCommand.profile.velocity = 100000  # Adjusted to a reasonable velocity
posCommand.profile.accTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.decTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.jerkAccRatio = 0.1  # Adjusted to a reasonable value
posCommand.profile.jerkDecRatio = 0.1  # Adjusted to a reasonable value
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(18)
