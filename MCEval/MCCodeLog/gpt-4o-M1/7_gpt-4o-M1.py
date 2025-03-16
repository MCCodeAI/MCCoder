
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Start a relative position command for Axis 6 with a distance of 199.9 and a velocity of 2000,
# using a jerk ratio profile with a jerk Acc Ratio of 0.3.

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 6
posCommand.target = 199.9
posCommand.profile.velocity = 2000
posCommand.profile.jerkAccRatio = 0.3
posCommand.profile.jerkDecRatio = 0.3  # Assuming symmetric jerk ratio for deceleration
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified relative position.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)
