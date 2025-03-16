
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set E-Stop Level 1 Type parameter
emergencyStopParam = Config_EmergencyStopParam()
ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
emergencyStopParam.eStopLevel1Type = Config_EStopLevel1Type.DecServoOff
ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
if ret != 0:
    print('Set eStopLevel1Type error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify the parameter
ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
if emergencyStopParam.eStopLevel1Type == Config_EStopLevel1Type.DecServoOff:
    # Move to 99.9
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.SCurve
    posCommand.axis = 9
    posCommand.target = 99.9
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(9)
else:
    # Move to -99.9
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.SCurve
    posCommand.axis = 9
    posCommand.target = -99.9
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    Wmx3Lib_cm.motion.Wait(9)
