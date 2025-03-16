
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set the E-Stop Level 1 Type parameter of Axis 9 to DecServoOff
emergencyStopParam = Config_EmergencyStopParam()
ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
emergencyStopParam.eStopLevel1Type = Config_EStopLevel1Type.DecServoOff
ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
if ret != 0:
    print('Set eStopLevel1Type error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check if the E-Stop Level 1 Type parameter is set correctly
ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
if emergencyStopParam.eStopLevel1Type == Config_EStopLevel1Type.DecServoOff:
    # Move Axis 9 to 99.9 with S curve profile
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
        exit()
    Wmx3Lib_cm.motion.Wait(9)
else:
    # Move Axis 9 to -99.9 with S curve profile
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
        exit()
    Wmx3Lib_cm.motion.Wait(9)
