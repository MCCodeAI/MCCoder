
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Set the Home Position parameter of Axis 3 to 8.8
axis = 3
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homePosition = 8.8

# Set the Home Position parameter
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homePosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Perform homing for Axis 3
axisSelection = AxisSelection()
axisSelection.axisCount = 1
axisSelection.SetAxis(0, axis)
ret = Wmx3Lib_cm.home.StartHome_AxisSel(axisSelection)
if ret != 0:
    print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the homing operation is complete
Wmx3Lib_cm.motion.Wait(axis)

# Change the Home Position parameter back to 0
homeParam.homePosition = 0
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homePosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
