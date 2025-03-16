
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# The following code sets the 'Match Pos' to True and the 'Sync Compensation Mode' to SymmetricVelocityOffset
# for Axis 9. Then the code verifies that these parameters were set correctly.
# If verification passes, Axis 9 is moved to 9.9; otherwise, it is moved to -9.9.
#
# Note: This example uses pseudo API calls (such as Wmx3Lib_cm.config.GetSyncParam, Wmx3Lib_cm.config.SetSyncParam,
# Wmx3Lib_cm.motion.StartPos, and Wmx3Lib_cm.motion.Wait) inherited from the reference.
# No motion libraries are imported as per instructions.

# Define the axis to use
axis = 9

# Create and get current sync parameters for the axis
syncParam = Config_SyncParam()
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)

# Set Match Pos to True and Sync Compensation Mode to SymmetricVelocityOffset
syncParam.matchPos = True
syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset

# Write the new sync parameters back to the axis configuration
ret, error = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print("Error while setting sync parameters on Axis", axis, "Error code:", ret)
    # Since parameter update failed, move Axis 9 to -9.9
    posCommand = Motion_PosCommand()
    posCommand.axis = axis
    posCommand.target = -9.9
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    # Wait until the motion stops
    Wmx3Lib_cm.motion.Wait(axis)
else:
    # Re-read the parameter to verify that they were set correctly
    ret, syncParam_check = Wmx3Lib_cm.config.GetSyncParam(axis)
    if (syncParam_check.matchPos == True and 
        syncParam_check.syncCompensationMode == Config_SyncCompensationMode.SymmetricVelocityOffset):
        # Parameters are set correctly: move Axis 9 to 9.9
        posCommand = Motion_PosCommand()
        posCommand.axis = axis
        posCommand.target = 9.9
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000
        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait until the axis has stopped moving
        Wmx3Lib_cm.motion.Wait(axis)
    else:
        # Parameters did not update as expected: move Axis 9 to -9.9
        posCommand = Motion_PosCommand()
        posCommand.axis = axis
        posCommand.target = -9.9
        posCommand.profile.type = ProfileType.Trapezoidal
        posCommand.profile.velocity = 1000
        posCommand.profile.acc = 10000
        posCommand.profile.dec = 10000
        ret = Wmx3Lib_cm.motion.StartPos(posCommand)
        # Wait until the axis has stopped moving
        Wmx3Lib_cm.motion.Wait(axis)
