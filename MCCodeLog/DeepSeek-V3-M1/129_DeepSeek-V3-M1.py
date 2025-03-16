
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Move Axis 9 to the position -911 at a speed of 1000, accTimeMilliseconds of 50ms, decTimeMilliseconds of 50000000000ms, using a TimeAccParabolic profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccParabolic
posCommand.axis = 9
posCommand.target = -911
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50000000000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(9)

# Move Axis 9 to the position 911 at a speed of 1000, accTimeMilliseconds of 50ms, decTimeMilliseconds of 50000000000ms, using a TimeAccParabolic profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccParabolic
posCommand.axis = 9
posCommand.target = 911
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50000000000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(9)

# Move Axis 9 to the position 168 at a speed of 1000, accTimeMilliseconds of 50ms, decTimeMilliseconds of 50000000000ms, using a TimeAccParabolic profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccParabolic
posCommand.axis = 9
posCommand.target = 168
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50000000000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(9)

# Move Axis 9 to the position 0 at a speed of 1000, accTimeMilliseconds of 50ms, decTimeMilliseconds of 50000000000ms, using a TimeAccParabolic profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccParabolic
posCommand.axis = 9
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50000000000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(9)
