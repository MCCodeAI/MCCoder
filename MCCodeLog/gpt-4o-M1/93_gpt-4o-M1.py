
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Set the Home Position parameter of Axis 3 to 8.8
axis = 3
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
axisParam.SetHomePosition(axis, 8.8)
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set Home Position error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Perform homing for Axis 3
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homeType = Config_HomeType.CurrentPos
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homeType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Execute homing
ret = Wmx3Lib_cm.motion.StartHoming(axis)
if ret != 0:
    print('StartHoming error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the homing process to complete
Wmx3Lib_cm.motion.Wait(axis)

# Change the Home Position parameter of Axis 3 to 0
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
axisParam.SetHomePosition(axis, 0)
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set Home Position error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
