
# Axes = [8]
# IOInputs = []
# IOOutputs = []

# Create the position command for Axis 8 using a Sine profile.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Sine
posCommand.axis = 8
posCommand.target = -580
posCommand.profile.velocity = 100000
posCommand.profile.acc = 10000
posCommand.profile.dec = 20000
posCommand.profile.startingVelocity = 0
posCommand.profile.endVelocity = 0

# Execute the command to move Axis 8 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(8)
