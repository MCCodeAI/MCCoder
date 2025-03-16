
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set the Match Pos and Sync Compensation Mode parameter of Axis 9 to true and SymmetricVelocityOffset
axis = 9

# Set Match Pos to True
syncParam = Config_SyncParam()
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
syncParam.matchPos = True

# Set Sync Compensation Mode to SymmetricVelocityOffset
syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset

# Apply the changes
ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print('SetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check if all parameters are set correctly
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Verify if Match Pos and Sync Compensation Mode are set correctly
if syncParam.matchPos == True and syncParam.syncCompensationMode == Config_SyncCompensationMode.SymmetricVelocityOffset:
    # Move Axis 9 to 9.9
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 9.9
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Move Axis 9 to -9.9
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = -9.9
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(axis)
