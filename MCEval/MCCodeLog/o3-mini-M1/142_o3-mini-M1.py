
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Create a position command instance for Axis 3.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.TimeAccTrapezoidal  # Use TimeAccTrapezoidal profile.
posCommand.axis = 3
posCommand.target = 99
posCommand.profile.velocity = 1000
posCommand.profile.accTimeMilliseconds = 50
posCommand.profile.decTimeMilliseconds = 50
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the command to move Axis 3 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 3 reaches the target position and stops.
    Wmx3Lib_cm.motion.Wait(3)
