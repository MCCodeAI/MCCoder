
# Axes = [6]
# IOInputs = []
# IOOutputs = []

axis = 6

# Set Following Error Stopped parameter
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.followingErrorStopped = 0.02
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorStopped error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Following Error Moving parameter
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.followingErrorMoving = 0.05
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorMoving error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Servo Off During Amp Alarm parameter
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.servoOffDuringAmpAlarm = False
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set servoOffDuringAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify parameters
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

if (alarmParam.followingErrorStopped == 0.02 and 
    alarmParam.followingErrorMoving == 0.05 and 
    not alarmParam.servoOffDuringAmpAlarm):
    # Move to 99
    ret = Wmx3Lib_cm.motion.MoveToPosition(axis, 99)
    if ret != 0:
        print('MoveToPosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for motion to complete
    ret = Wmx3Lib_cm.motion.WaitForMotionDone(axis)
    if ret != 0:
        print('WaitForMotionDone error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
else:
    # Move to 66
    ret = Wmx3Lib_cm.motion.MoveToPosition(axis, 66)
    if ret != 0:
        print('MoveToPosition error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    # Wait for motion to complete
    ret = Wmx3Lib_cm.motion.WaitForMotionDone(axis)
    if ret != 0:
        print('WaitForMotionDone error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
