
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Set the Home Position parameter of Axis 3 to 8.8
axis = 3
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
homeParam.homePosition = 8.8

# SetHomeParam -> First return value: Error code, Second return value: param error
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homePosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Perform homing for Axis 3
ret = Wmx3Lib_cm.motion.StartHome(axis)
if ret != 0:
    print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis completes the homing process
Wmx3Lib_cm.motion.Wait(axis)

# Change the Home Position parameter of Axis 3 back to 0
homeParam.homePosition = 0
ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
if ret != 0:
    print('Set homePosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
