
# Axes = [9]
# Inputs = []
# Outputs = []

# Define the motion command for Axis 9
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 9
posCommand.profile.velocity = 1200
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Initialize the variable x
x = False  # or True, depending on the desired condition

# Check the condition of variable x
if not x:
    # Move Axis 9 by a distance of -70 if x is false
    posCommand.target = -70
else:
    # Move Axis 9 by a distance of 70 if x is true
    posCommand.target = 70

# Execute the motion command
ret = Wmx3Lib_cm.motion.StartMov(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(9)
