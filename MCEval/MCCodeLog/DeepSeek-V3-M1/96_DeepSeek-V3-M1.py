
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Set the Following Error Stopped and Following Error Moving parameters for Axis 6
axis = 6

# Read the current values of parameters
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)

# Set Following Error Stopped to 0.02
alarmParam.followingErrorStopped = 0.02
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorStopped error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set Following Error Moving to 0.05
alarmParam.followingErrorMoving = 0.05
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorMoving error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set Servo Off During Amp Alarm to FALSE
alarmParam.servoOffDuringAmpAlarm = False
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set servoOffDuringAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Verify if all parameters are set correctly
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if (alarmParam.followingErrorStopped == 0.02 and 
    alarmParam.followingErrorMoving == 0.05 and 
    alarmParam.servoOffDuringAmpAlarm == False):
    # Move Axis 6 to 99
    ret = Wmx3Lib_cm.motion.StartMov(axis, 99)
    if ret != 0:
        print('Move to 99 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()
    # Wait for the axis to stop moving
    while True:
        ret, axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(axis)
        if ret != 0:
            print('GetAxisStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            exit()
        if axisStatus == AxisStatus.Idle:
            break
else:
    # Move Axis 6 to 66
    ret = Wmx3Lib_cm.motion.StartMov(axis, 66)
    if ret != 0:
        print('Move to 66 error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()
    # Wait for the axis to stop moving
    while True:
        ret, axisStatus = Wmx3Lib_cm.motion.GetAxisStatus(axis)
        if ret != 0:
            print('GetAxisStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
            exit()
        if axisStatus == AxisStatus.Idle:
            break
