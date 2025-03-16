
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Set Home Position parameter to 8.8
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam(3)
if ret != 0:
    print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axisParam.SetHomePosition(3, 8.8)
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set Home Position error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Perform homing on Axis 3
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(3)
if ret != 0:
    print('GetHomeParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

homeParam.homeType = Config_HomeType.CurrentPos
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(3, homeParam)
if ret != 0:
    print('SetHomeParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Start homing
ret = Wmx3Lib_cm.motion.Home(3)
if ret != 0:
    print('Home error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until homing completes
Wmx3Lib_cm.motion.Wait(3)

# Change Home Position parameter back to 0
axisParam = Config_AxisParam()
ret, axisParam = Wmx3Lib_cm.config.GetAxisParam(3)
if ret != 0:
    print('GetAxisParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

axisParam.SetHomePosition(3, 0)
ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
if ret != 0:
    print('Set Home Position error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
