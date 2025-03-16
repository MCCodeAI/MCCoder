
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Create a position command using the TimeAccJerkRatio profile to move Axis 7.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 7
posCommand.target = 99
posCommand.profile.velocity = 1000
# Set additional profile parameters (using example values)
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from current position to the target absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # If needed, handle error or exit.
else:
    # Wait until Axis 7 stops before proceeding.
    Wmx3Lib_cm.motion.Wait(7)
