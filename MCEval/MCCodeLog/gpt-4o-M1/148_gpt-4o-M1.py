
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 7 to position 99 with a speed of 1000 using a TimeAccJerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 7
posCommand.target = 99
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.decTimeMilliseconds = 50  # Example value, adjust as needed
posCommand.profile.jerkAccRatio = 0.5  # Example value, adjust as needed
posCommand.profile.jerkDecRatio = 0.5  # Example value, adjust as needed
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)
