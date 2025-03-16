
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to the position 50 at a speed of 1000, jerkAccRatio of 0.5, jerkDecRatio of 0.5, starting Velocity of 0, and end Velocity of 0, using a JerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 5
posCommand.target = 50
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Assuming a default acceleration value
posCommand.profile.dec = 10000  # Assuming a default deceleration value
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(5)
