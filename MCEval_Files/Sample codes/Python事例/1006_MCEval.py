# Write Python code to record and execute an API buffer with : Axis 4 moves to the target position of 150 at a speed of 100. When the RemainingTime is 3ms, it then moves to the target position of 250 at a speed of 2000. When the RemainingTime is again 3ms, it finally moves to the target position of 400 at a speed of 3000.

# Axes = [4]

    Wmx3Lib_buf = ApiBuffer(Wmx3Lib)
    #  Clear the buffer of the specified channel.
    Wmx3Lib_buf.Clear(0)
    # Create a buffer for the specified channel.
    Wmx3Lib_buf.CreateApiBuffer(0, 1024 * 1024 * 3)
    # Start recording for the specified channel.
    Wmx3Lib_buf.StartRecordBufferChannel(0)

    cond =ApiBufferCondition()

    # Add a position command to the API buffer.
    posCommand = Motion_PosCommand()
    posCommand.profile.type = ProfileType.Trapezoidal
    posCommand.axis = 4
    posCommand.target = 150
    posCommand.profile.velocity = 100
    posCommand.profile.endVelocity=100
    posCommand.profile.acc = 1000
    posCommand.profile.dec = 1000

    # Execute command to move to a specified absolute position.
    ret=Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Wait for position command to have 3ms remaining time
    cond.bufferConditionType=ApiBufferConditionType.RemainingTime
    cond.arg_remainingTime.axis=4
    cond.arg_remainingTime.timeMilliseconds=3
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    #Add a position command to the API buffer
    posCommand.axis = 4
    posCommand.target = 250
    posCommand.profile.velocity = 200
    posCommand.profile.endVelocity=2000
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified absolute position.
    ret =Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    #Wait for position command to have 3ms remaining time
    Wmx3Lib_buf.Wait_ApiBufferCondition(cond)

    #Add a position command to the API buffer
    posCommand.axis = 4
    posCommand.target = 400
    posCommand.profile.velocity = 3000
    posCommand.profile.endVelocity=0
    posCommand.profile.acc = 10000
    posCommand.profile.dec = 10000

    # Execute command to move to a specified absolute position.
    ret =Wmx3Lib_cm.motion.StartPos(posCommand)
    if ret != 0:
        print('StartPos error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # End Recording.
    Wmx3Lib_buf.EndRecordBufferChannel()
    # Drive the motion accumulated in the buffer so far.
    Wmx3Lib_buf.Execute(0)

    # Wait for the motion to complete. Start a blocking wait command, returning only when Axis 0 and Axis 1 become idle.

    ret = Wmx3Lib_cm.motion.Wait(4)
    if ret != 0:
        print('Wait error code is ' + str(ret) + ': ' + Wmx3Lib_cm.ErrorToString(ret))
        return

    # Destroy API buffer resources.
    Wmx3Lib_buf.Halt(0)
    Wmx3Lib_buf.FreeApiBuffer(0)

