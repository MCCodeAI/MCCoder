
# Axes = [3]
# IOInputs = []
# IOOutputs = []

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 3
posCommand.target = 88.8
posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.movingAverageTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(3)
