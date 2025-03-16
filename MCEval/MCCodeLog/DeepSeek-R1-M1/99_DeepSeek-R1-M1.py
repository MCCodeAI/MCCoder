
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set E-Stop Level 1 Type parameter to DecServoOff for Axis 9
emergencyStopParam = Config_EmergencyStopParam()
ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
if ret != 0:
    print('GetEmergencyStopParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set E-Stop Level 1 Type to DecServoOff
emergencyStopParam.eStopLevel1Type = Config_EStopLevel1Type.DecServoOff
ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
if ret != 0:
    print('Set eStopLevel1Type error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if the parameter was set correctly
ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
if ret != 0:
    print('GetEmergencyStopParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

if emergencyStopParam.eStopLevel1Type == Config_EStopLevel1Type.DecServoOff:
    # Move Axis 9 to 99.9 with S-curve profile
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

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(9)
else:
    # Move Axis 9 to -99.9 with S-curve profile
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

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(9)
