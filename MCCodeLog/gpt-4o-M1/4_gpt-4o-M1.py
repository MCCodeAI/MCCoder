
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Define the target positions and speed based on the value of XYZ
target_position_if_zero = 88
target_position_if_not_zero = 90
speed = 1100

# Check the value of XYZ and set the target position accordingly
if XYZ == 0:
    target_position = target_position_if_zero
else:
    target_position = target_position_if_not_zero

# Create a command value for the target position
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = target_position
posCommand.profile.velocity = speed
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move from current position to specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(4)
