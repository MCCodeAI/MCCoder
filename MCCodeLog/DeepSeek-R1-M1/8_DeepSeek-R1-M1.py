
# Axes = [8]
# IOInputs = []
# IOOutputs = []

    # Move Axis 8 by 60 distance with 1400 velocity
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 8
    posCommand.target = 60
    posCommand.profile.velocity = 1400
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret!=0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(8)

    # Execute sequential relative moves
    distances = [-30, 20, -30, 20, -30, 20, -30]
    for distance in distances:
        posCommand = Motion_PosCommand()
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.axis = 8
        posCommand.target = distance
        posCommand.profile.velocity = 1400
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000

        ret = Wmx3Lib_cm.motion.StartMov(posCommand)
        if ret!=0:
            print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            return

        # Wait after each individual move
        Wmx3Lib_cm.motion.Wait(8)
