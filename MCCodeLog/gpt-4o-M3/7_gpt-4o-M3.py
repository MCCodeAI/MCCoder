
# Axes = [6]
# Inputs = []
# Outputs = []

# Create a command for a relative position move on Axis 6
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 6
posCommand.target = 199.9
posCommand.profile.velocity = 2000

# Correct the jerkAccRatio and jerkDecRatio to be within the valid range
posCommand.profile.jerkAccRatio = 0.1  # Adjusted to a valid range
posCommand.profile.jerkDecRatio = 0.1  # Adjusted to a valid range

posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to a specified distance relatively.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(6)
