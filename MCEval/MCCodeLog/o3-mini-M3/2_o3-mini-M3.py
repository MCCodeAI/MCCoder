
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 2 to position -55 using an S-curve profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.SCurve
posCommand.axis = 2
posCommand.target = -55
posCommand.profile.velocity = 1000
# Using typical S-curve profile parameters for smooth motion:
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute motion command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 2 stops moving.
    Wmx3Lib_cm.motion.Wait(2)
