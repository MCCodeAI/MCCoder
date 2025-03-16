# Write Python code to set the Motion parameters for Axis 0. Set‘Quick Stop Dec’to 100000,‘Prohibit Overtravel’to ChangeDeceleration,‘Linear Intpl Override Type’to FastBlending,‘Linear Intpl Override Smooth Percent’to 30,‘Circular Intpl Override Type’to FALSE,‘Interrupted Intpl Use Quick Stop’to FALSE,‘Single Turn Reduce To Half Turn’to TRUE,‘Enable Global Starting Velocity’to FALSE,‘Global Starting Velocity ’to 0,‘Enable Global End Velocity’to FALSE,‘Enable Global End Velocity’to FALSE,‘ Global End Velocity’to 0,‘Enable Global Min Velocity’to FALSE,‘Global Min Velocity’to 0,‘Enable Global Moving Average Profile Time Milliseconds’to FALSE,‘Global Moving Average Profile Time Milliseconds’to 0,‘API Wait Until Motion Start’to TRUE,‘Linear Intpl Profile Calc Mode’to AxisLimit,
    # Axes = [0]

    # Example of Axis 0 Homing Parameters
    axis = 0

    # Quick Stop Dec   This parameter indicates whether the positive and negative limit switches are attached in the normal direction or the reverse direction.If this parameter is set to Normal, the positive limit switch should be attached in the positive direction of the axis and the negative limit switch should be attached in the negative direction of the axis. If this parameter is set to Reverse, the positive limit switch should be attached in the negative direction of the axis and the negative limit switch should be attached in the positive direction of the axis.
    # Variable Name:   quickStopDec
    # Type:            double
    # Unit:            user unit/second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   100000
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.quickStopDec = 100000
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set quickStopDec  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Prohibit Overtravel    This parameter determines whether an axis is allowed to overtravel beyond the target position, reverse direction, and move back to the target position if a profile could not be generated otherwise. For example, the axis may overtravel if an override is executed while the axis is at a high enough velocity such that it cannot decelerate to zero velocity before reaching the target position.
    # Variable Name:   prohibitOvertravel
    # Type:            ProhibitOvertravelType
    # Default Value:   ChangeDeceleration
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.prohibitOvertravel = Config_ProhibitOvertravelType.ChangeDeceleration
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set prohibitOvertravel  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Linear Intpl Override Type    This parameter determines the method by which a linear interpolation override is executed.When executing a linear interpolation override, the value of this parameter for the first axis of the override linear interpolation is applied.
    # Variable Name:   linearIntplOverrideType
    # Type:            LinearIntplOverrideType
    # Default Value:   FastBlending
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.linearIntplOverrideType = Config_LinearIntplOverrideType.FastBlending
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set linearIntplOverrideType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Linear Intpl Override Smooth Percent    This parameter determines the amount of smoothing to apply during linear interpolation overrides, as a percentage of the travel distance of the override linear interpolation.This parameter only has an effect if the Linear Intpl Override Type parameter is set to Smoothing.
    # Variable Name:   linearIntplOverrideSmoothPercent
    # Type:            unsigned int
    # Unit:            %
    # Minimum Value:   0
    # Maximum Value:   100
    # Default Value:   30
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.linearIntplOverrideSmoothPercent = 30
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set linearIntplOverrideSmoothPercent  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Circular Intpl Override Type    This parameter determines the method by which a circular interpolation override is executed. When executing a circular interpolation override, the value of this parameter for the first axis of the override circular interpolation is applied.
    # Variable Name:   circularIntplOverrideType
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.circularIntplOverrideType = Config_CircularIntplOverrideType.FastBlending
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set interruptedIntplUseQuickStop error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Interrupted Intpl Use Quick Stop     If an interpolation command is interrupted (one of the interpolating axes triggers a limit switch, reaches the software limit, generates an amp alarm, etc.), all interpolating axes will decelerate to a stop. For axes with this parameter set to FALSE, the axes will decelerate along the original interpolated path, retaining the composite deceleration of the original interpolation command. For axes with this parameter set to TRUE, the axes will decelerate independently at the deceleration of the Quick Stop Dec parameter.
    # Variable Name:   interruptedIntplUseQuickStop
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.interruptedIntplUseQuickStop = False
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set interruptedIntplUseQuickStop error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Single Turn Reduce To Half Turn    This parameter determines the method by which a circular interpolation override is executed. When executing a circular interpolation override, the value of this parameter for the first axis of the override circular interpolation is applied.
    # Variable Name:   singleTurnReduceToHalfTurn
    # Type:            bool
    # Default Value:   TRUE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.singleTurnReduceToHalfTurn = True
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set singleTurnReduceToHalfTurn  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable Global Starting Velocity   TRUE: The value specified in Starting Velocity for the motion commands of this axis will be ignored and overwritten by the value of the Global Starting Velocity parameter.FALSE: Starting Velocity is specified normally.
    # Variable Name:   enableGlobalStartingVelocity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.enableGlobalStartingVelocity = False
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set enableGlobalStartingVelocity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Global Starting Velocity    If Enable Global Starting Velocity is TRUE, the value set for this parameter will overwrite the Starting Velocity used by this axis during motion.
    # Variable Name:   globalStartingVelocity
    # Type:            double
    # Unit:            user unit / second
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.globalStartingVelocity = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set globalStartingVelocity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable Global End Velocity    TRUE: The value specified in End Velocity for the motion commands of this axis will be ignored and overwritten by the value of the Global End Velocity parameter.FALSE: End Velocity is specified normally.
    # Variable Name:   enableGlobalEndVelocity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.enableGlobalEndVelocity  = False
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set enableGlobalEndVelocity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable Global End Velocity    TRUE: The value specified in End Velocity for the motion commands of this axis will be ignored and overwritten by the value of the Global End Velocity parameter.FALSE: End Velocity is specified normally.
    # Variable Name:   enableGlobalEndVelocity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.enableGlobalEndVelocity  = False
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set enableGlobalEndVelocity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Global End Velocity     If Enable Global End Velocity is TRUE, the value set for this parameter will overwrite the End Velocity used by this axis during motion.
    # Variable Name:   globalEndVelocity
    # Type:            double
    # Unit:            user unit / second
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.globalEndVelocity  = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set globalEndVelocity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable Global Min Velocity    TRUE: The value specified to the Global Min Velocity parameter will set a minimum velocity at which the axis moves at during motion commands. The axis will never move at a velocity below the minimum velocity, regardless of the values set for Velocity, Starting Velocity, and End Velocity.
    # Variable Name:   enableGlobalMinVelocity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.enableGlobalMinVelocity  = False
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set enableGlobalMinVelocity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Global Min Velocity     TRUE: The value specified in End Velocity for the motion commands of this axis will be ignored and overwritten by the value of the Global End Velocity parameter.FALSE: End Velocity is specified normally.
    # Variable Name:   globalMinVelocity
    # Type:            double
    # Unit:            user unit / second
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.globalMinVelocity   = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set globalMinVelocity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable Global Moving Average Profile Time Milliseconds     TRUE: The value specified in Moving Average Time Milliseconds for the motion commands of this axis will be ignored and overwritten by the value of the Global Moving Average Profile Time Milliseconds parameter.FALSE: Moving Average Time Milliseconds is specified normally.
    # Variable Name:   enableGlobalMovingAverageProfileTimeMilliseconds
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.enableGlobalMovingAverageProfileTimeMilliseconds   = False
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set enableGlobalMovingAverageProfileTimeMilliseconds  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Global Moving Average Profile Time Milliseconds     TRUE: The value specified in End Velocity for the motion commands of this axis will be ignored and overwritten by the value of the Global End Velocity parameter.FALSE: End Velocity is specified normally.
    # Variable Name:   globalMovingAverageProfileTimeMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Minimum Value:   0
    # Maximum Value:   120000
    # Default Value:   0
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.globalMovingAverageProfileTimeMilliseconds   = 0
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set globalMovingAverageProfileTimeMilliseconds  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # API Wait Until Motion Start      TRUE: Motion API functions will wait until the motion has started before returning execution to the calling thread.FALSE: Motion API functions will return immediately, before the motion is actually started by the engine.
    # Variable Name:   apiWaitUntilMotionStart
    # Type:            bool
    # Default Value:   TRUE
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.apiWaitUntilMotionStart = True
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set apiWaitUntilMotionStart  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Linear Intpl Profile Calc Mode      This parameter will determine the method in which the profile parameters for the linear interpolation are calculated from the profile parameters specified for each interpolating axis.
    # Variable Name:   linearIntplProfileCalcMode
    # Type:            LinearIntplProfileCalcMode
    # Default Value:   AxisLimit
    # Read the current values of parameters
    motionParam = Config_MotionParam()
    ret, motionParam = Wmx3Lib_cm.config.GetMotionParam(axis)
    motionParam.linearIntplProfileCalcMode  = Config_LinearIntplProfileCalcMode.AxisLimit
    # motionParam -> First return value: Error code, Second return value: param error
    ret, motionParamError = Wmx3Lib_cm.config.SetMotionParam(axis, motionParam)
    if (ret != 0):
        print('Set linearIntplProfileCalcMode   error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

