
# Axes = [6]
# Inputs = []
# Outputs = []

# Define the axis number
axis = 6

# Set the Following Error Stopped and Following Error Moving parameters
alarmParam = Config_AlarmParam()
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
alarmParam.followingErrorStopped = 0.02
alarmParam.followingErrorMoving = 0.05
alarmParam.servoOffDuringAmpAlarm = False

# Set the parameters
ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
if ret != 0:
    print('Set AlarmParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify if the parameters are set correctly
ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
if (alarmParam.followingErrorStopped == 0.02 and
    alarmParam.followingErrorMoving == 0.05 and
    alarmParam.servoOffDuringAmpAlarm == False):
    # Move Axis 6 to position 99
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 99
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to the specified absolute position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move Axis 6 to position 66
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 66
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to the specified absolute position
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait until the axis moves to the target position and stops
    Wmx3Lib_cm.motion.Wait(axis)
