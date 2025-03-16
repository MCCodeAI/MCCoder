
# Axes = [3]
# Inputs = []
# Outputs = []

# Set the Home Position parameter of Axis 3 to 8.8
axis = 3
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homePosition = 8.8
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homePosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Perform homing for Axis 3
ret = Wmx3Lib_cm.home.StartHome(axis)
if ret != 0:
    print('Homing error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis completes homing
Wmx3Lib_cm.motion.Wait(axis)

# Change the Home Position parameter of Axis 3 to 0
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homePosition = 0
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homePosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
