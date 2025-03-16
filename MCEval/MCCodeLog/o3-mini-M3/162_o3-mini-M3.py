
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a position command to move Axis 2 to position 210.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccSin
posCommand.axis = 2
posCommand.target = 210
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the command to move Axis 2 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 2 moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(2)
