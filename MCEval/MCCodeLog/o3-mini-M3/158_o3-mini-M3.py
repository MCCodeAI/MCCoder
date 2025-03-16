
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 8 to position 88 using a TwoVelocityJerkRatio profile.
posCommand = Motion_PosCommand()
# Corrected the profile type attribute name based on the error: use TwoVelocityJerkRatio.
posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
posCommand.axis = 8
posCommand.target = 88
posCommand.profile.velocity = 1000

# Set additional required parameters for the TwoVelocityJerkRatio profile.
# (These example values can be adjusted as needed.)
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.jerkAccRatio = 0.5
posCommand.profile.jerkDecRatio = 0.5
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0
posCommand.profile.secondVelocity = 5000

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 8 stops moving.
    Wmx3Lib_cm.motion.Wait(8)
