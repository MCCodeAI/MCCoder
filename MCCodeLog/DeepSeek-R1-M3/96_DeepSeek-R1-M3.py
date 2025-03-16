
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Set Following Error Stopped parameter
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(6)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.followingErrorStopped = 0.02
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(6, alarmParam)
if ret != 0:
    print('Set followingErrorStopped error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Following Error Moving parameter
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(6)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.followingErrorMoving = 0.05
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(6, alarmParam)
if ret != 0:
    print('Set followingErrorMoving error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Set Servo Off During Amp Alarm parameter
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(6)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

alarmParam.servoOffDuringAmpAlarm = False
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(6, alarmParam)
if ret != 0:
    print('Set servoOffDuringAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Check if parameters are set correctly
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(6)
if ret != 0:
    print('GetAlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

parameters_correct = (
    alarmParam.followingErrorStopped == 0.02 and
    alarmParam.followingErrorMoving == 0.05 and
    not alarmParam.servoOffDuringAmpAlarm
)

if parameters_correct:
    target_position = 99
else:
    target_position = 66

# Move Axis 6 to target position
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = target_position
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait until the axis moves to the target position and stops
Wmx3Lib_cm.motion.Wait(6)
