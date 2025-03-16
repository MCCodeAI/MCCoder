
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to positions: 30, then 0, then 30, then 0,
# using a ConstantDec profile with startingVelocity of 100 and endVelocity of 0.
# Wait for axis stop after each motion.

# Move to position 30
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3
posCommand.target = 30
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 3 stops moving
    Wmx3Lib_cm.motion.Wait(3)

# Move to position 0
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3
posCommand.target = 0
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    Wmx3Lib_cm.motion.Wait(3)

# Move to position 30 again
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3
posCommand.target = 30
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    Wmx3Lib_cm.motion.Wait(3)

# Move to position 0 again
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.ConstantDec
posCommand.axis = 3
posCommand.target = 0
posCommand.profile.startingVelocity = 100
posCommand.profile.endVelocity = 0

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    Wmx3Lib_cm.motion.Wait(3)
