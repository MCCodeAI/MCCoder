
# Axes = [10]
# Inputs = []
# Outputs = []

# Initialize the counter
i = 0

# Loop while i is less than 3
while i < 3:
    # Create a command value for moving Axis 10 by a distance of 13.3
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 10
    posCommand.target = 13.3
    posCommand.profile.velocity = 1333
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified distance
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(10)

    # Increment the counter
    i += 1
