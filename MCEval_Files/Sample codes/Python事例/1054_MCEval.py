#Set the Alarm parameters for Axis 0. Set‘Following Error Stopped’to 0,‘Following Error Moving’to 0,‘Following Error Stopped’to 0,‘Following Error Type ’to NoAction,‘Velocity Following Error Stopped’to 0,‘Velocity Following Error Stopped Milliseconds ’to 0,‘Velocity Following Error Moving’to 0,‘Velocity Following Error Moving Milliseconds ’to 0,‘Velocity Following Error Type’to NoAction,‘Servo Off During Amp Alarm’to TRUE,‘Servo On Following Error’to 0.
    # Axes = [0]

    # Example of Axis 0 Homing Parameters
    axis = 0

    # Following Error Stopped    The maximum difference between the command position and feedback position that can be tolerated while the axis is in the Idle operation state before a following error alarm is triggered. A following error alarm will never be triggered while the axis is Idle if this value is set to 0.
    # Variable Name:   followingErrorStopped
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.followingErrorStopped = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set followingErrorStopped  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Following Error Moving     The maximum difference between the command position and feedback position that can be tolerated while the axis is executing a motion command before a following error alarm is triggered. A following error alarm will never be triggered while the axis is executing a motion command if this value is set to 0.
    # Variable Name:   followingErrorMoving
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.followingErrorMoving = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set followingErrorMoving  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Following Error Type     This parameter determines the action that is executed when the following error alarm is triggered. A following error alarm is triggered whenever the difference between the command position and feedback position of a Position mode axis exceeds the Following Error Stopped or Following Error Moving parameter, depending on whether the axis is currently executing a command or not.
    # Variable Name:   followingErrorType
    # Type:            FollowingErrorAlarmType
    # Default Value:   NoAction
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.followingErrorType  = Config_FollowingErrorAlarmType.NoAction
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set followingErrorType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Velocity Following Error Stopped     The maximum difference between the command velocity and feedback velocity that can be tolerated while the axis is in the Idle operation state before a following error alarm is triggered. A following error alarm will never be triggered while the axis is Idle if this value is set to 0.
    # Variable Name:   velocityFollowingErrorStopped
    # Type:            double
    # Unit:            user unit/second
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.velocityFollowingErrorStopped = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set velocityFollowingErrorStopped  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Velocity Following Error Stopped Milliseconds      If set to a value above 0, a following error alarm will only be triggered if the difference between the command velocity and feedback velocity exceeds the amount in Velocity Following Error Stopped continuously for the amount of time specified in this parameter while the axis is in the Idle operation state.
    # Variable Name:   velocityFollowingErrorStoppedMilliseconds
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.velocityFollowingErrorStoppedMilliseconds  = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set velocityFollowingErrorStoppedMilliseconds error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Velocity Following Error Moving      The maximum difference between the command velocity and feedback velocity that can be tolerated while the axis is executing a motion command before a following error alarm is triggered. A following error alarm will never be triggered while the axis is executing a motion command if this value is set to 0.
    # Variable Name:   velocityFollowingErrorMoving
    # Type:            double
    # Unit:            user unit/second
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.velocityFollowingErrorMoving  = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set velocityFollowingErrorMoving error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Velocity Following Error Moving Milliseconds       If set to a value above 0, a following error alarm will only be triggered if the difference between the command velocity and feedback velocity exceeds the amount in Velocity Following Error Moving continuously for the amount of time specified in this parameter while the axis is executing a motion command.
    # Variable Name:   velocityFollowingErrorMovingMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.velocityFollowingErrorMovingMilliseconds  = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set velocityFollowingErrorMovingMilliseconds error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Velocity Following Error Type      This parameter determines the action that is executed when the following error alarm is triggered. A following error alarm is triggered whenever the difference between the command velocity and feedback velocity of a Velocity mode axis exceeds the Velocity Following Error Stopped or Velocity Following Error Moving parameter, depending on whether the axis is currently executing a command or not.
    # Variable Name:   velocityFollowingErrorType
    # Type:            VelocityFollowingErrorAlarmType
    # Default Value:   NoAction
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.velocityFollowingErrorType  = Config_VelocityFollowingErrorAlarmType.NoAction
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set velocityFollowingErrorType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Servo Off During Amp Alarm     This parameter determines if a servo off signal should be sent to the servo when the servo reports an amplifier alarm. Many servos automatically turn off during amplifier alarms, even without receiving a servo off signal. Most users should keep this parameter at the default value.
    # Variable Name:   servoOffDuringAmpAlarm
    # Type:            bool
    # Default Value:   TRUE
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.servoOffDuringAmpAlarm  = True
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set servoOffDuringAmpAlarm error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Servo On Following Error       This parameter is a safety feature that prevents the servo from turning on if a servo on command is sent while the pulse unit difference in the command position and feedback position is greater than this value. If a servo on command is sent while the difference in the command position and feedback position is greater than this parameter, a following error alarm is triggered.
    # Variable Name:   servoOnFollowingError
    # Type:            int
    # Unit:            pulse
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Read the current values of parameters
    alarmParam = Config_AlarmParam()
    ret, alarmParam = Wmx3Lib_cm.config.GetAlarmParam(axis)
    alarmParam.servoOnFollowingError  = 10000
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetAlarmParam(axis, alarmParam)
    if (ret != 0):
        print('Set servoOnFollowingError error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

