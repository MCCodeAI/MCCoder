#Set the Emergency Stop parameters for Axis 0. Set‘E-Stop Dec’to 100000,‘Enable E-Stop Signal’to FALSE,‘E-Stop Signal Source’to Input,‘E-Stop Signal Level’to Level1,‘Invert E-Stop Signal Polarity’to FALSE,‘E-Stop Signal Byte Address’to 0,‘E-Stop Signal Bit Address’to 0,‘Enable E-Stop Status Signal’to FALSE,‘E-Stop Status Signal Destination’to FALSE,‘Invert E-Stop Status Signal Polarity’to FALSE,‘E-Stop Status Signal Byte Address’to 0,‘E-Stop Status Signal Bit Address’to 0,‘E-Stop Level 1 Type’to Dec.
    # Axes = [0]

    # Example of Axis 0
    axis = 0
    # E-Stop Dec       The deceleration to stop the axis at when the axis is stopped using E-Stop (emergency stop) with with an EStopLevel of Level1.
    # Variable Name:   eStopDec
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   100000
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.SetEStopDec(axis, 100000)
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam( emergencyStopParam)
    if (ret != 0):
        print('Set emergencyStopParam  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable E-Stop Signal       Set to TRUE to assign an input, output, or user memory bit to trigger and release the E-Stop (emergency stop).When the assigned signal bit is set high, an emergency stop will be triggered, and when it is set low, the emergency stop will be released.An emergency stop can still be triggered by other methods (such as the ExecEStop function or the ExecEStop event) regardless of the value of this parameter.
    # Variable Name:   enableEStopSignal
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.enableEStopSignal =False
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set enableEStopSignal error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Signal Source      The source (input, output, or user memory) of the emergency stop signal. This parameter has no effect if the Enable E-Stop Signal parameter is set to FALSE.If this parameter is set to Input, an I/O input bit will trigger the emergency stop.If this parameter is set to Output, an I/O output bit will trigger the emergency stop.
    # Variable Name:   eStopSignalSource
    # Type:            EStopSignalSource
    # Default Value:   Input
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopSignalSource = Config_EStopSignalSource.Input
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopSignalSource error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Signal Level       The level of the emergency stop that is triggered by the emergency stop signal. This parameter has no effect if the Enable E-Stop Signal parameter is set to FALSE.
    # Variable Name:   eStopSignalLevel
    # Type:            EStopLevel
    # Default Value:   Level1
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopSignalLevel = EStopLevel.Level1
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopSignalLevel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert E-Stop Signal Polarity       If set to TRUE, the emergency stop signal polarity will be inverted so that the emergency stop is triggered when the signal is low and released when the signal is high. This parameter has no effect if the Enable E-Stop Signal parameter is set to FALSE.
    # Variable Name:   invertEStopSignalPolarity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.invertEStopSignalPolarity  = False
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set invertEStopSignalPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Signal Byte Address      The maximum value for this parameter depends on the value of the E-Stop Signal Source parameter, and is summarized in the following table:The byte address of the emergency stop signal. This parameter has no effect if the Enable E-Stop Signal parameter is set to FALSE.
    # Variable Name:   eStopSignalByteAddress
    # Type:            unsigned int
    # Minimum Value:   0
    # Maximum Value:   See Below
    # Default Value:   0
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopSignalByteAddress  = 0
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set invertEStopSignalPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Signal Bit Address      The bit address of the emergency stop signal. This parameter has no effect if the Enable E-Stop Signal parameter is set to FALSE.
    # Variable Name:   eStopSignalBitAddress
    # Type:            unsigned char
    # Minimum Value:   0
    # Maximum Value:   7
    # Default Value:   0
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopSignalBitAddress   = 0
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopSignalBitAddress  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Enable E-Stop Status Signal       Set to TRUE to assign an output or user memory bit to show the triggered state of the E-Stop (emergency stop).The assigned signal bit will be set to high while the emergency stop has been triggered and low while the emergency stop is released. This signal bit will contain the same value as the Emergency Stop status.
    # Variable Name:   enableEStopStatusSignal
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.enableEStopStatusSignal   = False
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set enableEStopStatusSignal  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Status Signal Destination       The bit address of the emergency stop signal. This parameter has no effect if the Enable E-Stop Signal parameter is set to FALSE.
    # Variable Name:   eStopStatusSignalDestination
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopStatusSignalDestination = Config_EStopStatusSignalDestination.Output
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopStatusSignalDestination  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert E-Stop Status Signal Polarity     If set to TRUE, the emergency stop status signal polarity will be inverted so that the signal is low while the emergency stop is triggered and high while the emergency stop is released. This parameter has no effect if the Enable E-Stop Status Signal parameter is set to FALSE.
    # Variable Name:   invertEStopStatusSignalPolarity
    # Type:            bool
    # Default Value:   FALSE
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.invertEStopStatusSignalPolarity  = False
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set invertEStopStatusSignalPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Status Signal Byte Address      The maximum value for this parameter depends on the value of the E-Stop Status Signal Destination parameter, and is summarized in the following table:The byte address of the emergency stop status signal. This parameter has no effect if the Enable E-Stop Status Signal parameter is set to FALSE.
    # Variable Name:   eStopStatusSignalByteAddress
    # Type:            unsigned int
    # Minimum Value:   0
    # Maximum Value:   See Below
    # Default Value:   0
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopStatusSignalByteAddress  = 0
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopStatusSignalByteAddress error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Status Signal Bit Address      The bit address of the emergency stop status signal. This parameter has no effect if the Enable E-Stop Status Signal parameter is set to FALSE.
    # Variable Name:   eStopStatusSignalBitAddress
    # Type:            unsigned int
    # Minimum Value:   0
    # Maximum Value:   7
    # Default Value:   0
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopStatusSignalBitAddress = 0
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopStatusSignalBitAddress  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # E-Stop Level 1 Type      The action to take when a Level1 E-Stop (emergency stop) is triggered. This parameter affects all Level1 emergency stops, whether it was triggered by the ExecEStop function, the ExecEStop event, or the emergency stop signal set with Enable E-Stop Signal.
    # Variable Name:   eStopLevel1Type
    # Type:            EStopLevel1Type
    # Default Value:   Dec
    # Read the current values of parameters
    emergencyStopParam = Config_EmergencyStopParam()
    ret, emergencyStopParam = Wmx3Lib_cm.config.GetEmergencyStopParam()
    emergencyStopParam.eStopLevel1Type  = Config_EStopLevel1Type.Dec
    # emergencyStopParam -> First return value: Error code, Second return value: param error
    ret, emergencyStopParamError = Wmx3Lib_cm.config.SetEmergencyStopParam(emergencyStopParam)
    if (ret != 0):
        print('Set eStopLevel1Type  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

