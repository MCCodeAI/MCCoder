
# Axes = [9]
# IOInputs = []
# IOOutputs = []

axis = 9

# Read current sync parameters
syncParam = Config_SyncParam()
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set Match Pos to TRUE
syncParam.matchPos = True

# Set Sync Compensation Mode to SymmetricVelocityOffset
syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset

# Set the updated parameters
ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print('SetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Verify parameters
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if ret != 0:
    print('GetSyncParam error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

params_correct = (syncParam.matchPos == True and 
                 syncParam.syncCompensationMode == Config_SyncCompensationMode.SymmetricVelocityOffset)

# Create motion command
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

if params_correct:
    posCommand.target = 9.9
else:
    posCommand.target = -9.9

# Execute motion
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait for motion to complete
Wmx3Lib_cm.motion.Wait(axis)
