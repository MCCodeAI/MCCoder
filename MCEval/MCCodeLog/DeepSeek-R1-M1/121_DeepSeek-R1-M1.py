
# Axes = [1, 2, 3, 4]
# IOInputs = []
# IOOutputs = []

# Move Axis 1 with SCurve profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Default acceleration
posCommand.profile.dec = 10000  # Default deceleration
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(1)

# Move Axis 2 with Parabolic profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Parabolic
posCommand.axis = 2
posCommand.target = -202
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Default acceleration
posCommand.profile.dec = 10000  # Default deceleration
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(2)

# Move Axis 3 with TimeAccAdvancedS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 3
posCommand.target = 303
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(3)

# Move Axis 4 with JerkLimitedFixedVelocityS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityS
posCommand.axis = 4
posCommand.target = -404
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000  # Default acceleration
posCommand.profile.dec = 10000  # Default deceleration
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)
