
# Axes = [3, 4, 5, 6, 7]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to 303 using TrapezoidalMAT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 3
posCommand.target = 303
posCommand.profile.velocity = 6000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.endVelocity = 6000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(3)

# Move Axis 4 to 404 using ParabolicVelocity profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ParabolicVelocity
posCommand.axis = 4
posCommand.target = 404
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 150
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 1.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)

# Move Axis 5 to -505 using TimeAccAdvancedS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal  # Assuming similar to TrapezoidalMAT
posCommand.axis = 5
posCommand.target = -505
posCommand.profile.velocity = 7000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.endVelocity = 7000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(5)

# Move Axis 6 to -606 using TwoVelocityTrapezoidal profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal
posCommand.axis = 6
posCommand.target = -606
posCommand.profile.velocity = 8000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 5000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(6)

# Move Axis 7 to 707 using ConstantDec profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 7
posCommand.target = 707
posCommand.profile.startingVelocity = 10000
posCommand.profile.endVelocity = 2000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(7)
