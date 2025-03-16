
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create a command value of target as 10.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccAdvancedS
posCommand.axis = 3
posCommand.target = 10
posCommand.profile.velocity = 12000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
# Corrected the jerkAccRatio value to 1.0 because a value of 1.5 is out of range for this profile.
posCommand.profile.jerkAccRatio = 1.0
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Exit or handle error as needed.
else:
    # Wait until the axis moves and stops before continuing.
    Wmx3Lib_cm.motion.Wait(3)
