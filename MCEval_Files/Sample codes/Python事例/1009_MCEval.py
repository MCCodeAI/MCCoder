# Write Python code to run an API buffer, if output 2,6 equals 1, move Axis 5 as a distance of 100, otherwise move as a distance of -100.
# Axes = [5]

    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    cond = ApiBufferCondition()

    # Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    cond = ApiBufferCondition()
    opt = ApiBufferOptions()

    # Add a position command to the API buffer.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.target = 100
    posCommand.profile.velocity = 1000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Set the IF branch
    cond.bufferConditionType = ApiBufferConditionType.IOOutput
    cond.arg_ioOutput.byteAddress = 2
    cond.arg_ioOutput.bitAddress = 6
    Wmx3Lib_buf.FlowIf(cond)

    # Add position command
    posCommand.axis = 5
    posCommand.target = 100

    # Execute command to move to a specified relative position.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Set the ELSE branch
    Wmx3Lib_buf.FlowElse()

    # Add position command
    posCommand.axis = 5
    posCommand.target = -100

    # Execute command to move to a specified relative position.
    ret = Wmx3Lib_cm.motion.StartMov(posCommand)
    if ret != 0:
        print('StartMov error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Set the END IF
    Wmx3Lib_buf.FlowEndIf()

    # End Recording.
    Wmx3Lib_buf.EndRecordBufferChannel()

    Wmx3Lib_buf.Execute(0)

    # Wait for the axis 5 motion to complete.
    Wmx3Lib_cm.motion.Wait(5)

    # Destroy API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)
