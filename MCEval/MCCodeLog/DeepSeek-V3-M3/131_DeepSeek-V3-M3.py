
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Move Axis 2 to the position 120 at a speed of 1000, acceleration of 10000, deceleration of 10000, starting Velocity of 0, and end Velocity of 20, using an SCurve profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve
posCommand.axis = 2
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 20

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(2)
