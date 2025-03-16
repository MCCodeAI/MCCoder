
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Example of Axis 6 Alarm Parameters
axis = 6

# Set Following Error Stopped
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.followingErrorStopped = 0.02
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorStopped error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Following Error Moving
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.followingErrorMoving = 0.05
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorMoving error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Servo Off During Amp Alarm
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.servoOffDuringAmpAlarm = False
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set servoOffDuringAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify parameters
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if (alarmParam.followingErrorStopped == 0.02 and
    alarmParam.followingErrorMoving == 0.05 and
    alarmParam.servoOffDuringAmpAlarm == False):
    # Move Axis 6 to 99
    ret = Wmx3Lib_cm.motion.MoveAxis(axis, 99)
    if ret != 0:
        print('MoveAxis error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
else:
    # Move Axis 6 to 66
    ret = Wmx3Lib_cm.motion.MoveAxis(axis, 66)
    if ret != 0:
        print('MoveAxis error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
