
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Move Axis 8 to the position -99 at a speed of 1000, accTimeMilli of 50ms, decTimeMilli of -50ms, starting Velocity of 0, and end Velocity of 0, using a TimeAccTrapezoidal profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccTrapezoidal
posCommand.axis = 8
posCommand.target = -99
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = -50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(8)
