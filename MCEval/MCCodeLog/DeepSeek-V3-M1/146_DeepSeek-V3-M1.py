
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to the position 144 and then 0 at a speed of 1000, acceleration of 10000, deceleration of 10000, starting Velocity of 30, and end Velocity of 0, using an S profile.

# First motion: Move Axis 4 to position 144
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.S
posCommand.axis = 4
posCommand.target = 144
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 30
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# Second motion: Move Axis 4 to position 0
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.S
posCommand.axis = 4
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 30
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)
