
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to the position -10, 10, -10, and 0 at a speed of 1000 using a twoVelTrapezoidal profile.

# Move to -10
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.twoVelTrapezoidal
posCommand.axis = 4
posCommand.target = -10
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 1000
posCommand.profile.endVelocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)

# Move to 10
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.twoVelTrapezoidal
posCommand.axis = 4
posCommand.target = 10
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 1000
posCommand.profile.endVelocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)

# Move to -10
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.twoVelTrapezoidal
posCommand.axis = 4
posCommand.target = -10
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 1000
posCommand.profile.endVelocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)

# Move to 0
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.twoVelTrapezoidal
posCommand.axis = 4
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 1000
posCommand.profile.endVelocity = 1000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

Wmx3Lib_cm.motion.Wait(4)
