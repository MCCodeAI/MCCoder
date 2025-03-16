
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create and configure a position command for Axis 3 using the TwoVelocitySCurve profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 3
posCommand.target = 33
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000        # Maximum acceleration (example value)
posCommand.profile.dec = 10000        # Maximum deceleration (example value)
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 5000  # Second velocity for the two-velocity profile

# Execute the absolute position command to move Axis 3.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 3 finishes moving.
    Wmx3Lib_cm.motion.Wait(3)
