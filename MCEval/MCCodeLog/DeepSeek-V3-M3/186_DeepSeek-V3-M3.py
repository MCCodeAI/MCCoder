
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to the position 10 at a speed of 1000, acceleration of 10000, deceleration of 10000, starting Velocity of 0, and end Velocity of 0, using a Parabolic profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Parabolic
posCommand.axis = 5
posCommand.target = 10
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(5)
