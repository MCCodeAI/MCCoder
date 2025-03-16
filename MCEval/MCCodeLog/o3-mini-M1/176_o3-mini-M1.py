
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Create a motion command to move Axis 6 to position 60 using JerkLimitedAdvancedS profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimitedAdvancedS
posCommand.axis = 6
posCommand.target = 60
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAcc = 1000
posCommand.profile.jerkDec = 1000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 6 reaches the target position and stops.
Wmx3Lib_cm.motion.Wait(6)
