
# Axes = [10]
# IOInputs = []
# IOOutputs = []

# Set the Axis Polarity parameter of Axis 10 to -1
axis = 10
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
axisParam.SetAxisPolarity(axis, -1)

# Set the Axis Polarity parameter
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set axisPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check if the Axis Polarity parameter is set correctly
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
currentPolarity = axisParam.GetAxisPolarity(axis)

if currentPolarity == -1:
    # Move Axis 10 to 100 if the polarity is set correctly
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
        exit()

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move Axis 10 to -10 if the polarity is not set correctly
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
        exit()

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
