#Set the Homing parameters for Axis 0. Set‘Home Type’to CurrentPos,‘Home Direction’to Positive,‘Homing Velocity Slow’to 10000,‘Homing Velocity Slow Acc’to 10000,‘Homing Velocity Slow Dec’to 10000,‘Homing Velocity Fast’to 10000,‘Homing Velocity Fast Acc’to 10000,‘Homing Velocity Fast Dec’to 10000,‘Homing Reverse Distance’to 0,‘Home Shift Velocity’to 10000,‘Home Shift Acc’to 10000,‘Home Shift Dec’to 10000,‘Home Shift Distance’to 0,‘Invert HS Polarity ’to FALSE,‘Multiple Z-Pulse’to 0,‘Round Pos Cmd After Homing’to FALSE,‘Pause Mode’to FALSE,‘Max HS On At Start Reverse Distance’to 0,‘Max LS Reverse Distance’to 0,‘Z-Pulse Distance Check ’to 0,‘Home Position’to 0,‘Gantry Homing Use Slave HS’to FALSE,‘Gantry Homing Use Slave LS’to FALSE,‘Gantry Homing Use Slave Z-Pulse’to FALSE,‘Gantry Homing Use Slave Touch Probe’to FALSE,‘Gantry Homing Use Slave Mechanical End’to FALSE,‘Gantry Homing Retain Sync Offset’to FALSE,‘Immediate Stop at LS’to FALSE,‘Mechanical End Detection Pos Diff ’to 0,‘Mechanical End Detection Time Milliseconds’to 0,‘Mechanical End Detection Ignore LS’to FALSE,‘Mechanical End Detection First Torque Limit’to 0,‘Mechanical End Detection Second Torque Limit’to 0,‘Open Loop Homing’to FALSE,‘Clear Home Done On Servo Off’to FALSE,‘Clear Home Done On Comm Stop’to True.
    # Axes = [0]

    # Example of Axis 0 Homing Parameters
    axis = 0
    # Home Type        The method of homing during a home operation. Each method is explained in detail in Homing.
    # Variable Name:   homeType
    # Type:            HomeType
    # Default Value:   CurrentPos
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeType = Config_HomeType.CurrentPos
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homeType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Home Direction  The direction to search for the home position during a home operation. This direction is the homing direction and the opposite direction is the reverse direction in the discussion in Homing.
    # Variable Name:   homeDirection
    # Type:            HomeDirection
    # Default Value:   Positive
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeDirection  = Config_HomeDirection.Positive
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homeDirection error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Velocity Slow    The "slow" homing velocity to use during a home operation. See Homing for information on when the "slow" homing velocity is used for each home type.
    # Variable Name:   homingVelocitySlow
    # Type:            double
    # Unit:            user unit / second
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingVelocitySlow  = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocitySlow error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Velocity Slow Acc    The acceleration to use when accelerating to the "slow" homing velocity. See Homing for information on when the "slow" homing velocity is used for each home type.
    # Variable Name:   homingVelocitySlowAcc
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingVelocitySlowAcc  = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocitySlowAcc error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Velocity Slow Dec    The acceleration to use when accelerating to the "slow" homing velocity. See Homing for information on when the "slow" homing velocity is used for each home type.
    # Variable Name:   homingVelocitySlowDec
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingVelocitySlowDec  = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocitySlowDec error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Velocity Fast     The "fast" homing velocity to use during a home operation. See Homing for information on when the "fast" homing velocity is used for each home type.
    # Variable Name:   homingVelocityFast
    # Type:            double
    # Unit:            user unit / second
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingVelocityFast   = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocitySlowDec error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Velocity Fast Acc     The acceleration to use when accelerating to the "fast" homing velocity. See Homing for information on when the "fast" homing velocity is used for each home type.
    # Variable Name:   homingVelocityFastAcc
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingVelocityFastAcc  = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocityFastAcc error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Velocity Fast Dec    The deceleration to use when decelerating from the "fast" homing velocity. See Homing for information on when the "fast" homing velocity is used for each home type.
    # Variable Name:   homingVelocityFastDec
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingVelocityFastDec  = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocityFastDec  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Homing Reverse Distance     The distance to continue reversing after clearing the home switch during a home operation. The home switch is cleared after the first home switch search of a HSHS or HSTouchProbe home operation.
    # Variable Name:   homingReverseDistance
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homingReverseDistance   = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingReverseDistance  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Home Shift Velocity     The velocity to use to move the axis to the home position after the home position is found. If the Home Shift Distance parameter is large, the home position may be far from the axis position when the home position is found. Even if the Home Shift Distance parameter is 0, the axis will still need to execute a home shift motion because the axis will not be exactly at the home position after it stops from the velocity it was at when searching for the home position.
    # Variable Name:   homeShiftVelocity
    # Type:            double
    # Unit:            user unit / second
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeShiftVelocity  = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homeShiftVelocity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Home Shift Acc     The acceleration to use when accelerating to the Home Shift Velocity.
    # Variable Name:   homeShiftAcc
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeShiftAcc = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homingVelocitySlowDec error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Home Shift Dec     The deceleration to use when decelerating from the Home Shift Velocity.
    # Variable Name:   homeShiftDec
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeShiftDec   = 10000
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homeShiftDec  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Home Shift Distance      The distance to shift the home position after it is found. A positive value indicates a shift in the direction of homing and a negative value indicates a shift in the reverse direction (the direction of homing is determined by the Home Direction parameter). The shifted home position becomes the actual home position.
    # Variable Name:   homeShiftDistance
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   -274877906943
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homeShiftDistance  = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homeShiftDistance error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Invert HS Polarity     If set to FALSE, the home switch will be active high. If set to TRUE, the home switch polarity will be inverted and become active low.
    # Variable Name:   invertHSPolarity
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.invertHSPolarity  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set invertHSPolarity error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Multiple Z-Pulse     For home types that search for the Z-pulse (index pulse), the number of Z-pulses to search for. If set to 0 or 1, the home position will be set to the position of the first Z-pulse that is found. If set to a value greater than 1, the home position will be set to the position after that many Z-pulses have been found.
    # Variable Name:   multipleZPulse
    # Type:            unsigned int
    # Minimum Value:   0
    # Maximum Value:   100
    # Default Value:   0
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.multipleZPulse  = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set multipleZPulse error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Round Pos Cmd After Homing     Whether to round the command position to the nearest whole number after homing. If set to FALSE, decimal user units of the command position will remain after homing. If set to TRUE, decimal user units of the command position will be rounded to the nearest whole number after homing. This does not change the home position; it will only adjust the command position (the same as if a position command to the rounded position is executed).
    # Variable Name:   roundPosCmdAfterHoming
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.roundPosCmdAfterHoming  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set roundPosCmdAfterHoming error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Pause Mode       Whether to pause the homing operation when the axis changes direction or momentarily stops during homing. While the homing operation is paused, the axis servo may be turned on or off without canceling the home operation. To continue the homing operation from the paused state, call the Continue function.
    # Variable Name:   pauseMode
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.pauseMode  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set pauseMode error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Max HS On At Start Reverse Distance      For home types that search for the home switch, if the home switch is already on when homing is started, the axis will move in the reverse homing direction to clear the home switch. This parameter determines the maximum distance that the axis can reverse to clear the home switch. If this distance is exceeded, the axis will stop and register a home error. If this parameter is set to 0, there is no limit to the reverse travel distance.
    # Variable Name:   maxHSOnAtStartReverseDistance
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.maxHSOnAtStartReverseDistance  = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set maxHSOnAtStartReverseDistance error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Max LS Reverse Distance      For home types that search for the home switch, if the limit switch is triggered while searching for the home switch or touch probe, the axis will reverse until the falling edge of the home switch is found. This parameter determines the maximum distance the axis can reverse to find the falling edge of the home switch. If this distance is exceeded, the axis will stop and register a home error. If this parameter is set to 0, there is no limit to the reverse travel distance.
    # Variable Name:   maxLSReverseDistance
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.maxLSReverseDistance   = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set maxLSReverseDistance  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Z-Pulse Distance Check     If set to a non-zero value, whenever a homing procedure that searches for multiple Z-pulses (index pulses) is executed, the distance between successive Z-pulses is checked. If the distance does not equal the distance specified in this parameter, a home error will be registered.
    # Variable Name:   zPulseDistanceCheck
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.zPulseDistanceCheck   = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set zPulseDistanceCheck  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Home Position    The command position at the home position. At the end of homing, the axis will be at the home position with a command position equal to this value. This effectively shifts the zero position. The difference between this parameter and the Home Shift Distance is that the axis does not move by the shift amount at the end of homing.
    # Variable Name:   homePosition
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   -274877906943
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.homePosition   = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set homePosition  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gantry Homing Use Slave HS      This parameter only affects gantry homing. If this parameter is set to TRUE, the homing procedure will search for the slave axis home switches in addition to the home switch of the master axis. If this parameter is set to FALSE, the homing procedure will only search for the master axis home switch.
    # Variable Name:   gantryHomingUseSlaveHS
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.gantryHomingUseSlaveHS   = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set gantryHomingUseSlaveHS  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gantry Homing Use Slave LS     This parameter only affects gantry homing. If this parameter is set to TRUE, the homing procedure will search for the slave axis limit switches in addition to the limit switch of the master axis. If this parameter is set to FALSE, the homing procedure will only search for the master axis limit switch.
    # Variable Name:   gantryHomingUseSlaveLS
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.gantryHomingUseSlaveLS  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set gantryHomingUseSlaveLS error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gantry Homing Use Slave Z-Pulse      This parameter only affects gantry homing. If this parameter is set to TRUE, the homing procedure will search for the slave axis Z-pulses (index pulses) in addition to the Z-pulse of the master axis. If this parameter is set to FALSE, the homing procedure will only search for the master axis Z-pulse.
    # Variable Name:   gantryHomingUseSlaveZPulse
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.gantryHomingUseSlaveZPulse   = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set gantryHomingUseSlaveZPulse  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gantry Homing Use Slave Touch Probe      This parameter only affects gantry homing. If this parameter is set to TRUE, the homing procedure will search for the slave axis touch probes in addition to the touch probe of the master axis. If this parameter is set to FALSE, the homing procedure will only search for the master axis touch probe.
    # Variable Name:   gantryHomingUseSlaveTouchProbe
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.gantryHomingUseSlaveTouchProbe  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set gantryHomingUseSlaveTouchProbe error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gantry Homing Use Slave Mechanical End      This parameter only affects gantry homing. If this parameter is set to TRUE, the homing procedure will search for the slave axis mechanical ends in addition to the mechanical end of the master axis. If this parameter is set to FALSE, the homing procedure will only search for the master axis mechanical end.
    # Variable Name:   gantryHomingUseSlaveMechanicalEnd
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.gantryHomingUseSlaveMechanicalEnd  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set gantryHomingUseSlaveMechanicalEnd error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Gantry Homing Retain Sync Offset      This parameter only affects gantry homing. If this parameter is set to TRUE, during the homing procedure, the sync offset between the master and slave is never broken. Depending on other parameters, the slave home positions may be searched, but they will be ignored after they are found, and the slave axes will follow the master axis to its home position instead.
    # Variable Name:   gantryHomingRetainSyncOffset
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.gantryHomingRetainSyncOffset   = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set gantryHomingRetainSyncOffset  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Immediate Stop at LS      If this parameter is set to TRUE, and the home type uses limit switches, the axis will immediately stop after detecting the limit switch, with infinite deceleration. No position command beyond the position where the limit switch was detected will be sent to the servo. This parameter is for servos that ignore position commands beyond the limit switch after the limit switch is detected. Enabling this parameter can reduce the time taken for the homing operation to complete, as no time is spent sending position commands that the servo will ignore anyway.
    # Variable Name:   immediateStopAtLS
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.immediateStopAtLS  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set immediateStopAtLS error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Mechanical End Detection Pos Diff      This parameter only affects mechanical end detection home types. When the axis presses against the mechanical end, the home position will be detected when the difference between the command position and feedback position exceeds this parameter for Mechanical End Detection Time Milliseconds.
    # Variable Name:   mechanicalEndDetectionPosDiff
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.mechanicalEndDetectionPosDiff  = 0
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set mechanicalEndDetectionPosDiff error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Mechanical End Detection Time Milliseconds      This parameter only affects mechanical end detection home types. The home position will be detected when the difference between the command position and feedback position exceeds the Mechanical End Detection Pos Diff for the amount of time specified in this parameter.
    # Variable Name:   mechanicalEndDetectionTimeMilliseconds
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.mechanicalEndDetectionTimeMilliseconds  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set mechanicalEndDetectionTimeMilliseconds error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Mechanical End Detection Ignore LS      This parameter only affects mechanical end detection home types, and it does not affect the MechanicalEndDetectionLS home type. When this parameter is set to TRUE, the limit switch in the direction of homing will be ignored if triggered. (Depending on the servo hardware and settings, the servo may still perform some action when the limit switch is triggered, such as generate an amp alarm.)
    # Variable Name:   mechanicalEndDetectionIgnoreLS
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.mechanicalEndDetectionIgnoreLS  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set mechanicalEndDetectionIgnoreLS error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Mechanical End Detection First Torque Limit       This parameter only affects mechanical end detection home types (MechanicalEndDetection, MechanicalEndDetectionHS, MechanicalEndDetectionLS, and MechanicalEndDetectionReverseZPulse).
    # Variable Name:   mechanicalEndDetectionFirstTorqueLimit
    # Type:            double
    # Unit:            %
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.mechanicalEndDetectionFirstTorqueLimit  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set mechanicalEndDetectionFirstTorqueLimit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Mechanical End Detection Second Torque Limit       This parameter only affects the MechanicalEndDetectionHS and MechanicalEndDetectionLS home types.
    # Variable Name:   mechanicalEndDetectionSecondTorqueLimit
    # Type:            double
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   274877906943
    # Default Value:   0
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.mechanicalEndDetectionSecondTorqueLimit  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set mechanicalEndDetectionSecondTorqueLimit error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Open Loop Homing      If set to FALSE, homing will be executed normally. If set to TRUE, the command position will be used instead of the feedback position to determine the home position. This parameter does not affect homing that uses the Z-pulse (index pulse) or touch probe, as these home types do not use the position feedback when determining the home position.
    # Variable Name:   openLoopHoming
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master/Slave
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.openLoopHoming  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set openLoopHoming error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Clear Home Done On Servo Off       If set to TRUE, the home done status will be cleared (set to 0) when the axis servo is in the servo off state. If set to FALSE, the home done status will not change when the axis servo is in the servo off state.
    # Variable Name:   clearHomeDoneOnServoOff
    # Type:            bool
    # Default Value:   FALSE
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.clearHomeDoneOnServoOff  = False
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set clearHomeDoneOnServoOff error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Clear Home Done On Comm Stop       If set to TRUE, the home done status will be cleared (set to 0) for all axes when the communication with the servo network is stopped. If set to FALSE, the home done status will not change when the communication with the servo network is stopped.
    # Variable Name:   clearHomeDoneOnCommStop
    # Type:            bool
    # Default Value:   True
    # Gantry Homing:   Master
    # Read the current values of parameters
    homeParam = Config_HomeParam()
    ret, homeParam = Wmx3Lib_cm.config.GetHomeParam(axis)
    homeParam.clearHomeDoneOnCommStop  = True
    # SetHomeParam -> First return value: Error code, Second return value: param error
    ret, homeParamError = Wmx3Lib_cm.config.SetHomeParam(axis, homeParam)
    if(ret!=0):
        print('Set clearHomeDoneOnCommStop error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

