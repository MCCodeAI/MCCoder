
# Axes = [7]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sin  # Changed from Sine to Sin
posCommand.axis = 7
posCommand.target = 550
posCommand.profile.velocity = 100000
posCommand.profile.acc = 10000
posCommand.profile.dec = 20000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)
