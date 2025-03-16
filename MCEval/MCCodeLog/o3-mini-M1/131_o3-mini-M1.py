
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a position command object for Axis 2.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve
posCommand.axis = 2
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 20

# Execute the absolute position command using SCurve profile.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 2 finishes moving.
    Wmx3Lib_cm.motion.Wait(2)
