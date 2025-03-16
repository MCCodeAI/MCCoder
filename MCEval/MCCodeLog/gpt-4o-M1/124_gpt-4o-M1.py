
# Axes = [3]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 3
posCommand.target = 33
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 2000  # Assuming a second velocity for TwoVelocitySCurve

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)
