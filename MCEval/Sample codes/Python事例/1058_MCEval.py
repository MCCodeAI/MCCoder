#Set the Axis parameters for Axis 0. Set‘Axis Command Mode’to Position,‘Gear Ratio Numerator’to 1,‘Gear Ratio Denominator’to 1,‘Single Turn Mode ’to FALSE,‘Single Turn Encoder Count’to 65536,‘Max Trq Limit’to 300,‘Negative Trq Limit ’to 300,‘Positive Trq Limit’to 300,‘Axis Unit’to 0,‘Axis Polarity’to 1,‘Max Motor Speed’to 3000,‘Absolute Encoder Mode’to FALSE,‘Absolute Encoder Home Offset’to 0,‘Encoder Range Mode’to FALSE,‘Encoder Range Low’to 0,‘Encoder Range High’to 0.
    # Axes = [0]

    # Example of Axis 0
    axis = 0
    # Axis Command Mode    The command mode of the axis. The available options are position (CSP), velocity (CSV), and torque (CST). The command mode determines whether the axis receives a position command, a velocity command, or a torque command every cycle.
    # Variable Name:   axisCommandMode
    # Type:            AxisCommandMode
    # Default Value:   Position
    # Set Function:    SetAxisCommandMode
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetAxisCommandMode(axis, AxisCommandMode.Position)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set axisParam  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gear Ratio Numerator     The minimum and maximum values of this parameter depends on the value of the Gear Ratio Denominator parameter. The ratio Gear Ratio Numerator / Gear Ratio Denominator must be equal to or greater than 0.000001 and equal to or less than 2147483647.
    # Variable Name:   gearRatioNumerator
    # Type:            double
    # Unit:            none
    # Minimum Value:   See Below
    # Maximum Value:   See Below
    # Default Value:   1
    # Set Function:    SetGearRatio
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetGearRatioNumerator(axis,1)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set gearRatioNumerator error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gear Ratio Denominator     The minimum and maximum values of this parameter depends on the value of the Gear Ratio Numerator parameter. The ratio Gear Ratio Numerator / Gear Ratio Denominator must be equal to or greater than 0.000001 and equal to or less than 2147483647.
    # Variable Name:   gearRatioDenominator
    # Type:            double
    # Unit:            none
    # Minimum Value:   See Below
    # Maximum Value:   See Below
    # Default Value:   1
    # Set Function:    SetGearRatio
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetGearRatioDenominator(axis,1)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set gearRatioDenominator error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Single Turn Mode      If this parameter is set to TRUE, this axis will be a single turn axis. A single turn axis only retains position information within a certain range, and if the axis moves out of this range, the position wraps around to the other end of the range. If this parameter is set to FALSE, the axis will be a normal axis.
    # Variable Name:   singleTurnMode
    # Type:            bool
    # Default Value:   FALSE
    # Set Function:    SetSingleTurn
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetSingleTurnMode(axis,False)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set gearRatioDenominator error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Single Turn Encoder Count     This parameter determines the wrap around range for axes with Single Turn Mode enabled. If the axis would move out of the range between 0 and this value, the axis position wraps around to the other end of this range.
    # Variable Name:   singleTurnEncoderCount
    # Type:            unsigned int
    # Unit:            pulse
    # Minimum Value:   256
    # Maximum Value:   2147483648
    # Default Value:   65536
    # Set Function:    SetSingleTurn
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetSingleTurnEncoderCount(axis,65536)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set singleTurnEncoderCount error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Max Trq Limit    The maximum torque that will be applied by the servo motor in either direction.This parameter requires the axis servo to support and be configured to receive the maximum torque limit input. Whether the axis is configured to receive maximum torque limit inputs can be checked from the Max Trq Limit Support status.
    # Variable Name:   maxTrqLimit
    # Type:            double
    # Unit:            %
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   300
    # Set Function:    SetMaxTrqLimit
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetMaxTrqLimit(axis,300)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set maxTrqLimit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Negative Trq Limit    The maximum torque that will be applied by the servo motor in the negative direction.This parameter requires the axis servo to support and be configured to receive the negative torque limit input. Whether the axis is configured to receive negative torque limit inputs can be checked from the Negative Trq Limit Support status.
    # Variable Name:   negativeTrqLimit
    # Type:            double
    # Unit:            %
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   300
    # Set Function:    SetNegativeTrqLimit
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetNegativeTrqLimit(axis,300)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set negativeTrqLimit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Positive Trq Limit    The maximum torque that will be applied by the servo motor in the positive  direction.This parameter requires the axis servo to support and be configured to receive the negative torque limit input. Whether the axis is configured to receive negative torque limit inputs can be checked from the Positive Trq Limit Support status.
    # Variable Name:   positiveTrqLimit
    # Type:            double
    # Unit:            %
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   300
    # Set Function:    SetPositiveTrqLimit
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetPositiveTrqLimit(axis,300)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set positiveTrqLimit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Axis Unit        The minimum unit of the command position, feedback position, command velocity, and feedback velocity. The Pos Cmd, Actual Pos, Velocity Cmd, and Actual Velocity statuses will be rounded to the nearest multiple of this value in the direction of zero.
    # Variable Name:   axisUnit
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   none
    # Default Value:   0
    # Set Function:    SetAxisUnit
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetAxisUnit (axis,0)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set axisUnit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Axis Polarity    If set to 1, the polarity of the axis will be normal. If set to -1, the polarity of the axis will be reversed, and motion in the positive direction will result in position commands in the negative direction to be sent to the axis servo.
    # Variable Name:   axisPolarity
    # Type:            char
    # Allowed Values:  1 (Normal), -1 (Reverse)
    # Default Value:   1
    # Set Function:    SetAxisPolarity
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetAxisPolarity(axis,1)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set axisPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Max Motor Speed  This parameter sets the maximum motor speed of an axis. The speed of the axis in either direction during all motions will be limited to this value.This parameter requires the axis servo to support and be configured to receive maximum motor speed inputs. Whether the axis is configured to receive maximum motor speed inputs can be checked from the Max Motor Speed Support status.
    # Variable Name:   maxMotorSpeed
    # Type:            double
    # Unit:            rpm
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   3000
    # Set Function:    SetMaxMotorSpeed
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetAxisPolarity(axis,1)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set axisPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Absolute Encoder Mode   This parameter sets the absolute encoder mode of an axis. If this parameter is set to enabled, the home offset specified by the Absolute Encoder Home Offset parameter will be applied. The Absolute Encoder Home Offset parameter will also be updated when the axis completes a homing function.
    # Variable Name:   absoluteEncoderMode
    # Type:            bool
    # Default Value:   FALSE
    # Set Function:    SetAbsoluteEncoderMode
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetAbsoluteEncoderMode (axis,False)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set absoluteEncoderMode error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Absolute Encoder Home Offset   This parameter stores the absolute encoder home offset (the offset used to determine the home position). This parameter has no effect while the Absolute Encoder Mode parameter is set to FALSE.If the Absolute Encoder Mode parameter is set to TRUE, this value will set the home offset of the axis.
    # Variable Name:   absoluteEncoderHomeOffset
    # Type:            double
    # Unit:            pulse
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Set Function:    SetAbsoluteEncoderHomeOffset
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetAbsoluteEncoderHomeOffset(axis,0)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set SetAbsoluteEncoderHomeOffset error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Encoder Range Mode   This parameter sets the encoder range mode.
    # Variable Name:   encoderRangeMode
    # Type:            bool
    # Default Value:   FALSE
    # Set Function:    SetEncoderRange
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetEncoderRangeMode(axis,False)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set encoderRangeMode error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Encoder Range Low   If the Encoder Range Mode parameter is set to TRUE, this parameter will specify the low end of the encoder range.This parameter can be set to a value between 0 and -(2^31).
    # Variable Name:   encoderRangeLow
    # Type:            int
    # Unit:            pulse
    # Minimum Value:   -2147483648
    # Maximum Value:   0
    # Default Value:   0
    # Set Function:    SetEncoderRange
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetEncoderRangeLow(axis,0)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set encoderRangeLow error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Encoder Range High   If the Encoder Range Mode parameter is set to TRUE, this parameter will specify the high end of the encoder range.This parameter can be set to a value between 0 and 2^31 - 1.
    # Variable Name:   encoderRangeHigh
    # Type:            int
    # Unit:            pulse
    # Minimum Value:   0
    # Maximum Value:   2147483647
    # Default Value:   0
    # Set Function:    SetEncoderRange
    # Read the current values of parameters
    axisParam = Config_AxisParam()
    ret, axisParam = Wmx3Lib_cm.config.GetAxisParam()
    axisParam.SetEncoderRangeHigh(axis,0)
    # axisParam -> First return value: Error code, Second return value: param error
    ret, axisParamError = Wmx3Lib_cm.config.SetAxisParam(axisParam)
    if (ret != 0):
        print('Set SetEncoderRange error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

