
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to the position 30 and 0 and 30 and 0 at starting Velocity of 100, and end Velocity of 0, using a ConstantDec profile.

posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3

# Move to position 30
posCommand.target = 30
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)

# Move to position 0
posCommand.target = 0
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)

# Move to position 30
posCommand.target = 30
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)

# Move to position 0
posCommand.target = 0
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)
