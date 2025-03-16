
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Start a relative position command for Axis 6 with a distance of 199.9 and a velocity of 2000,
# using a JerkRatio profile with a jerkAccRatio of 0.3.

# Create and configure the motion command for Axis 6.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 6
posCommand.target = 199.9
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000  # Default acceleration value
posCommand.profile.dec = 10000  # Default deceleration value
posCommand.profile.jerkAccRatio = 0.3

# Execute the relative position command.
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 6 completes its relative move.
    Wmx3Lib_cm.motion.Wait(6)
