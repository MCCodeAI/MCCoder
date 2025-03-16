
# Axes = [4]
# IOInputs = []
# IOOutputs = []

# Ensure the variable XYZ is defined. For this example, we'll set it to 0.
XYZ = 0  # Change this value as needed.

# Determine target position and speed based on the value of XYZ.
if XYZ == 0:
    target_position = 88
    speed = 1100
else:
    target_position = 90
    speed = 1100  # Assuming the same speed for the other case

# Create a motion command for Axis 4.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 4
posCommand.target = target_position
posCommand.profile.velocity = speed
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the absolute position command.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Wait until Axis 4 has stopped moving.
    Wmx3Lib_cm.motion.Wait(4)
