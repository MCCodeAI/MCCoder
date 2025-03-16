
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create a motion position command for Axis 0.
posCommand = Motion_PosCommand()
# Use the JerkLimitedFixedVelocityT profile.
posCommand.profile.type = ProfileType.JerkLimitedFixedVelocityT
posCommand.axis = 0
posCommand.target = 130
posCommand.profile.velocity = 1000
# Setting additional profile parameters using example defaults.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAcc = 1000
posCommand.profile.jerkDec = 1000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 0 stops moving.
Wmx3Lib_cm.motion.Wait(0)
