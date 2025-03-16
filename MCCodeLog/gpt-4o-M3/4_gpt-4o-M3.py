
# Axes = [4]
# Inputs = []
# Outputs = []

# Define the variable XYZ
XYZ = 0  # This should be set according to your specific condition

# Create a command value for the position
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4

# Check the condition of XYZ and set the target position accordingly
if XYZ == 0:
    posCommand.target = 88
    posCommand.profile.velocity = 1100
else:
    posCommand.target = 90
    posCommand.profile.velocity = 1100

# Set acceleration and deceleration
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute command to move to the specified absolute position
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(4)
