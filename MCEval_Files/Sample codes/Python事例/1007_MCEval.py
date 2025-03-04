# Write Python code to record and execute an API buffer with :Move Axis 3 and 4 to a relative position of 50 at a speed of 1000. After executing, rewind the apibuffer once.
# Axes = [3, 4]

    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    bufStatus = ApiBufferStatus()

    # Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    cond = ApiBufferCondition()

    # Add a position command to the API buffer.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 3
    posCommand.target = 50
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified relative position.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Add a position command to the API buffer
    posCommand.axis = 4
    # Execute command to move to a specified relative position.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Pause execution until both axes have finished motion
    Wmx3Lib_buf.Wait(3)
    Wmx3Lib_buf.Wait(4)

    # End Recording.
    Wmx3Lib_buf.EndRecordBufferChannel()
    # Drive the motion accumulated in the buffer so far.
    Wmx3Lib_buf.Execute(0)

    # Check the status periodically to see if execution has finished
    counter = 50
    while True:
        ret, bufStatus = Wmx3Lib_buf.GetStatus(0)
        sleep(0.01)
        counter = counter - 1
        if (bufStatus.remainingBlockCount <= 0 and counter <= 0):
            break

    # Rewind the buffer, and then execute it again
    Wmx3Lib_buf.Rewind(0)

    # Wait for the axis to complete motion
    Wmx3Lib_cm.motion.Wait(3)
    Wmx3Lib_cm.motion.Wait(4)

    # Destroy API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)
