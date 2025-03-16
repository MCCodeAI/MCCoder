
# Axes = [7]
# IOInputs = []
# IOOutputs = []

# Create an absolute position command for Axis 7 to move to position 550 using a cosine profile.
# Note: Since ProfileType.Cosine is not a valid profile type, we use ProfileType.Sin as an alternative.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sin  # Changed from Sine to Sin per error suggestion
posCommand.axis = 7
posCommand.target = 550
posCommand.profile.velocity = 100000
posCommand.profile.acc = 10000
posCommand.profile.dec = 20000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move the axis from the current position to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Return or exit the function/program as needed
else:
    # Wait until the axis stops moving after the motion.
    Wmx3Lib_cm.motion.Wait(7)
