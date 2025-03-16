
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def move_axis_9(x):
    # Create a command value for Axis 9.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 9
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    if not x:
        # Variable x is False, so move by a distance of -70 with velocity 1200.
        posCommand.target = -70
        posCommand.profile.velocity = 1200
        ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    else:
        # Otherwise, move by a distance of 70.
        posCommand.target = 70
        posCommand.profile.velocity = 1200
        ret = Wmx3Lib_cm.motion.StartMov(posCommand)

    if ret != 0:
        print("StartMov error code is {}: {}".format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait until Axis 9 stops moving.
    Wmx3Lib_cm.motion.Wait(9)


# Example usage:
x = False  # Set x to False or True to test the behavior.
move_axis_9(x)
