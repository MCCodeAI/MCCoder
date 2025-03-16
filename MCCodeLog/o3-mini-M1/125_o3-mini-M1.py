
# Axes = [0]
# IOInputs = []
# IOOutputs = []

# Create and configure the position command for Axis 0 using a JerkLimited profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkLimited
posCommand.axis = 0
posCommand.target = 10
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAcc = 1000
posCommand.profile.jerkDec = 1000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position move command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 0 stops moving.
    Wmx3Lib_cm.motion.Wait(0)
