
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 3 to position 88.8 with a velocity of 1200 using a TrapezoidalMAT profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 3
posCommand.target = 88.8
posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000  # Assuming default acceleration
posCommand.profile.dec = 10000  # Assuming default deceleration
posCommand.profile.movingAverageTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)
