
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 7 to position -99 with a speed of 1000 using a TwoVelocityJerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 7
posCommand.target = -99
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Assuming default values for acceleration and deceleration
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.5  # Assuming default jerk ratios
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 1000  # Assuming second velocity is the same as max velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)
