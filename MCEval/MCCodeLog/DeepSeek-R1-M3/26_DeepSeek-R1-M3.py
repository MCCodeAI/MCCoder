
# Axes = [6, 7]
# IOInputs = []
# IOOutputs = []

# Establish synchronization between Axis 6 (master) and Axis 7 (slave)
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# First movement to position 120
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for first motion completion
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Second movement to position 240
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 240
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for second motion completion
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Release synchronization
ret = Wmx3Lib_cm.sync.ResolveSync(7)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
