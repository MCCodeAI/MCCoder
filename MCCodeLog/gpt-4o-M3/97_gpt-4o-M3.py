
# Axes = [9]
# Inputs = []
# Outputs = []

# Define the axis number
axis = 9

# Set the Match Pos and Sync Compensation Mode parameters
syncParam = Config_SyncParam()
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
syncParam.matchPos = True
syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset

# Apply the parameters
ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print('Error setting parameters: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Verify if parameters are set correctly
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
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
        print('Error moving to 9.9: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    else:
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
        print('Error moving to -9.9: ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    else:
        Wmx3Lib_cm.motion.Wait(axis)
