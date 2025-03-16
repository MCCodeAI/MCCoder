
# Axes = [22]
# IOInputs = []
# IOOutputs = []

# Create a position command object for Axis 22 using the JerkRatioFixedVelocityS profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.JerkRatioFixedVelocityS
posCommand.axis = 22
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 22 stops moving after the single motion command.
    Wmx3Lib_cm.motion.Wait(22)
