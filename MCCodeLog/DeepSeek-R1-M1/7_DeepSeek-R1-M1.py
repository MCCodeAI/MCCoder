
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Start a relative position command for Axis 6 with specified parameters
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 6
posCommand.target = 199.9  # Relative distance
posCommand.profile.velocity = 2000
posCommand.profile.acc = 10000  # Default acceleration from context examples
posCommand.profile.dec = 10000  # Default deceleration from context examples
posCommand.profile.jerkAccRatio = 0.3
posCommand.profile.jerkDecRatio = 0.3  # Assumed same as jerkAccRatio
posCommand.profile.startingVelocity = 0  # From context examples
posCommand.profile.endVelocity = 0  # From context examples

# Execute relative position command
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print(f'StartMov error code: {ret} - {Wmx3Lib_cm.ErrorToString(ret)}')
    exit()

# Wait until axis completes motion
Wmx3Lib_cm.motion.Wait(6)
