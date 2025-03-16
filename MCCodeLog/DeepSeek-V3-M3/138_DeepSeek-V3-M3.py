
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Move Axis 10 to -10, 20, -30, 40, and 0 using TimeAccAdvancedS profile
positions = [-10, 20, -30, 40, 0]
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TimeAccAdvancedS
    posCommand.axis = 10
    posCommand.target = pos
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.accTimeMilliseconds = 50  # Example acceleration time
    posCommand.profile.decTimeMilliseconds = 50  # Example deceleration time
    posCommand.profile.jerkAccRatio = 0.5  # Example jerk ratio (valid range: 0 to 1)
    posCommand.profile.jerkDecRatio = 0.5  # Example jerk ratio (valid range: 0 to 1)
    posCommand.profile.startingVelocity = 0  # Example starting velocity
    posCommand.profile.endVelocity = 0  # Example end velocity

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)

# Move Axis 10 to -10, 20, -30, 40, and 0 using TwoVelocityTrapezoidal profile
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal
    posCommand.axis = 10
    posCommand.target = pos
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.acc = 10000  # Example acceleration
    posCommand.profile.dec = 10000  # Example deceleration
    posCommand.profile.startingVelocity = 0  # Example starting velocity
    posCommand.profile.endVelocity = 0  # Example end velocity
    posCommand.profile.secondVelocity = 5000  # Example second velocity

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)

# Move Axis 10 to -10, 20, -30, 40, and 0 using ConstantDec profile
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.ConstantDec
    posCommand.axis = 10
    posCommand.target = pos
    posCommand.profile.startingVelocity = 10000  # Example starting velocity
    posCommand.profile.endVelocity = 2000  # Example end velocity

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)

# Move Axis 10 to -10, 20, -30, 40, and 0 using ParabolicVelocity profile
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.ParabolicVelocity
    posCommand.axis = 10
    posCommand.target = pos
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.accTimeMilliseconds = 50  # Example acceleration time
    posCommand.profile.decTimeMilliseconds = 150  # Example deceleration time
    posCommand.profile.jerkAccRatio = 0.5  # Example jerk ratio (valid range: 0 to 1)
    posCommand.profile.jerkDecRatio = 0.5  # Example jerk ratio (valid range: 0 to 1)
    posCommand.profile.startingVelocity = 0  # Example starting velocity
    posCommand.profile.endVelocity = 0  # Example end velocity

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)

# Move Axis 10 to -10, 20, -30, 40, and 0 using JerkRatioFixedVelocityS profile
for pos in positions:
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
    posCommand.axis = 10
    posCommand.target = pos
    posCommand.profile.velocity = 1000  # Example velocity
    posCommand.profile.acc = 10000  # Example acceleration
    posCommand.profile.dec = 10000  # Example deceleration
    posCommand.profile.jerkAccRatio = 0.5  # Example jerk ratio (valid range: 0 to 1)
    posCommand.profile.jerkDecRatio = 0.5  # Example jerk ratio (valid range: 0 to 1)
    posCommand.profile.startingVelocity = 0  # Example starting velocity
    posCommand.profile.endVelocity = 0  # Example end velocity

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)
