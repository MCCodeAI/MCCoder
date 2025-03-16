
# Axes = [8]
# Inputs = []
# Outputs = []

# Create a command value to move Axis 8 to position 88 with a velocity of 1000 using a TwoVelocityJerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 8
posCommand.target = 88
posCommand.profile.velocity = 1000
# Assuming default values for acceleration, deceleration, and jerk ratios as they are not specified in the question.
posCommand.profile.acc = 10000  # Example value
posCommand.profile.dec = 10000  # Example value
posCommand.profile.jerkAccRatio = 0.5  # Example value
posCommand.profile.jerkDecRatio = 0.5  # Example value
posCommand.profile.startingVelocity = 0  # Example value
posCommand.profile.endVelocity = 0  # Example value
posCommand.profile.secondVelocity = 5000  # Example value

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(8)
