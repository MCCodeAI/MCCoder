
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 0 to move to position 130 with a speed of 1000 using a JerkLimitedFixedVelocityT profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT
posCommand.axis = 0
posCommand.target = 130
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Assuming default acceleration
posCommand.profile.dec = 10000  # Assuming default deceleration
posCommand.profile.jerkAcc = 1000  # Assuming default jerkAcc
posCommand.profile.jerkDec = 1000  # Assuming default jerkDec
posCommand.profile.startingVelocity = 0  # Assuming starting velocity
posCommand.profile.endVelocity = 0  # Assuming end velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(0)
