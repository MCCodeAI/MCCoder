
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Initialize the counter
i = 0

# Loop while i is less than 3
while i < 3:
    # Create a command value of target as 13.3
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 10
    posCommand.target = 13.3
    posCommand.profile.velocity = 1333
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to specified absolute position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)

    # Increment the counter
    i += 1
