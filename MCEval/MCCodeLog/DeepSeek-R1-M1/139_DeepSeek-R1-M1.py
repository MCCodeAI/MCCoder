
# Axes = [30]
# IOInputs = []
# IOOutputs = []

# Move Axis 30 to multiple positions using TrapezoidalMAT profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TrapezoidalMAT
posCommand.axis = 30
posCommand.profile.velocity = 10020
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.movingAverageTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Move to -310
posCommand.target = -310
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(30)

# Move to 100
posCommand.target = 100
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(30)

# Move to -40
posCommand.target = -40
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(30)

# Move to 0
posCommand.target = 0
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
Wmx3Lib_cm.motion.Wait(30)
