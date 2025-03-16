
# Axes = [3, 4]
# IOInputs = []
# IOOutputs = []

# Move Axis 3 to position 33 at speed 1000 using a TwoVelocitySCurve profile,
# then move Axis 4 to position 77 with the same profile.
#
# Note: The following code assumes that the motion library with classes like
# Motion_PosCommand, ProfileType, and the object Wmx3Lib_cm is available.

# Create and configure the motion command for Axis 3.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 3
posCommand.target = 33
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000      # Set maximum acceleration (example value)
posCommand.profile.dec = 10000      # Set maximum deceleration (example value)
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 5000   # Example second target velocity

# Execute the absolute position move command for Axis 3.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 3 stops moving before starting the next move.
    Wmx3Lib_cm.motion.Wait(3)

# Create and configure the motion command for Axis 4.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVelocitySCurve
posCommand.axis = 4
posCommand.target = 77
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000      # Set maximum acceleration (example value)
posCommand.profile.dec = 10000      # Set maximum deceleration (example value)
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 5000   # Example second target velocity

# Execute the absolute position move command for Axis 4.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 4 stops moving.
    Wmx3Lib_cm.motion.Wait(4)
