
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Define the axis number
axis = 9

# Create a configuration object for sync parameters
syncParam = Config_SyncParam()

# Retrieve current sync parameters for the axis
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set the Match Pos parameter to TRUE
syncParam.matchPos = True

# Set the Sync Compensation Mode to SymmetricVelocityOffset
syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset

# Apply the sync parameters to the axis
ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print('SetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Verify if the parameters are set correctly
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check if the parameters are set correctly
if syncParam.matchPos == True and syncParam.syncCompensationMode == Config_SyncCompensationMode.SymmetricVelocityOffset:
    # Create a motion command to move Axis 9 to position 9.9
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = 9.9
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute the motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Create a motion command to move Axis 9 to position -9.9
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = axis
    posCommand.target = -9.9
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute the motion command
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        exit()

    # Wait until the axis stops moving
    Wmx3Lib_cm.motion.Wait(axis)
