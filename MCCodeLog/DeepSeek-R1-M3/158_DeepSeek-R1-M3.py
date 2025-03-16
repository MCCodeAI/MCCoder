
# Axes = [8]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 8
posCommand.target = 88
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Add acceleration parameter
posCommand.profile.dec = 10000  # Add deceleration parameter
posCommand.profile.jerkAccRatio = 1.0  # Use jerkAccRatio instead of jerkRatio
posCommand.profile.jerkDecRatio = 1.0  # Use jerkDecRatio instead of jerkRatio
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 1000  # Add secondVelocity parameter

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(8)
