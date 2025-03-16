
# Axes = [1, 12]
# IOInputs = []
# IOOutputs = []

def main():
    # Create a position command for Axis 12 to move to 101.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 12
    posCommand.target = 101
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Axis 12 StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 12 finishes moving.
    Wmx3Lib_cm.motion.Wait(12)

    # Get the status for all axes (we are interested in Axis 12).
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if ret != 0:
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Retrieve the status for Axis 12.
    axis12Status = CmStatus.GetAxesStatus(12)
    # Compare Actual Torque and pos cmd for Axis 12.
    if axis12Status.actualTorque == axis12Status.posCmd:
        newTarget = 201
    else:
        newTarget = -201

    # Create a new position command for Axis 1 with target determined above.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 1
    posCommand.target = newTarget
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('Axis 1 StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 1 finishes moving.
    Wmx3Lib_cm.motion.Wait(1)

if __name__ == '__main__':
    main()
