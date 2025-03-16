
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Move Axis 6 to the position -90 at a speed of 1000, acceleration of 10000, deceleration of 10000, jerkAcc of 1000, jerkDec of 1000, starting Velocity of 0, and end Velocity of 0, using a JerkLimited-AdvancedS profile.

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedAdvancedS
posCommand.axis = 6
posCommand.target = -90
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000  # Deceleration should be positive
posCommand.profile.jerkAcc = 1000
posCommand.profile.jerkDec = 1000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)
