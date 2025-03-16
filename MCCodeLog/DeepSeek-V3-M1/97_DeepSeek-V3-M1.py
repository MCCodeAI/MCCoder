
# Axes = [9]
# IOInputs = []
# IOOutputs = []

# Set the Match Pos and Sync Compensation Mode parameter of Axis 9
axis = 9

# Set Match Pos to True
syncParam = Config_SyncParam()
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
syncParam.matchPos = True
ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print('Set matchPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Set Sync Compensation Mode to SymmetricVelocityOffset
syncParam.syncCompensationMode = Config_SyncCompensationMode.SymmetricVelocityOffset
ret, syncParamError = Wmx3Lib_cm.config.SetSyncParam(axis, syncParam)
if ret != 0:
    print('Set syncCompensationMode error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Check if all parameters are set correctly
ret, syncParam = Wmx3Lib_cm.config.GetSyncParam(axis)
if syncParam.matchPos != True or syncParam.syncCompensationMode != Config_SyncCompensationMode.SymmetricVelocityOffset:
    print('Parameters are not set correctly.')
    target_position = -9.9
else:
    print('Parameters are set correctly.')
    target_position = 9.9

# Move Axis 9 to the target position
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = axis
posCommand.target = target_position
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    exit()

# Wait until the axis stops moving
Wmx3Lib_cm.motion.Wait(axis)
