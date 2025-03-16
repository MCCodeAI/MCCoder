
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 to the position 88 at a speed of 1000 using a TwoVel-JerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelJerkRatio
posCommand.axis = 8
posCommand.target = 88
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
Wmx3Lib_cm.motion.Wait(8)
