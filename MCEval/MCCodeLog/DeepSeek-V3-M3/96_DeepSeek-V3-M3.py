
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Set the Following Error Stopped and Following Error Moving parameters for Axis 6
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(6)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.followingErrorStopped = 0.02
alarmParam.followingErrorMoving = 0.05
alarmParam.servoOffDuringAmpAlarm = False

ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(6, alarmParam)
if ret != 0:
    print('SetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify if the parameters are set correctly
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(6)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

if (alarmParam.followingErrorStopped == 0.02 and 
    alarmParam.followingErrorMoving == 0.05 and 
    alarmParam.servoOffDuringAmpAlarm == False):
    
    # Move Axis 6 to 99 if parameters are set correctly
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 99
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(6)

else:
    # Move Axis 6 to 66 if parameters are not set correctly
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 6
    posCommand.target = 66
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops.
    Wmx3Lib_cm.motion.Wait(6)
