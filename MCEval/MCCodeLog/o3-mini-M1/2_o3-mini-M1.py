
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a position command for Axis 2 to move to -55 using an SCurve profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve
posCommand.axis = 2
posCommand.target = -55
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute positioning command for Axis 2
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 2 completes its motion and stops
    Wmx3Lib_cm.motion.Wait(2)
