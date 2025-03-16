
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Define the variable x
x = False  # or True, depending on your requirement

# Check the value of variable x
if not x:
    # Move Axis 9 by a distance of -70 with a velocity of 1200
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 9
    posCommand.target = -70
    posCommand.profile.velocity = 1200
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to a specified distance relatively.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(9)
else:
    # Move Axis 9 by a distance of 70 with a velocity of 1200
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 9
    posCommand.target = 70
    posCommand.profile.velocity = 1200
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to a specified distance relatively.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(9)
