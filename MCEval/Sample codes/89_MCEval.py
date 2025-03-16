# Write Python code to set the Limit parameters for Axis 0. Set‘LS Type’to None,‘Positive LS Type’to None,‘Negative LS Type’to None,‘Invert Positive LS Polarity’to FALSE,‘Invert Negative LS Polarity’to FALSE,‘Near LS Type’to None,‘Near Positive LS Type’to None,‘Near Negative LS Type’to None,‘Near Positive LS Byte’to 0,‘Near Positive LS Bit’to 0,‘Invert Near Positive LS Polarity’to False,‘Near Negative LS Byte’to 0,‘Near Negative LS Bit’to 0,‘Invert Near Negative LS Polarity’to False,‘External LS Type’to None,‘External Positive LS Type’to None,‘External Negative LS Type’to None,‘External Positive LS Byte’to 0,‘Near Positive LS Bit’to 0,‘Invert External Positive LS Polarity’to False,‘External Positive LS Byte’to 0,‘External Negative LS Bit’to 0,‘Invert External Negative LS Polarity’to False,‘Soft Limit Type’to None,‘Positive Soft Limit Type’to None,‘Negative Soft Limit Type’to None,‘Soft Limit Positive Pos’to 0,‘Soft Limit Negative Pos’to 0,‘LS Dec’to 10000,‘LS Slow Dec’to 10000,‘All LS During Homing 'to 10000,‘LS Direction’to Normal.
    # Axes = [0]

    # Example of Axis 0
    axis = 0

    # LS Type          This parameter determines the action executed when the positive or negative limit switch is triggered.
    # Variable Name:   lsType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.lsType = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set lsType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Positive LS Type      This parameter determines the action executed when the positive limit switch is triggered and the LS Type parameter is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   positiveLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.positiveLSType = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set positiveLSType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Negative LS Type     This parameter determines the action executed when the negative limit switch is triggered and the LS Type parameter is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   negativeLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.negativeLSType = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set negativeLSType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert Positive LS Polarity      TRUE: The positive limit switch polarity will be inverted and become active low.FALSE: The positive limit switch polarity will be normal and be active high.
    # Variable Name:   invertPositiveLSPolarity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.invertPositiveLSPolarity  = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set invertPositiveLSPolarity  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert Negative LS Polarity      TRUE: The negative limit switch polarity will be inverted and become active low.FALSE: The negative limit switch polarity will be normal and be active high.
    # Variable Name:   invertNegativeLSPolarity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.invertNegativeLSPolarity   = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set invertNegativeLSPolarity   error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near LS Type     This parameter determines the action executed when the positive or negative near limit switch is triggered. The near limit switch is a software-based limit switch that can be mapped to any I/O input.If this parameter is set to None, the near limit switch will be disabled.
    # Variable Name:   nearLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearLSType   = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearLSType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Positive LS Type      This parameter determines the action executed when the positive near limit switch is triggered and the Near LS Type is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   nearPositiveLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearPositiveLSType    = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearPositiveLSType   error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Negative LS Type    This parameter determines the action executed when the negative near limit switch is triggered and the Near LS Type is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   nearNegativeLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearNegativeLSType   = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearPositiveLSType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Positive LS Byte    The byte address of the positive near limit switch I/O input.
    # Variable Name:   nearPositiveLSByte
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7999
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearPositiveLSByte  = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearPositiveLSByte error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Positive LS Bit     The bit address of the positive near limit switch I/O input.
    # Variable Name:   nearPositiveLSBit
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearPositiveLSBit = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearPositiveLSBit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert Near Positive LS Polarity    TRUE: The positive near limit switch polarity will be inverted and become active low.FALSE: The positive near limit switch polarity will be normal and be active high.
    # Variable Name:   invertNearPositiveLSPolarity
    # Type:            bool
    # Default Value:   False
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.invertNearPositiveLSPolarity = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set invertNearPositiveLSPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Negative LS Byte    The byte address of the Negative near limit switch I/O input.
    # Variable Name:   nearNegativeLSByte
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7999
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearNegativeLSByte = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearNegativeLSByte error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Negative LS Bit     The bit address of the Negative near limit switch I/O input.
    # Variable Name:   nearNegativeLSBit
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.nearNegativeLSBit = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set nearNegativeLSBit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert Near Negative LS Polarity    TRUE: The negative near limit switch polarity will be inverted and become active low.FALSE: The negative near limit switch polarity will be normal and be active high.
    # Variable Name:   invertNearNegativeLSPolarity
    # Type:            bool
    # Default Value:   False
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.invertNearNegativeLSPolarity = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set invertNearNegativeLSPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # External LS Type     This parameter determines the action executed when the positive or negative external limit switch is triggered. The external limit switch is a software-based limit switch that can be mapped to any I/O input. There is no difference between external limit switches and near limit switches, except that they use a different set of parameters.If this parameter is set to None, the external limit switch will be disabled.
    # Variable Name:   externalLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalLSType   = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalLSType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # External Positive LS Type     This parameter determines the action executed when the positive external limit switch is triggered and the External LS Type is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   externalPositiveLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalPositiveLSType  = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalPositiveLSType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # External Negative LS Type   This parameter determines the action executed when the negative external limit switch is triggered and the External LS Type is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   externalNegativeLSType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalNegativeLSType   = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalNegativeLSType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # External Positive LS Byte    The byte address of the positive external limit switch I/O input.
    # Variable Name:   externalPositiveLSByte
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7999
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalPositiveLSByte = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalPositiveLSByte error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Near Positive LS Bit     The bit address of the positive external limit switch I/O input.
    # Variable Name:   externalPositiveLSBit
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalPositiveLSBit  = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalPositiveLSBit  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert External Positive LS Polarity    TRUE: The positive external limit switch polarity will be inverted and become active low.FALSE: The positive external limit switch polarity will be normal and be active high.
    # Variable Name:   invertExternalPositiveLSPolarity
    # Type:            bool
    # Default Value:   False
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.invertExternalPositiveLSPolarity = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set invertExternalPositiveLSPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # External Negative LS Byte    The byte address of the negative external limit switch I/O input.
    # Variable Name:   externalNegativeLSByte
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7999
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalNegativeLSByte  = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalNegativeLSByte error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # External Negative LS Bit     The bit address of the negative external limit switch I/O input.
    # Variable Name:   externalNegativeLSBit
    # Type:            int
    # Minimum Value:   0
    # Maximum Value:   7
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.externalNegativeLSBit = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set externalNegativeLSBit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert External Negative LS Polarity    TRUE: The negative external limit switch polarity will be inverted and become active low.FALSE: The negative external limit switch polarity will be normal and be active high.
    # Variable Name:   invertExternalNegativeLSPolarity
    # Type:            bool
    # Default Value:   False
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.invertExternalNegativeLSPolarity = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set invertExternalNegativeLSPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Soft Limit Type   This parameter determines the action executed when the axis reaches the positive or negative software limit.
    # Variable Name:   softLimitType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.softLimitType  = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set softLimitType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Positive Soft Limit Type   This parameter determines the action executed when the axis reaches the positive software limit and the Soft Limit Type is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   positiveSoftLimitType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.positiveSoftLimitType  = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set positiveSoftLimitType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Negative Soft Limit Type   This parameter determines the action executed when the axis reaches the negative software limit and the Soft Limit Type is set to SeparatePositiveLSNegativeLS.
    # Variable Name:   negativeSoftLimitType
    # Type:            LimitSwitchType
    # Default Value:   None
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.negativeSoftLimitType  = Config_LimitSwitchType.PyNone
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set negativeSoftLimitType  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Soft Limit Positive Pos   The position at which the positive software limit will be triggered. If the axis command position exceeds this value in the positive direction, a software limit will be triggered.No software limit will be set for the positive direction if this parameter is set to 0.
    # Variable Name:   softLimitPositivePos
    # Type:            double
    # Uinit:           user unit
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.softLimitPositivePos  = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set softLimitPositivePos  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Soft Limit Negative Pos   The position at which the Negative software limit will be triggered. If the axis command position exceeds this value in the Negative direction, a software limit will be triggered.No software limit will be set for the Negative direction if this parameter is set to 0.
    # Variable Name:   softLimitNegativePos
    # Type:            double
    # Uinit:           user unit
    # Default Value:   0
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.softLimitNegativePos  = 0
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set softLimitNegativePos  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # LS Dec           The deceleration to stop the axis at when the limit switch is triggered. This parameter is applicable for the Dec and DecServoOff limit switch types.
    # Variable Name:   lsDec
    # Type:            double
    # Uinit:           user unit/second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.lsDec   = 10000
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set lsDec  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # LS Slow Dec      The deceleration to stop the axis at when the limit switch is triggered. This parameter is applicable for the SlowDec and SlowDecServoOff limit switch types. This parameter and the LS Dec parameter affect different limit switch types, but otherwise have the same functionality.
    # Variable Name:   lsSlowDec
    # Type:            double
    # Uinit:           user unit/second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.lsSlowDec   = 10000
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set lsSlowDec  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # All LS During Homing     TRUE: While homing, the positive limit switch can trigger while the axis is moving in the negative direction, and the negative limit switch can trigger while the axis is moving in the positive direction.FALSE:The positive limit switch will not trigger while the axis is moving in the negative direction, and the negative limit switch will not trigger while the axis is moving in the positive direction.
    # Variable Name:   allLSDuringHoming
    # Type:            bool
    # Default Value:   False
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.allLSDuringHoming = False
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set allLSDuringHoming error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # LS Direction     This parameter indicates whether the positive and negative limit switches are attached in the normal direction or the reverse direction.If this parameter is set to Normal, the positive limit switch should be attached in the positive direction of the axis and the negative limit switch should be attached in the negative direction of the axis. If this parameter is set to Reverse, the positive limit switch should be attached in the negative direction of the axis and the negative limit switch should be attached in the positive direction of the axis.
    # Variable Name:   lsDirection
    # Type:            LimitSwitchDirection
    # Default Value:   Normal
    # Read the current values of parameters
    limitParam = Config_LimitParam()
    ret, limitParam = Wmx3Lib_cm.config.GetLimitParam(axis)
    limitParam.lsDirection  = Config_LimitSwitchDirection.Normal
    # limitParam -> First return value: Error code, Second return value: param error
    ret, limitParamError = Wmx3Lib_cm.config.SetLimitParam(axis, limitParam)
    if (ret != 0):
        print('Set lsDirection  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

