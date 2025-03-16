
# Axes = [10]
# Inputs = []
# Outputs = []

# Move Axis 10 to various positions using different motion profiles

# TimeAccAdvancedS Profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 10
posCommand.target = -10
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.05  # Adjusted to be within valid range
posCommand.profile.jerkDecRatio = 0.05  # Adjusted to be within valid range
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop
Wmx3Lib_cm.motion.Wait(10)

# TwoVelocityTrapezoidal Profile
posCommand.profile.type = ProfileType.TwoVelocityTrapezoidal
posCommand.target = 20
posCommand.profile.secondVelocity = 1500  # Adjusted to be within valid range

# Execute command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop
Wmx3Lib_cm.motion.Wait(10)

# ConstantDec Profile
posCommand.profile.type = ProfileType.ConstantDec
posCommand.target = -30

# Execute command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop
Wmx3Lib_cm.motion.Wait(10)

# ParabolicVelocity Profile
posCommand.profile.type = ProfileType.ParabolicVelocity
posCommand.target = 40
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 150

# Execute command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop
Wmx3Lib_cm.motion.Wait(10)

# JerkRatioFixedVelocityS Profile
posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
posCommand.target = 0

# Execute command
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the axis to stop
Wmx3Lib_cm.motion.Wait(10)
