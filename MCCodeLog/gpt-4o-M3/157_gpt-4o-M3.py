
# Axes = [7]
# Inputs = []
# Outputs = []

# Create a command to move Axis 7 to the position -99 at a speed of 1000 using a TwoVelocityJerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 7
posCommand.target = -99
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Assuming a default value for maximum acceleration
posCommand.profile.dec = 10000  # Assuming a default value for maximum deceleration
posCommand.profile.jerkAccRatio = 0.5  # Assuming a default value for acceleration jerk ratio
posCommand.profile.jerkDecRatio = 0.5  # Assuming a default value for deceleration jerk ratio
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 1500  # Assuming a default value for second velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)
