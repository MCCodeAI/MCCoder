
# Axes = [4, 6]
# IOInputs = []
# IOOutputs = []

import time

def move_axis():
    # Move Axis 4 to 300
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.target = 300
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(4)

    # Get Axis 4 status and check Actual Pos
    actual_pos = Wmx3Lib_cm.axis.GetActualPos(4)
    if actual_pos == 200:
        # Move to 50 if Actual Pos is 200
        posCommand.target = 50
    else:
        # Move to -50 otherwise
        posCommand.target = -50

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(4)

    # Move Axis 6 to 111 with TwoVelocityJerkRatio profile
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.TwoVelocityJerkRatio
    posCommand.axis = 6
    posCommand.target = 111
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(6)

move_axis()
