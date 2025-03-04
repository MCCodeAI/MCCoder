#Get the Axis statuses for Axis 0.

    # Axes = [0]


    # Example of Axis 0 Status
    axis = 0
    # Servo On      TRUE: The axis servo is on. FALSE: The axis servo is off.
    # Variable Name:   servoOn
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Servo On : ' + str(CmStatus.GetAxesStatus(axis).servoOn))

    # Servo Offline     TRUE: The axis is offline. The axis servo could not be found in the network, or the axis is not in operational state. FALSE: The axis is online.
    # Variable Name:   servoOffline
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Servo Offline : ' + str(CmStatus.GetAxesStatus(axis).servoOffline))

    # Amp Alarm     TRUE: The axis encountered an amp alarm. FALSE: The axis has no amp alarm.
    # Variable Name:   ampAlarm
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Amp Alarm : ' + str(CmStatus.GetAxesStatus(axis).ampAlarm))

    # Amp Alarm Code        The amp alarm code, if the axis has an amp alarm (if Amp Alarm is TRUE).
    # Variable Name:   ampAlarmCode
    # Type:            int
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Amp Alarm Code : ' + str(CmStatus.GetAxesStatus(axis).ampAlarmCode))

    # Master Axis       If this axis is a synchronous control slave axis, this status contains the master axis. Otherwise, this status contains -1.
    # Variable Name:   masterAxis
    # Type:            int
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Master Axis : ' + str(CmStatus.GetAxesStatus(axis).masterAxis))

    # Second Master Axis        If this axis is a combine sync control slave axis, this status contains the second master axis. Otherwise, this status contains -1.
    # Variable Name:   secondMasterAxis
    # Type:            int
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Second Master Axis : ' + str(CmStatus.GetAxesStatus(axis).secondMasterAxis))

    # Pos Cmd       The command position of the axis. For axes in Position Axis Command Mode, the command position is set cyclically by motion commands the axis is executing. For axes in Velocity or Torque Axis Command Mode, the command position is set equal to Actual Pos every cycle (this prevents the axis from moving suddenly when its mode is changed to Position).
    # Variable Name:   posCmd
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Pos Cmd : ' + str(CmStatus.GetAxesStatus(axis).posCmd))

    # Actual Pos        The feedback position of the axis. For this status to return a value, the servo must be configured to return position feedback data. Whether the servo is correctly configured to return position feedback data can be checked with the Pos Feedback Support status.
    # Variable Name:   actualPos
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Actual Pos : ' + str(CmStatus.GetAxesStatus(axis).actualPos))

    # Comp Pos Cmd      The command position of the axis after applying compensation offsets.
    # Variable Name:   compPosCmd
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Comp Pos Cmd : ' + str(CmStatus.GetAxesStatus(axis).compPosCmd))

    # Comp Actual Pos       The feedback position of the axis after applying compensation offsets.
    # Variable Name:   compActualPos
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Comp Actual Pos : ' + str(CmStatus.GetAxesStatus(axis).compActualPos))

    # Sync Pos Cmd      If this axis is a synchronous control slave axis, this status contains the command position after sync offsets are applied. This will shift the slave command position to have the same coordinates as the master axis. This value will normally contain the same value as the master axis command position. If this axis is not a synchronous control slave axis, this status contains the same value as the command position.
    # Variable Name:   syncPosCmd
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Sync Pos Cmd : ' + str(CmStatus.GetAxesStatus(axis).syncPosCmd))

    # Sync Actual Pos       If this axis is a synchronous control slave axis, this status contains the feedback position after sync offsets are applied. This will shift the slave feedback position to have the same coordinates as the master axis. If synchronization is perfect, this value will contain the same value as the master axis feedback position. If this axis is not a synchronous control slave axis, this status contains the same value as the feedback position.
    # Variable Name:   syncActualPos
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Sync Actual Pos : ' + str(CmStatus.GetAxesStatus(axis).syncActualPos))

    # Encoder Command       The 32-bit integer command position that is sent to the servo. This command position is the final position command that is sent to the servo, after modifying the command position by the compensation, home offsets, and sync offsets.
    # Variable Name:   encoderCommand
    # Type:            int
    # Unit:            pulse
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Encoder Command : ' + str(CmStatus.GetAxesStatus(axis).encoderCommand))

    # Encoder Feedback      The 32-bit integer feedback position that is received from the servo. This feedback position is the actual position of the servo, without accounting for compensation, home offests, and sync offsets.
    # Variable Name:   encoderFeedback
    # Type:            int
    # Unit:            pulse
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Encoder Feedback : ' + str(CmStatus.GetAxesStatus(axis).encoderFeedback))

    # Accumulated Encoder Feedback      A 64-bit signed integer that contains the accumulated value of the encoder feedback since starting the engine. The difference in the value of the 32-bit Encoder Feedback is calculated every cycle and added to this accumulated sum. Once the accumulated feedback reaches 2^63 - 1 or -(2^63), it will stop increasing beyond that position. This represents the upper and lower limits of the feedback position that can be calculated for a linear axis (for Single Turn axes, this value will loop back at Single Turn Encoder Count intervals, so there is no limit).
    # Variable Name:   accumulatedEncoderFeedback
    # Type:            long long
    # Unit:            pulse
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Accumulated Encoder Feedback : ' + str(CmStatus.GetAxesStatus(axis).accumulatedEncoderFeedback))

    # Velocity Cmd      The command velocity of the axis. For axes in Velocity mode, the command velocity is set cyclically by velocity commands the axis is executing. For axes in Position mode, this status returns the instantaneous velocity calculated from the position commands of this cycle and the previous cycle.
    # Variable Name:   velocityCmd
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Velocity Cmd : ' + str(CmStatus.GetAxesStatus(axis).velocityCmd))

    # Actual Velocity       The feedback velocity of the axis. If the servo is not configured to return velocity feedback data (if the Velocity Feedback Support status is FALSE), or if the Velocity Monitor Source parameter is set to CalculateFromPositionFeedback, this status will contain a velocity calculated from the feedback position over several cycles. Otherwise, this status will contain the feedback velocity from the servo drive.
    # Variable Name:   actualVelocity
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Actual Velocity : ' + str(CmStatus.GetAxesStatus(axis).actualVelocity))

    # Velocity Lag      The difference between the command velocity and the feedback velocity. If the servo is not configured to return velocity feedback data (if the Velocity Feedback Support status is FALSE), or if the Velocity Monitor Source parameter is set to CalculateFromPositionFeedback, a velocity calculated from the feedback position is used in place of the feedback velocity from the servo drive to calculate the velocity lag.
    # Variable Name:   velocityLag
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Velocity Lag : ' + str(CmStatus.GetAxesStatus(axis).velocityLag))

    # Torque Cmd        The command torque of the axis. For axes in Torque mode, the command torque is set cyclically by torque commands the axis is executing.
    # Variable Name:   torqueCmd
    # Type:            double
    # Unit:            %
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Torque Cmd : ' + str(CmStatus.GetAxesStatus(axis).torqueCmd))

    # Actual Torque     The feedback torque of the axis. For this status to return a value, the servo must be configured to return torque feedback data. Whether the servo is correctly configured to return torque feedback data can be checked with the Trq Feedback Support status.
    # Variable Name:   actualTorque
    # Type:            double
    # Unit:            %
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Actual Torque : ' + str(CmStatus.GetAxesStatus(axis).actualTorque))

    # Actual Following Error        Feedback following error in pulses. For this status to return a value, the servo must be configured to return following error data.
    # Variable Name:   actualFollowingError
    # Type:            double
    # Unit:            pulse
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Actual Following Error : ' + str(CmStatus.GetAxesStatus(axis).actualFollowingError))

    # Compensation / Pitch Error Compensation       The compensation offset currently applied by the pitch error compensation function.
    # Variable Name:   pitchErrorCompensation
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Compensation / Pitch Error Compensation : ' + str(CmStatus.GetAxesStatus(axis).compensation.pitchErrorCompensation))

    # Compensation / Pitch Error Compensation 2D        The compensation offset currently applied by the two-dimensional pitch error compensation function.
    # Variable Name:   pitchErrorCompensation2D
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Compensation / Pitch Error Compensation 2D : ' + str(CmStatus.GetAxesStatus(axis).compensation.pitchErrorCompensation2D))

    # Compensation / Backlash Compensation      The compensation offset currently applied by the backlash compensation function.
    # Variable Name:   backlashCompensation
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    tempCompensation = CmStatus.GetAxesStatus(axis).compensation
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Compensation / Backlash Compensation : ' + str(CmStatus.GetAxesStatus(axis).compensation.backlashCompensation))

    # Compensation / Total Pos Compensation     The total position compensation offset applied by all compensation functions.
    # Variable Name:   totalPosCompensation
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Compensation / Total Pos Compensation : ' + str(CmStatus.GetAxesStatus(axis).compensation.totalPosCompensation))

    # Axis Supported Function / Pos Feedback Support        TRUE: The axis returns position feedback data every cycle. The position feedback data is stored in the Actual Pos status. FALSE: The axis does not return position feedback data every cycle.
    # Variable Name:   posFeedbackSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Pos Feedback Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.posFeedbackSupport))

    # Axis Supported Function / Pos Command Support     TRUE: The axis supports receiving position command data every cycle. The Axis Command Mode must be set to Position to execute position command data. FALSE: The axis does not support receiving position command data every cycle.
    # Variable Name:   posCommandSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Pos Command Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.posCommandSupport))

    # Axis Supported Function / Velocity Feedback Support       TRUE: The axis returns velocity feedback data every cycle. The velocity feedback data is stored in the Actual Velocity status. FALSE: The axis does not return velocity feedback data every cycle.
    # Variable Name:   velocityFeedbackSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Velocity Feedback Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.velocityFeedbackSupport))

    # Axis Supported Function / Velocity Command Support        TRUE: The axis supports receiving velocity command data every cycle. The Axis Command Mode must be set to Velocity to execute velocity command data. FALSE: The axis does not support receiving velocity command data every cycle.
    # Variable Name:   velocityCommandSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Velocity Command Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.velocityCommandSupport))

    # Axis Supported Function / Velocity Offset Support     TRUE: The axis supports receiving velocity offset data every cycle. The velocity offset data is generated for sync slave axes with the Sync Compensation Mode parameter set to VelocityOffset or SymmetricVelocityOffset and sync master axes with the Sync Compensation Mode parameter of the slave axis set to SymmetricVelocityOffset. FALSE: The axis does not support receiving velocity offset data every cycle.
    # Variable Name:   velocityOffsetSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Velocity Offset Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.velocityOffsetSupport))

    # Axis Supported Function / Trq Feedback Support        TRUE: The axis returns torque feedback data every cycle. The torque feedback data is stored in the Actual Torque status. FALSE: The axis does not return torque feedback data every cycle.
    # Variable Name:   trqFeedbackSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Trq Feedback Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.trqFeedbackSupport))

    # Axis Supported Function / Trq Command Support     TRUE: The axis supports receiving torque command data every cycle. The Axis Command Mode must be set to Torque to execute torque command data. FALSE: The axis does not support receiving torque command data every cycle.
    # Variable Name:   trqCommandSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Trq Command Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.trqCommandSupport))

    # Axis Supported Function / Max Trq Limit Support       TRUE: The axis supports receiving maximum torque limit data every cycle. The maximum torque limit is set by the Max Trq Limit parameter. FALSE: The axis does not support receiving maximum torque limit data every cycle.
    # Variable Name:   maxTrqLimitSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Max Trq Limit Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.maxTrqLimitSupport))

    # Axis Supported Function / Positive Trq Limit Support      TRUE: The axis supports receiving positive torque limit data every cycle. The positive torque limit is set by the Positive Trq Limit parameter. FALSE: The axis does not support receiving positive torque limit data every cycle.
    # Variable Name:   positiveTrqLimitSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Positive Trq Limit Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.positiveTrqLimitSupport))

    # Axis Supported Function / Negative Trq Limit Support      TRUE: The axis supports receiving negative torque limit data every cycle. The negative torque limit is set by the Negative Trq Limit parameter. FALSE: The axis does not support receiving negative torque limit data every cycle.
    # Variable Name:   negativeTrqLimitSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Negative Trq Limit Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.negativeTrqLimitSupport))

    # Axis Supported Function / Max Motor Speed Support     TRUE: The axis supports receiving maximum motor speed data every cycle. The maximum motor speed is set by the Max Motor Speed parameter. FALSE: The axis does not support receiving maximum motor speed data every cycle.
    # Variable Name:   maxMotorSpeedSupport
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Supported Function / Max Motor Speed Support : ' + str(CmStatus.GetAxesStatus(axis).axisSupportedFunction.maxMotorSpeedSupport))

    # Op State      The operation state of the axis. The operation state shows the type of motion command that the axis is currently executing.
    # Variable Name:   opState
    # Type:            OperationState::T
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Op State : ' + str(CmStatus.GetAxesStatus(axis).opState))

    # Detail Op State       The detailed operation state of the axis. This status is similar to the Op State status, except the states are subdivided into more specific states.
    # Variable Name:   detailOpState
    # Type:            DetailOperationState::T
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Detail Op State : ' + str(CmStatus.GetAxesStatus(axis).detailOpState))

    # Axis Command Mode     The command mode of the axis. The command mode determines whether the axis is executing cyclic position commands, cyclic velocity commands, or cyclic torque commands. This status equals the value set by the Axis Command Mode parameter.
    # Variable Name:   axisCommandMode
    # Type:            AxisCommandMode::T
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Command Mode : ' + str(CmStatus.GetAxesStatus(axis).axisCommandMode))

    # Axis Command Mode Feedback        The feedback from the servo of the current command mode of the axis. When the command mode is changed, the servo may take a few cycles to switch to the new command mode. This status returns the old command mode until the switch is complete.
    # Variable Name:   axisCommandModeFeedback
    # Type:            AxisCommandMode::T
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Command Mode Feedback : ' + str(CmStatus.GetAxesStatus(axis).axisCommandModeFeedback))

    # Axis Sync Mode        The sync control mode of the axis. If the axis is not a synchronous control slave axis, the sync control mode is NoSync. If the axis is a sync slave, the sync control mode depends on the Sync Compensation Mode of the axis and whether the axis has Velocity Offset Support.
    # Variable Name:   axisSyncMode
    # Type:            AxisSyncMode::T
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Axis Sync Mode : ' + str(CmStatus.GetAxesStatus(axis).axisSyncMode))

    # Sync Offset       If the axis is a synchronous control slave axis, this status contains the sync offset between the master axis and the slave axis. The sync offset is calculated when synchronous control is started as the difference between the master axis and slave axis command positions. If useMasterFeedback is set, the master feedback position is used instead of the master command position for calculating the sync offset.
    # Variable Name:   syncOffset
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Sync Offset : ' + str(CmStatus.GetAxesStatus(axis).syncOffset))

    # Sync Phase Offset     If the axis is a synchronous control slave axis, this status contains the phase offset between the master axis and the slave axis. The phase offset can be modified with functions such as SetAbsoluteSyncPhase and AddRelativeSyncPhase.
    # Variable Name:   syncPhaseOffset
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Sync Phase Offset : ' + str(CmStatus.GetAxesStatus(axis).syncPhaseOffset))

    # Sync Gear Ratio       If the axis is a synchronous control slave axis, this status contains the sync gear ratio between the master axis and the slave axis. The sync gear ratio can be modified with functions such as SetSyncGearRatio.
    # Variable Name:   syncGearRatio
    # Type:            double
    # Unit:            none (ratio)
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Sync Gear Ratio : ' + str(CmStatus.GetAxesStatus(axis).syncGearRatio))

    # Profile Total Milliseconds        The total time the current motion profile will take to complete. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileTotalMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Total Milliseconds : ' + str(CmStatus.GetAxesStatus(axis).profileTotalMilliseconds))

    # Profile Acc Milliseconds      The total time the current motion profile will spend accelerating. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileAccMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Acc Milliseconds : ' + str(CmStatus.GetAxesStatus(axis).profileAccMilliseconds))

    # Profile Cruise Milliseconds       The total time the current motion profile will spend at a constant velocity. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileCruiseMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Cruise Milliseconds : ' + str(CmStatus.GetAxesStatus(axis).profileCruiseMilliseconds))

    # Profile Dec Milliseconds      The total time the current motion profile will spend decelerating. If the motion is an override that causes the axis to change the direction of travel, the time spent decelerating before reversing direction is not included in this value. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileDecMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Dec Milliseconds : ' + str(CmStatus.GetAxesStatus(axis).profileDecMilliseconds))

    # Profile Remaining Milliseconds        The remaining time the current motion profile will take to complete. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileRemainingMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Remaining Milliseconds : ' + str(CmStatus.GetAxesStatus(axis).profileRemainingMilliseconds))

    # Profile Completed Milliseconds        The time that the current motion profile has executed for. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileCompletedMilliseconds
    # Type:            double
    # Unit:            milliseconds
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Completed Milliseconds : ' + str(CmStatus.GetAxesStatus(axis).profileCompletedMilliseconds))

    # Profile Target Pos        The target positon of the current motion profile. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileTargetPos
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Target Pos : ' + str(CmStatus.GetAxesStatus(axis).profileTargetPos))

    # Profile Total Distance        The total distance that the current motion profile will move. This is equal to the sum of the Profile Remaining Distance and the Profile Completed Distance. For the motion profiles of interpolation commands, this is the composite distance along the interpolation path. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileTotalDistance
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Total Distance : ' + str(CmStatus.GetAxesStatus(axis).profileTotalDistance))

    # Profile Remaining Distance        The remaining distance until the current motion profile completes. For the motion profiles of interpolation commands, this is the composite remaining distance along the interpolation path. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileRemainingDistance
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Remaining Distance : ' + str(CmStatus.GetAxesStatus(axis).profileRemainingDistance))

    # Profile Completed Distance        The distance moved so far by the current motion profile. For the motion profiles of interpolation commands, this is the composite distance moved along the interpolation path. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   profileCompletedDistance
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Profile Completed Distance : ' + str(CmStatus.GetAxesStatus(axis).profileCompletedDistance))

    # Intpl Velocity        If the axis is executing an interpolation command, this status contains the composite velocity along the interpolation path. All axes executing the same interpolation command will have the same value. For axes executing Trigger Motion as an override, the profile status of the overridden motion will be returned until the trigger condition is satisfied. If the trigger motion is started from Idle state, the profile status will return 0 until the trigger condition is satisfied.
    # Variable Name:   intplVelocity
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Intpl Velocity : ' + str(CmStatus.GetAxesStatus(axis).intplVelocity))

    # Intpl Segment     If the axis is executing an interpolation command consiting of several segments (such as path interpolation and spline interpolation), this status contains the index of the currently executing segment.
    # Variable Name:   intplSegment
    # Type:            int
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Intpl Segment : ' + str(CmStatus.GetAxesStatus(axis).intplSegment))

    # Following Error Alarm     TRUE: Following error has occurred. FALSE: Following error has not occurred. The condition for the following error is configured with the Following Error Type and Velocity Following Error Type parameters. This status is also turned on when the error configured with the Servo On Following Error parameter occurs.
    # Variable Name:   followingErrorAlarm
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Following Error Alarm : ' + str(CmStatus.GetAxesStatus(axis).followingErrorAlarm))

    # Command Ready     TRUE: The axis is in a state that is able to accept motion commands, including overrides. FALSE: The axis is in a state that is unable to accept motion commands.
    # Variable Name:   commandReady
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Command Ready : ' + str(CmStatus.GetAxesStatus(axis).commandReady))

    # Waiting for Trigger       TRUE: The axis is waiting for the trigger condition of a trigger motion to be satisfied. For more information regarding trigger motion, see Trigger Motion. FALSE: The axis is not waiting for a trigger condition.
    # Variable Name:   waitingForTrigger
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Waiting for Trigger : ' + str(CmStatus.GetAxesStatus(axis).waitingForTrigger))

    # Motion Paused     TRUE: The axis motion has been paused by a function such as Pause. FALSE: The axis motion is not paused, or the axis is not executing motion.
    # Variable Name:   motionPaused
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Motion Paused : ' + str(CmStatus.GetAxesStatus(axis).motionPaused))

    # Motion Complete       This status is set to 0 when a new motion command is started. When the motion completes, this status is set to 1 in the same cycle that the operation state (Op State) is set to Idle. This status is set to 0 when a stop function is called. The status remains 0 after the axis stops. This status is also set to 0 when a jog or velocity command is started. These motion commands do not set this status to 1. This status is also set to 0 when one of the following conditions cause the axis to stop. •A limit switch is triggered for the axis with the DecServoOff, Dec, SlowDecServoOff, or SlowDec limit switch type. •A following error alarm is triggered for the axis with the QuickStop following error alarm type. •A velocity following error alarm is triggered for the axis with the QuickStop velocity following error alarm type. •A sync master axis has desynchronized with the DecServoOff or Dec master desync type. •An emergency stop is triggered with the Level1 emergency stop level. This status is not updated for Sync axes. This status is also set to 1 in the abnormal case in which one of the motion commands in the above two tables are executed, but the target position is farther away than the Maximum Travel Distance.
    # Variable Name:   motionComplete
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Motion Complete : ' + str(CmStatus.GetAxesStatus(axis).motionComplete))

    # Exec Superimposed Motion      TRUE: Axis is executing superimposed motion. FALSE: Axis is not executing superimposed motion.
    # Variable Name:   execSuperimposedMotion
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Exec Superimposed Motion : ' + str(CmStatus.GetAxesStatus(axis).execSuperimposedMotion))

    # Cmd Acc       Instantaneous command acceleration calculated from command velocity (for Velocity mode axes) or command position (for Position mode axes). This status is returned regardless of the motion command that is being executed.
    # Variable Name:   cmdAcc
    # Type:            double
    # Unit:            user unit / second^2
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Cmd Acc : ' + str(CmStatus.GetAxesStatus(axis).cmdAcc))

    # Acc Flag      TRUE: Axis is accelerating. FALSE: Axis is not accelerating.
    # Variable Name:   accFlag
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Acc Flag : ' + str(CmStatus.GetAxesStatus(axis).accFlag))

    # Dec Flag      TRUE: Axis is decelerating. FALSE: Axis is not decelerating.
    # Variable Name:   decFlag
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Dec Flag : ' + str(CmStatus.GetAxesStatus(axis).decFlag))

    # In Pos        TRUE: The axis is within the In Pos Width of the target position of the current motion command. FALSE: The axis is not within the In Pos Width of the target position of the current motion command. In Position State for Single Turn Axes : Single turn axes are set using the Single Turn Mode parameter. Wraparound around the single turn encoder count range is considered when calculating the in position state for single turn axes. For example, if the single turn encoder count is the equivalent of 1000 user units, the in position width is 100 user units, and the cyclic command position is 0, the axis will be in position if the feedback position is between 900-1000 or between 0-100. If a position command causes the axis to move a distance greater than one single turn encoder count, the axis will be in position each time the axis passes the target position inside the single turn encoder count range. For example, if the single turn encoder count is the equivalent of 1000 user units, and a relative position command of 5000 user units is executed, the axis will wrap around the single turn range five times, passing by the target position four times and stopping at the target position on the fifth lap. Each time the axis passes the target position, the axis will be in position as long as the distance between the feedback position and the target position is within the in position width. Wraparound around the single turn encoder count range is NOT considered when calculating the in position state during the execution of an interpolation command.
    # Variable Name:   inPos
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('In Pos : ' + str(CmStatus.GetAxesStatus(axis).inPos))

    # In Pos 2      TRUE: The axis is within the In Pos Width 2 of the target position of the current motion command. FALSE: The axis is not within the In Pos Width 2 of the target position of the current motion command. This status is the same as the In Pos status except the In Pos Width 2 parameter is used instead of In Pos Width.
    # Variable Name:   inPos2
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('In Pos 2 : ' + str(CmStatus.GetAxesStatus(axis).inPos2))

    # In Pos 3      TRUE: The axis is within the In Pos Width 3 of the target position of the current motion command. FALSE: The axis is not within the In Pos Width 3 of the target position of the current motion command. This status is the same as the In Pos status except the In Pos Width 3 parameter is used instead of In Pos Width.
    # Variable Name:   inPos3
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('In Pos 3 : ' + str(CmStatus.GetAxesStatus(axis).inPos3))

    # In Pos 4      TRUE: The axis is within the In Pos Width 4 of the target position of the current motion command. FALSE: The axis is not within the In Pos Width 4 of the target position of the current motion command. This status is the same as the In Pos status except the In Pos Width 4 parameter is used instead of In Pos Width.
    # Variable Name:   inPos4
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('In Pos 4 : ' + str(CmStatus.GetAxesStatus(axis).inPos4))

    # In Pos 5      TRUE: The axis is within the In Pos Width 5 of the target position of the current motion command. FALSE: The axis is not within the In Pos Width 5 of the target position of the current motion command. This status is the same as the In Pos status except the In Pos Width 5 parameter is used instead of In Pos Width.
    # Variable Name:   inPos5
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('In Pos 5 : ' + str(CmStatus.GetAxesStatus(axis).inPos5))

    # Cmd Distribution End      TRUE: The command position of the axis is equal to the target position of the current motion command. The actual position (Actual Pos) of the axis may still not be at the target position. This status indicates that the axis has completed the motion command and is in Idle operation state. FALSE: The command position of the axis is not equal to the target position of the current motion command. The axis is still executing the motion command.
    # Variable Name:   cmdDistributionEnd
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Cmd Distribution End : ' + str(CmStatus.GetAxesStatus(axis).cmdDistributionEnd))

    # Pos Set       TRUE: The command position of the axis is equal to the target position of the current motion command and the feedback position is within the Pos Set Width of the target position. FALSE: The command position of the axis is not equal to the target position of the current motion command, or the feedback position is not within the Pos Set Width of the target position. If the Cmd Distribution End status is TRUE, and the difference between the Actual Pos and Pos Cmd is less than or equal to the Pos Set Width parameter, this status will be set to TRUE. Otherwise, this status will be set to FALSE. If the Servo On status is FALSE, this status will be set to FALSE. Pos Set State for Single Turn Axes : Single turn axes are set using the Single Turn Mode parameter. Wraparound around the single turn encoder count range is considered when calculating this status. For example, if the single turn encoder count is the equivalent of 1000 user units, the Pos Set Width is 100 user units, and the target position is 0, this status will be set to TRUE if the feedback position is between 900-1000 or between 0-100.
    # Variable Name:   posSet
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Pos Set : ' + str(CmStatus.GetAxesStatus(axis).posSet))

    # Delayed Pos Set       TRUE: The command position of the axis is equal to the target position of the current motion command and the feedback position remained within the Delayed Pos Set Width of the target position continuously for Delayed Pos Set Milliseconds amount of time. FALSE: The command position of the axis is not equal to the target position of the current motion command, or the feedback position is not within the Delayed Pos Set Width of the target position, or the axis did not remain within this range continuously for Delayed Pos Set Milliseconds amount of time. If the Servo On status is FALSE, this status will be set to FALSE. Delayed Pos Set State for Single Turn Axes : Single turn axes are set using the Single Turn Mode parameter. Wraparound around the single turn encoder count range is considered when calculating this status. For example, if the single turn encoder count is the equivalent of 1000 user units, the Delayed Pos Set Width is 100 user units, and the target position is 0, this status will be set to TRUE if the feedback position is between 900-1000 or between 0-100 for Delayed Pos Set Milliseconds amount of time.
    # Variable Name:   delayedPosSet
    # Type:            bool
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Delayed Pos Set : ' + str(CmStatus.GetAxesStatus(axis).delayedPosSet))

    # Cmd Distribution End Delayed Pos Set Diff     The duration between when the Cmd Distribution End status was set and when the Delayed Pos Set status was set, in units of communication cycles. This value is set during the cycle that the Delayed Pos Set status is set. This value is cleared whenever the Cmd Distribution End status changes from FALSE to TRUE.
    # Variable Name:   cmdDistributionEndDelayedPosSetDiff
    # Type:            unsigned int
    # Unit:            communication cycles
    # Update Timing:   Acyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Cmd Distribution End Delayed Pos Set Diff : ' + str(CmStatus.GetAxesStatus(axis).cmdDistributionEndDelayedPosSetDiff))

    # Positive LS       TRUE: Positive limit switch is on. FALSE: Positive limit switch is off. If the Invert Positive LS Polarity parameter is set to TRUE, this status will return TRUE when the positive limit switch signal from the servo is low and FALSE when the positive limit switch signal from the servo is high.
    # Variable Name:   positiveLS
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Positive LS : ' + str(CmStatus.GetAxesStatus(axis).positiveLS))

    # Negative LS       TRUE: Negative limit switch is on. FALSE: Negative limit switch is off. If the Invert Negative LS Polarity parameter is set to TRUE, this status will return TRUE when the negative limit switch signal from the servo is low and FALSE when the negative limit switch signal from the servo is high.
    # Variable Name:   negativeLS
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Negative LS : ' + str(CmStatus.GetAxesStatus(axis).negativeLS))

    # Near Positive LS      TRUE: Positive near limit switch is on. FALSE: Positive near limit switch is off. If the Invert Near Positive LS Polarity parameter is set to TRUE, this status will return TRUE when the positive near limit switch signal is low and FALSE when the positive near limit switch signal is high. This status will always return FALSE if the Near LS Type parameter is set to None or if the Near LS Type parameter is set to SeparatePositiveLSNegativeLS and the Near Positive LS Type parameter is set to None.
    # Variable Name:   nearPositiveLS
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Near Positive LS : ' + str(CmStatus.GetAxesStatus(axis).nearPositiveLS))

    # Near Negative LS      TRUE: Negative near limit switch is on. FALSE: Negative near limit switch is off. If the Invert Near Negative LS Polarity parameter is set to TRUE, this status will return TRUE when the negative near limit switch signal is low and FALSE when the negative near limit switch signal is high. This status will always return FALSE if the Near LS Type parameter is set to None or if the Near LS Type parameter is set to SeparatePositiveLSNegativeLS and the Near Negative LS Type parameter is set to None.
    # Variable Name:   nearNegativeLS
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Near Negative LS : ' + str(CmStatus.GetAxesStatus(axis).nearNegativeLS))

    # External Positive LS      TRUE: Positive external limit switch is on. FALSE: Positive external limit switch is off. If the Invert External Positive LS Polarity parameter is set to TRUE, this status will return TRUE when the positive external limit switch signal is low and FALSE when the positive external limit switch signal is high. This status will always return FALSE if the External LS Type parameter is set to None or if the External LS Type parameter is set to SeparatePositiveLSNegativeLS and the External Positive LS Type parameter is set to None.
    # Variable Name:   externalPositiveLS
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('External Positive LS : ' + str(CmStatus.GetAxesStatus(axis).externalPositiveLS))

    # External Negative LS      TRUE: Negative external limit switch is on. FALSE: Negative external limit switch is off. If the Invert External Negative LS Polarity parameter is set to TRUE, this status will return TRUE when the negative external limit switch signal is low and FALSE when the negative external limit switch signal is high. This status will always return FALSE if the External LS Type parameter is set to None or if the External LS Type parameter is set to SeparatePositiveLSNegativeLS and the External Negative LS Type parameter is set to None.
    # Variable Name:   externalNegativeLS
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('External Negative LS : ' + str(CmStatus.GetAxesStatus(axis).externalNegativeLS))

    # Positive Soft Limit       TRUE: Positive software limit is on. FALSE: Positive software limit is off.
    # Variable Name:   positiveSoftLimit
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Positive Soft Limit : ' + str(CmStatus.GetAxesStatus(axis).positiveSoftLimit))

    # Negative Soft Limit       TRUE: Negative software limit is on. FALSE: Negative software limit is off.
    # Variable Name:   negativeSoftLimit
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Negative Soft Limit : ' + str(CmStatus.GetAxesStatus(axis).negativeSoftLimit))

    # Home State        If the axis is executing a homing operation, this status contains the homing state of the axis.
    # Variable Name:   homeState
    # Type:            HomeState::T
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Home State : ' + str(CmStatus.GetAxesStatus(axis).homeState))

    # Home Error        The last encountered homing error code. This error code is cleared when an axis starts a new homing operation.
    # Variable Name:   homeError
    # Type:            HomeError::T
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Home Error : ' + str(CmStatus.GetAxesStatus(axis).homeError))

    # Home Offset       The cumulative sum of the offsets applied from changes to the home position. This value will change after performing a homing operation.
    # Variable Name:   homeOffset
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Home Offset : ' + str(CmStatus.GetAxesStatus(axis).homeOffset))

    # Home Switch       TRUE: Home switch is on. FALSE: Home switch is off. If the Invert HS Polarity parameter is set to TRUE, this status will return TRUE when the home switch signal from the servo is low and FALSE when the home switch signal from the servo is high.
    # Variable Name:   homeSwitch
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Home Switch : ' + str(CmStatus.GetAxesStatus(axis).homeSwitch))

    # Home Done     TRUE: Homing is complete. FALSE: Homing is not complete. Homing can be executed using functions such as StartHome. This status can also be manually toggled using the SetHomeDone function. If the Clear Home Done On Servo Off parameter is enabled for an axis, this status is set to FALSE when the servo is turned off. If the Clear Home Done On Comm Stop parameter is enabled for an axis, this status is set to FALSE when communication is stopped. When the servo is offline (see Servo Offline), this status is set to FALSE. This status is also set to FALSE when a new homing routine is started. When this status is set to FALSE, homing must be completed again before this status becomes TRUE. This status affects certain operations, such as the software limit (see Soft Limit Type).
    # Variable Name:   homeDone
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Home Done : ' + str(CmStatus.GetAxesStatus(axis).homeDone))

    # Home Paused       TRUE: Axis is paused while homing. FALSE: Axis is not paused while homing.
    # Variable Name:   homePaused
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Home Paused : ' + str(CmStatus.GetAxesStatus(axis).homePaused))

    # Cmd Pos To Fb Pos Flag        TRUE: Axis is executing a SetCommandPosToFeedbackPos operation. FALSE: Axis is not executing a SetCommandPosToFeedbackPos operation.
    # Variable Name:   cmdPosToFbPosFlag
    # Type:            bool
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Cmd Pos To Fb Pos Flag : ' + str(CmStatus.GetAxesStatus(axis).cmdPosToFbPosFlag))

    # Single Turn Counter       If the axis is a single turn axis (if the Single Turn Mode parameter is set to TRUE), this status contains the number of single turn rotations since starting single turn mode. When the axis position exceeds the Single Turn Encoder Count and loops back, this value increases by one. When the axis position goes below zero and loops back, this value decreases by one. This value itself loops around at 0 and 2^32-1 (for example, if this value decreases by 1 from 0, it becomes 2^32-1). This value is reset to 0 each time the Single Turn Encoder Count, Single Turn Mode, Gear Ratio Numerator, Gear Ratio Denominator, or Axis Polarity parameter is changed. This status contains 0 for non-single turn axes.
    # Variable Name:   singleTurnCounter
    # Type:            unsigned int
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Single Turn Counter : ' + str(CmStatus.GetAxesStatus(axis).singleTurnCounter))

    # User Offset       This status contains the user offset. The user offset is an additional offset that is applied to the command and feedback position. It can be freely set when developing a customized User RTDLL.
    # Variable Name:   userOffset
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('User Offset : ' + str(CmStatus.GetAxesStatus(axis).userOffset))

    # User Offset Pos Cmd       This status contains the command position of the axis after applying the user offset.
    # Variable Name:   userOffsetPosCmd
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('User Offset Pos Cmd : ' + str(CmStatus.GetAxesStatus(axis).userOffsetPosCmd))

    # User Offset Actual Pos        This status contains the feedback position of the axis after applying the user offset.
    # Variable Name:   userOffsetActualPos
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('User Offset Actual Pos : ' + str(CmStatus.GetAxesStatus(axis).userOffsetActualPos))

    # User Velocity Offset      This status contains the user velocity offset. The user velocity offset is an additional offset that is applied to the command and feedback velocity. It can be freely set when developing a customized User RTDLL.
    # Variable Name:   userVelocityOffset
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('User Velocity Offset : ' + str(CmStatus.GetAxesStatus(axis).userVelocityOffset))

    # User Torque Offset        This status contains the user torque offset. The user torque offset is an additional offset that is applied to the command and feedback torque. It can be freely set when developing a customized User RTDLL.
    # Variable Name:   userTorqueOffset
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('User Torque Offset : ' + str(CmStatus.GetAxesStatus(axis).userTorqueOffset))

    # Vibration Pos Min     The status measures the minimum value of Actual Pos - Pos Cmd while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. Whenever a smaller value of Actual Pos - Pos Cmd is measured while the axis is stationary, this status updates to equal that value. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationPosMin
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Pos Min : ' + str(CmStatus.GetAxesStatus(axis).vibrationPosMin))

    # Vibration Pos Max     The status measures the maximum value of Actual Pos - Pos Cmd while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. Whenever a larger value of Actual Pos - Pos Cmd is measured while the axis is stationary, this status updates to equal that value. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationPosMax
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Pos Max : ' + str(CmStatus.GetAxesStatus(axis).vibrationPosMax))

    # Vibration Pos Average     The status measures the average value of Actual Pos - Pos Cmd while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. On the cycles in which the axis is stationary, the average is updated with the new measured value of Actual Pos - Pos Cmd. The average is not affected by the value of Actual Pos - Pos Cmd while the axis is not stationary. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationPosAvg
    # Type:            double
    # Unit:            user unit
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Pos Average : ' + str(CmStatus.GetAxesStatus(axis).vibrationPosAvg))

    # Vibration Vel Min     The status measures the minimum value of Actual Velocity while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. Whenever a smaller value of Actual Velocity is measured while the axis is stationary, this status updates to equal that value. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationVelMin
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Vel Min : ' + str(CmStatus.GetAxesStatus(axis).vibrationVelMin))

    # Vibration Vel Max     The status measures the maximum value of Actual Velocity while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. Whenever a larger value of Actual Velocity is measured while the axis is stationary, this status updates to equal that value. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationVelMax
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Vel Max : ' + str(CmStatus.GetAxesStatus(axis).vibrationVelMax))

    # Vibration Vel Average     The status measures the average value of Actual Velocity while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. On the cycles in which the axis is stationary, the average is updated with the new measured value of Actual Velocity. The average is not affected by the value of Actual Velocity while the axis is not stationary. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationVelAvg
    # Type:            double
    # Unit:            user unit / second
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Vel Average : ' + str(CmStatus.GetAxesStatus(axis).vibrationVelAvg))

    # Vibration Trq Min     The status measures the minimum value of Actual Torque while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. Whenever a smaller value of Actual Torque is measured while the axis is stationary, this status updates to equal that value. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationTrqMin
    # Type:            double
    # Unit:            %
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Trq Min : ' + str(CmStatus.GetAxesStatus(axis).vibrationTrqMin))

    # Vibration Trq Max        The status measures the maximum value of Actual Torque while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. Whenever a larger value of Actual Torque is measured while the axis is stationary, this status updates to equal that value. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationTrqMax
    # Type:            double
    # Unit:            %
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Trq Max : ' + str(CmStatus.GetAxesStatus(axis).vibrationTrqMax))

    # Vibration Trq Average     The status measures the average value of Actual Torque while the axis is stationary. The axis is considered to be stationary if the Op State of the axis is Idle or Sync, and the Delayed Pos Set signal has become TRUE at least once after the axis entered one of these operation states. This status is 0 when the engine is started. On the cycles in which the axis is stationary, the average is updated with the new measured value of Actual Torque. The average is not affected by the value of Actual Torque while the axis is not stationary. This status is reset to 0 when the axis changes from non-stationary to stationary state. The ClearVibrationStatus function can also be called to reset this status to 0 on the next communication cycle.
    # Variable Name:   vibrationTrqAvg
    # Type:            double
    # Unit:            %
    # Update Timing:   Cyclic
    # Read the current system status from the engine
    # GetStatus -> First return value : Error code, Second return value: CoreMotionStatus
    ret, CmStatus = Wmx3Lib_cm.GetStatus()
    if (ret != 0):
        print('GetStatus error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    print('Vibration Trq Average : ' + str(CmStatus.GetAxesStatus(axis).vibrationTrqAvg))

