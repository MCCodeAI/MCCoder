
# Axes = [18]
# IOInputs = []
# IOOutputs = []

# Create a position command to move Axis 18 to position 99 at a speed of 1000000000000000 using a TimeAccJerkRatio profile
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccJerkRatio
posCommand.axis = 18
posCommand.target = 99
# Corrected: Reduced the velocity value to an acceptable range.
posCommand.profile.velocity = 1000000
# Using the same profile values as in the example for TimeAccJerkRatio
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the absolute position move command on Axis 18.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
    # Exit or handle the error as needed.
else:
    # Wait until Axis 18 stops moving.
    Wmx3Lib_cm.motion.Wait(18)
