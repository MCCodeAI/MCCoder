
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Create a position command using a Trapezoidal profile for Axis 10
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 10
posCommand.target = 10
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000
posCommand.profile.startingVelocity = 10
posCommand.profile.endVelocity = 0

# Execute the command to move Axis 10 to the specified absolute position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit(1)

# Wait until Axis 10 moves to the target position and stops.
Wmx3Lib_cm.motion.Wait(10)
