
# Axes = [6]
# IOInputs = []
# IOOutputs = []

# Note:
# This code sets the Following Error Stopped parameter and Following Error Moving parameter of Axis 6 to 0.02 and 0.05 respectively.
# It also sets Servo Off During Amp Alarm to FALSE.
# Then it reads back the Alarm parameters and checks if all have been set correctly.
# If the settings are verified correct, Axis 6 will be commanded to move to position 99;
# otherwise, it will move to position 66.
#
# The code follows a similar structure to the context examples provided.
# After each motion command, the code waits for the axis to stop moving by calling the Wait function.

axis = 6

# -----------------------------
# Set Following Error Stopped = 0.02
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.followingErrorStopped = 0.02
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorStopped error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# -----------------------------
# Set Following Error Moving = 0.05
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.followingErrorMoving = 0.05
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set followingErrorMoving error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# -----------------------------
# Set Servo Off During Amp Alarm = FALSE
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.servoOffDuringAmpAlarm = False
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set servoOffDuringAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# -----------------------------
# Verify that the parameters are set correctly.
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if (abs(alarmParam.followingErrorStopped - 0.02) < 1e-6 and
    abs(alarmParam.followingErrorMoving - 0.05) < 1e-6 and
    (alarmParam.servoOffDuringAmpAlarm == False)):
    targetPosition = 99
else:
    targetPosition = 66

# -----------------------------
# Create a motion command to move Axis 6 to the target position.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = targetPosition
posCommand.profile.velocity = 1000    # Example velocity
posCommand.profile.acc = 10000          # Example acceleration
posCommand.profile.dec = 10000          # Example deceleration

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for Axis 6 to stop moving.
Wmx3Lib_cm.motion.Wait(axis)
