
# Axes = [5]
# IOInputs = []
# IOOutputs = []

# Move Axis 5 to the position 550 at a speed of 100000, acceleration of 10000, deceleration of 10000, starting Velocity of 0, and end Velocity of 0, using a Sine profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sine
posCommand.axis = 5
posCommand.target = 550
posCommand.profile.velocity = 100000
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
