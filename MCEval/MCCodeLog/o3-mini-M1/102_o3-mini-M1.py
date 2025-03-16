
# Axes = [2, 4]
# IOInputs = []
# IOOutputs = []

def main():
    # First motion: Move Axis 2 to 200 and Axis 4 to 110.
    # Move Axis 2 to 200.
    posCommand_axis2 = Motion_PosCommand()
    posCommand_axis2.profile.type = ProfileType.Trapezoidal
    posCommand_axis2.axis = 2
    posCommand_axis2.target = 200
    posCommand_axis2.profile.velocity = 1000
    posCommand_axis2.profile.acc = 10000
    posCommand_axis2.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis2)
    if ret != 0:
        print('StartPos error for Axis 2, error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 2 reaches its target and stops.
    Wmx3Lib_cm.motion.Wait(2)

    # Move Axis 4 to 110.
    posCommand_axis4 = Motion_PosCommand()
    posCommand_axis4.profile.type = ProfileType.Trapezoidal
    posCommand_axis4.axis = 4
    posCommand_axis4.target = 110
    posCommand_axis4.profile.velocity = 1000
    posCommand_axis4.profile.acc = 10000
    posCommand_axis4.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis4)
    if ret != 0:
        print('StartPos error for Axis 4, error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until Axis 4 reaches its target and stops.
    Wmx3Lib_cm.motion.Wait(4)

    # Check condition based on the commanded positions.
    # In this case, position command for Axis 2 minus that for Axis 4: 200 - 110 = 90.
    # If the value equals 90, we will move both axes to 300,
    # otherwise, move them to 50.
    target_axis2_initial = 200
    target_axis4_initial = 110
    if (target_axis2_initial - target_axis4_initial) == 90:
        new_target = 300
    else:
        new_target = 50

    # Second motion: Move Axis 2 and Axis 4 concurrently to the new target.
    # Command for Axis 2.
    posCommand_axis2.target = new_target
    ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis2)
    if ret != 0:
        print('StartPos error for Axis 2 (second move), error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Command for Axis 4.
    posCommand_axis4.target = new_target
    ret = Wmx3Lib_cm.motion.StartPos(posCommand_axis4)
    if ret != 0:
        print('StartPos error for Axis 4 (second move), error code: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for both Axis 2 and Axis 4 to complete their motion.
    Wmx3Lib_cm.motion.Wait(2)
    Wmx3Lib_cm.motion.Wait(4)

if __name__ == '__main__':
    main()
