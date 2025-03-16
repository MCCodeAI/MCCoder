
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Check the value of the variable XYZ
if XYZ == 0:
    target_position = 88
else:
    target_position = 90

# Create a command value for Axis 4
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = target_position
posCommand.profile.velocity = 1100
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until Axis 4 moves to the target position and stops
Wmx3Lib_cm.motion.Wait(4)
