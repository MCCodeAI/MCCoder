
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Create and configure the motion command for Axis 9 using a Jerk-Ratio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatio
posCommand.axis = 9
posCommand.target = 90
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000     # Assumed acceleration based on context examples.
posCommand.profile.dec = 10000     # Assumed deceleration based on context examples.
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from the current position to the target position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 9 reaches the target position and stops moving.
    Wmx3Lib_cm.motion.Wait(9)
