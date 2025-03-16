# Write python code to run an API buffer.
# Write python code to Record and execute an API buffer with two segments: Move Axis 0 to position 200 and Axis 1 to postion 100.

    # Axes = [0, 1]

    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    #  Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    # Create a command value.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 0
    posCommand.target = 200
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified absolute position. 
    Wmx3Lib_cm.motion.StartPos(posCommand)

    Wmx3Lib_buf.Wait(0)

    posCommand.axis = 1
    posCommand.target = 100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified absolute position.
    Wmx3Lib_cm.motion.StartPos(posCommand)
    Wmx3Lib_buf.Wait(1)

    # End Recording.
    Wmx3Lib_buf.EndRecordBufferChannel()
    # Drive the motion accumulated in the buffer so far.
    Wmx3Lib_buf.Execute(0)

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.
    axisSel = AxisSelection()
    axisSel.axisCount = 2
    axisSel.SetAxis(0, 0)
    axisSel.SetAxis(1, 1)
    ret = Wmx3Lib_cm.motion.Wait_AxisSel(axisSel)
    if ret != 0:
        print('Wait_AxisSel error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Destroy API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

