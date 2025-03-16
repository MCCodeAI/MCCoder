
# Axes = [2]
# IOInputs = []
# IOOutputs = []

# Set Soft Limit Positive Position and Soft Limit Negative Position for Axis 2
axis = 2

# Read the current limit parameters
limitParam = Config_LimitParam()
ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
if ret != 0:
    print('GetLimitParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Soft Limit Positive Position to 133
limitParam.softLimitPositivePos = 133

# Set Soft Limit Negative Position to -133
limitParam.softLimitNegativePos = -133

# Apply the updated limit parameters
ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
if ret != 0:
    print('SetLimitParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify if Soft Limit Positive Position and Soft Limit Negative Position are set correctly
ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
if ret != 0:
    print('GetLimitParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

if limitParam.softLimitPositivePos == 133 and limitParam.softLimitNegativePos == -133:
    # Move Axis 2 to 132
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 132
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move Axis 2 to -132
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = -132
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
