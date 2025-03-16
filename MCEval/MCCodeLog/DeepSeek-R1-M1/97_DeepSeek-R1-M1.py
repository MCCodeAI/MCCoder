
# Axes = [9]
# IOInputs = []
# IOOutputs = []

def set_axis_parameters():
    # Create a Config_SyncParam object
    syncParam = Config_SyncParam()
    
    # Read current sync parameters for Axis 9
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(9)
    if ret != 0:
        print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Set Match Pos to TRUE
    syncParam.matchPos = True
    
    # Set Sync Compensation Mode to SymmetricVelocityOffset
    syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset
    
    # Set the updated parameters
    ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(9, syncParam)
    if ret != 0:
        print('SetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Verify the parameters
    ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(9)
    if ret != 0:
        print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    if syncParam.matchPos and syncParam.syncCompensationMode == Config_SyncCompensationMode.SymmetricVelocityOffset:
        print("Parameters set correctly. Moving to 9.9...")
        target = 9.9
    else:
        print("Parameters not set correctly. Moving to -9.9...")
        target = -9.9
    
    # Create motion command
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 9
    posCommand.target = target
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000
    
    # Execute motion
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return
    
    # Wait for motion to complete
    Wmx3Lib_cm.motion.Wait(9)

# Execute the function
set_axis_parameters()
