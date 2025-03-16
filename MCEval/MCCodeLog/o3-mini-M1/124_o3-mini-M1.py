
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create a position command using the TwoVelocitySCurve profile to move Axis 3 to position 33 at 1000 velocity.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 3
posCommand.target = 33
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
# Using a second velocity value as an example; ensure it is greater than the maximum profile velocity.
posCommand.profile.secondVelocity = 5000

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until Axis 3 stops moving.
Wmx3Lib_cm.motion.Wait(3)
