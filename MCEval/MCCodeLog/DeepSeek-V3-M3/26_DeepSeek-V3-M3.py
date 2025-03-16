
# Axes = [6, 7]
# IOInputs = []
# IOOutputs = []

# Establish the synchronization between Axis 6 and Axis 7, with Axis 6 designated as the master axis and Axis 7 as the slave axis.
ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(6, 7)
if ret != 0:
    print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create a command with target position 120 and velocity 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 120
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the command to move the master axis from its current position to a specified absolute position, with the slave axis moving in synchronization.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the positioning motion to complete. Start a blocking wait command, returning only when Axis 6 becomes idle.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Create a command with target position 240 and velocity 1000.
posCommand = Motion_PosCommand()
posCommand.profile.type = ProfileType.Trapezoidal
posCommand.axis = 6
posCommand.target = 240
posCommand.profile.velocity = 1000
posCommand.profile.acc = 10000
posCommand.profile.dec = 10000

# Execute the command to move the master axis from its current position to a specified absolute position, with the slave axis moving in synchronization.
ret = Wmx3Lib_cm.motion.StartPos(posCommand)
if ret != 0:
    print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Wait for the positioning motion to complete. Start a blocking wait command, returning only when Axis 6 becomes idle.
ret = Wmx3Lib_cm.motion.Wait(6)
if ret != 0:
    print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return

# Release the synchronization between Axis 6 and Axis 7.
ret = Wmx3Lib_cm.sync.ResolveSync(7)
if ret != 0:
    print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
    return
