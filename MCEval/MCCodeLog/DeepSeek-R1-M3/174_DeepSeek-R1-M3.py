
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to position -20
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.AdvancedS
posCommand.axis = 3
posCommand.target = -20
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
    return

Wmx3Lib_cm.motion.Wait(3)

# Move Axis 3 to position 30
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.AdvancedS
posCommand.axis = 3
posCommand.target = 30
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
    return

Wmx3Lib_cm.motion.Wait(3)

# Move Axis 3 to position -40
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.AdvancedS
posCommand.axis = 3
posCommand.target = -40
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
    return

Wmx3Lib_cm.motion.Wait(3)

# Move Axis 3 to position 0
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.AdvancedS
posCommand.axis = 3
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
    return

Wmx3Lib_cm.motion.Wait(3)
