
# Axes = [3, 4, 5, 6, 7]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to 303 using TrapezoidalMAT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 3
posCommand.target = 303
posCommand.profile.velocity = 6000  # Example velocity
posCommand.profile.acc = 10000     # Example acceleration
posCommand.profile.dec = 10000     # Example deceleration
posCommand.profile.endVelocity = 6000  # Example end velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(3)

# Move Axis 4 to 404 using ParabolicVelocity profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ParabolicVelocity
posCommand.axis = 4
posCommand.target = 404
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.accTimeMilliseconds = 50  # Example acceleration time
posCommand.profile.decTimeMilliseconds = 150  # Example deceleration time
posCommand.profile.jerkAccRatio = 0.5  # Example jerk acceleration ratio
posCommand.profile.jerkDecRatio = 1.5  # Example jerk deceleration ratio
posCommand.profile.startingVelocity = 0  # Example starting velocity
posCommand.profile.endVelocity = 0  # Example end velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(4)

# Move Axis 5 to -505 using TimeAccAdvancedS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 5
posCommand.target = -505
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.acc = 10000     # Example acceleration
posCommand.profile.dec = 10000     # Example deceleration
posCommand.profile.endVelocity = 0  # Example end velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 6 to -606 using TwoVelocityTrapezoidal profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal
posCommand.axis = 6
posCommand.target = -606
posCommand.profile.velocity = 1000  # Example velocity
posCommand.profile.acc = 10000     # Example acceleration
posCommand.profile.dec = 10000     # Example deceleration
posCommand.profile.startingVelocity = 0  # Example starting velocity
posCommand.profile.endVelocity = 0  # Example end velocity
posCommand.profile.secondVelocity = 5000  # Example second velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(6)

# Move Axis 7 to 707 using ConstantDec profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 7
posCommand.target = 707
posCommand.profile.startingVelocity = 10000  # Example starting velocity
posCommand.profile.endVelocity = 2000  # Example end velocity

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(7)
