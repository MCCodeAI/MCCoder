
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Set Axis Polarity to -1
axis = 10
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
if ret != 0:
    print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axisParam.SetAxisPolarity(axis, -1)
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set axisPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if Axis Polarity is set correctly
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
if ret != 0:
    print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

current_polarity = axisParam.GetAxisPolarity(axis)
if current_polarity == -1:
    # Move to 100
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move to -10
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = -10
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(axis)
