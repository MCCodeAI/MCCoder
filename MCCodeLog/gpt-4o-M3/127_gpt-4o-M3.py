
# Axes = [0]
# Inputs = []
# Outputs = []

# Create a command to move Axis 0 to position 130 with a velocity of 1000 using a JerkLimitedFixedVelocityT profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT
posCommand.axis = 0
posCommand.target = 130
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Example acceleration value
posCommand.profile.dec = 10000  # Example deceleration value
posCommand.profile.jerkAcc = 1000  # Example jerk acceleration value
posCommand.profile.jerkDec = 1000  # Example jerk deceleration value
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(0)
