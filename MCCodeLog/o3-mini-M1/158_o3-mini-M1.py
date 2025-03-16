
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Create a motion position command using the TwoVel-JerkRatio profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TwoVel_JerkRatio  # Set profile to TwoVel-JerkRatio
posCommand.axis = 8                                     # Target axis 8
posCommand.target = 88                                  # Set target position to 88
posCommand.profile.velocity = 1000                      # Set velocity to 1000

# Optionally, you can set default acceleration and deceleration values if needed.
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until the axis reaches the target position and stops.
    Wmx3Lib_cm.motion.Wait(8)
