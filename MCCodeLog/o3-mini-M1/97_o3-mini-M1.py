
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set the Match Pos and Sync Compensation Mode parameter for Axis 9
axis = 9

# Retrieve current sync parameters for Axis 9
syncParam = Config_SyncParam()
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print("Error getting sync parameters for Axis {}: {}".format(axis, ret))
    # In a real application, you would handle the error appropriately.
    # For now, we assume the parameters could not be verified.
else:
    # Set the parameters:
    #   Match Pos to TRUE
    #   Sync Compensation Mode to SymmetricVelocityOffset
    syncParam.matchPos = True
    syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset

    # Apply the new sync parameters for Axis 9
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
    if ret != 0:
        print("Error setting sync parameters for Axis {}: {}".format(axis, ret))

# Now, verify the parameters have been set correctly.
ret, syncParamCheck = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print("Error re-reading sync parameters for Axis {}: {}".format(axis, ret))
    # If reading fails, default to moving in the negative direction.
    moveTarget = -9.9
else:
    if syncParamCheck.matchPos == True and syncParamCheck.syncCompensationMode == Config_SyncCompensationMode.SymmetricVelocityOffset:
        moveTarget = 9.9
    else:
        moveTarget = -9.9

# Create a position command for Axis 9.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = moveTarget
# Set a sample velocity, acceleration, and deceleration.
posCommand.profile.velocity = 500
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the motion command to move Axis 9.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print("Error starting position command for Axis {}: {}".format(axis, ret))
else:
    # Wait until Axis 9 stops moving.
    Wmx3Lib_cm.motion.Wait(axis)
