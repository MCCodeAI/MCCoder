
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Move Axis 4 to position 144 using S profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.S
posCommand.axis = 4
posCommand.target = 144
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 30
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(4)

# Move Axis 4 to position 0 using S profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.S
posCommand.axis = 4
posCommand.target = 0
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 30
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(4)
