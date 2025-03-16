
# Axes = [6, 7]
# Inputs = []
# Outputs = []

# Establish the synchronization between master Axis 6 and slave Axis 7.
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create a command to move Axis 6 to position 120 with a velocity of 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the command to move the master axis to the specified position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the positioning motion to complete.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create a command to move Axis 6 to position 240 with a velocity of 1000.
posCommand.target = 240

# Execute the command to move the master axis to the specified position.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the positioning motion to complete.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Release the synchronization between Axis 6 and Axis 7.
ret = Wmx3Lib_cm.sync.ResolveSync(7)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
