
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Create a position command object
posCommand = Motion_PosCommand()

# Move to -10 using TimeAccAdvancedS profile
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 10
posCommand.target = -10
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
    exit()

Wmx3Lib_cm.motion.Wait(10)  # Added axis parameter

# Move to 20 using TwoVelocityTrapezoidal profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal
posCommand.axis = 10
posCommand.target = 20
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 500

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

Wmx3Lib_cm.motion.Wait(10)  # Added axis parameter

# Move to -30 using ConstantDec profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 10
posCommand.target = -30
posCommand.profile.startingVelocity = 1000
posCommand.profile.endVelocity = 500

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

Wmx3Lib_cm.motion.Wait(10)  # Added axis parameter

# Move to 40 using ParabolicVelocity profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ParabolicVelocity
posCommand.axis = 10
posCommand.target = 40
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 150
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 1.0  # Reduced from 1.5 to 1.0
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

Wmx3Lib_cm.motion.Wait(10)  # Added axis parameter

# Move to 0 using JerkRatioFixedVelocityS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
posCommand.axis = 10
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

Wmx3Lib_cm.motion.Wait(10)  # Added axis parameter
