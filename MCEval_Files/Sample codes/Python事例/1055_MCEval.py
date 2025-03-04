#Set the Sync parameters for Axis 0. Set‘In Sync Width’to 0,‘Sync Gain ’to 0,‘Sync Compensation Mode’to VelocityOffset,‘Master Desync Type’to NoAction,‘Master Desync Dec’to 10000,‘Slave Desync Type’to NoAction,‘Slave Desync Dec’to 10000,‘Match Pos’to FALSE.
    # Axes = [0]

    # Example of Axis 0 Homing Parameters
    axis = 0

    # In Sync Width    This parameter determines when sync compensation should be applied to a sync slave axis. When the feedback position difference between the master axis and the slave axis exceeds this value, sync compensation will be applied.
    # Variable Name:   inSyncWidth
    # Type:            int
    # Unit:            user unit
    # Minimum Value:   0
    # Maximum Value:   2147483647
    # Default Value:   0
    # Axis:            Slave/Master
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.inSyncWidth = 0
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set inSyncWidth  error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Sync Gain        This parameter determines the gain when sync compensation is applied. The feedback position difference between the master axis and slave axis will be multiplied by this value when applying sync compensation.
    # Variable Name:   syncGain
    # Type:            double
    # Unit:            none
    # Minimum Value:   0
    # Maximum Value:   3
    # Default Value:   0
    # Axis:            Slave/Master
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.syncGain  = 0
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set syncGain error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Sync Compensation Mode      This parameter determines the mode at which additional compensation is applied to improve the synchronization between the master and slave axes. See SyncCompensationMode for additional information of each mode.
    # Variable Name:   syncCompensationMode
    # Type:            SyncCompensationMode
    # Default Value:   VelocityOffset
    # Axis:            Slave
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.syncCompensationMode  = Config_SyncCompensationMode.VelocityOffset
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set syncCompensationMode error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Master Desync Type       The action executed by the master axis when it one of the slave axes loses synchronization. A sync slave axis can lose synchronization if it encounters an amp alarm, the servo turns off, etc. This action is not executed if synchronization is deliberately stopped with functions such as ResolveSync.
    # Variable Name:   masterDesyncType
    # Type:            MasterDesyncType
    # Default Value:   NoAction
    # Axis:            Master
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.masterDesyncType  = Config_MasterDesyncType.NoAction
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set masterDesyncType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Master Desync Dec        This parameter determines the gain when sync compensation is applied. The feedback position difference between the master axis and slave axis will be multiplied by this value when applying sync compensation.
    # Variable Name:   masterDesyncDec
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Axis:            Master
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.masterDesyncDec  = 10000
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set masterDesyncDec error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Slave Desync Type       The action executed by the slave axis when it loses synchronization with the master axis due to the master axis servo turning off.
    # Variable Name:   slaveDesyncType
    # Type:            SlaveDesyncType
    # Default Value:   NoAction
    # Axis:            Slave
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.slaveDesyncType  = 0
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set slaveDesyncType error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Slave Desync Dec       This parameter is reserved, and has no effect.
    # Variable Name:   slaveDesyncDec
    # Type:            double
    # Unit:            user unit / second^2
    # Minimum Value:   1e-6
    # Maximum Value:   274877906943
    # Default Value:   10000
    # Axis:            Slave
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.slaveDesyncDec  = 10000
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set slaveDesyncDec error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Match Pos        TRUE: Sync Pos Cmd and Sync Actual Pos will be used instead of Pos Cmd and Actual Pos for the following functions:SetLog SetFlightRecorderParam  SetEvent SetPSOConfig SetPlannedVelOverrideConfig SetSoftwareTouchProbe SetCommandPos SetFeedbackPos StartECAM (if this axis is a slave axis and also an ECAM master axis)
    # Variable Name:   matchPos
    # Type:            bool
    # Default Value:   FALSE
    # Axis:            Slave
    # Read the current values of parameters
    syncParam = Config_SyncParam()
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
    syncParam.matchPos  = False
    # syncParam -> First return value: Error code, Second return value: param error
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if (ret != 0):
        print('Set matchPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

