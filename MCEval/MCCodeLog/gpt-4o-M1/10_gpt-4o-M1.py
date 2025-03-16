
# Axes = [10]
# IOInputs = []
# IOOutputs = []

i = 0
while i < 3:
    # Create a command value for moving Axis 10 by a distance of 13.3 with a velocity of 1333.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 10
    posCommand.target = 13.3  # Relative movement
    posCommand.profile.velocity = 1333
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move from current position to a specified distance relatively.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        break

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(10)

    # Increment i by 1
    i += 1
