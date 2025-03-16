
# Axes = [1, 2, 3, 4, 5, 6]
# IOInputs = []
# IOOutputs = []

# Move Axis 1 to position 101 at a speed of 1000 using a TimeAccJerkRatio profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 1
posCommand.target = 101
posCommand.profile.velocity = 1000
# Additional parameters for TimeAccJerkRatio profile can be added here

# Execute command and wait for completion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(1)

# Move Axis 2 to position 202 using JerkRatio profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 2
posCommand.target = 202
# Additional parameters for JerkRatio profile can be added here

# Execute command and wait for completion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(2)

# Move Axis 3 to position 303 using TrapezoidalMAT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 3
posCommand.target = 303
# Additional parameters for TrapezoidalMAT profile can be added here

# Execute command and wait for completion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(3)

# Move Axis 4 to position 404 using TimeAccTrapezoidal profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccTrapezoidal
posCommand.axis = 4
posCommand.target = 404
# Additional parameters for TimeAccTrapezoidal profile can be added here

# Execute command and wait for completion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(4)

# Move Axis 5 to position 505 using JerkRatioFixedVelocityS profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
posCommand.axis = 5
posCommand.target = 505
# Additional parameters for JerkRatioFixedVelocityS profile can be added here

# Execute command and wait for completion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(5)

# Move Axis 6 to position 606 using JerkLimitedFixedVelocityT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT
posCommand.axis = 6
posCommand.target = 606
# Additional parameters for JerkLimitedFixedVelocityT profile can be added here

# Execute command and wait for completion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(6)
