# Write python code to Establish synchronous control between master axis 0 and a slave axis 1, then move Axis 0 to position 188 with velocity 1200.
    # Axes = [0, 1]

    # Establish the synchronization between Axis 0 and Axis 1, with Axis 0 designated as the master axis and Axis 1 as the slave axis.
    ret = Wmx3Lib_cm.sync.SetSyncMasterSlave(0, 1)
    if ret != 0:
        print('SetSyncMasterSlave error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Create a command with target position 1,000,000 and velocity 100,000.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 188
    posCommand.profile.velocity = 1200
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute the command to move the master axis from its current position to a specified absolute position, with the slave axis moving in synchronization.
    ret = Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Wait for the positioning motion to complete. Start a blocking wait command, returning only when Axis 0 becomes idle.
    ret = Wmx3Lib_cm.motion.Wait(0)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Release the synchronization between Axis 0 and Axis 1.
    ret = Wmx3Lib_cm.sync.ResolveSync(1)
    if ret != 0:
        print('ResolveSync error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

