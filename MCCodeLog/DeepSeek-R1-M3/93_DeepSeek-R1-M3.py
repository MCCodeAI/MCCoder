
# Axes = [3]
# IOInputs = []
# IOOutputs = []

# Set Home Position parameter to 8.8
homeParam = Config_HomeParam()
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(3)
if ret != 0:
    print('GetHomeParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

homeParam.homePosition = 8.8

ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(3, homeParam)
if ret != 0:
    print('SetHomeParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Perform homing
ret = Wmx3Lib_cm.home.StartHome(3)
if ret != 0:
    print('StartHome error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until homing completes
Wmx3Lib_cm.motion.Wait(3)

# Change Home Position parameter back to 0
ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(3)
if ret != 0:
    print('GetHomeParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

homeParam.homePosition = 0

ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(3, homeParam)
if ret != 0:
    print('SetHomeParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
