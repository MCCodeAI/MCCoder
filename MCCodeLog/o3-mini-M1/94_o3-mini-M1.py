
# Axes = [2]
# IOInputs = []
# IOOutputs = []

def main():
    axis = 2

    # 1. Set Soft Limit Positive Position and Soft Limit Negative Position
    # Create a new limit parameter configuration for the axis.
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    if ret != 0:
        print("Error getting limit parameters for Axis {}: {}"
              .format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Set the soft limit positions.
    limitParam.softLimitPositivePos = 133
    limitParam.softLimitNegativePos = -133

    # Write the new limit parameters to the axis.
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if ret != 0:
        print("Error setting soft limit parameters for Axis {}: {}"
              .format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # 2. Read back the parameters to verify they have been set correctly.
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    if ret != 0:
        print("Error re-reading limit parameters for Axis {}: {}"
              .format(axis, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # 3. Check if the soft limit parameters equal 133 and -133.
    if (limitParam.softLimitPositivePos == 133 and
        limitParam.softLimitNegativePos == -133):
        target_position = 132
    else:
        target_position = -132

    # 4. Create a position command for the axis.
    posCommand = Motion_PosCommand()
    posCommand.axis = axis
    posCommand.target = target_position
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Move Axis 2 to the target position.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print("StartPos error code is {}: {}"
              .format(ret, Wmx3Lib_cm.ErrorToString(ret)))
        return

    # Wait until Axis 2 finishes moving.
    Wmx3Lib_cm.motion.Wait(axis)

if __name__ == '__main__':
    main()
