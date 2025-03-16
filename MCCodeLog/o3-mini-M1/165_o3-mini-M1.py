
# Axes = [11]
# IOInputs = []
# IOOutputs = []

def move_axis_11():
    # Move Axis 11 to the absolute position 110.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.JerkLimitedSCurve
    posCommand.axis = 11
    posCommand.target = 110
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    posCommand.profile.jerkAcc = 1000
    posCommand.profile.jerkDec = 1000
    posCommand.profile.startingVelocity = 0
    posCommand.profile.endVelocity = 0

    # Execute absolute position command.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 11 reaches position 110 and stops.
    Wmx3Lib_cm.motion.Wait(11)

    # Move Axis 11 to the absolute position -99.
    posCommand.target = -99
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 11 reaches position -99 and stops.
    Wmx3Lib_cm.motion.Wait(11)

    # Move Axis 11 to the absolute position 0.
    posCommand.target = 0
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is " + str(ret) + ": " + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 11 reaches position 0 and stops.
    Wmx3Lib_cm.motion.Wait(11)

if __name__ == '__main__':
    move_axis_11()
