
# Axes = [15]
# IOInputs = []
# IOOutputs = []

# Create a command to move Axis 15 to the position -410 using a Parabola-curve profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Parabolic
posCommand.axis = 15
posCommand.target = -410
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute command to move from the current position to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    # Handle error appropriately (e.g., exit the function or program)
    exit()

# Wait until the axis reaches the target position and stops.
Wmx3Lib_cm.motion.Wait(15)
